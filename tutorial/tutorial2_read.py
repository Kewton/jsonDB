# ----------------------------
import sys
import os
# このスクリプトの親ディレクトリへのパスを取得
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.pathに親ディレクトリを追加
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
# ----------------------------
from localjsondb.jsonDB import ValidatedSchemaFactory, BaseJsonDbORM, DoFactory
import json


class _MyData_Prop:
    name: str
    email: str = ""
    data: dict = {}


class _MyData_Schema(_MyData_Prop, ValidatedSchemaFactory):
    pass


class MyData_Do(_MyData_Prop, DoFactory):
    pass


class MyJson_ORM(BaseJsonDbORM):
    schema = _MyData_Schema
    dbname = "read"


if __name__ == '__main__':
    data = MyData_Do()
    for _name in ["name_1", "name_2", "name_3"]:
        data.name = _name
        data.email = "test@ma"
        data.data = {
            "test": "aaaaaaaaaaaaaaaaaaaaaaa",
            "hogehoge": "uoooooooooooooooooo",
            "aaa": [
                {"a": 1},
                {"a": 2}
            ]
        }
        MyJson_ORM().upsertByprimaryKey(data)

    for _name in ["name_4", "name_5", "name_6"]:
        data.name = _name
        data.email = "test@ya"
        data.data = {
            "test": "aaaaaaaaaaaaaaaaaaaaaaa",
            "hogehoge": "uoooooooooooooooooo",
            "aaa": [
                {"a": 1},
                {"a": 2}
            ]
        }
        MyJson_ORM().upsertByprimaryKey(data)

    query = MyData_Do()
    query.email = "test@ma"
    print("Make sure it's registered by query.")
    for a in MyJson_ORM().jsondb.getByQuery(query.to_query_dict()):
        data = MyData_Do().from_json_dict(a).to_dict()
        print(data)

    print("Make sure it's registered.")
    for a in MyJson_ORM().jsondb.getAll():
        data = MyData_Do().from_json_dict(a).to_dict()
        print(data)