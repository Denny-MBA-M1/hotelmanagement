
#importing mysql connector and naming as mycon
import mysql.connector as mycon
#importing pickle
import pickle
import random


#making connection with mysql
try:
        conn=mycon.connect(host = "localhost" , user = "root" , password = "yourpasswd")
        print("Connected")
except:
        print("Connection Error")

password1=12345678
#making connection with the cursor to execute SQL statements        
cur=conn.cursor()

#in order to run the code myltiple times the existing database should be removed and recreated again
cur.execute('drop database hotelmanagement;')
cur.execute('create database hotelmanagement')

#using the database hotelmanagement
cur.execute('use hotelmanagement;')

#creating table hotel_records
cur.execute("create table HOTEL_RECORDS(Cust_ID int primary key unique, Cust_Name varchar(40), Check_IN date, Check_Out date, Room_ID int, Room_Price int, No_of_Days int );")

#inserting values into the table of hotel_records

cur.execute("insert into HOTEL_RECORDS values(1001, 'Thomas Shelby', '2022/10/31', '2022/11/02', 101, 2000, 2);")
cur.execute("insert into HOTEL_RECORDS values(1002, 'Sandra Bullock','2022/10/31','2022/11/01', 102, 1000, 1);")
cur.execute("insert into HOTEL_RECORDS values(1003, 'Emmanuel Thomas','2022/10/31','2022/11/03', 105, 3000, 3);")
cur.execute("insert into HOTEL_RECORDS values(1004, 'Vicky Mohan', '2022/10/31','2022/11/01', 106, 1000, 1);")
cur.execute("insert into HOTEL_RECORDS values(1005, 'Andy Samberg','2022/10/31','2022/11/02', 107, 2000, 2)")
cur.execute("insert into HOTEL_RECORDS values(1006, 'Pravan Raj','2022/10/31','2022/11/04', 108, 4000, 4)")
cur.execute("insert into HOTEL_RECORDS values(1007, 'Scaria Fernandes','2022/10/31','2022/11/02', 110, 2000, 2)")
cur.execute("insert into HOTEL_RECORDS values(1008, 'Maria S','2022/10/31','2022/11/01', 120, 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1009, 'Albin Pinoybalakumar M.S.K','2022/10/31','2022/11/03', 122, 3000, 3)")
cur.execute("insert into HOTEL_RECORDS values(1010, 'Harikeshan R.M','2022/10/31','2022/11/02', 123, 2000,2)")
cur.execute("insert into HOTEL_RECORDS values(1011, 'Leo S.','2022/10/31','2022/11/01', 125, 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1012, 'Hithesh Vazhyamen','2022/10/31','2022/11/02', 130, 2000, 2)")
cur.execute("insert into HOTEL_RECORDS values(1013, 'Jefferey Richford','2022/10/31','2022/11/06', 140, 6000, 6)")
cur.execute("insert into HOTEL_RECORDS values(1014, 'Samuel Wozowski','2022/10/31','2022/11/02', 154, 2000,2)")
cur.execute("insert into HOTEL_RECORDS values(1015, 'Anupam Baby Jr.','2022/10/31','2022/11/01', 169, 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1016, 'Mohandas Freds','2022/10/31','2022/11/02', 175, 2000,2)")
cur.execute("insert into HOTEL_RECORDS values(1017, 'Denny M. Greatruther C.','2022/10/31','2022/11/01', 180, 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1018, 'Alia Kiran','2022/10/31','2022/11/02', 189, 2000, 2)")
cur.execute("insert into HOTEL_RECORDS values(1019, 'Inglesias Fluffy','2022/10/31','2022/11/02', 195, 3000, 3)")
cur.execute("insert into HOTEL_RECORDS values(1020, 'Kenny Seb.','2022/10/31','2022/11/01', 210 , 1000, 1)")
cur.execute("insert into HOTEL_RECORDS values(1021, 'Rahul S.','2022/10/31','2022/11/01', 220, 1000, 1)")


#by this function we can fully enter the data given abpve in the SQL table
conn.commit()   

def menu():
    while True:
                print("Welcome to CDE HOTEL & RECIDENCY\n")
                print("Choose one of the following options -- \n")
                print("Press 1 -- To Book for a Hotel Room ")
                print("Press 2 -- To Cancel a Booking")
                print("Press 3 -- To Search you booking")
                print("Press 4 -- To Edit the booking ")
                print("Press 5 -- To find the Hotel Records of Customers (FOR AUTHORISED PERSONNEL ONLY)")
                print("Press 6 -- To Export the list of Hotel Records (FOR AUTHORISED PERSONNEL ONLY)")
                print("Press 7 -- To Exit from this program\n")
                c=int(input("Enter your Choice --  "))
                if c==1:
                    Book_Room()
                elif c == 2:
                    Cancel_Room()
                elif c == 3:
                    Search_Book()
                elif c == 4:
                    Edit_Book()
                elif c == 5:
                    Display_Record()
                elif c == 6:
                    export_record()
                elif c == 7:
                    exit(0)
                else:
                    print("Invalid Choice")

