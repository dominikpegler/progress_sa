from progress_sa.base import ProgressDialect, ProgressExecutionContext
from sqlalchemy.connectors.pyodbc import PyODBCConnector
from sqlalchemy.util import asbool
import sys


class ProgressExecutionContext_pyodbc(ProgressExecutionContext):
    pass

class Progress_pyodbc(PyODBCConnector, ProgressDialect):
    pyodbc_driver_name = "DataDirect 7.1 Progress OpenEdge Wire Protocol" #"Progress OpenEdge 11.7 Driver"
    execution_ctx_cls = ProgressExecutionContext_pyodbc

    def __init__(self, description_encoding='latin-1', **kwargs):
        super(Progress_pyodbc, self).__init__(**kwargs)
        self.description_encoding = description_encoding

dialect = Progress_pyodbc
