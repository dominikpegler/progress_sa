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

# driver name may vary
pyodbc_connstr = r'DRIVER={Progress OpenEdge 11.7 Driver};HOST=<host>;PORT=<port>;DB=<db>;UID=<user>;PWD=<password>;DEFAULTSCHEMA=PUB;'

connstr = 'progress+pyodbc:///?odbc_connect={}'.format(pyodbc_connstr)
engine = create_engine(connstr)
```

## Use with Apache Superset

Create a file named `progress.py` in `<superset_root_dir>/superset/db_engine_specs` with the following content:

(Not much testing has happened here yet, it's still a very early phase. It might also be possible to integrate the `allow_limit_clause` keyword directly into the dialect. Not sure about it.)

```python
from superset.db_engine_specs.base import BaseEngineSpec

class ProgressBaseEngineSpec(BaseEngineSpec):
    """Abstract class for Postgres 'like' databases"""

    engine = "progress"
    engine_name = "progress"
    allow_limit_clause = False
    
```
