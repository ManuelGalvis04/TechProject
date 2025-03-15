import pyodbc

def get_db_connection():
    server = 'localhost'  # Cambia esto por el nombre de tu servidor
    database = 'MasterDataDB'  # Cambia esto por el nombre de tu base de datos
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=' + server + ';'
        'DATABASE=' + database + ';'
        'Trusted_Connection=yes;'
    )
    conn = pyodbc.connect(conn_str)
    return conn
