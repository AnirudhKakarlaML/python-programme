#Encapsulation + Abstraction + Polymorphism
#Encapsulation ---- > Private Classes And Their Accesment Via Function
'''class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.__balance = balance#Private Data
    def get_value(self):#Getter
        return self.__balance
    def set_value(self , newbalance):
        self.__balance = newbalance
acc1 = BankAccount("Rahul" , 200000)
print(acc1._BankAccount__balance)#method but not good practice
print(acc1.get_value())#Good Practice'''
'''#Inheritance ---> Properties Get Transfered From Parent Class To Sub Classes
class employee:
    start_time = "10am"
    end_time = "5pm" #Single level inheritance
class Teacher(employee):
    def __init__(self , role):
        self.role  = role
t1 = Teacher("teach")
print(t1.role , t1.start_time)
'''
'''#Multi Level Inheritance
class Employee:
    start_time = "10am"
    end_time = "6pm"
class AdminStaff(Employee):
    def __init__(self , role):
        self.role = role
class Accountant(AdminStaff):
    def __init__(self, salary ,role):
       super().__init__(role)
       self.salary = salary
acc1 = Accountant(25000 , "Ca")
'''
'''#Multiple Level Inheritance
class Teacher:
    def __init__(self , salary):
        self.salary = salary
class Student:
    def __init__(self , gpa):
        self.gpa = gpa
class Ta(Teacher,Student):
    def __init__(self , salary , role , gpa):
        super().__init__(salary)
        Student.__init__(self , gpa)
        self.role = role
t1 = Ta(250000 , "teacher" , 9.6)'''
'''#Abstraction
from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass
class Lion(Animal):
    def make_sound(self):
        print("roar")
l1 = Lion()       
l1.make_sound()'''
'''#Polymorphism ----> FinctionOverridind and ducktyping
#Function Overriding
class Employee:
    def get_designation(self):
        print("Emplyee") 
class Teacher:
    def get_designation(self):
        print("Teacher")
t1 = Teacher()
t1.get_designation()       

'''
#Apna Clg Assignment Q1
'''class BankAccount:
    def __init__(self , account_number , owner_name , balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self , amount):
        self.balance+= amount
    def withdraw(self , amount):
        if self.balance>=amount:
            self.balance-=amount
            return True
        return False
    def check_balance(self):
        return f"balance is {self.balance}"
acc1 = BankAccount("1097885" , "Rahul Jaykar" , 200000)'''
'''class Book:
    def __init__(self , title , author , price):
        self.title = title
        self.author = author
        self.price = price
    def display_details(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price : {self.price}")
    def is_expensive(self):
        if self.price > 500:
            return True
        else :
            return False'''
'''#Encapsulation--Data Hiding
class Student:
    def  __init__(self , name , roll_no , marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks
    def get_name(self):
        return self.__name
    def set_name(self , new_name):
        if new_name.strip() == "":
            print("Name Cannot be empty")
        else:
            self.__name = new_name
    def get_rollno(self):
        return self.__roll_no
    def set_rollno(self , new_roll):
        if 1<= new_roll <= 100:
            self.__roll_no = new_roll
        else:
            print("Enter B/w 1 - 100")
    def get_marks(self):
        return self.__marks
    def set_marks(self , new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
        else : 
            print("Enter Positive Marks")'''
'''#FUNCTION OVER RIDING
class Shape: #Multiple Errors
    def area():
        pass
class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
    def area(self , radius):
        self.area = 3.14 *radius*radius
class Recatangle(Shape):
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth
    def area(self , length , breadth):
        self.area = length * breadth
class Triangle(Shape):
    def __init__(self , base , height):
        self.base = base 
        self.height = height
    def area(self , base , height):
        self.area = 0.5 * base * height'''
'''#Function Over Rididng
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius*self.radius
class Rectangle(Shape):
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class Triangle(Shape):
    def __init__(self , base , height):
        self.base = base
        self.height = height #Correct Version
    def area(self):
        return 0.5 * self.base*self.height'''
'''#Inheritance
class Vehicle:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
class Car(Vehicle):
    def __init__(self , brand , model , seats):
        super().__init__(brand)
        super().__init__(model)
        self.seats = seats
class Bike(Vehicle):
    def __init__(self , brand , model , seats , engiene_cc):
        super().__init__(brand)
        super().__init__(model)
        super().__init__(seats)
        self.engiene_cc = engiene_cc


class Vehicle:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
class Car(Vehicle):
    def __init__(self ,  seats):
        self.seats = seats
class Bike(Vehicle , Car):
    def __init__(self , brand , model , seats , engiene_cc):
        super().__init__(brand)
        super().__init__(model)
        super().__init__(seats) #Super init only once
        self.engiene_cc = engiene_cc'''
'''class Vehicle:
    def __init__( self ,brand , model):
        self.brand = brand
        self.model = model 
class Car(Vehicle):
    def __init__(self , brand , model , seats):
        super().__init__(brand , model)
        self.seats = seats
class Bike(Vehicle):
    def __init__(self , brand , model , engiene_cc):
        super().__init__(brand , model)
        self.engiene_cc = engiene_cc'''
'''#Abstraction
from abc import ABC , abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Intern(Employee):
        def __init__(self , stipend):
             self.stipend = stipend
        def caluculate_salary(self):
             return self.stipend
class FullTimeEmployee(Employee):
     def __init__(self , base_salary , bonus):
          self.base_salary = base_salary
          self.bonus = bonus
     def calculate_salary(self):
          return self.base_salary + self.bonus
class ContractEmployee(Employee):
    def __init__(self, hours_worked, rate_per_hour):
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour'''
'''#Multiple Inheritance
class Herbivore:
    def eat_plants(self):
        return "Eats plants"


class Carnivore:
    def eat_meat(self):
        return "Eats meat"


class Omnivore:
    def eat_both(self):
        return "Eats plants and meat"


class Bear(Herbivore, Carnivore, Omnivore):
    def info(self):
        return "Bear can eat everything"
'''
    

          
        



        
        
        