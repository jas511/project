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
    except:
        return False

def loginuser(data):
    try:
        cursor.execute("SELECT * FROM `users` WHERE username=%s AND password=%s",data)
        return cursor.fetchone()
    except:
        return False
    
def enterbookdetail(data):
    try:
        cursor.execute("INSERT INTO `books` (`bookname`,`authorname`,`location`) VALUES (%s,%s,%s)",data)
        Info.commit()
        return True
    except:
        return False
    
def fetchbookdetails():
    try:
        cursor.execute("SELECT * FROM `books`")
        return cursor.fetchall()
    except:
        return False
    
def fetchissuedetails():
    try:
        cursor.execute("SELECT * FROM `issue`")
        return cursor.fetchall()
    except:
        return False
    
def fetchreturndetails():
    try:
        cursor.execute("SELECT * FROM `issue` WHERE `status` = %s",'r')
        return cursor.fetchall()
    except:
        return False
    
def fetchmemberdetails():
    try:
        cursor.execute("SELECT * FROM `users`")
        return cursor.fetchall()
    except:
        return False
    

def fetchnewspaperdetails():
    try:
        cursor.execute("SELECT * FROM `newspaper`")
        return cursor.fetchall()
    except:
        return False
    
def checkbookavailability(bookname):
    try:
        cursor.execute("SELECT * FROM `books` WHERE `bookname` = %s",bookname)
        return cursor.fetchone()
    except:
        return False
    
def enterissuedetail(details):
    try:
        cursor.execute("INSERT into `issue` (`bookname`,`username`,`id`) VALUES(%s,%s,%s)",details)
        Info.commit()
        return True
    except:
        return False

def enterreturndetail(details):
    try:
        cursor.execute("INSERT into `issue` (`bookname`,`username`,`id`) VALUES(%s,%s,%s)",details)
        Info.commit()
        return True
    except:
        return False