import sys
import os

# このスクリプトの親ディレクトリへのパスを取得
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.pathに親ディレクトリを追加
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
from localjsondb.jsonDB import ValidatedSchemaFactory, BaseJsonDbORM, DoFactory


class _MyData_Prop:
    name: str
    email: str
    data: dict

class _MyData_Schema(_MyData_Prop, ValidatedSchemaFactory):
    pass

class MyData_Do(_MyData_Prop, DoFactory):
    pass

class MyJson_ORM(BaseJsonDbORM):
    schema = _MyData_Schema
    dbname = "db2"


if __name__ == '__main__':
    # myJson_ORM = MyJson_ORM()
    data = MyData_Do()
    data.name = "aaaaaaaaaa"
    data.email = "test@ma"
    data.data = {
        "test":"aaaaaaaaaaaaaaaaaaaaaaa",
        "hogehoge":"uoooooooooooooooooo",
        "aaa": [
            {"a":1},
            {"a":2},
            {"a":3},
            {"a":4},
            {"a":5}
        ]
    }
    MyJson_ORM().upsert(data)

    # myJson_ORM2 = MyJson_ORM()
    data2 = MyData_Do()
    data2.name = "bbbbbbbbbbbbbbbbbbb"
    data2.email = "test@ma"
    data2.data = {
        "test":"aaaaaaaaaaaaaaaaaaaaaaa",
        "hogehoge":"uoooooooooooooooooo",
        "aaa": [
            {"a":11},
            {"a":12},
            {"a":13},
            {"a":14}
        ]
    }
    MyJson_ORM().upsert(data2)

    query = MyData_Do()
    query.name = "bbbbbbbbbbbbbbbbbbb"
    for a in MyJson_ORM().jsondb.getByQuery(query.to_query_dict()):
        data = MyData_Do().from_json_dict(a)
        print(data.name)
        