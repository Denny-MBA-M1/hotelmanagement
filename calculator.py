#importing the mysql connector module
import mysql.connector as mycon
#establishing connection with the mysql conenctor
conn=mycon.connect(host='localhost', user='root', password='yourpasswd')
if conn.is_connected():
    print("Connected")
#establishing connection with the mysql cursor
cur=conn.cursor()
#printing the databases in mysql
cur.execute('Show databases')

#dropping existing database hotelmanagement
cur.execute("drop database hotelmanagement;")
#recreating database hotelmanagement in order to run the program multiple times
cur.execute("create database hotelmanagement;")
#listing the final databases list
cur.execute("show databases;")

