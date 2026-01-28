#---------class user----------


#---------class room-----------
class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.booked = False

#---------class booking---------
def __init__(self, bid, username, name, phone, room, checkin, checkout, days, total):
        self.bid = bid
        self.username = username
        self.name = name
        self.phone = phone
        self.room = room
        self.checkin = checkin
        self.checkout = checkout
        self.days = days
        self.total = total
        self.paid = False

#--------class hotelsystem--------

class HotelSystem:
    def __init__(self):
        self.users = [User("admin123", "admin123", "admin")]
        self.rooms = [
            Room(101, "Standard", 500000),
            Room(102, "Deluxe", 800000),
            Room(103, "VIP", 1200000)
        ]
        self.bookings = []
        self.bid = 1
    # ---------- REGISTER ----------
    

    # ---------- LOGIN ----------
    

    # ---------- VIEW ROOMS ----------
    
    def show_rooms(self):
        print("\nROOM LIST")
        for r in self.rooms:
            status = "Booked" if r.booked else "Available"
            print(r.number, "|", r.room_type, "|", r.price, "|", status)
    # ---------- VIEW CUSTOMERS (ADMIN) ----------
   

    # ---------- BOOK ROOM ----------
    def book_room(self, username):
        print("\nBOOK ROOM")
        name = input("Full name: ")
        phone = input("Phone (10 digits): ") #dang ky phong

        if not phone.isdigit() or len(phone) != 10:#neu nhap sai so dien thoai
            print("Invalid phone number!")
            return

        try:
            room_num = int(input("Room number: "))
        except:
            print("Invalid room number!")
            return

        checkin = input("Check-in (dd/mm/yyyy): ")
        checkout = input("Check-out (dd/mm/yyyy): ")#luu ngay nhan phong

        try:
            ci = datetime.strptime(checkin, "%d/%m/%Y")
            co = datetime.strptime(checkout, "%d/%m/%Y")
        except:
            print("Invalid date format!")
            return

        if co <= ci:
            print("Check-out must be after check-in!")
            return

        for r in self.rooms:
            if r.number == room_num:
                if r.booked:
                    print("Room already booked!")
                    return

                days = (co - ci).days
                total = days * r.price
                r.booked = True

                self.bookings.append(
                    Booking(self.bid, username, name, phone,
                            room_num, checkin, checkout, days, total)
                )

                print("Booking successful!")
                print("Booking ID:", self.bid)
                print("Total price:", total)
                self.bid += 1
                return

        print("Room not found!")

    # ---------- CANCEL BOOKING ----------
    
 def cancel_booking(self, username):
        try:
            bid = int(input("Booking ID: "))
        except:
            print("Invalid Booking ID!")
            return

        for b in self.bookings:
            if b.bid == bid and b.username == username:
                self.bookings.remove(b)
                for r in self.rooms:
                    if r.number == b.room:
                        r.booked = False
                print("Booking cancelled successfully!")
                return

        print("Booking not found!")
    # ---------- PAYMENT ----------
    

    # ---------- ADMIN MENU ----------
    

    # ---------- CUSTOMER MENU ----------
    

    # ---------- START ----------
    

