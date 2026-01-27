#---------class user----------


#---------class room-----------


#---------class booking---------


#--------class hotelsystem--------


    # ---------- REGISTER ----------
    

    # ---------- LOGIN ----------
    

    # ---------- VIEW ROOMS ----------
    

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
    
