'''#OOP
class Student:
    def __init__(self , name , mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def average(self):
        return (self.mark1 + self.mark2 +self.mark3)/3
    def result(self):
        if  self.average() >=40:
            print("Pass")
        else :
            print("Fail")
s1 = Student("Anirudh" , 98 , 99 , 98)
print(f"Name : {s1.name}" )
print(f"AVG : {s1.average()}")
s1.result()'''
'''#Bank Account System
class BankAccount:#CGPT VERSION
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient balance")
            return False

    def transfer(self, to_account, amount):
        if self.withdraw(amount):
            to_account.deposit(amount)


# Testing
acc1 = BankAccount("Anirudh", 5000)
acc2 = BankAccount("Rahul", 2000)

print("Before Transfer:")
print(acc1.name, acc1.balance)
print(acc2.name, acc2.balance)

acc1.transfer(acc2, 1000)

print("\nAfter Transfer:")
print(acc1.name, acc1.balance)
print(acc2.name, acc2.balance)'''
'''class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount

    def withdraw(self , amount):
        if amount <= self.balance:   # ✅ FIXED LINE
            self.balance -= amount
            return True
        else:
            print("insufficient Funds")
            return False

    def transfer(self , to_account , amount):
        if self.withdraw(amount):
            to_account.deposit(amount)


# Testing
acc1 = BankAccount("Anirudh", 5000)
acc2 = BankAccount("Rahul", 2000)

print("Before Transfer:")
print(acc1.name, acc1.balance)
print(acc2.name, acc2.balance)

acc1.transfer(acc2, 1000)

print("\nAfter Transfer:")
print(acc1.name, acc1.balance)
print(acc2.name, acc2.balance)'''
'''class Laptop:
    def __init__(self , brand , ram , price):
        self.brand = brand
        self.price = price
        self.ram = ram
    def is_gaming(self):
        if self.ram >= 16 and self.price>=60000:
            return True
        else:
            return False
L1 = Laptop("HP VICTUS" , 16 , 82500)
L2 = Laptop("Lenovo" , 8 , 56000)
print(L1.is_gaming())
print(L2.is_gaming())
    '''
'''class Movie:
    def __init__(self , title , rating , duration ):
        self.title = title
        self.rating = rating
        self.duration = duration
    def is_hit(self):
        if self.rating>7 and self.duration <180:
            return True
        else:
            return False
    def titles(self):
        print(f"{self.title}")
M1 = Movie("RRR" , 8.6 , 176)
M2 = Movie("Salaar" , 9.2 , 182)
M3 = Movie("Akhanda 2" , 9.6 , 156)
M4 = Movie("Kalki" , 9.4 , 182)
M5 = Movie("Varanasi" , 9.2 , 189)
movies = [M1 , M2 , M3 , M4 , M5]
for m in movies:
    if m.is_hit():
        m.titles()'''
'''class Cart:
    def __init__(self):
        self.items = []

    def add_items(self, name, price, qty):
        self.items.append((name, price, qty))

    def total_bill(self):
        total = 0
        for t in self.items:
            name, price, qty = t
            total = total + price * qty
        return total


cart = Cart()
cart.add_items("Pen", 10, 3)
cart.add_items("Book", 50, 2)
cart.add_items("Milk", 60, 1)

print("Total Bill:", cart.total_bill())'''
'''class Book:
    def __init__(self , title , pages):
        self.title = title
        self.pages = pages
    def reading_time(self ):
        time = self.pages * 1.5
        return time
B1 = Book("Alone" , 15)
print(B1.title)
print(B1.reading_time())
        '''
'''class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    def apply_bonus(self , percent):
        bonus = (percent/100) * self.salary
        self.salary+=bonus
        return self.salary
E1 = Employee("Anirudh" , 200000)
print(E1.apply_bonus(10))
print(E1.name)'''
'''class Product:
    def __init__(self , costprice , sellingprice):
        self.costprice = costprice
        self.sellingprice = sellingprice
    def profit(self):
        return self.sellingprice - self.costprice
    def is_profit(self):
        if self.sellingprice > self.costprice:
            return True
        else:
            return False
p1 = Product(2000 ,2500)
print(p1.profit())
print(p1.is_profit())
    '''
