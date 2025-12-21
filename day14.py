#Object Oriented Programming
'''class BankAccount:
    def __init__(self , account_holder , balance):  Q - 1
        self.__account_holder = account_holder
        if balance < 0:
            raise ValueError("The Balance Can't Be Negative")
        else :
            self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self , amount):
        if amount <= 0 :
            raise ValueError("The Amount Can't Be Negative")
        else  :
            self.__balance+=amount
            print("Deposit Succesful")
    def withdraw(self , amount):
        if amount < 0:
            raise ValueError("The Amount Cannot Be Negative")
        elif amount > self.__balance:
            raise ValueError("No Sufficient Balance")
        elif self.__balance>=amount and amount>=0:
            self.__balance=self.__balance - amount
            print("Withdraw Succesful")

acc = BankAccount("Anirudh", 5000)
acc.deposit(2000)
acc.withdraw(1000)
print(acc.get_balance())'''

'''class Employee:
    def __init__(self , name , base_salary):  # Q - 2
        self.name = name
        self.base_salary = base_salary
    def get_salary(self):
        return self.base_salary
    
class Developer(Employee):
    def __init__(self , name , base_salary , bonus):
        super().__init__(name , base_salary)
        self.bonus = bonus
    def get_salary(self):
        return self.base_salary + self.bonus
class SeniorDeveloper(Developer):
    def __init__(self , name , base_salary , bonus, stock_bonus):
        super().__init__(name , base_salary , bonus)
        self.stock_bonus = stock_bonus
    def get_salary(self):
        return self.base_salary +self.bonus + self.stock_bonus
emp = Employee("Anil", 30000)
dev = Developer("Ravi", 50000, 10000)
senior = SeniorDeveloper("Sunil", 80000, 20000, 30000)

print(emp.get_salary())      # 30000
print(dev.get_salary())      # 60000
print(senior.get_salary())   # 130000'''

'''class Employee:
    def __init__(self , name , base_salary): # Q - 3
        self.name = name
        self.base_salary = base_salary
    def get_salary(self):
        return self.base_salary
    
class Developer(Employee):
    def __init__(self , name , base_salary , bonus):
        super().__init__(name , base_salary)
        self.bonus = bonus
    def get_salary(self):
        return self.base_salary + self.bonus
class SeniorDeveloper(Developer):
    def __init__(self , name , base_salary , bonus, stock_bonus):
        super().__init__(name , base_salary , bonus)
        self.stock_bonus = stock_bonus
    def get_salary(self):
        return self.base_salary +self.bonus + self.stock_bonus
emp = Employee("Anil", 30000)
dev = Developer("Ravi", 50000, 10000)
senior = SeniorDeveloper("Sunil", 80000, 20000, 30000)

def print_salary(emp):
    return emp.get_salary()
print(print_salary(emp))
print(print_salary(dev))
print(print_salary(senior))'''

'''from abc import ABC , abstractmethod
class Employee(ABC):
    def __init__(self , name , base_salary): # Q - 4
        self.name = name
        self.base_salary = base_salary
    @abstractmethod
    def caluculate_salary(self):
        return self.base_salary
class FullTimeEmployee(Employee):
    def __init__(self , name , base_salary , bonus):
        super().__init__(name , base_salary)
        self.bonus = bonus
    def caluculate_salary(self):
        return self.base_salary + self.bonus
class PartTimeEmployee(Employee):
    def __init__(self , name , base_salary , hours_worked):
        super().__init__(name , base_salary)
        self.hours_worked = hours_worked
    def caluculate_salary(self):
        return self.base_salary * self.hours_worked
    
ft = FullTimeEmployee("Anirudh" , 200000 , 30000)
print(ft.caluculate_salary())
pt = PartTimeEmployee("Ravi", 500, 40)
print(pt.caluculate_salary())'''

'''class Mobile:
    store_name = "Smart World"
    def __init__(self , brand , price):   # Q - 5
        self.brand = brand
        self.price = price
    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Price : {self.price}")
        print(f"Store Name  : {self.store_name}")
    @classmethod
    def change_store_name( cls , new_name):
        cls.store_name = new_name
    @staticmethod
    def is_expensive(price):
        if price > 50000:
            print("Expensive")
        else : 
            print("Affordable")

m1 = Mobile("iPhone", 80000)
m2 = Mobile("Samsung", 30000)

Mobile.change_store_name("Tech Plaza")

m1.show_details()
m2.show_details()

Mobile.is_expensive(m1.price)
Mobile.is_expensive(m2.price)
'''

#Loops And Conditionals
'''#Standard Fibonacci Problem
n = int(input("Enter A Number : "))
a = 0 # 
b = 1
c = a + b#Wrong
for i in range(0 , n+1):
    
    a , b = b , a+b
    print(a)
'''

'''#Fibonacci
n = int(input())
a = 0 # q -6
b = 1
if n >= 1:
    print(a)
if n >=2:
    print(b)
for i in range (2 , n):
    c = a + b
    print(c)
    a = b
    b = c'''

#prime Number Check
'''n = int(input())

if n <= 1:
    print("Not Prime")
else:
    is_prime = True # Q -7

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")'''

'''a = int(input("Enter Your Number:"))
b = int(input("Enter your Number:"))
c = int(input("Enter Your Number:"))

if a > b and a > c:
    print("a is greatest")

elif b > a and b > c:
    print("b is greatest") # Q - 8

elif c > a and c > b:
    print("c is greatest")'''

#Counting Even And Odd Digits In Number
'''n = int(input("Enter A Number "))
e_c = 0
o_c = 0
while n > 0:
    ld = n % 10
    n = n // 10 # Q - 9
    if ld % 2 == 0:
        e_c+=1
    elif ld % 2 !=0:
        o_c+=1
print(e_c)
print(o_c)'''

'''n = int(input("Enter No of rows :")) # Q - 10
for i in range(1 , n+1):
    print("*" * i)
    '''

#Functions
'''#Max In the LST
def max_lst(lst):
    max = lst[0]
    for n in lst:
        if n > max:
            max = n
    return max
lst = [5 , 9 , 8 , 7]
print(max_lst(lst))'''

'''def greet(name, msg="Hello"):
    print(msg, name)

greet("Anirudh")
greet("Anirudh", "Good Morning")
'''

'''def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))'''







    




   













    