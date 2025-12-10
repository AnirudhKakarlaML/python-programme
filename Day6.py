'''#Problem 1
l = [10, 20, 30, 40, 50]
count = 0
avg = 0
for n in l:
    avg += n/len(l)
for x in l :
    if x > avg :
        count = count + 1 
print(count)'''
'''#Problem 2--Removal of a number
nums = [2, 3, 2, 5, 2, 7]
num_set=set(nums)
target = 2
num_set.remove(target)
l = []
for n in num_set:
    if n not in l:
        l.append(n)#m -1
print(l)'''
'''#Problem - 2 M - 2
nums = [2, 3, 2, 5, 2, 7]
r_n = []
target = 2
for n in nums:
    if n!=target:
        r_n.append(n)
print(r_n)'''
'''nums = [1, 2, 3, 4, 5]
rotated_nums = [nums[4]]
for n in nums:
    if n != nums[4]:
        rotated_nums.append(n)
print(rotated_nums)
   '''
'''nums = [1, 2, 3, 4, 5]

rotated = []

# Step 1: add last element
rotated.append(nums[-1])

# Step 2: add all elements except last one
for i in range(0, len(nums) - 1):
    rotated.append(nums[i])
#gpt
print(rotated)

'''
'''words = ["apple", "banana", "kiwi", "strawberry", "dog"]
s=""
for char in words:
    if len(char)>len(s):
        s = char
print(s)
    '''
'''#Splitting A List Into Positive , negative and zero
nums = [-3, 0, 12, -1, 5, 0, -8]
positive_num=[]
negative_num=[]
zero_num=[]
for n in nums:
    if n > 0 :
        positive_num.append(n)
    elif n < 0 :
        negative_num.append(n)
    elif n == 0 :
        zero_num.append(n)
print(positive_num)
print(negative_num)
print(zero_num)'''
'''#Counting The No.Of Elements That Appear More Than Once
nums = [1, 2, 3, 2, 4, 5, 1, 1]

freq = {}

# Build frequency dictionary
for n in nums:
    if n not in freq:
        freq[n] = 1
    else:
        freq[n] += 1

# Count how many elements appear more than once
count = 0
for n in freq:
    if freq[n] > 1:
        count += 1

print(count)'''
'''nums = [4, 10, 2, 8, 6]
max = nums[0]
for n in nums :
    if n > max :
        max = n
print(max)
min = nums[0]
for n in nums :
    if n < min:
        min = n
print(min)
diff = max - min
print(diff)
'''
'''nums= [4,3,10,2]
max=nums[0]
min=nums[0]
for n in nums:
    if n>max: #My logic test
        max=n
print(max)
for n in nums:
    if n < min:
        min = n
print(min)'''
'''words = ["mom", "apple", "level", "dog", "noon"]

count = 0

for w in words:
    rev = ""
    for ch in w:
        rev = ch + rev   # build reverse manually
    
    if rev == w:
        count += 1

print(count)
'''
'''nums = [4, 5, 4, 6, 7, 5, 8]
freq = []
for w in nums:
    if w not in freq:
        freq.append(w)
    elif w in freq:
       freq .remove(w)
print(freq)
    
    '''
'''nums = [4, 5, 4, 6, 7, 5, 8]

freq = {}

# Count frequency of each number
for n in nums:
    if n not in freq:
        freq[n] = 1
    else:
        freq[n] += 1

# Build list of elements that appear exactly once
unique_list = []
for n in freq:
    if freq[n] == 1:
        unique_list.append(n)

print(unique_list)'''
'''nums = [5, 8, 12, 15]
for i in range(len(nums) - 1):
    d = nums[i+1]-nums[i]
    print(d)
'''
'''nums = [10, 20, 30, 40, 50]
nums_o=[]
for n in range (len(nums)):
    if n % 2 != 0:
        nums_o.append(nums[n])
print(nums_o) '''      
'''#Set Problems
nums = [1, 2, 2, 3, 4, 4, 5]
nums_s = set(nums)
print(nums_s)'''
'''#Coverting A String Into A Set Of Unique Characters
s = "programming"
s_s = set()
for w in s :
    s_s.add(w)
print(s_s)
'''
'''A = {1, 2, 3, 4}#Union
B = {3, 4, 5, 6}
u_s=set()
for n in A:
    u_s.add(n)
for x in B:
    u_s.add(x)
print(u_s)      '''
'''#Intersection
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
i_s=set()
for n in A:
    if x in B:
        i_s.add(x)
print(i_s)
'''
'''#Symmetric Difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
s_d=set()
for x in A:
    s_d.add(x)
    if x in B:
        s_d.remove(x)
print(s_d)
'''
'''A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

d_s = set()

for x in A:
    if x not in B:
        d_s.add(x)

print(d_s)

'''
'''#Symmetric Difference = a-b U b-a
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
d_s = set()
for x in A:
    if x not in B:
        d_s.add(x)
for n in B:
    if n not in A:
        d_s.add(n)
print(d_s) '''
'''#Creation Of A Tuple Of Squares
number = int(input("Enter A Number" ))
l=[]
for n in range(1 , number+1):
    l.append(n**2)
l = tuple(l)
print(l)
'''
'''t = (10, 5, 20, 8, 15)
max1=t[0]
max2=t[0]
for n in t:
    if n>max1:
        max1 = n
for n in t:
    if n>max2 and n<max1:
        max2 = n
print(max2)'''
#Word Frequency Dictionary
'''s = "apple banana apple mango banana apple"
w=s.split()
freq = {}
for x in w:
    if x not in freq:
        freq[x]=1
    elif x in freq:
        freq[x]+=1
print(freq)
'''
'''A={}
for i in range(1 ,11):
    A.update({i : i**3})
print(A)'''
'''original = {"a": 1, "b": 2, "c": 3}
swapped = {}
for n in original:
    value = original[n]
    swapped[value]=n
print(swapped)'''
'''#Loop Problems
#Printing Factors Of A Particular Number
n = int(input("Enter A  Number :"))
for i in range(1 , n+1):
    if n % i == 0:
        print(i)'''
