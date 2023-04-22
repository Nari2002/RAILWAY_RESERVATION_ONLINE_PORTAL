#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas
import random
import datetime
days=["monday","tuesday","wednesday","thursday","friday"]
wend=["saturday","sunday"]
trname=['krishna exp','palnadu exp','vandebharath','warangal exp','nalgonda exp']
trnum=[52341,54321,21345,13245,43215]
sources1=['guntur jun','nalgonda','vikarabad jun']
sources=['adilabad','nizamabad jun','bhongir','warangal','khammam','nellore','thirupathi']
source2=['secundrabad jun','nalgonda','guntur','nellore','thirupathi']
source3=['secundrabad jun','bhongir','kazipet','warangal']
source4=['secundrabad jun','ghatkesar','chityal','nalgonda']
namest={'TRAINS':trname,"NUMBERS":trnum}
namesw={'TRAINS':trname[0:3],"NUMBERS":trnum[0:3]}
krishna={'krishna exp':sources}
pal={'palnadu exp':sources1}
vb={'vandebharath':source2}
we={'warangal exp':source3}
ne={'nalgonda exp':source4}
seatac=15
seat2ac=20
seatsl=50
AC=1500
AC2=1000
SL=500
seatavalb={"NO. OF SEATS":[seatac,seat2ac,seatsl],"PRICES":[AC,AC2,SL]}
pnr=[]
gname=[]
gage=[]
gaddress=[]
ggender=[]
gpwd=[]
logusers={"NAMES":gname,"AGE":gage,"GENDER":ggender,"ADDRESS":gaddress}
s=''
cust_details={"name":'','age':'','gender':'','source':'','destination':'','seat type':'','no of seats':'','AMOUNT':'','pnr':''}
class users:
    def user(self):
        print("THE ACTIVE USERS IN OUR PORTAL")
        print(pandas.DataFrame(logusers))
class manual_ck(users):
    def manualcheck(self):
            while True:
                self.source=input("enter your source:")
                if self.source in sources:
                    cust_details['source']=self.source
                    break
                elif self.source in sources1:
                    cust_details['source']=self.source
                    break
                elif self.source in source2:
                    cust_details['source']=self.source
                    break
                elif self.source in source3:
                    cust_details['source']=self.source
                    break
                elif self.source in source4:
                    cust_details['source']=self.source
                    break
                else:
                    print("PLASE ENTER CORRECT SOURCE:")
            while True:
                self.destination=input("enter your destination:")
                if self.source==self.destination:
                    print("SORRY PLEASE CHOOSE CORRECT DESTINATION")
                elif self.destination in sources:
                    cust_details['destination']=self.destination
                    break
                elif self.destination in sources1:
                    cust_details['destination']=self.destination
                    break
                elif self.destination in source2:
                    cust_details['destination']=self.destination
                    break
                elif self.destination in source3:
                    cust_details['destination']=self.destination
                    break
                elif self.destination in source4:
                    cust_details['destination']=self.destination
                    break
                else:
                    print("PLEASE ENTER VALID DESTINATION:")
            while True:
                if self.source in sources and self.destination in sources:
                    print("THE AVAILABLE TRAIN IS:",trname[0],"\nTRAIN NUMBER IS:",trnum[0])
                    break
                elif self.source in sources1 and self.destination in sources1:
                    print("THE AVAILABLE TRAIN IS:",trname[1],"\nTRAIN NUMBER IS:",trnum[1])
                    break
                elif self.source in source2 and self.destination in source2:
                    print("THE AVAILABLE TRAIN IS:",trname[2],"\nTRAIN NUMBER IS:",trnum[2])
                    break
                elif self.source in source3 and self.destination in source3:
                    print("THE AVAILABLE TRAIN IS:",trname[3],"\nTRAIN NUMBER IS:",trnum[3])
                    break
                elif self.source in source4 and self.destination in source4:
                    print("THE AVAILABLE TRAIN IS:",trname[4],"\nTRAIN NUMBER IS:",trnum[4])
                    break
                else:
                    print("THERE IS NO TRAIN AVAILABLE IN THIS ROUTE OR CHANGE THE ROUTE\nTRY TO CHECK TRAIN AVAILABILTY")
                    break
    