def Book_Room():
    try:
        Cust_ID=random.randint(1000,10000)
        Name=input("Please ENTER your name -- ")
        Check_in=input("Enter the CHECK-IN date (Format - YYYY/MM/DD -- ")
        Check_out=input("Enter the CHECK-OUT date (Format - YYYY/MM/DD -- ")
        Room_Id=int(input("Enter the Room ID you choose -- "))
        Days_Stay=int(input("Enter the Number of days you are staying -- "))
        Room_Price=Days_Stay*1000
        listing=(Cust_ID, Name, Check_in, Check_out, Room_Id, Room_Price, Days_Stay)

        co="insert into Hotel_Records values(%s,%s,%s,%s,%s,%s,%s)"

        cur.execute(co,listing)
        conn.commit()
        print()
        print(" Please wait, your booking is processsing.....")
        print()
        import time
        time.sleep(3)
        print(" **CUSTOMER DETAILS ADDED SUCCESSFULLY** ")
        print()
        print(" GOING BACK TO MENU...\n")
        time.sleep(2)
        print()
        menu()
    except:
        mycon.error
        Cust_ID=random.randint(1000,10000)   

    
def Cancel_Room():
        cnm="delete from hotel_records where id=%s"
        data=cur.fetchall()
        while True:
                Id=int(input("Enter the Booking ID of Customer -- "))
                t=(Id,)
                for row in data:
                        if row[0]==Id:
                               cur.execute(cnm,t)
                               check=True
                        else:
                                pass
        if check!=True:
                print("doesn't exist")
                        
        
                
                

def Search_Book():

                while True:
                        Id=int(input("Enter the Booking ID you want to search for -- "))
                        da=(Id, )
                        df="select Cust_ID, Cust_Name, Check_IN, Check_Out from hotel_records where Cust_ID=%s;"
                        cur.execute(df,da)
                        data=cur.fetchall()
                        for row in data:
                                if row[0]==Id:
                                        print()
                                        print("Please wait.... Fetching Result")
                                        import time
                                        time.sleep(2)
                                        print("Customer ID -- ", row[0],
                                              " Customer Name -- ", row[1],
                                              "Check-IN Date -- ", row[2],
                                              "Check-OUT Date -- ", row[3])
                                        return()
                                else:
                                        pass
                        print("Booking ID doesn't exist")


def Edit_Book():
        
        
        while True:
                Id=int(input("Enter the Booking ID you want to search for -- "))
                dq=(Id,)
                dr="select Cust_ID, Cust_Name, Check_IN, Check_Out, Room_ID, Room_Price, No_of_Days from hotel_records where Cust_ID=%s;"
                cur.execute(dr,dq)
                data=cur.fetchall()
                for row in data:
                        if row[0]==Id:
                                print("Customer ID - ",row[0],"Name - ", row[1], "Check_IN - ", row[2], "Check_Out - ",row[3], "Room ID - ",row[4], "Room Price - ", row[5],
                                      "No of days of stay - ", row[6])
                                print("Enter the changes in the Booking")
                                custid=print("Customer ID -", row[0])
                                name=input("Enter the new name -- ")
                                chck_in=input("Enter the check in date in the format (YYYY,MM,DD)")
                                chck_out=input("Enter the check out date in the format (YYYY,MM,DD)")
                                room_id1=int(input("Enter the room ID to be changed"))
                                days=int(input("Enter the No. of days to stay -- "))
                                room_price=days*1000
                                klist=(custid, name, chck_in, chck_out, room_id1, room_price, days)
                                cj="update hotel_records set Cust_ID=%s, Cust_Name=%s, Check_IN=%s, Check_Out=%s, Room_ID=%s, Room_Price=%s, No_of_Days=%s where Cust_ID=1001"
                                cur.execute(cj,klist)
                                conn.commit()
                                print("Changed")
                                menu()

                                

def Display_Record():
        passw=int(input("Enter the password to continue:"))
        if passw==password1:
                print("Successfully Authorised")
                
                cur.execute("select * from hotel_records")
                data=cur.fetchall()
                print()
                print("Printng Records....")
                print()
                import time
                time.sleep(3)
                for row in data:
                       time.sleep(.1) 
                       print(" ",row,"\n")


menu()
        
        
        
                
        


       
