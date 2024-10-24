import pyodbc

# Configura tu conexión a SQL Server
conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=serverCliente;'
        'Trusted_Connection=yes;'
    )
cursor = conn.cursor()
