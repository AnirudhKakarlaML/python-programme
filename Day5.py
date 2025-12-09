'''#Q-1[Print Even Index Elements In The List]
a = [10 , 20 , 30 , 40]
for i in range(len(a)):
    if(i % 2 == 0):
        print(a[i])
'''
'''#Squaring A List
a = [10 ,20 ,30 , 40]
a_s=[]
for n in a :
    a_s.append(n**2)
print(a_s)'''
'''#Printing The Names Starting With Vowel
names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Kiran"]
for name in names:
    if(name[0].lower() in "aeiou"):
        print(name)'''
'''#Counting Elements Divisible by 3 in the list
nums = [10, 12, 15, 19, 21, 30]
o_c = 0
for n in nums :
    if (n % 3 == 0):
        o_c = o_c + 1
print(o_c)'''
'''#Sum Of elements in the list
a = [10 ,20,30,40]
sum_a = 0
for n in a :
    sum_a += n
print(sum_a)'''
'''#Counting The Number Of Strings Having Length Greater Than 5
words = ["apple", "banana", "cat", "elephant", "sun"]
count = 0
for name in words:
    if len(name) > 5 :
        count = count + 1
print(count)'''
'''#Printing Negative Numbers In The List\
nums = [10, -5, 3, -8, 2, -1]
for n in nums :
    if(n < 0):
        print(n)'''
'''#Splitting The List Into Even And Odd
nums = [10, 15, 8, 21, 30, 7]
nums_even = []
nums_odd  = []
for n in nums :
    if n % 2 == 0:
        nums_even.append(n)
    elif n % 2 !=0 :
        nums_odd.append(n)
print(nums_even)
print(nums_odd)'''
'''#Reversing A List 
nums = [1, 2, 3, 4, 5]
num_rev = []
for i in range(len(nums)-1, -1, -1):
    num_rev.append(nums[i])
print(num_rev)'''
'''#Finding MAx Element MAnually
nums = [15, 8, 22, 5, 31, 18]
max1 = nums[0]
for n in nums :
    if n > max1:
        max1 = n
print(max1)
'''
'''#List To Tuple And Tuple To List
l = [1, 2, 3]
t = (4, 5, 6)
t_l=[]
l_t =(1 , 2 ,3)
for n in t:
    t_l.append(n)
print(t_l)
print(l_t)
''''''#List To Tuple And Tuple To List Method 2
l = [1, 2, 3]
t = (4, 5, 6)
l_t=tuple(l)
t_l=list(t)
print(l_t)
print(t_l)
'''
'''#concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6, 7)
print(t1 + t2)'''
'''#Target Element Count
t = (1, 2, 2, 3, 4, 2, 5)
target = 2
count = 0
for n in t :
    if n == target :
        count+=1
print(count)'''
'''#BASIC DICTIONARY PROBLEMS
#Print Name Of The Student Whose MArks Are greater than 80
students = {
    "Amit": 85,
    "Riya": 76,
    "Karan": 92,
    "Neha": 67,
    "Sai": 88
}
for names in students:
    marks = students[names]
    if students[names] > 80:
        print(names)'''
'''#Dictionary Problem 2
sq = {}
for i in range(1 ,11):
    sq.update({i : i*i})
print(sq)'''
'''#Merging Dictionaries
merged_dictionary = {}
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged_dictionary.update(d1)
merged_dictionary.update(d2)
print(merged_dictionary)'''
'''#Vowel Count In A Word-Dict
s = "beautiful day"
v_d = {}
a_c = 0
e_c = 0
i_c = 0
o_c = 0
u_c = 0
for i in s:
    if i == 'a':
        a_c+=1
    elif i == 'e':
        e_c+=1
    elif i == 'i' :
        i_c+=1
    elif i == 'o' :
        o_c+=1
    elif i == 'u' :
        u_c+=1
v_d.update({
    "a" : a_c,
      "e" :e_c,
     "i" :i_c,
     "o" : o_c,
     "u" : u_c
})
print(v_d)#My version
'''
'''#c - gpt version
s = "beautiful day"
vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

for ch in s:
    if ch in vowels:
        vowels[ch] += 1

print(vowels)
'''
'''#swapping values
d = {"a": 1, "b": 2, "c": 3}
swapped = {}

for key in d:
    value = d[key]
    swapped[value] = key

print(swapped)
'''
'''#Word Frequency
s = "python is easy and python is powerful"
word = s.split()
freq={}
for w in word:
    if w not in freq:
        freq[w] = 1
    elif w in freq :
        freq[w]+=1
print(freq)
'''
'''#SETS
nums = [1, 2, 2, 3, 4, 4, 5]
set_nums=set()
for n in nums : #method 1
    set_nums.add(n)
print(set_nums)
#Method-2
nums = [1, 2, 2, 3, 4, 4, 5]
set_nums = set(nums)
print(set_nums)'''
'''#Question 2
s = "programming"
set_s = set()
for ch in s:
    set_s.add(ch)
print(set_s)'''
'''nums = {10, 15, 22, 33, 40, 55}
o_s=set()
for n in nums:
    if n % 2 != 0:
     o_s.add(n)
print(o_s)'''

'''s = "Hello World 123"

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    elif ch.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
'''
'''s = "Python"
l = [ ]
for i in range(len(s)-1 , -1 ,-1):
      l.append(s[i])
print(l)
stm=str(l)  
print(stm)'''
'''s = "Python"
rev = ""

for i in range(len(s)-1, -1, -1):
    rev += s[i]

print(rev)
'''
'''s1 = "listen"
s2 = "silent"
s1=list(s1)
s2=list(s2)
s1.sort()
s2.sort()
if s1 == s2:
    print("Anagram")
else :
    print("not anagram")'''
'''s = "beautiful day"
rev = ""
for ch in s:
    if ch.lower() in "aeiou":
        x = ch
    elif ch.isalpha():
        rev+=ch
print(rev)
        '''
s = "hello world python"
'''new_s = ""

for ch in s:
    if ch == " ":
        new_s += "_"
    else:
        new_s += ch

print(new_s)'''
'''#While Loop
n = 1234
rev = 0
while (n > 0):
    ld = n % 10
    rev = rev * 10 + ld
    n = n // 10
print(rev)'''
'''#Function
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# test
num = 17
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")
'''
