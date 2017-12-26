Simple account/transactions model with a RESTful API
----------------------------------------------------


# Requirements

 - Python 3
 - virtualenv
 - PostrgreSQL 9.5 or higer

### PostgreSQL:

```
psql < pg.sql
```

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

### Run migration and load fixtures

Got to project dir and run:

```
manage.py migrate
./manage.py loaddata accounts
```


# Run tests

```
./manage.py test
```


# Run application


```
./manage.py runserver
```


# Manual tests

### Get list of accounts:

```
curl http://127.0.0.1:8000/v1/accounts
```

### Create payment

```
curl -X POST -H 'content-type: application/json' -d '{"from_account": "bob123", "to_account": "alice456", "amount": 100}' http://127.0.0.1:8000/v1/payments
```

### Get list of payments

```
curl http://127.0.0.1:8000/v1/accounts
```
