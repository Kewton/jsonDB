# 概要
# 環境準備
```
python -m venv .venv
.venv\Scripts\activate.ps1
.venv\Scripts\python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

# チュートリアル
## サンプルアプリ
'sample.py':
```python
from jsonDB import ValidatedSchemaFactory, BaseJsonDbORM, DoFactory


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
```
## 実行方法
```
python sample.py
```
## 実行結果
- ./myjsondbフォルダにdb2.jsonというファイルが作成されます<br>
'db2.json':
```json
{
   "data": [
      {
         "registration_date": "20240306231242452892",
         "name": "aaaaaaaaaa",
         "email": "test@ma",
         "data": {
            "test": "aaaaaaaaaaaaaaaaaaaaaaa",
            "hogehoge": "uoooooooooooooooooo",
            "aaa": [
               {
                  "a": 1
               },
               {
                  "a": 2
               },
               {
                  "a": 3
               },
               {
                  "a": 4
               },
               {
                  "a": 5
               }
            ]
         },
         "id": 218606492260928183
      },
      {
         "registration_date": "20240306231242461246",
         "name": "bbbbbbbbbbbbbbbbbbb",
         "email": "test@ma",
         "data": {
            "test": "aaaaaaaaaaaaaaaaaaaaaaa",
            "hogehoge": "uoooooooooooooooooo",
            "aaa": [
               {
                  "a": 11
               },
               {
                  "a": 12
               },
               {
                  "a": 13
               },
               {
                  "a": 14
               }
            ]
         },
         "id": 198016610469183284
      }
   ]
}
```