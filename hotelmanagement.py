import mysql.connector as mycon
conn=mycon.connect(host="localhost", user="root", password="D@en#n#y@2004#")
if conn.is_connected():
    print("connected")
cur=conn.cursor()
cur.execute('Show databases')
print("The databaases in the server are:")
for db in cur:
    print(db)
cur.close()

conn= mycon.connect(host="localhost", user="root", password="D@en#n#y@2004#", )
cur=conn.cursor()
cur.execute("drop database HOTELMANAGEMENT")
cur.execute("Create database HOTELMANAGEMENT")
cur.close()

cur.execute('Show databases')


conn=mycon.connect(host="localhost", user="root", password="D@en#n#y@2004#", database="hotelmanagement")
cur=conn.cursor()
cur.close()

cur.execute("create table empd(CUSTID int Primary key, Name varchar(50),CUT_ADDRESS varchar(50),CUST_AGE int)")
cur.execute("show tables")