class create_acc(manual_ck):
    def __init__(self,name='',age='',address='',gender='',pwd=''):
        self.name=name
        self.age=age
        self.address=address
        self.gender=gender
        self.pwd=pwd
    def create(self):
        name=input("ENTER YOUR NAME:")
        gname.append(name)
        age=int(input("ENTER YOUR AGE:"))
        gage.append(age)
        address=input("ENTER YOUR ADDRESS:")
        gaddress.append(address)
        print("\n1:MALE\n2:FEMALE\n3:OTHERS")
        gender=int(input("SELECT YOUR GENDER"))
        if gender==1:
            gender='MALE'
            ggender.append(gender)
        elif gender==2:
            gender='FEMALE'
            ggender.append(gender)
        else:
            gender='OTHERS'
            ggender.append(gender)
        while True:
            pwd=input("CREATE YOUR PASSWORD:")
            pwd1=input("CONFIRM YOUR PASSWORD")
            if pwd==pwd1:
                gpwd.append(pwd)
                print(name,"YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED")
                break
            else:
                print("YOU NEED TO MATCH THE PASSWORD")
    def logg(self):
        while True:
            self.uname=input("ENTER YOUR USER NAME:")
            self.lpwd=input("ENTER YOUR PASSWORD:")
            if self.uname in gname and self.lpwd in gpwd:
                print("WELCOME",self.uname)
                break
            else:
                print("PLEASE CHECK THE DETAILS:")
class train_availability(create_acc):
    def availabilty(self):
        while True:
            self.day=input("ENTER A DAY:")
            if self.day in days:
                print("Trains are available....\nThe Trains are:\n")
                print(pandas.DataFrame(namest,index=['1','2','3','4','5']))
                break
            elif self.day in wend:
                print("weekends may trains are run on rush\nThe Trains are:\n")
                print(pandas.DataFrame(namesw,index=['1','2','3']))
                break
            else:
                print("ENTER CORRECT DAY NAME..")
class src(train_availability):
    def srcs(self):
        while True:
            print("THE TRAINS ARE:\n")
            print(pandas.DataFrame(namest,index=['1','2','3','4','5']))
            print("TO SEE SOURCES FOR YOUR TRAIN:")
            self.source=int(input("ENTER TRAIN NUMBER:"))
            if self.source==trnum[0]:
                print("The sources for your choosen Train is:\n")
                print(pandas.DataFrame(krishna,index=['start/end','1','2','3','4','5','end/start']))
                break
            elif self.source==trnum[1]:
                print("The sources for your choosen Train is:\n")
                print(pandas.DataFrame(pal,index=['start/end','1','end/start']))
                break
            elif self.source==trnum[2]:
                print("The sources for your choosen Train is:\n")
                print(pandas.DataFrame(vb,index=['start/end','1','2','3','end/start']))
                break
            elif self.source==trnum[3]:
                print("The sources for your choosen Train is:\n")
                print(pandas.DataFrame(we,index=['start/end','1','2','end/start']))
                break
            elif self.source==trnum[4]:
                print("The sources for your choosen Train is:\n")
                print(pandas.DataFrame(ne,index=['start/end','1','2','end/start']))
                break
            else:
                print("PLEASE ENTER VALID TRAIN NAME....")
class ticket_book(src):
    def book(self):
        global s
        global seatac
        global seat2ac
        global seatsl
        print('LOGIN TO BOOK TICKETS:')
        self.logg()
        self.manualcheck()
        print("ENTER PASSENGER DETAILS...")
        self.name=input("enter your name:")
        cust_details['name']=self.name
        self.age=int(input("enter your age:"))
        cust_details['age']=self.age
        self.gender=input("enter your gender:")
        cust_details['gender']=self.gender
        while True:
            self.seat=input("\n1:AC\n2:2AC\n3:SLEEPER CLASS\nEnter your seat type:")
            if self.seat=='1':
                cust_details['seat type']="AC"
                self.nseats=int(input("ENTER NO OF TICKETS:"))
                if self.nseats<=seatac:
                    cust_details['no of seats']=self.nseats
                    self.total=self.nseats*AC
                    seatac=seatac-self.nseats
                    print("EACH TICKET =",AC,"TOTAL AMOUNT IS:\t",self.total)
                    cust_details['AMOUNT']=self.total
                    break
                else:
                    print("NO SEATS AVAILABLE PLEASE CHECK SEAT AVAILABILITY")
            elif self.seat=='2':
                if self.nseats<=seat2ac:
                    cust_details['seat type']="2AC"
                    self.nseats=int(input("ENTER NO OF TICKETS:"))
                    cust_details['no of seats']=self.nseats
                    self.total=self.nseats*AC2
                    seat2ac=seat2ac-self.nseats
                    print("EACH TICKET =",AC2,"TOTAL AMOUNT IS:\t",self.total)
                    cust_details['AMOUNT']=self.total
                    break
                else:
                    print("NO SEATS AVAILABLE PLEASE CHECK SEAT AVAILABILITY")
            elif self.seat=='3':
                if self.nseats<=seatsl:
                    cust_details['seat type']="SLEEPER CLASS"
                    self.nseats=int(input("ENTER NO OF TICKETS:"))
                    cust_details['no of seats']=self.nseats
                    self.total=self.nseats*SL
                    seatsl=seatsl-self.nseats
                    print("EACH TICKET =",SL,"TOTAL AMOUNT IS:\t",self.total)
                    cust_details['AMOUNT']=self.total
                    break
                else:
                    print("NO SEATS AVAILABLE PLEASE CHECK SEAT AVAILABILITY")
            else:
                print("PLEASE CHOOSE VALID SEAT TYPE:")
        print("PRESS 1 TO CONFIRM\nPRESS OTHER TO EXIT:")
        self.con=int(input())
        if self.con==1:
            print(self.name," your booking is successful:")
            t=datetime.datetime.now()
            print(t)
            print("YOUR PNR NUMBER IS::")
            for i in range(13):
                self.r=random.randint(0,9)
                print(self.r,end="")
                s+=str(self.r)
            cust_details['pnr']=int(s)
            print("\nYOUR DETAILS ARE:")
            print(pandas.DataFrame(cust_details,index=['1']))
            print()
        else:
            exit()
