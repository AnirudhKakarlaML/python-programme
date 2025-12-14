#Object Oriented Programming
#Student Attendance System
'''class Student:
    def __init__(self , name , total_days , present_days):
        self.name = name 
        self.total_days = total_days
        self.present_days = present_days
    def attendance_percentage(self):
        return (self.present_days/self.total_days)*100
    def is_eligible(self):
        if self.attendance_percentage()>=75:
            return True
        else :
            return False
S1 = Student("Anirudh" , 365 , 352)
print(S1.attendance_percentage())
print(S1.is_eligible())
'''
'''
#Bank Accounts Transfer
class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance
    def deposit(self , amount):
        if amount > 0:
         self.balance+=amount
         return True
        return False
    def withdraw(self , amount):
        if amount<=self.balance:
            self.balance = self.balance - amount
            return True
        else :
            print("Insufficient Funds")
            return False
    def transfer( self , to_account, amount):
        if self.withdraw(amount):
            to_account.deposit(amount)
    def show_summary(self):
        return f"Name: {self.name}, Balance: {self.balance}"
    
    
    
        
acc1 = BankAccount("Anirudh", 5000)
acc2 = BankAccount("Rahul", 2000)

print("Before Transfer:")
print(acc1.name, acc1.balance)
print(acc2.name, acc2.balance)

acc1.transfer(acc2, 1000)

print("\nAfter Transfer:")
print(acc1.name, acc1.balance)
print(acc2.name, acc2.balance)
print(acc1.show_summary())
    '''
#Product inventory
'''class Product:
    def __init__(self ,name , price , stock):
        self.name = name
        self.price = price
        self.stock = stock
    def sell(self , quantity):
        if quantity>0 and self.stock >= quantity:
            self.stock-=quantity
            return True
        return False
    def restock(self , quantity):
        if quantity > 0:
         self.stock+=quantity
         return self.stock
            
    def total_value(self):
        if self.price>0:
            return self.price*self.stock
p1 = Product("Pen" , 10 ,100)
p1.sell(45)
p1.sell(45)
print(p1.restock(150))  
print(p1.total_value())     
'''
'''class Product:#After Correction
    def __init__(self, name, price, stock):
        self.name = name
        if price > 0:
            self.price = price
        else:
            self.price = 0

        if stock >= 0:
            self.stock = stock
        else:
            self.stock = 0

    def sell(self, quantity):
        if quantity > 0 and self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def restock(self, quantity):
        if quantity > 0:
            self.stock += quantity
            return True
        return False

    def total_value(self):
        return self.price * self.stock


p1 = Product("Pen", 10, 100)
p1.sell(45)
p1.sell(45)
p1.restock(150)

print(p1.stock)
print(p1.total_value())'''
'''#Movie Theatre Booking System
class Movie:
    def __init__(self ,name , seats_available):
        self.name = name
        if seats_available>0:
            self.seats_available= seats_available
        else:
            self.seats_available = 0
    def book_ticket(self, count):
        if count > 0 and count <= self.seats_available:
            self.seats_available -= count
            return True
        return False
    def cancel_ticket(self, count):
        if count > 0:
            self.seats_available += count
            return True
        return False
m1 = Movie("Inception", 100)

m1.book_ticket(30)
m1.book_ticket(50)
m1.cancel_ticket(10)

print("Seats available:", m1.seats_available)

'''
#List problems
#MAx element in the list
'''lst = [1, 2, 2, 3, 1, 1]
freq = {}
for n in lst:
    if n not in freq:
        freq[n] = 1
    else :
        freq[n]+=1
max_count = 0
max_element = None
for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        max_element = key
print(max_element)
'''
