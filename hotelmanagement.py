
#importing mysql connector and naming as mycon
import mysql.connector as mycon
#importing pickle
import pickle

#making connection with mysql
try:
        conn=mycon.connect(host = "localhost" , user = "root" , password = "yourpasswd")
        print("Connected")
except:
        print("Connection Error")

#making connection with the cursor to execute SQL statements        
cur=conn.cursor()

#in order to run the code myltiple times the existing database should be removed and recreated again
cur.execute('drop database hotelmanagement;')
cur.execute('create database hotelmanagement')

#using the database hotelmanagement
cur.execute('use hotelmanagement;')

#creating table hotel_records
cur.execute("create table HOTEL_RECORDS(Cust_ID int primary key unique, Cust_Name varchar(40), Room_ID int, Room_Price int, No_of_Days int );")

#inserting values into the table of hotel_records
cur.execute("insert into HOTEL_RECORDS values(1001, 'Thomas Shelby', 101, 2000, 2);")
cur.execute("insert into HOTEL_RECORDS values(1002, 'Sandra Bullock', 102, 1000, 1);")
cur.execute("insert into HOTEL_RECORDS values(1003, 'Emmanuel Thomas', 105, 3000, 3);")
cur.execute("insert into HOTEL_RECORDS values(1004, 'Vicky Mohan', 106, 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1005, 'Andy Samberg', 107, 2000, 2)")
cur.execute("insert into HOTEL_RECORDS values(1006, 'Pravan Raj', 108, 4000, 4)")
cur.execute("insert into HOTEL_RECORDS values(1007, 'Scaria Fernandes', 110, 2000, 2)")
cur.execute("insert into HOTEL_RECORDS values(1008, 'Maria S', 120, 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1009, 'Albin Braceford M.S.K', 122, 3000, 3)")
cur.execute("insert into HOTEL_RECORDS values(1010, 'Harikeshan R.M', 123,2000,2)")
cur.execute("insert into HOTEL_RECORDS values(1011, 'Leo S.', 125, 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1012, 'Hithesh Vazhyamen', 130, 2000, 2)")
cur.execute("insert into HOTEL_RECORDS values(1013, 'Jefferey Richford', 140, 6000, 6)")
cur.execute("insert into HOTEL_RECORDS values(1014, 'Samuel Wozowski', 154, 2000,2)")
cur.execute("insert into HOTEL_RECORDS values(1015, 'Anupam Baby Jr.', 169, 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1016, 'Mohandas Freds', 175, 2000,2)")
cur.execute("insert into HOTEL_RECORDS values(1017, 'Denny M. Greatruther C.', 180, 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1018, 'Alia Kiran', 189, 2000, 2)")
cur.execute("insert into HOTEL_RECORDS values(1019, 'Inglesias Fluffy', 195, 3000, 3)")
cur.execute("insert into HOTEL_RECORDS values(1020, 'Kenny Seb.', 210 , 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1021, 'Rahul S.', 220, 1000, 1)")
#by this function we can fully enter the data given abpve in the SQL table
conn.commit()

#menu fuction to display at the start of the program
def menu():
    choice='Y' or 'y'
    while choice=='Y' or 'y':
        print()
        print("WElCOME TO CDE HOTEL & RESIDENCY\n")
        print("Choose one of the below options to continue -- \n")
        print("1. Booking a Room")
        print("2. Cancelling the Booking of a room")
        print("3. Show Available Rooms")
        print("4. Extend the stay at the hotel")
        print("5. Checking out of the hotel")
        print("6. To View the Hotel Records (For Authorised Personnel ONLY)\n")
        ch=int(input("Enter the option you would like to choose -- "))
        if ch==1:
            book_room()
        elif ch==2:
            cancel_room()
        elif ch==3:
            avai_rooms()
        elif ch==4:
            extend_stay()
        elif ch==5:
            check_out()
        else:
            print("Please enter a valid option")
    choice=input("Would you like to continue the services -- Press ('Y' for Yes/'N' for No")

def book_room():
    for i in (1000,2001):
        rows=cur.fetchall()
        for row in rows:
            id=randint(i)
            i!=row[0]
            print(row[0])
menu()
        
        
        


            
                        


