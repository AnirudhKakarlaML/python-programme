#Object Oriented Programming + List+ Tuples +Sets +Dictionaries +Strings+ Loops +Function[practice]
'''class Student:
    def __init__(self , name ,age):
        self.name = name
        self.age =  age
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
stu1 = Student("Anirudh" , 19)
stu2 = Student("Priya" , 18)
stu3 = Student("Ravi" , 20)
stu1.display_info()
stu2.display_info()
stu3.display_info()
'''
'''class Rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
rect1 = Rectangle(5 , 4)
rect2 = Rectangle(3 ,7)
print(rect1.area())
print(rect2.area())'''
'''class Car:
    def __init__(self , brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def details(self):
        print(f"{self.brand} {self.model} ({self.year})")
c1 = Car("Toyota" , "Corolla" , 2020)
c2 = Car("Skoda" , "rapido" , 2025)
c3 = Car("Mg" , "XEV9" , 2025)
c1.details()
c2.details()
c3.details()
'''
'''class BankAccount :
    def __init__(self , Holdername ,CurrentBalance):
        self.Holdername = Holdername
        self.CurrentBalance = CurrentBalance
    def deposit(self ,amount):
        self.CurrentBalance+=amount
    def withdraw(self , amount):
            if amount <= self.CurrentBalance:
               self.CurrentBalance = self.CurrentBalance - amount
            elif amount>self.CurrentBalance:
                 print("Insufficient Funds")
    def show_balance(self):
        print(self.CurrentBalance)
       
acc = BankAccount("Anirudh", 1000)
acc.deposit(500)
acc.withdraw(2000)
acc.show_balance()
'''
'''class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    def give_raise(self, percent):
        self.salary+= self.salary *percent/100
        print(self.salary)
E1 = Employee("Anirudh" , 200000)
E2 = Employee("Yash" , 40000)
E1.give_raise(10)
E2.give_raise(10)
'''
'''class GroceryItem:
    def __init__(self , name , price ,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total(self):
        return self.price*self.quantity
G1 = GroceryItem("Corriander" , 10 , 3)
G2 = GroceryItem("Cheese" , 100 ,3)
G3 = GroceryItem("Milk" , 80 ,4)
print(G1.total())
print(G2.total())
print(G3.total())
'''
'''#Temperature Converter Using OOP
class Temperature:
    def __init__(self , celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        self.farenheit = self.celsius*9/5 + 32
        return self.farenheit
C1 = Temperature(37)
C2 = Temperature(52)
C3 = Temperature(62)
print(C1.to_fahrenheit())
print(C2.to_fahrenheit())
print(C3.to_fahrenheit())'''
'''class Book:
    def __init__(self , title , author ,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def is_big(self):
        if self.pages > 300:
            return True
        else:
            return False
B1 = Book("Atomic Habits" , "ABC" , 252)
B2 = Book("Rich Dad Poor Dad" , "ABC" , 352 )
B3 = Book("Dark Psycholgy" , "ABC" , 300)
print(B1.is_big())
print(B2.is_big())
print(B3.is_big())'''
'''class Product:
    def __init__(self , id ,name ,price):
        self.id = id
        self.name = name
        self.price = price
    def show(self):
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Price : {self.price}")
    def filtered(self):
        if self.price > 500:
            print(self.name)
p1 = Product("b1" , "pen" ,589)
p2 = Product("b1" , "pen" ,9)#Wrong
p3 = Product("b1" , "pen" ,5829)
p4 = Product("b1" , "pen" ,5889)
p5 = Product("b1" , "pen" ,89)
'''
'''class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def show(self):
        print(self.pid, self.name, self.price)

    def is_expensive(self):
        return self.price > 500


# Create 5 products
p1 = Product(1, "Shoes", 799)
p2 = Product(2, "Pen", 50)
p3 = Product(3, "Bag", 1200)
p4 = Product(4, "Book", 300)
p5 = Product(5, "Headphones", 999)

products = [p1, p2, p3, p4, p5]

# Print products whose price > 500
for p in products:
    if p.is_expensive():
        p.show()'''
'''class Marks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # list of 5 marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def passed(self):
        if self.average() >= 40:
            return True
        else:
            return False


# Create 3 students
s1 = Marks("Anirudh", [50, 60, 70, 80, 90])
s2 = Marks("Yash", [30, 20, 40, 35, 25])
s3 = Marks("Rohit", [40, 40, 40, 40, 40])

# Print results
print(s1.average(), s1.passed())
print(s2.average(), s2.passed())
print(s3.average(), s3.passed())

'''
'''class Student:
    def __init__(self , name ,scores):
        self.name = name
        self.scores = scores 
    def average(self):
        if len(self.scores)==0:
            return 0
        else :
         return sum(self.scores)/len(self.scores)
    def highest_score(self):
       if len(self.scores) == 0:
          return 0
       else:
          return highscore
     
    '''
'''#lists
nums = [1, 2, 3, 4, 5, 6]
for a in nums:
    for b in nums:
        if (a+b) % 2==0:
            print(a,b)
 #Tuples'''
'''nums = (1, 2, 3, 4, 5, 6, 7, 8)
even_l = []
for n in nums:
    if n % 2 == 0:
        even_l.append(n)
even_l = tuple(even_l)
print(even_l)
print(type(even_l))'''
'''#string Problems
s = "a1b2c3d4e5f6"
s1 = ""
for char in s:
    if char.isalpha():
        s1+=char
print(s1)'''
'''#string problem
s = "banana"
freq ={}
for char in s:
    if char not in freq:
        freq[char] = 1
    else:
        freq[char]+=1
print(freq)
       '''
'''#Highest Scorer In Dictionary
marks = {
    "Anirudh": 88,
    "Yash": 76,
    "Rohit": 92,
    "Kiran": 45
}

top_name = None
top_score = -1  # safe initial value since marks are non-negative
for name , score in marks.items():
    if score > top_score:
        top_score = score
        top_name = name
print(top_name)
'''
'''sentence = "Python is super powerful"
sentence_2 = sentence.split()
freq = {}
count = 0
for s in sentence_2:
    freq[s] = len(s)
print(freq)

'''
'''l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7]
for n in l1:
    if n in l2:
        print(n)'''
'''list1 = [1, 2, 2, 3]
list2 = [3, 4, 5]

# Step 1: Combine both lists
combined = list1 + list2

freq={}
for n in combined:
    if n not in freq:
        freq[n] = 1
    else:
        freq[n]+=1

for key in freq:
    if freq[key] == 1:
        print(key)

    
'''
'''count_3 = 0
count_5 = 0
for i in range (1 ,201):
    if i % 3 == 0:
        count_3+=1
    elif i % 5 == 0:
        count_5+=1
print(count_5)
print(count_3)'''
'''count = 0

for i in range(1, 201):
    if i % 3 == 0 or i % 5 == 0:
        count += 1

print(count)'''
'''#functions
def sum_digits(n):
    temp = n
    sum_digits = 0
    while temp > 0:
        ld = temp % 10
        sum_digits+=ld
        temp = temp // 10
    print(sum_digits)
 

sum_digits(135)
'''

