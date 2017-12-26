Employee Manager
====
API to manage employees' information, such as name, e-mail and department.

## How to Setup

### With Docker
1. Clone the project.
2. `cd employee_manager`
3. `docker-compose up --build` or `sudo docker-compose up --build -d` (daemon)

### Without Docker
1. Create and active a Python3 [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/):
    * `mkvirtualenv manager` to create a virtualenv called manager.
    * `workon manager` to active the virtualenv whenever you work on the project

2. Install the requirements:
    * `pip install config/requirements/dev.pip`

3. Create a `project.env` file inside the `src` folder with some configurations (Example):
```
DEBUG=True
DATABASE_URL=postgres://pguser:pgpassword@host/databasename
SECRET_KEY=+x$q@du#gz@bkf4ow!eu6=vl0uxs&5e&slw$&0th4+q$n(rg%c
```

4. And run!
    * `python src/manage.py runserver`

## Docs
To see the docs, run the project and go to `/docs/` page.