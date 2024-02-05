import mysql.connector
Info = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = "",
    db="library")
cursor = Info.cursor()


def loginadmin(data):
    try:
        cursor.execute("SELECT * FROM `admin` WHERE username=%s AND password=%s",data)
        return cursor.fetchone()
    except:
        return False