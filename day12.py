# 4 - Day - Practice [ series ]
'''class Student:  #Q - 1
    def __init__(self , name , roll_no):
        self.name = name
        self.roll_no = roll_no
    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no}")
S1 = Student("Anirudh" ,  2511026010793)


S1.display_details()'''
'''class Rectangle: # Q - 2
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
R1 = Rectangle(25 , 13)
print(R1.area())'''


'''class BankAccount: # Q - 3
    def __init__(self , balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
B1 = BankAccount(250000)
print(B1.get_balance())'''


'''class BankAccount:  # Q - 4
    def __init__(self , balance):
        self.__balance = balance
    def set_balance(self ,  new_balance):
         self.__balance = new_balance
    def get_balance(self):
        return self.__balance
B1 = BankAccount(250000)
B1.set_balance(25000)
print(B1.get_balance())'''

'''class Person:
    def __init__(self , name): # Q - 5
        self.name = name
class Student(Person):
    def __init__(self , name ,  roll_no):
        super().__init__(name)
        self.roll_no = roll_no
    def display_details(self):
        print(f"Name : {self.name} \n Roll No : {self.roll_no}")
S1 = Student("Anirudh" , 2511026010793)
S1.display_details()
'''

'''class Animal:
    def sound(self): # Q - 6
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
d1 = Dog()
d1.sound()'''

'''class Herbivore:
    def eating_kind(self): # Q- 7
        print("I EAT PLANTS")
class Carnivore:
    def eating_kind(self):
        print("I Eat Animals")
H1 = Herbivore()
C1 = Carnivore()
H1.eating_kind()
C1.eating_kind()'''

'''class PB_8:
    company_name = "TechCorp"


C1 = PB_8()
C2 = PB_8()
print(C1.company_name)
print(C2.company_name)'''

#LOOPS AND CONDITIONALS
'''N = int(input("Enter A Number : ")) # Q - 9
for i in range(1 , N+1):
    print(i)'''

'''N = int(input("Enter A Number : ")) # Q - 10
if N % 2 == 0:
    for i in range (2 , N+1 , 2):
        print(i)
elif N % 2 != 0 :
    for i in range(1 , N+1 , 2):
     print(i)'''

'''for i in range (1 , 51): # Q - 11
    if i % 2 == 0:
        print(i)
'''

'''n = int(input("Enter A Number : ")) # Q - 12
count = 0
temp = n
while n > 0:
    temp = n % 10
    count+=1
    n = n // 10
print(count)'''

'''n = int(input("Enter Your Number : ")) # Q - 13
sum = 0
for i in range (1 , n+1):
    sum += i
print(sum)
'''

#Functions
'''def sum_two(a , b): # Q - 14
    return a + b   
x = 4
y = 7
print(sum_two(x , y))
'''

'''def square_number(a):  # Q - 15
    return a*a
x = 9

print(square_number(x))'''

'''def number_check(a): #Q - 16
    if a > 0 :
        print("The Number Is Positive")
    elif a < 0:
        print("The Number Is Negative")
    else :
        print("The Number Is Zero")
l = 9
number_check(l)'''

'''def name(a):
    print(f"Hello {a}") # Q - 17
a = "Anirudh"
name(a)'''

#Data Structures
'''l = [1 , 2 , 3 , 4 , 5 , 6] # Q - 18
for n in l:
    print(n)'''

'''l = [1 , 5 , 7 , 9 , 8] # Q - 19
max_val = 0 
for n in l:
    if n > max_val:
        max_val = n
print(max_val)'''

'''s = "HelloWorld"
count = 0 #Q - 20
for n in s:
    if n.lower() in "aeiou":
        count+=1
print(count)'''

'''l = [1 , 2 , 3 , 4 ,5 ,3 , 2] # Q - 21
l = set(l)
print(l)'''

#HACKER RANK - Competetive Programming
'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''
#!/bin/python3
'''
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip()) # q1
if 1 <= n <=100:
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <=5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <=20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")'''

# Q - 2 [ Hacker Rank]
'''if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)'''

# Q - 3 [Hacker Rank]
'''if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)'''



