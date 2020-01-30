def getAllUsers(conn):
    cursor = conn.cursor()
    allUsers = cursor.execute('SELECT * FROM  Users')
    return allUsers