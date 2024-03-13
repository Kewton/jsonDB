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
    issingleton = True

    def __init__(self, _dbname):
        self.dbname = _dbname
        super().__init__()
    


if __name__ == '__main__':
    # myJson_ORM = MyJson_ORM()
    data = MyData_Do()
    data.name = "aaaaaaaaaa"
    data.email = "test@ma"
    data.data = {
        "test":"aaaaaaaaaaaaaaaaaaaaaaa_11111111111111",
        "hogehoge":"uoooooooooooooooooo",
        "aaa": [
            {"a":1},
            {"a":2},
            {"a":3},
            {"a":4},
            {"a":5}
        ]
    }
    myJson_ORM_1 = MyJson_ORM("db_test1")
    myJson_ORM_2 = MyJson_ORM("db_test2")
    myJson_ORM_3 = MyJson_ORM("db_test3")


    myJson_ORM_1.upsert(data)

    # myJson_ORM2 = MyJson_ORM()
    data2 = MyData_Do()
    data2.name = "bbbbbbbbbbbbbbbbbbb"
    data2.email = "test@ma"
    data2.data = {
        "test":"aaaaaaaaaaaaaaaaaaaaaaa_222222222222222",
        "hogehoge":"uoooooooooooooooooo",
        "aaa": [
            {"a":11},
            {"a":12},
            {"a":13},
            {"a":14}
        ]
    }
    
    myJson_ORM_2.upsert(data2)

    
    myJson_ORM_3.upsert(data2)

    query = MyData_Do()
    query.name = "bbbbbbbbbbbbbbbbbbb"
    
    for a in myJson_ORM_2.jsondb.getByQuery(query.to_query_dict()):
        data = MyData_Do().from_json_dict(a)
        print(data.name)

    print("=======")
    print(myJson_ORM_2.jsondb.getAll())
    for a in myJson_ORM_2.jsondb.getAll():
        print("-----")
        data = MyData_Do().from_json_dict(a)
        print(data.to_dict())

    