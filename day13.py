#Object Oriented Programming #Day-2 [p- fundae]
'''class Student:   #Q - 1
    def __init__(self , marks):
        self.__marks = marks
    def set_marks(self , new_marks):
        self.__marks = new_marks
    def get_marks(self):
        return self.__marks'''

'''class Student:   #Q - 2[Modification]
    def __init__(self , marks):
        self.__marks = marks
    def set_marks(self , new_marks):
        if new_marks < 0:
            print("Invalid Marks")
        else:
            self.__marks = new_marks
    def get_marks(self):
        return self.__marks'''

'''class Vehicle:
    def start(self): #Q - 3
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")'''

'''class Employee:
    def __init__(self , name , salary): # Q - 4
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self , name , salary , department):
        super().__init__(name , salary)
        self.department = department
    def display_details(self):
        print(f"Name : {self.name} \n Salary : {self.salary} \n Department : {self.department}")'''

'''class Employee:
    def get_role(self):
        return "Employee" #Q - 5
class Manager(Employee):
    def get_role(self):
        return "Manager"'''

'''class Employee:
    def get_role(self): # Q - 6
        return "Employee"
class Manager(Employee):
    def get_role(self):
        return "Manager"
    
#Creation Of Lists
E1 = Employee()
M1 = Manager()

lst = [E1 , M1]
#Looping
for items in lst:
    print(items.get_role())'''

'''from abc import ABC , abstractmethod

class Shape(ABC):   # Q - 7
    @abstractmethod
    def area(self):
        pass'''

'''from abc import ABC , abstractmethod

class Shape(ABC): # Q - 8
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth'''

# Loops And Conditionals
'''n = int(input("Enter The Number Of The Multiplication Table To Be Printed : ")) # Q - 9
for i in range(1 , 11):
    print(f"{n} x {i} = {n * i}")'''

'''n = int(input("Enter A Number : ")) # Q - 10
sum_digits = 0
while n > 0:
    ld = n  % 10
    sum_digits += ld
    n = n // 10
print(sum_digits)'''

'''n = int(input("enter A Number")) # Q - 11
rev = 0
while n > 0:
    ld = n % 10
    rev = rev * 10 + ld
    n = n // 10

print(rev)'''

'''for i in range (1 , 101): # Q - 12
    if i % 5 == 0:
        print(i)'''

'''n = int(input("enter A Number")) # Q - 13
rev = 0
temp = n
while n > 0:
    ld = n % 10
    rev = rev * 10 + ld
    n = n // 10

print(rev)
if rev == temp:
    print("Palindrome")
else : 
    print("Not Palindrome")'''

#Functions
'''def even_odd(a): # Q - 14
    if a % 2 == 0:
        return "Even"
    elif a % 2 != 0 :
        return "Odd"
a = 7
print(even_odd(a))''' 

'''def factorial(n): # Q - 15
    fact = 1
    for i in range(1 , n+1):
        fact*=i
    return fact
a = 5
print(factorial(5))'''

'''def count_digits(n): # Q - 16
    count = 0
    while n > 0:
        ld = n % 10
        count+=1
        n = n // 10
    return count
a = 123456
print(count_digits(a))'''

'''#Logic
a = "python"
b = ""
for char in range(len(a)-1 , -1 , -1):
    b+=a[char]
print(b)'''

#Function
'''def reversed_string(a): # Q - 17
    b = ""
    for char in range(len(a) - 1 , -1 , -1):
        b+=a[char]
    return b
a = "JAVA"
print(reversed_string(a))
'''
# Data Structures
'''A = [1, 2, 2, 3, 3, 3]# Q - 18[Frequency dict]
freq = {}
for n in A:
    if n not in freq:
        freq[n] = 1
    elif n in  freq:
        freq[n]+=1
print(freq)'''

'''A = [1, 2, 3] #Merging Two Lists
B = [4, 5, 6] # Q - 19
C = []
for n in A:
    C.append(n)
for n in B:
    C.append(n)
print(C)'''

'''students = {
    "Anil": 85, # Q - 20
    "Sunil": 90,
    "Ravi": 78
}
for name , marks in students.items():
    print(f"{name} : {marks}") # q -21[broken logic]
     '''

'''students = {
    "Anil": 85,
    "Sunil": 90,
    "Ravi": 78
}
for name  in students:
    if name == "Anil" in students:
        print("Exists")
    else :
        print("Not exists")'''
'''
students = {
    "Anil": 85, # Q - 21
    "Sunil": 90,
    "Ravi": 78
}

name = "Anil"

if name in students:
    print("Exists")
else:
    print("Not Exists")
'''









    
      

    


    




        










    




