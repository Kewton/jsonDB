from pydantic import BaseModel, ValidationError, Field
from pysondb import db
from pysondb.db import JsonDatabase
from datetime import datetime
import os


DEFAULT_DB_PATH = "./myjsondb/"


class DoFactory:
    def to_dict(self):
        # インスタンスのプロパティを辞書に変換します。
        # __dict__を利用して、インスタンスの属性とその値を取得します。
        # この方法は、インスタンスの直接的な公開プロパティのみを扱います。
        # プライベート属性やプロパティメソッドは含まれません。
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}


    def to_query_dict(self):
        # インスタンスのプロパティを辞書に変換します。
        # __dict__を利用して、インスタンスの属性とその値を取得します。
        # この方法は、インスタンスの直接的な公開プロパティのみを扱います。
        # プライベート属性やプロパティメソッドは含まれません。
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_') and len(value)>0}


def _base_validate_and_upsert_to_jsondatabase(_MyDataModel: BaseModel, dataset_db: JsonDatabase, datainstance: DoFactory)-> bool:
    try:
        data = datainstance.to_dict()
        validated_data = _MyDataModel(**data)
        _query = {}
        for _key in _MyDataModel.model_json_schema()["required"]:
            _query[_key] = data[_key]
        _data = dataset_db.getByQuery(query=_query)
        if len(_data) == 0:
            # データベースにデータを挿入
            dataset_db.add(validated_data.model_dump(mode="json"))
        else:
            _id = _data[0]["id"]
            dataset_db.updateById(_id, validated_data.model_dump(mode="json"))
    except ValidationError as e:
        print("バリデーションエラー:", e.json())
        return False
    return True


def _base_validate_and_upserts_to_jsondatabase(_MyDataModel: BaseModel, dataset_db: JsonDatabase, dataList: list[DoFactory])-> bool:
    try:
        _dataList = []
        for data in dataList:
            validated_data = _MyDataModel(**data.to_dict())
            _dataList.append(validated_data.model_dump(mode="json"))
        
        for data in _dataList:
            _query = {}
            for _key in _MyDataModel.model_json_schema()["required"]:
                _query[_key] = data[_key]
            _data = dataset_db.getByQuery(query=_query)
            if len(_data) == 0:
                # データベースにデータを挿入
                dataset_db.add(data)
            else:
                _id = _data[0]["id"]
                dataset_db.updateById(_id, data)
    except ValidationError as e:
        print("バリデーションエラー:", e.json())
        return False
    return True


def _base_validate_and_update_all_to_jsondatabase(_MyDataModel: BaseModel, dataset_db: JsonDatabase, queryinstance: DoFactory, datainstance: DoFactory) -> bool:
    try:
        data = datainstance.to_dict()
        _query = queryinstance.to_query_dict()
        _data = dataset_db.getByQuery(query=_query)
        for _rec in _data:
            _data = _rec
            _id = _rec["id"]
            _data.update(data)
            validated_data = _MyDataModel(**_data)
            # データベースにデータを挿入
            dataset_db.updateById(_id, validated_data.model_dump())
    except ValidationError as e:
        print("バリデーションエラー:", e.json())
        return False
    return True


def _base_delete_to_jsondatabase(dataset_db: JsonDatabase, queryinstance: DoFactory) -> bool:
    try:
        _query = queryinstance.to_query_dict()
        _data = dataset_db.getByQuery(query=_query)
        for _rec in _data:
            _id = _rec["id"]
            dataset_db.deleteById(_id)
    except ValidationError as e:
        print("バリデーションエラー:", e.json())
        return False
    return True


class BaseJsonDbORM:
    _instances = {}
    dbpath: str = None
    dbname: str = None
    schema: BaseModel = None
    jsondb: JsonDatabase = None

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self):
        if self.dbpath is None:
            os.makedirs(DEFAULT_DB_PATH, exist_ok=True)
            dataset_path = f'{DEFAULT_DB_PATH}/{self.dbname}.json'
        else:
            os.makedirs(self.dbpath, exist_ok=True)
            dataset_path = f'{self.dbpath}/{self.dbname}.json'
        self.jsondb = db.getDb(dataset_path)

    def upsert(self, datainstance: DoFactory):
        return _base_validate_and_upsert_to_jsondatabase(self.schema, self.jsondb, datainstance)

    def upserts(self, dataList: list[DoFactory]):
        return _base_validate_and_upserts_to_jsondatabase(self.schema, self.jsondb, dataList)

    def update_all(self, queryinstance: DoFactory, datainstance: DoFactory):
        return _base_validate_and_update_all_to_jsondatabase(self.schema, self.jsondb, queryinstance, datainstance)

    def delete(self, queryinstance: DoFactory):
        return _base_delete_to_jsondatabase(self.jsondb, queryinstance)


def gettimestamp():
    current_time = datetime.now()
    timestamp_str = current_time.strftime('%Y%m%d%H%M%S%f')
    return timestamp_str


class ValidatedSchemaFactory(BaseModel):
    registration_date: str = Field(default_factory=gettimestamp)
