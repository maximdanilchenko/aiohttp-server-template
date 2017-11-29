## Aiohttp template

It is very basic aiohttp web service template with swagger, 
debugtoolbar, postgres, tests (via pytest) and versioning setup  

Before running the app you should run postgres 
(or another database and edit "app/db.py") or 
comment ```from .db import init_db, close_db``` line 
in "app/__init__.py"

Run app:
```
python main.py
```

Run with gunicorn:
```
> gunicorn -c gunicorn.conf.py -b :$PORT main:app 
```

Run pytest:
```
py.test
```

Debugtoolbar: ```/_debugtoolbar``` (edit in "app/__init__.py")

Swagger: ```/v1/doc``` (edit in "app/__init__.py")


Feel free to use, fork, develop :)
