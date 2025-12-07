'''#Q1
age = int(input("Enter Your Age:-"))
if (age < 13) :
    print("You Are A Child")
elif (13 < age < 18) :
    print("You Are A Teen")
else :
    print("Adult")
'''
'''#Q2
username = str(input("Enter The Username:-"))
password = str(input("Enter Your Password:-"))
if (username == "admin" and password == "pass") :
    print("Logged In")
elif (username != "admin" and password == "pass") :
    print("Wrong  Username")
elif (username == "admin" and password != "pass") :
    print("Wrong Password")
else :
    print("Invalid Credentials")'''
'''#Q3
num1 = int(input("Enter The Number:-"))
if (num1 %2 == 0):
    print("Even")
else :
    print ("Odd")'''
'''#Q4
color = str(input("Enter The Color:-"))
match (color) :
    case ("Green") :
        print("Go")
    case ("Red") :
        print("Stop")
    case ("Orange"):
        print("Move Steady Buddy")
    case _ :
        print("Inavlid Color")'''
#Q5
'''i=1
while i<=5:
    print("hi")
    i+=1'''
'''#Q6
i = 1
while (i <= 5):
    print(i)
    i += 1'''
"""#Q7
i = 1
while (i <= 5):
    print(i)
    i += 1"""
'''#q8
#printing from 5-1
i = 5
while (i>=1):
    print(i)
    i -=1'''
"""#Q9
i = 10
while (i >= 1 and i < 11):
    print (f"5 * i = {5*i}")
    i+=1"""
'''#q10
name=str(input("Enter Your Name:-"))
age=int(input("Enter Your Age:-"))
height=float(input("Enter Your Height In Feet:-"))
print(f"Hello {name}, you are {age} years old and {height} feet tall")'''
'''#q11
num_1 = int(input("Enter A Number(Only Integer):-"))
num_2 = int(input("Enter A Number(Only Integer):-"))
sum = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2
quotient = num_1 / num_2
remainder = num_1 % num_2
power = num_1 ** num_2
print(f" The Sum is {sum}, The Difference is {difference} ,The Product Is {product}, The Quotient Is {quotient},The Remainder Is {remainder} and The Power Is {power}")
'''
#q12
'''num_1 = int(input("Enter A Number : - "))
if (num_1 > 50) :
    print("True")
else :
    print("False")'''
'''#q13
age = int(input("enter Your Age : "))
country = input("Enter Your Country : ").strip().capitalize()#Strip For Removing Unnecessary Gaps Capitaize For Making First LetterCapital
if (age >= 18 and country == "India"):
    print("You Are Eligible")
else :
    print("You Are Not Eligible")'''
'''#q14
num = float(input("Enter A Number :"))
if (num > 0) :
    print("Positive")
elif (num < 0) :
    print("Negative")#Complex()--->can handle complex
elif (num == 0) :
    print("Zero")
else : 
    print("Complex Numbers")'''
'''#q15-->>Even Or Odd
num_1 = int(input("Enter A Number :"))
if (num_1  % 2 == 0):
    print("Even")
else :
    print("Odd")'''
'''#q16
age = int(input("Enter A Number : "))
marks = int(input("Enter Your Marks : "))
if (age >= 18):
    if (marks >= 60):
        print("Eligible For Admission")
    else :
        print("Marks Too Low")
else :
    print("Age Too Low")
    '''

'''option = int(input("Enter A Number (1/2/3) : "))#Q17
match(option) :
    case 1 :
        print("Start")
    case 2 :
        print("save")
    case 3 :
        print("exit")
    case _:
        print("Invalid Number")

'''
'''#q18
i = 1
while(i <= 10):
    print(i)
    i+=1'''
''' #Q20i = 20 
while(i >= 1):
    print(i)
    i -= 1'''
'''#Multiplication Table
n = int(input("Enter A Number : "))
i = 1
while(i<=10):
    print(n*i)
    i+=1'''
'''i = 1

while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1
''''''#reversing A Number Using A While Loop
n = int(input("Enter A Number :- "))
rev = 0
while (n > 0) :
    ld = n % 10
    rev = rev * 10 + ld
    n = n // 10
print(rev)'''