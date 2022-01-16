def a_connect():  #the first function
    import mysql.connector
    mydb = mysql.connector.connect(host="34.133.7.196", user="root")
    if mydb.is_connected() == False:
        return("error connecting to MySQL")
    mycursor =  mydb.cursor()
    try:
        mycursor.execute("DROP database IF EXISTS todolist")
        mycursor.execute("CREATE database todolist")
    except:
        return("error creating databse")
    return

def connect1(): #used by other functions to skip duplication
    import mysql.connector
    mydb = mysql.connector.connect(host="34.133.7.196", user="root", database="todolist")
    if mydb.is_connected() == False:
        exit()
    cursor = mydb.cursor()
    return mydb 
    
def b_create_room():  #the second function
    import random
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    roomno = ""
    for i in range(0,4):
        no = random.randint(0,25)
        roomno += s[no]
    mydb = connect1()
    if mydb.is_connected() == False:
      return "","error connecting to MySQL"
    cursor = mydb.cursor()
    cursor.execute("create table %s(Name varchar(20) Primary key,Creator varchar(20),ctime varchar(20),Doer varchar(20),stime varchar(20),Completer varchar(20),etime varchar(20))"%(roomno))
    return roomno

def c_create_task(Tname,creator,roomno):  #third function
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time24 = current_time
    if int(time24[0:2]) > 12:
        current_time = "%d:%s %s"%(int(time24[0:2])-12,time24[3:5],"pm")
    elif int(time24[0:2]) == 12:
        current_time = "%d:%s %s"%(12,time24[3:5],"pm")
    elif int(time24[0:2]) < 12:
        current_time = "%d:%s %s"%(int(time24[0:2]),time24[3:5],"am")
    mydb = connect1()
    if mydb.is_connected() == False:
      return "","error connecting to MySQL"
    cursor = mydb.cursor()
    cursor.execute("insert into {} values('{}','{}','{}',NULL,NULL,NULL,NULL)".format(roomno,Tname,creator,current_time))
    mydb.commit()
    return

def d_start_task(Tname,doer_name,roomno):  #fourth function
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time24 = current_time
    if int(time24[0:2]) > 12:
        current_time = "%d:%s %s"%(int(time24[0:2])-12,time24[3:5],"pm")
    elif int(time24[0:2]) == 12:
        current_time = "%d:%s %s"%(12,time24[3:5],"pm")
    elif int(time24[0:2]) < 12:
        current_time = "%d:%s %s"%(int(time24[0:2]),time24[3:5],"am")
    mydb = connect1()
    if mydb.is_connected() == False:
      return "","error connecting to MySQL"
    cursor = mydb.cursor()
    cursor.execute("update {} set Doer='{}',stime='{}' where Name='{}'".format(roomno, doer_name, current_time, Tname))
    mydb.commit()
    return 

def e_complete(Tname,doer_name,roomno):  #fifth function
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time24 = current_time
    if int(time24[0:2]) > 12:
        current_time = "%d:%s %s"%(int(time24[0:2])-12,time24[3:5],"pm")
    elif int(time24[0:2]) == 12:
        current_time = "%d:%s %s"%(12,time24[3:5],"pm")
    elif int(time24[0:2]) < 12:
        current_time = "%d:%s %s"%(int(time24[0:2]),time24[3:5],"am")
    mydb = connect1()
    if mydb.is_connected() == False:
      return "","error connecting to MySQL"
    cursor = mydb.cursor()
    cursor.execute("update {} set completer='{}',etime='{}' where Name='{}'".format(roomno, doer_name, current_time, Tname))
    mydb.commit()
    return 

def f_retrieve(roomno):  #sixth function
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    mydb = connect1()
    if mydb.is_connected() == False:
      return "","error connecting to MySQL"
    cursor = mydb.cursor()
    cursor.execute("select* from {}".format(roomno))
    rec = cursor.fetchall()
    return rec

##if __name__=="__main__":
##    s=b_create_room()
##    c_create_task("clean","aaron",s)
##    print(d_start_task("clean", "amarnath",s))
##    print(e_complete("clean","amarnath",s))
##    print(f_retrieve(s))
