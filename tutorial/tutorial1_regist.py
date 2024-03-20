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
    email: str
    data: dict


class _MyData_Schema(_MyData_Prop, ValidatedSchemaFactory):
    pass


class MyData_Do(_MyData_Prop, DoFactory):
    pass


class MyJson_ORM(BaseJsonDbORM):
    schema = _MyData_Schema
    dbname = "regist"


if __name__ == '__main__':
    data = MyData_Do()
    data.email = "test@ma"
    data.data = {
        "test": "aaaaaaaaaaaaaaaaaaaaaaa",
        "hogehoge": "uoooooooooooooooooo",
        "aaa": [
            {"a": 1},
            {"a": 2}
        ]
    }

    for _name in ["name_1", "name_2", "name_3"]:
        data.name = _name
        MyJson_ORM().upsertByprimaryKey(data)
