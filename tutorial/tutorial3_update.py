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


class _MyData_Prop:
    name: str
    email: str = ""
    data: dict = dict

class _MyData_Schema(_MyData_Prop, ValidatedSchemaFactory):
    pass

class MyData_Do(_MyData_Prop, DoFactory):
    pass

class MyJson_ORM(BaseJsonDbORM):
    schema = _MyData_Schema
    dbname = "update"


if __name__ == '__main__':
    data = MyData_Do()
    for _name in ["name_1", "name_2", "name_3"]:
        data.name = _name
        data.email = "test@ma"
        data.data = {
            "test":"aaaaaaaaaaaaaaaaaaaaaaa",
            "hogehoge":"uoooooooooooooooooo",
            "aaa": [{"a":1},{"a":2}]
        }
        MyJson_ORM().upsert(data)

    for _name in ["name_4", "name_5", "name_6"]:
        data.name = _name
        data.email = "test@ya"
        data.data = {
            "test":"aaaaaaaaaaaaaaaaaaaaaaa",
            "hogehoge":"uoooooooooooooooooo",
            "aaa": [{"a":1},{"a":2}]
        }
        MyJson_ORM().upsert(data)

    query = MyData_Do()
    query.email = "test@ma"
    for a in MyJson_ORM().jsondb.getByQuery(query.to_query_dict()):
        data = MyData_Do().from_json_dict(a)
        print("-----")
        print(data.name)
        print(data.email)
        print(data.data)

    updatedata = MyData_Do()
    updatedata.name = "name_1"
    updatedata.email = "test@ya"
    updatedata.data = {
        "test":"aaaaaaaaaaaaaaaaaaaaaaa",
        "hogehoge":"uoooooooooooooooooo",
        "aaa": [{"a":1},{"a":2}]
    }
    MyJson_ORM().upsert(updatedata)


    query = MyData_Do()
    query.email = "name_1"
    for a in MyJson_ORM().jsondb.getByQuery(query.to_query_dict()):
        data = MyData_Do().from_json_dict(a)
        print("-----")
        print(data.name)
        print(data.email)
        print(data.data)