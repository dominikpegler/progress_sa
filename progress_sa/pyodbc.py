from progress_sa.base import ProgressDialect, ProgressExecutionContext
from sqlalchemy.connectors.pyodbc import PyODBCConnector
from sqlalchemy import util
import sys


class ProgressExecutionContext_pyodbc(ProgressExecutionContext):
    pass


class Progress_pyodbc(PyODBCConnector, ProgressDialect):
#    pyodbc_driver_name = 'Progress OpenEdge Wire Protocol'
    pyodbc_driver_name = 'DataDirect 7.1 Progress OpenEdge Wire Protocol'
    execution_ctx_cls = ProgressExecutionContext_pyodbc
    def __init__(self, **kwargs):
        super(Progress_pyodbc, self).__init__(**kwargs)

    # supposed to override the original method from SQLAlchemy's connectors/pyodbc.py
    def create_connect_args(self, url):
        opts = url.translate_connect_args(username="user")
        opts.update(url.query)

        keys = opts

        query = url.query

        connect_args = {}
        for param in ("ansi", "unicode_results", "autocommit"):
            if param in keys:
                connect_args[param] = util.asbool(keys.pop(param))

        if "odbc_connect" in keys:
            connectors = [util.unquote_plus(keys.pop("odbc_connect"))]
        else:

            def check_quote(token):
                if ";" in str(token):
                    token = "{%s}" % token.replace("}", "}}")
                return token

            keys = dict((k, check_quote(v)) for k, v in keys.items())

            dsn_connection = "dsn" in keys or (
                "host" in keys and "database" not in keys    
            )
            
            if dsn_connection:
                connectors = [
                    "dsn=%s" % (keys.pop("host", "") or keys.pop("dsn", ""))
                ]
            else:
                port = ""
                if "port" in keys and "port" not in query:
                    port = "%d" % int(keys.pop("port"))

                connectors = []
                driver = keys.pop("driver", self.pyodbc_driver_name)
                if driver is None and keys:
                    # note if keys is empty, this is a totally blank URL
                    util.warn(
                        "No driver name specified; "
                        "this is expected by PyODBC when using "
                        "DSN-less connections"
                    )
                else:
                    connectors.append("DRIVER={%s}" % driver)
                connectors.extend(
                    [
                        "HOST=%s" % keys.pop("host", ""),
                        "PORT=%s" % port,
                        "DB=%s" % keys.pop("database", ""),
                    ]
                )

            user = keys.pop("user", None)
            if user:
                connectors.append("UID=%s" % user)
                pwd = keys.pop("password", "")
                if pwd:
                    connectors.append("PWD=%s" % pwd)
            else:
                authentication = keys.pop("authentication", None)
                if authentication:
                    connectors.append("Authentication=%s" % authentication)
                else:
                    connectors.append("Trusted_Connection=Yes")

            # if set to 'Yes', the ODBC layer will try to automagically
            # convert textual data from your database encoding to your
            # client encoding.  This should obviously be set to 'No' if
            # you query a cp1253 encoded database from a latin1 client...
            if "odbc_autotranslate" in keys:
                connectors.append(
                    "AutoTranslate=%s" % keys.pop("odbc_autotranslate")
                )

            connectors.extend(["%s=%s" % (k, v) for k, v in keys.items()])

        return [[";".join(connectors)], connect_args]
        
        
        
dialect = Progress_pyodbc
