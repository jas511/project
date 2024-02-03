import mysql.connector
import login
Info = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = "",
    db="library")
cursor = Info.cursor()

def registeruser(data):
    try:
        cursor.execute("INSERT INTO `users` (`email`,`username`,`password`) VALUES (%s,%s,%s)",data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

def loginuser(data):
    try:
        cursor.execute("SELECT * FROM `users` WHERE username=%s AND password=%s",data)
        return cursor.fetchone()
    except:
        return False