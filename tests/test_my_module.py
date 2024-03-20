# ----------------------------
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
# ----------------------------
from localjsondb.jsonDB import ValidatedSchemaFactory, BaseJsonDbORM, DoFactory


class _MyData_Prop:
    # Required input
    name: str
    email: str
    # Optional input
    data: dict = {}
    uso: str = "aaaaaa"


class _MyData_Schema(_MyData_Prop, ValidatedSchemaFactory):
    pass


class MyData_Do(_MyData_Prop, DoFactory):
    pass


class MyJson_ORM(BaseJsonDbORM):
    dbpath = "./tests/mydb/test"
    schema = _MyData_Schema

    def __init__(self, _dbname):
        self.dbname = _dbname
        super().__init__()


class MyJson_ORM2(BaseJsonDbORM):
    dbpath = "./tests/mydb/test2"
    schema = _MyData_Schema
    dbname = "single"


def test_upsertByprimaryKey():
    _testname = "test_upsertByprimaryKey"
    myJson_ORM_1 = MyJson_ORM(_testname)
    if os.path.exists(os.path.join("./tests/mydb/test", f"{_testname}.json")):
        assert True
    else:
        assert False

    data = MyData_Do()
    data.name = "aaaaaaaaaa"
    data.email = "test@ma"
    data.data = {
        "test": "aaaaaaaaaaaaaaaaaaaaaaa_11111111111111",
        "hogehoge": "uoooooooooooooooooo",
        "aaa": [
            {"a": 1},
            {"a": 2},
            {"a": 3},
            {"a": 4},
            {"a": 5}
        ]
    }

    myJson_ORM_1.upsertByprimaryKey(data)
    for a in myJson_ORM_1.jsondb.getByQuery(data.to_query_dict()):
        _data = MyData_Do().from_json_dict(a)
        if data.name == _data.name and data.email == _data.email:
            assert True
        else:
            assert False

        print(_data.data)
        if data.data == _data.data:
            assert True
        else:
            assert False

        if data.uso == "aaaaaa":
            assert True
        else:
            assert False
