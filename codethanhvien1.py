from datetime import datetime

def has_letter_and_number(text):
    return any(c.isalpha() for c in text) and any(c.isdigit() for c in text)

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


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
    def register(self):
        username = input("Username: ")
        if not has_letter_and_number(username):
            print("Username must contain letters and numbers!")
            return

        if any(u.username == username for u in self.users):
            print("Username already exists!")
            return

        password = input("Password: ")
        if not has_letter_and_number(password):
            print("Password must contain letters and numbers!")
            return

        self.users.append(User(username, password, "customer"))
        print("Registration successful!")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        for u in self.users:
            if u.username == username and u.password == password:
                return u
        print("Login failed!")
        return None

