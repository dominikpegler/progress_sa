from progress_sa.base import ProgressDialect, ProgressExecutionContext
from sqlalchemy.connectors.pyodbc import PyODBCConnector
from sqlalchemy.util import asbool
import sys


class ProgressExecutionContext_pyodbc(ProgressExecutionContext):
    pass

class Progress_pyodbc(PyODBCConnector, ProgressDialect):
    pyodbc_driver_name = 'Progress OpenEdge Wire Protocol'
    execution_ctx_cls = ProgressExecutionContext_pyodbc

    def __init__(self, **kwargs):
        super(Progress_pyodbc, self).__init__(**kwargs)

dialect = Progress_pyodbc
