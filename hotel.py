from datetime import date
class hotel:
    def __init__(self):
        self.rooms={}
        self.available_rooms ={'std':[101, 102,103],'delux':[201, 202,203],'execu':[301, 302,303]}
        self.roomprice={1:2000, 2:4000, 3:6000}

    def check_in(self,name,address,ph):
        roomtype=int(input("roomtype\n1. Std \n2. Delux \n3. Executive  \nSelect the room type: "))
        if roomtype==1:
            if self.available_rooms['std']:
                room_no=self.available_rooms['std'].pop(0)
            else:
                print("sorry, std rooms are not available")
                return
        if roomtype==2:
            if self.available_rooms['delux']:
                room_no=self.available_rooms['delux'].pop(0)
            else:
                print("sorry, delux rooms are not available")
                return
        if roomtype==3:
            if self.available_rooms['execu']:
                room_no=self.available_rooms['execu'].pop(0)
            else:
                print("sorry, exec rooms are not available")
                return
        else:
            print("choose a valid room type")
        d,m,y=map(int,input("enter chech_in_date in date,month,year: ").split())
        check_in=date(y,m,d)
        self.rooms[room_no]={
            "name":name,
            "address" :address,
            "phone" : ph,
            "chech_in_date" : check_in,
            "room_type" :roomtype,
            "roomservice":0
            }
        print(f"cheked in {name} , {address}  to room: {room_no} on {check_in}")
    
    def room_service(self,room_no):
        if room_no in self.rooms:
            print("-------TEJ'S HOTEL MENU--------")
            print("1. tea = 20 \n2.tiffin(idly,sambar,red chetni,dosa,vada) = 100 \n3.full meals = 150 \n4.snacks = 40 \n5.room_clean = 50 \n6.exit")

            
            while 1:
                select=int(input("what do you want sir(to exit enter 6): "))
                if select == 1:
                    quantity=int(input("enter the quantity "))
                    self.rooms[room_no]['roomservice']+=20*quantity
                elif select == 2:
                    quantity=int(input("enter the quantity "))
                    self.rooms[room_no]['roomservice']+=100*quantity 
                elif select == 3:
                    quantity=int(input("enter the quantity "))
                    self.rooms[room_no]['roomservice']+=150*quantity  
                elif select == 4:
                    quantity=int(input("enter the quantity "))
                    self.rooms[room_no]['roomservice']+=40*quantity
                elif select == 5:
                    quantity=int(input("enter the quantity "))
                    self.rooms[room_no]['roomservice']+=50*quantity
                elif select == 6:
                    break
                else:
                    print("invalid option")
            print("Room sevice rs: ",self.rooms[room_no]['roomservice'],"\n")
            
    def display_occupied_rooms(self):
        if not self.rooms:
            print("no rooms are occupied at the moment")
        else:
            print("Occupied Rooms: ")
            print("--------------------------------------------------------")
            print("Room no.    Name      Phone         place")
            print("--------------------------------------------------------")
            for room,details in self.rooms.items():
                print(room,'\t',details['name'],'\t' ,details['phone'] ,'\t',details['address'])


    def check_out(self,room_number):
        if room_number in self.rooms:
           check_in_date=self.rooms[room_number]["chech_in_date"]
           check_out_date=date.today()
           days=(check_out_date-check_in_date).days

           room_type=self.rooms[room_number]["room_type"]
           if room_type==1:
               self.available_rooms['std'].append(room_number)
           elif room_type==2:
               self.available_rooms['delux'].append(room_number)
           elif room_type==3:
               self.available_rooms['execu'].append(room_number)
        
        total=self.rooms[room_number]['roomservice']
        roombill=self.roomprice[room_type]
        total_bill=total+roombill*days
        print(("-")*50,"TEJ'S HOTEL",("-")*50)
        print(f"check_in_date:{check_in_date.strftime('%d %B %y')}{(" ")*30}check_out_date{check_out_date.strftime('%d %B %y')}")
        print(f"Name:{self.rooms[room_number]['name']}{(" ")*50}Phone_number:{self.rooms[room_number]['phone']}")
        print(f"Address:{self.rooms[room_number]['address']}{(" ")*46}Total_room_bill:{roombill}")
        print(f"Days:{days}{(" ")*49}room_service:{total}")
        print(f"Total_Bill:{total_bill}")
        



    def start_app(self):
        while True:
            print("------------------------")
            print("welcome to TEJ'S Hotel")
            print("1. Check_in")
            print("2. Roomservice")
            print("3. Display occupied rooms")
            print("4. Check_out")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice== '1':
                name=input("Enter your name: ")
                address=input("Enter your address " )
                ph=int(int(input("Enter your phone number ")))
                self.check_in(name,address,ph)
            elif choice=='2':
                room_no=int(input("Enter the roomnumber: "))
                self.room_service(room_no)
        
            elif choice== '3':
                self.display_occupied_rooms()
            elif choice== '4':
                room_number=int(input("Enter the room number "))
                self.check_out(room_number)
            elif choice== '5':
                break
            else:
                print("Invalid choice, please try again")
h=hotel()
h.start_app()




