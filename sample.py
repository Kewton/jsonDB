from jsonDB import ValidatedSchemaFactory, BaseJsonDbORM, DoFactory


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
    print(MyJson_ORM().jsondb.getByQuery({"name":"bbbbbbbbbbbbbbbbbbb"})[0])