'''for i in range(1, 101):
    if i % 10 == 5:
        continue
    print(i)'''
'''sum = 0
for i in range(1 , 31):
    sum+=i
print(sum)
'''
'''count = 0

for num in range(1, 101):
    temp = num
    digit_sum = 0

    while temp > 0:
        ld = temp % 10
        digit_sum += ld
        temp //= 10

    if digit_sum % 2 == 0:
        count += 1

print("Count:", count)
'''
'''for num in range(1, 201):
    temp = num
    has_seven = False

    while temp > 0:
        ld = temp % 10
        if ld == 7:
            has_seven = True
            break
        temp //= 10

    if has_seven:
        print(num)
'''
'''#OOP
class student:
    subject = "python"
    clg = "apna"
stu1 = student()
print(stu1.subject)
    '''
'''class student:
    def __init__(self , name , cgpa):
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self):
        return self.cgpa
    
stu1 = student("rahul" , 9.4)
print(stu1.name)
print(stu1.get_cgpa())'''
'''#Laptop And Info Using OOP
class laptop :
    storage_type = "ssd"
    def __init__(self , RAM ,storage):
        self.RAM = RAM
        self.storage = storage
    @classmethod
    def storage__type(cls):
        print(f"The Storage Type is {cls.storage_type}")
    
    def get_info(self):
        print(f"The Storage is {self.storage} and ram is {self.RAM} and storage type is {self.storage_type}")
    @staticmethod
    def discount(price , off):
        f_p = price - (off * price / 100)
        print(f_p)



l1 = laptop("16gb" , "1tb")
l2 = laptop("32gb" , "512gb")
l1.get_info()
l1.storage__type()
laptop.storage__type()
l1.discount(40_000,10)
'''
'''#Product Store:
class product:
    count = 0
    def __init__(self , name ,price):
        self.name = name
        self.price = price
        product.count +=1
    def info(self):
        print(f"The Product Name is {self.name} & price is {self.price}")
    @classmethod
    def total(cls):
        print(cls.count)
p1 = product("Laptop" , 40_000)
p2 = product("pen" , 10)
p1.info()
p1.total()'''
'''#Question
class Student:
    school_name = "ABC School" 
    def __init__(self , name ,roll_no):
        self.name = name
        self.roll_no = roll_no
    def display_info(self):
        print(f"The name is {self.name} and andd roll no is {self.roll_no} and school is {self.school_name}")
s1 = Student("Rahul", 101)
s2 = Student("Anita", 102)
s1.display_info()
s2.display_info()
'''
'''class BankAccount:
    def __init__(self ,name , balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"The Deposited is {amount}")
        print(f"The Balance IS {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrawn: {amount}")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient Balance")

acc1 = BankAccount("Anirudh", 1000)
acc1.deposit(500)
acc1.withdraw(300)
acc1.withdraw(2000)
    '''
'''class Book:
    category = "Education"
    def __init__( self ,title , author):
        self.title =title
        self.author = author
    def show_details(self):
        print(f"Title : {self.title}")
        print(f" Author : {self.author}")
        print(f"Category : {self.category}")
b1 = Book("Python Basics", "Guido")
b1.show_details()
        '''
'''class Mobile:
    store_name = "Smart World"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")
        print(f"Store: {self.store_name}")
        print()

    @classmethod
    def change_store_name(cls, new_name):
        cls.store_name = new_name

    @staticmethod
    def is_expensive(price):
        if price > 50000:
            print("Expensive Mobile")
        else:
            print("Affordable Mobile")


m1 = Mobile("iPhone", 80000)
m2 = Mobile("Samsung", 30000)

m1.show_details()
m2.show_details()

Mobile.change_store_name("Tech Plaza")

m1.show_details()
m2.show_details()

Mobile.is_expensive(m1.price)
Mobile.is_expensive(m2.price)'''







       