class cancel_ticket(ticket_book):
    def cancel(self):
        print("1:BY MISTAKE I BOOKED\n2:PLAN CANCELLED\n3:EXIT")
        self.options=input("WHY YOU WANT TO CANCEL TICKET")
        if self.options==1 or 2:
            self.N=int(input("ENTER YOUR PNR NUMBER:"))
            if self.N==cust_details['pnr']:
                cust_details.clear()
                print("YOUR TICKET HAS BEEN CANCELLED SUCCESSFULLY")
                t=datetime.datetime.now()
                print(t)
                print("YOUR CANCELLATION ID IS::")
                for i in range(13):
                    self.r=random.randint(0,9)
                    print(self.r,end="")
        else:
            exit()
class seat_aval(cancel_ticket):
    def __init__(self,choice=''):
        self.choice=choice
    def seats(self):
        print("THE TRAINS ARE:\n")
        print(pandas.DataFrame(namest,index=['1','2','3','4','5']))
        while True:
            choice=int(input("ENTER TRAIN NUMBER TO VIEW SEATS:"))
            if choice in trnum:
                print(pandas.DataFrame(seatavalb,index=['AC','2AC','SLEEPER CLASS']))
                break
            else:
                print("PLAESE CHOOSE CORRECT TRAIN:")
class check_previous(seat_aval):
    def __init__(self,previous=''):
        self.previous=previous
    def prev(self):
        print('LOGIN TO VIEW YOUR PREVIOUS BOOKINGS:')
        self.logg()
        print("\nYOUR PREVIOUS BOOKINGS ARE...:")
        print(pandas.DataFrame(cust_details,index=['1']))
class check_pnr(check_previous):
    def cpnr(self):
        while True:
            self.check=int(input("ENTER YOUR PNR NUMBER:"))
            if self.check==cust_details['pnr']:
                print(pandas.DataFrame(cust_details,index=['1']))
                break
            else:
                print("PLEASE CHECK PNR NUMBER")

class menu(check_pnr):
    def __init__(self,choice=''):
        self.choice=choice
    def main_menu(self):
        while True:
            print("------------------------WELCOME-------------------------")
            print("--------------------INDIAN RAILWAYS---------------------")
            print("---------------------ONLINE PORTAL----------------------")
            print("1:CREATE ACCOUNT\n2:LOGIN\n3:TRAIN AVAILABILITY\n4:SOURCES FOR SELECTED TRAIN\n5:SEAT AVAILABILITY\n6:BOOK A TICKET\n7:CANCEL A TICKET\n8:CHECK PREVIOUS BOOKINGS\n9:CHECK PNR\n10:CHECK TRAINS BY YOUR LOCATION\n11:USERS IN OUR PORTAL\n12:EXIT")
            choice=int(input("ENTER YOUR CHOICE:"))
            if choice==1:
                self.create()
            elif choice==2:
                self.logg()
            elif choice==3:
                self.availabilty()
            elif choice==4:
                self.srcs()
            elif choice==5:
                self.seats()
            elif choice==6:
                self.book()
            elif choice==7:
                self.cancel()
            elif choice==8:
                self.prev()
            elif choice==9:
                self.cpnr()
            elif choice==10:
                self.manualcheck()
            elif choice==11:
                self.user()
            elif choice==12:
                print("---------------------THANK YOU------------------------")
                print("------------------INDIAN RAILWAYS---------------------")
                print("EXITED....")
                break
            else:
                print("PLEASE CHOOSE VALID OPTION:")

m=menu()
m.main_menu()
        


# In[ ]:




