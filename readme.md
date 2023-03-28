## Futuretech api_ft readme

### header file and pycharm conf

```
 # NA.
```

 * to set up the header, if you are using pycharm
 * goto -> setting -> editor -> file and header template -> create a header.py -> add into *.py as  ```#parse ("header.py")```

### This is a Model-Controller API soft which uses routes and CORS.

 * FLASK as the framework docs -> https://flask.palletsprojects.com/en/2.2.x/
 * use FLASK SQLalchemy docs -> https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/
 * use FLASK CORS docs -> https://flask-cors.readthedocs.io/en/latest/
 * use FLASK RESTful docs -> https://flask-restful.readthedocs.io/en/latest/
 * use FLASK Migration docs -> https://flask-migrate.readthedocs.io/en/latest/
 * use Alembic docs -> https://alembic.sqlalchemy.org/en/latest/
 * use PyJWT docs -> https://pyjwt.readthedocs.io/en/stable/

### Installation of the system

 * install nodejs v18.13.0
 * install python v3.11.0 
 * install mysql v5.7.0 (require python V3.7.0 for install connector for python, uninstall and install python v3.11.0 after installed mySQL)

### Running the system and setup

 * Create a ".env" file from ".env.sample"
 * FLASK_APP should be the main running *.py file (apprun.py)
 * Set the SQL URI of the MySQL connection with username and password (port default 3306)

 ```shell
  # Windows env after you have clone from git
  C:... > cd to the location of the main system file
  C:... > py -m venv .venv
  C:... > .venv\scripts\activate
  (.venv) C:... > pip install -r requirements.txt
  (.venv) C:... > flask run 
 ```
 
 * The system should run and listen to 127.0.0.1:8080, or urs set address or ip addr:8080

### Running migration (code first approach)

 * You need to create the model under dir "..app\models\...*.py" -> create a class

```python   
    import uuid
    from app import db
    from app.models.datasource.DataSourceBase import BaseObject
    from sqlalchemy_utils import UUIDType

class something(db.model):
    __tablename__ = "table name"

    id = db.Column('id', UUIDType(binary = False), primary_key = True, default = uuid.uuid4)

    def __init__(self):
        self.id = uuid.uuid4()
```

 * Create Schema of the table and change SQL URI accordingly in the .env or/and config.py under dir "..app\config.py"
```
  C:.. > cd to the location of the main system file
  C:... > .venv\scripts\activate 
  (.venv) C:... > py -m flask db init # if the dir "migration" folder not exists
  (.venv) C:... > py -m flask db migrate # if any changes to new models added
  (.venv) C:... > py -m flask db upgrade # migrate into the database schema
```
 * To create custom revision ```py -m flask db revision```, or without ```py -m```

### File Directory explanation
```bash
|--- app
|   |--- models
|       |--- __init__.py (all models call for migration and packagae call) 
|       |--- datasource (all database models ORM)
|       |--- dataobject (all data object to be use within the app)
|   |--- repositories (repo which contact ORM data object from ..models which to save, update, delete, alter)
|       |--- __init__.py (all repo rundown for package call)
|   |--- rest
|       |--- functions (helper for https api class)
|           |--- __init__.py
|       |--- https (all restful api call method class)
|           |--- __init__.py
|               |--- admin
|                   |--- __init__.py (admin https packages)
|               |--- frontend
|                   |--- __init__.py (frontend https packages)
|   |--- services (all logic class and algorithm are here as weel calling 3rd party APIs)
|       |--- __init__.py (all services rundown for package call)
|       |--- *.py
|   |--- __init__.py (app package init)
|   |--- config.py (system configuration & load .env)
|--- migrations (auto) 
|--- route
|   |--- __init__.py (route package)
|   |--- admin.py (admin route for ..rest api </api/admin>)
|   |--- frontend.py (frontend route for ..rest api </api/frontend>)
|--- apprun.py (main run file)
|--- .env (system configuration)
```

### After run, use postmen to register by using URLs if frontend is not ready

 * <url>/api/admin/register
```json
    {
        "role": "", # it will seed when run migration current "admin"/"user"
        "name": "",
        "email": "",
        "password": ""
    }
```
 * <url>/api/admin/login
```python
    # In Source should
    response = requests.get(url, auth=HTTPBasicAuth('<username>', '<password>'))
```
 * using postmen go to Authorization
 * choose Basic Auth -> key in your username and password
 * token should generate
 * and put into environment as "x-access-tokens" to use in Authentication for api