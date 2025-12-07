"""n = int(input("Enter a number: "))

i = 1
fact = 1

while i <= n:
    fact = fact * i#solution seen
    i += 1

print("Factorial is:", fact)
"""
"""num =int(input("Enter The Number :-"))
digit = 0
while(num>0):
    num = num //10
    digit = digit +1
print(digit)
"""
'''#Printing All The Odd Numbers From 1-10
i = 1
while (i <= 10) :
    if (i % 2 == 0) :
        i += 1
        continue
    print(i)
    i += 1'''
'''#Printing No . Of i's repeated In The Word Artificial Intelligence
word = "Artificial intelligence"
count = 0
for ch in word:
    if (ch == 'i'):
        count += 1
print(count)'''
'''
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

'''
'''#Printing Natural Numbers Sum 
n = int(input("Enter Your Number : "))
sum = 0
for i in range(1 , n+1) :
    sum += i
print(sum)'''
'''#Function Definition And Call
def hello():
    print("Hi Through Functions")
hello()'''
'''#Sum Through Functions
def sum (a,b):
    sum = a + b
    return sum
ans = sum (3,4)
print(ans)'''
'''#Three functions avg
def avg (a , b ,c):
    a=int(input("Enter The Number"))
    b=int(input("Enter The Number"))
    c=int(input("Enter The Number"))
    _avg = (a+b+c)/3
    return _avg
ans = avg (1 ,2 ,3)#Not Recomended To Take inputs Insiderthe functions
print(ans)
'''
'''
def avg(a, b, c):
    return (a + b + c) / 3

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))#Correct Way

z = int(input("Enter number 3: "))

ans = avg(x, y, z)
print(ans)
'''
'''def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial is:", result)
'''
'''#Defining Factorial Using A Function
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact 

x=int(input("Enter"))
ans=factorial(x)
print(ans)'''
''' #Printing 1 to n using a while loop
n = int(input("Enter A Number : "))
i = 1
while (i <= n):
    print(i)
    i = i + 1'''
'''#Reverse Order Printing
n=6
i=n
while(i>=1):
    print(i)
    i= i-1'''
'''#Printing Even Numbers B/q 1-50
i=2
while(i%2==0 and i<=50):
    print(i)
    i = i+2'''
'''#Logic 2
i = 1

while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1
'''
'''n = int(input("Enter A Number : "))
i = 1
while(i<=10):
    print (n*i)
    i = i+1'''
'''#Counting No.Of Digits
n=int(input("Enter A Number : -"))
count = 0
i = 1
while (n > 0):
    n = n//10
    count+=i
print(count)'''
'''n = int(input("Enter A Number :- "))
rev = 0

while n > 0:
    last_digit = n % 10
    rev = rev * 10 + last_digit
    n = n // 10

print("Reversed number:", rev)
'''
'''#Sum Of Digits Using A While Loop
n = int(input("Enter A Number : "))
sum = 0
while (n > 0) :
    ld = n % 10
    sum += ld
    n = n // 10
print(sum)'''
'''#Palindrome Check--Dimmag Kharabh
n = int(input("Enter A Number : "))
rev = 0
temp = n
while (n > 0):
    ld = n % 10
    rev = rev * 10 + ld
    n = n // 10 
print(rev)
print(temp)
if ( rev == temp) :
    print("Palindrome")
else :
    print("not palindrome")'''
'''#For Loop
n=100
for i in range (1,n + 1) :
    print(i)'''
'''#Squares Using For Loop
n = 21
for i in range (1 , n ) :
    print(i ** 2)'''
'''#Multiples Of 5 B/w 1 - 100
n = 101
for i in range (1 , n) :
    if (i % 5 == 0):
        print(i)'''
'''#Vowel Counter
word = "hello"
vowel_c = 0
for ch in word :
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        vowel_c += 1
print(vowel_c)
        '''
'''#Counting Upper Case And Lower Case
word = str(input("Enter Your Word : "))
u = 0
l = 0
for ch in word :
    print(ch)
    if ch.isupper():
      u += 1
    elif ch.islower():
      l += 1
print(f"{u},{l}")
'''
'''#Fibonacci Series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
'''
'''#Prime Number Checking Using For Loop
# Q7: Print primes from 1 to 50
for num in range(2, 51):       # Start from 2 (1 is not prime)
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
'''
'''#Functions--square
def square(n):
    square = n**2
    return square
x=5
ans = square(x)
print(ans)
'''
'''#Functions --- Even Or Odd
def even_odd (n):
    if(n % 2 == 0):
        print("Even")
    else :
        print("Odd")
x = 30
even_odd(x)
'''
'''#Factorial Of A Number Using Functions
def factorial_for_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

num = 5
result = factorial_for_loop(num)
print(f"The factorial of {num} is {result}")
# Output: The factorial of 5 is 120'''
'''#Counting Sum Of Digits
def sum_digits (n) :
    sum = 0
    while (n > 0) :
        ld = n % 10
        sum += ld
        n = n // 10
        return sum
x=1234
ans = sum_digits(x)
print(ans)
'''
'''#Sum Using -- While Loop
n = int(input("Enter Your Number: "))
sum = 0
while (n > 0) :
    ld = n % 10
    sum += ld
    n = n // 10
print(sum)'''
'''def sum_digits(n):
    sum = 0
    while(n > 0):
        ld = n % 10
        sum += ld
        n = n // 10
    return sum
x = 1234
y =sum_digits(x)
print(y)'''
'''def large_number(a , b , c):
    if(a > b and a > c):
        print("a is largest")
    elif(b > a and b > c):
        print("b is largest")
    elif(c > a and c > b):
        print(" C is largest")
a=5
b=4
c=7
large_number(a , b , c)'''