'''#List Problems
lst = [1, 2, 3, 2, 4, 2]
lst_new = []
target = 2
for n in lst:
    if n != target:
        lst_new.append(n)
print(lst_new)
'''
'''L = [1 ,2,3,4]
rev_l = [L[3]]
for n in range(len(L)-2 ,  -1 , -1):
    rev_l.append(L[n])
print(rev_l)    


'''
'''L = [1, 2, 3, 4]
rev_l = []

for i in range(len(L)-1, -1, -1):
    rev_l.append(L[i])

print(rev_l)
'''
'''#creating a list with elements greater than average
numbers = [10, 20, 30, 40, 50]
g_a = []
sum = 0
count = 0
for n in numbers:
    sum+=n
avg = sum / len(numbers)
for n in numbers:
    if n > avg:
        g_a.append(n)
        count+=1
print(g_a)#Manual Method Of finding range is simply to create a variable like total and declare value to 0 and increment by +1
print(count)
'''
'''#Finding The Second Smallest Element In The List
numbers = [5, 1, 4, 2, 3]
min1 = numbers[0]
min2 = numbers[0]
for n in numbers:
    if n < min1:
        min1 = n
for n in numbers:
    if n < min2 and n > min1:
        min2 = n
print(min2)
'''
'''numbers = [5, 1, 4, 2, 3]

min1 = float('inf')
min2 = float('inf')

for n in numbers:
    if n < min1:
        min2 = min1
        min1 = n
    elif n < min2 and n != min1:
        min2 = n

print(min2)
'''
'''#Rotation Of Lists:
numbers = [1, 2, 3, 4, 5]
k = 2  

for n in range(k):
    last = numbers[-1]
    for i in range(len(numbers)-1 ,0 ,-1):
        numbers[i] = numbers[i - 1]
    numbers[0] = last
print(numbers)

'''
'''a = {1 , 2 , 3}
b = {4 , 5 ,6}
c = set()
for n in a:
    c.add(n)
for n in b:
    c.add(n)
print(c)'''
'''A = [ 1 , 2 , 3 , 4]
B = [3 , 4, 5 ,6]
c = [ ]
for n in A:
    if n not in c:
        c.append(n)
for x in B:
    if  x not in c:
        c.append(x)
print(c)
'''
'''A = [1, 2, 3, 4]#Intersection of sets
B = [3, 4, 5, 6]
c=[]
for n in A:
    if n in B:
        c.append(n)
print(c)'''
'''A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
c = []
for n in A:
    if n not in B:
        c.append(n)
print(c)
  '''
'''#frequency dictionary
lst = [1, 2, 2, 3, 1, 1]
lst_dict = {}
for n in lst:
    if n not in lst_dict:
        lst_dict[n] = 1
    else:
        lst_dict[n]+=1
print(lst_dict)'''
'''students = {
    "Anirudh": 82,
    "Rahul": 68,
    "Priya": 91,
    "Neha": 74
}
for names , marks in students.items():
    if marks > 75:
        print(names)
    '''
#merge Two Dictionaries
'''d1 = {"a": 10, "b": 5}
d2 = {"a": 2, "c": 4}
merged = {}#Wrong Values Must Add 
for letter , marks in d1.items():
    merged.update({letter : marks})
for letter , marks in d2.items():
    merged.update({letter : marks})
print(merged)
        '''
'''d1 = {"a": 10, "b": 5}
d2 = {"a": 2, "c": 4}
merged = {}
for letter , count in d1.items():
    merged[letter] = count
for letter , count in d2.items():
    if letter in merged:
        merged[letter]+=count
    else:
        merged[letter] = count
print(merged)'''
'''#Strings ---> Logic Builder's = "Hello123!"
s = "Hello132!"
vowel_c = 0
digit_c = 0
consonant_c = 0
special_c = 0
for w in s:
    if w.lower() in "aeiou":
        vowel_c+=1
    elif w.isdigit():
        digit_c+=1
    elif w.isalpha():
        consonant_c+=1
    else:
        special_c+=1
print(vowel_c)
print(digit_c)
print(consonant_c)
print(special_c)'''
#Loops And Functions
'''def is_prime(n):
    if n<=1:
        return False
    for i in range(2 , n):
        if n % i == 0:
            return False
        return True
print(is_prime(7))'''
'''#counting numbers with 4
def numbers_4():
    count = 0
    for i in range(1 ,201):
        if '4' in str(i):
            count+=1
    return count
print(numbers_4())
        '''
'''def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a, end=" ")
        a , b = b , a+b
fibonacci(7)

'''








