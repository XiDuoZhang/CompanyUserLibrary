import pyodbc

def read(conn):
    cursor = conn.cursor()
    allUsers = cursor.execute('SELECT * FROM  Users')
    for user in allUsers:
        print(user)

def connection():
    server = 'BIGMUSCLE\SQLEXPRESS'
    database = 'CompanyUsers'

    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server}; SERVER='+ server + ';DATABASE='+ database + ';Trusted_Connection=yes')
    return conn;
#     read(conn)

# read(conn)