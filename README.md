# SQLAlchemy dialect for Progress OpenEdge

An adaption of [this work](https://github.com/dholth/progress_sa) for Python3 and Progress OpenEdge 11.7

## Install

```$ git clone https://github.com/dominikpegler/progress_sa.git
$ cd progress_sa
$ python setup.py install
```

## Usage

```python
from sqlalchemy import create_engine

pyodbc_connstr = r'DRIVER={Progress OpenEdge 11.7 Driver};HOST=<host>;PORT=<port>;DB=<db>;UID=<user>;PWD=<password>;DEFAULTSCHEMA=PUB;'

connstr = 'progress+pyodbc:///?odbc_connect={}'.format(pyodbc_connstr)
engine = create_engine(connstr)
```
