# Play with Alembic

For database migrations in Python.

## Setup

To reproduce this repository you will need:

- A bash shell
- Docker installed
- Python 3.9 or above

### Set up Python environment

To install the required Python dependencies first create a virtual environment
and use `pip` to install dependencies from the
[`requirements.txt`](./requirements.txt) file.

```bash
# create a virtual environment
python -m venv venv

# activate the virtual environment
. venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

## Applying migrations

You can apply a migration with:

```bash
alembic upgrade head
```

## Checking after migrations

With `psql` installed you can check after you've run a migration that the table
exists with:

```bash
psql -h localhost -U postgres -p 5432 -d newsletter -c "select * from test;"
```
