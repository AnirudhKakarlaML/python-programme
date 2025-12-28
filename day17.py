'''for i in range(1 ,101):
    if i % 3 != 0:
        print(i)'''

'''n = int(input())
sum = 0
while n > 0 :
    ld = n % 10
    sum+=ld
    n = n // 10
print(sum)'''

'''n = int(input())
rev = 0
while n > 0:
    ld = n % 10
    rev = rev * 10 + ld
    n = n // 10
print(rev)'''

'''n = int(input())
temp = n
num = n
sum = 0
power = 0
while n > 0:
    md = n % 10
    power+=1
    n = n//10
while num > 0:
    ld = num % 10
    sum+=ld ** power
    num = num // 10
if sum == temp:
    print("Armstrong")
else : 
    print("Not Armstrong")'''

'''n = int(input())
count = 0
while n > 0:
    ld = n % 10
    count+=1
    n = n // 10
print(count)'''

'''n = str(input())
rev =""
for char in range(len(n)-1 , -1 , -1):
    rev+=n[char]
print(rev)'''

'''#Palindrome String Check
n = str(input())
rev =""
for char in range(len(n)-1 , -1 , -1):
    rev+=n[char]
if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")'''

'''word = str(input("Enter The Word : "))#Enter lower case letters
vowels = 0
consonants = 0
digits = 0
spaces = 0
for char in word:
    if char.lower() in "aeiou":
        vowels+=1
    elif char.isalpha():
        consonants+=1
    elif char.isdigit():
        digits+=1
    elif char == " ":
        spaces+=1
print(vowels , consonants , digits , spaces)'''

'''word = input()

vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in word:
    if char == " ":
        spaces += 1
    elif char.isdigit():
        digits += 1
    elif char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(vowels, consonants, digits, spaces)'''

#Restart
#28th december--no stop from today
'''name  =  str(input())
digits = 0
vowels = 0
consonants = 0
spaces = 0
for char in name :
    if char == " ":
        spaces+=1
    elif char.isdigit():
        digits+=1
    elif char.lower() in "aeiou":
        vowels+=1
    elif char.isalpha():
        consonants+=1
print(vowels , consonants , digits , spaces)'''

#Reverse A String
'''word = str(input())
word_rev = ""
for char in range(len(word)-1 , -1 , -1):
    word_rev += word[char]
print(word_rev)'''

#Checking Palindrome String
'''word = str(input())
word_rev = ""
for char in range(len(word)-1 , -1 , -1):
    word_rev += word[char]
if word_rev == word :
    print("Palindrome")
else :
    print("Not Palindrome")'''

#Sum Of Digits Of A Number
'''number = int(input())
sum = 0
while number > 0 :
    ld = number % 10
    sum += ld
    number = number // 10
print(sum)'''

#Count Digits In A Number
'''number = int(input())
count = 0
while number > 0 :
    ld = number % 10
    count += 1
    number = number // 10
print(count)
'''

#Armstrong Number
'''number = int(input())
temp = number
digits = 0
sum = 0
original_num = number
while number > 0 :
    ld = number % 10
    digits += 1
    number = number // 10
while temp > 0:
    arm = temp % 10
    sum += arm**digits
    temp = temp // 10
if (sum == original_num):
    print("Armstrong")
else :
    print("Not Armstrong")'''

#Prime Number Check
'''n = int(input())
is_prime = True
if (n <= 1):
 print("Not Prime")

for i in range(2 , n):
    if n % i == 0:
        is_prime = False
        break
if is_prime == True:
 print("Prime")
else :
  print("Not Prime")
'''

#First Non Repeating Char
'''word = str(input())
freq = {}
for char in word:
    if char not in freq:
        freq[char] = 1
    else:
        freq[char]+=1
found = False
for w in word:
    if freq[w] == 1:
        print(w)
        found = True
        break
if not found:
    print(None)'''
#Character frequency
'''s = str(input())
freq = {}
for char in s:
    if char not in freq:
        freq[char] = 1
    elif char in freq:
        freq[char]+=1
print(freq)'''

'''#Replacing Vowels With Star
s = str(input())
w = ""
for char in s:
    if char.lower() in "aeiou":
        w+='*'
    else:
        w+=char
print(w)
        '''
'''s = input()
result = ""
for char in s:
    if char not in result:
        result += char
print(result)'''


    

    
        
    

    

   
    

        
    





















    
