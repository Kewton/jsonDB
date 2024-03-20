# LocalJsonDB

"LocalJsonDB" is a lightweight database that allows you to easily manage json format data locally.

# Features
* Improving development efficiency
    - You can use schema-managed jsonDB by simply defining the schema as a class property and inheriting some base classes.
    - You can register, read, update and delete data without writing queries.
    - Quality is improved because a schema can be defined for each json file.
- Improving code maintainability
    - Improves code maintainability by automatically generating mappings between objects and database files.

# Requirement

* python >=3.11
* pysondb
* pydantic


# Installation

Install LocalJsonDB with pip command.

```bash
pip install git+https://github.com/Kewton/jsonDB
```

# Usage
1. Please create python code named "myStreamlit.py".
    ```python
    from localjsondb.jsonDB import ValidatedSchemaFactory, BaseJsonDbORM, DoFactory


    class _MyStreamlitProp:
        formname: str
        keyname: str
        value: dict

    class _MyStreamlitSchema(_MyStreamlitProp, ValidatedSchemaFactory):
        pass

    class MyStreamlitDo(_MyStreamlitProp, DoFactory):
        pass

    class MyStreamlitOrm(BaseJsonDbORM):
        dbpath = "./mydb/system"
        schema = _MyStreamlitSchema 

        def __init__(self, _dbname):
            self.dbname = _dbname
            super().__init__()
        
    MyStremalit = MyStreamlitOrm("myStreamlit")
    ```
1. Please create python code named "datamanipulate.py".
    ```python
    from myStreamlit import MyStreamlitDo, MyStremalit


    if __name__ == '__main__':
        myStreamlitDo = MyStreamlitDo()
        myStreamlitDo.formname = "main"
        myStreamlitDo.keyname = "form_menu"
        myStreamlitDo.value = {
            "form_menu":[
                "chat",
                "Document registration",
                "Document editing"
            ]
        }

        MyStremalit.upsertByprimaryKey(myStreamlitDo)
    ```
1. Run "datamanipulate.py"
    ```bash
    python datamanipulate.py
    ```
1. Check the contents of "./mydb/system/myStreamlit.json" with a text editor
    ```
    {
    "data": [
        {
            "registration_date": "20240308223121194049",
            "formname": "main",
            "keyname": "form_menu",
            "value": {
                "form_menu": [
                "chat",
                "Document registration",
                "Document editing"
                ]
            },
            "id": 751105024836777431
        }
    ]
    }
    ```

# Note

Tested only on windows and mac. Other OSs have not been tested.


# Development
## How to build a development environment?
* Install the required libraries.
    - For winddows
    ```bash
    git clone https://github.com/Kewton/jsonDB
    cd jsonDB
    python -m venv .venv
    .venv\Scripts\activate.ps1
    .venv\Scripts\python.exe -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install pytest
    pip install mkdocs
    ```

    - For mac
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    # deactivate
    pip install -r requirements.txt
    pip install pytest
    pip install mkdocs
    ```

## How to run the tutorial?
We provide tutorials for registering, reading, updating, and deleting.
* If you want to run the "Registering" tutorial, Run "tutorial1_regist.py"
    ```bash
    python .\tutorial\tutorial1_regist.py 
    ```
* If you want to run the "Reading" tutorial, Run "tutorial2_read.py"
    ```bash
    python .\tutorial\tutorial2_read.py 
    ```
* If you want to run the "Updating" tutorial, Run "tutorial3_update.py"
    ```bash
    python .\tutorial\tutorial3_update.py 
    ```
* If you want to run the "Deleting" tutorial, Run "tutorial4_delete.py"
    ```bash
    python .\tutorial\tutorial4_delete.py 
    ```

## How to run unit tests?
* Run "test_my_module.py"
    ```bash
    pytest ./tests/test_my_module.py
    ```

## How to test your documentation?
* Run mkdocs
    ```bash
    mkdocs serve
    mkdocs build
    ```

# License

"LocalJsonDB" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

Enjoy civic development!

Thank you!
