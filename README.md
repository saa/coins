Simple account/transactions model with a RESTful API
----------------------------------------------------


# Requirements

 - Python 3
 - virtualenv
 - PostrgreSQL 9.5 or higer

### PostgreSQL:

 1. Create user `coins` with password `coins`: `CREATE USER coins WITH password 'coins';`
 2. Create database coins: `CREATE DATABASE coins;`
 3. Grant: `GRANT ALL ON DATABASE coins TO coins;`
 4. Grant createdb: `ALTER USER coins WITH createdb;`

# Build project


### Install virtualenv

```
pip install virtualenv --user
```

### Create and activate virtualenv

```
virtualenv -p python3 /tmp/coins-env
source /tmp/coins-env/bin/activate
```

### Install requirements

```
pip install -r requirements.txt
```

### Run migration

Got to project dir and run:

```
manage.py migrate
```


# Run tests

```
./manage.py test
```


# Run application


```
./manage.py runserver
```
