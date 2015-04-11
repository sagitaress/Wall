__author__ = 'Faaiz'
import psycopg2
from Member import *


class MemberStorage():
    def __init__(self,system):
        self.system = system
        try:
            self.db = psycopg2.connect(database='Wall',user='postgres',password='pP3819269')
            self.db.autocommit=True
            self.cur = self.db.cursor()
        except:
            print('error')

    def checkLogin(self,username,password):
        self.cur.execute("SELECT * FROM members WHERE username = '"+username+"' and password = '"+password+"'")

        row= self.cur.fetchall()
        if len(row)==0:
            return
        row = row[0]
        if len(row)==0:
            print('password or username is incorrect')
        else:
            return Member(username=row[0],password=row[1],firstname=row[2],lastname=row[3],email=row[4],wallId=row[5])

    def checkSignup(self,username,password,first,last,email):
        self.cur.execute("SELECT username FROM members WHERE username = '"+username+"'")
        if len(self.cur.fetchall())==0:
            self.addMember(username,password,first,last,email)
            return True
        return False

    def addMember(self,username,password,first,last,email):
        self.cur.execute("SELECT count(*) from members")
        wallid = self.cur.fetchone()[0]
        self.cur.execute("INSERT INTO members(username,password,firstname,lastname,email,wallid)"+
                         "VALUES('"+username+"', '"+password+"', '"+first+"', '"+last+"', '"+email
                         +"', '"+str(wallid)+"')")