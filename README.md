# Disclaimer
I am fine tuning this Progress Openedge SQLalchemy dialect for use in a meltano based data infrastructure improvement at my organization.




# SQLAlchemy dialect for Progress OpenEdge

An adaption of [this work](https://github.com/dholth/progress_sa) for Python3 and Progress OpenEdge 11.7

## Install

```$ git clone https://github.com/dominikpegler/progress_sa.git
$ cd progress_sa
$ python setup.py install
```
## DRIVER_NAME env variable
Due to variation in driver names, create an environment variable called PROGRESS_OE_DRIVER_NAME with your particular driver name and the driver will pull it in and use it. 

## Usage

```python
from sqlalchemy import create_engine
import pandas as pd
import sys

# driver name may vary
pyodbc_str = r"""
    DRIVER={Progress OpenEdge 11.7 Driver};
    HOST=<host>;
    PORT=<port>;
    DB=<db>;
    UID=<user>;
    PWD=<password>;
    DEFAULTSCHEMA=PUB;
"""

if (sys.platform == "win32") | (sys.platform == "win64") | (sys.platform == "win"):
    sa_str = "progress+pyodbc:///?odbc_connect={}".format(pyodbc_connstr)

else:
    sa_str = "progress+pyodbc://<user>:<password>@<host>:<port>/<db>?DEFAULTSCHEMA=PUB"

engine = create_engine(sa_str)

pd.read_sql("""SELECT TOP 10 * FROM sysprogress.systables""", engine)
```

## Use with Apache Superset

Create a file named `progress.py` in `<superset_root_dir>/superset/db_engine_specs` with the following content:

(Not much testing has happened here yet, it's still a very early phase. It might also be possible to integrate the `allow_limit_clause` keyword directly into the dialect. Not sure about it.)

```python
from superset.db_engine_specs.base import BaseEngineSpec

class ProgressBaseEngineSpec(BaseEngineSpec):

    engine = "progress"
    engine_name = "progress"
    allow_limit_clause = False
    allows_alias_in_select = True
    force_column_alias_quotes = True

    _time_grain_expressions = {
    None: "{col}",
    "P1D": "{col}",
    "P1W": "{col} + 1 - DAYOFWEEK({col})", # assuming sunday is the first day of the week
    "P1M": "TO_DATE(TO_CHAR(YEAR({col})) + '-' + TO_CHAR(MONTH({col})) + '-01')",
    "P3M": "TO_DATE(TO_CHAR(YEAR({col})) + '-' + TO_CHAR(3*QUARTER({col})-2) + '-01')",
    "P1Y": "TO_DATE(TO_CHAR(YEAR({col})) + '-01-01')",
}    
```

Create a new database connection in Apache Superset by entering a connection string in this format:
```
progress+pyodbc://<user>:<password>@<host>:<port>/<db>?DEFAULTSCHEMA=PUB
```
