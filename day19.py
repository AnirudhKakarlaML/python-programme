'''#Frequency Dictionary Of A String
A = "hello"
freq = {}
for char in A:
    if char not in freq:
        freq[char] = 1
    elif char in freq:
        freq[char]+=1
print(freq)'''

#Word Frequency
'''A = "Hello Python I Am Anirudh Trying To Master Python That Is You"
words = A.split()
freq = {}
for char in words:
    if char not in freq:
        freq[char] = 1
    elif char in freq:
        freq[char]+=1
print(freq)'''

'''#Which Key Has Max Value??
A = {'a' : 25 , 'b' : 30 , 'c':75}
max = 0
for n in A.values():
    if n > max:
        max = n
for letter, value in A.items():
    if A[letter] == max:
        print(letter)'''

'''#Stack Overflow 
# Source - https://stackoverflow.com/q
# Posted by user998316, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-30, License - CC BY-SA 3.0

dictionary = {'george' : 16, 'amber' : 19}
search_age = raw_input("Provide age")
for age in dictionary.values():
    if age == search_age:
        name = dictionary[age]
        print name'''

'''#Converting Dictionary Keys to list
data = {'x': 1, 'y': 2, 'z': 3}
list_keys = []
for char in data:
    list_keys.append(char)
print(list_keys)'''

'''#Convert List to Dictionary (index : value)
lst = ['a', 'b', 'c']
dict_u = {}
for n in range(0 , len(lst)):
    dict_u.update({n : lst[n]})
print(dict_u)'''

'''#Sort List Ascending Order
A = {'a' : 3 , 'b' : 1, 'c' : 2 }
b = list(A.values())
b.sort()
c = {}
'''
'''A = {'a': 3, 'b': 1, 'c': 2}

# Phase 1: extract values
values = []
for v in A.values():
    values.append(v)

# Phase 2: sort values
values.sort()

# Phase 3: rebuild dictionary
sorted_dict = {}
used_keys = []

for val in values:
    for key, value in A.items():
        if value == val and key not in used_keys:
            sorted_dict[key] = value
            
            

print(sorted_dict)'''
A = {'a': 3, 'b': 1, 'c': 2}

'''# Phase 1: extract values
values = []
for v in A.values():
    values.append(v)

# Phase 2: sort values
values.sort()
c = {

}
d = []
for val in values:
    for key , value in A.items():
        if value == val and key not in d:
            c[key] = value
print(c)'''

'''#Merged Dictionary
A = {'a': 10, 'b': 20}
B = {'b': 5, 'c': 7}
C = {}
for names in A:
    if names in B:
        C.update({names : A[names] + B[names]})
    if names not in B:
        C.update({names : A[names]})
for names in B:
    if names not in C:
        C.update({names : B[names]})
print(C)'''

#File Handling
'''with open("sample.txt" , 'r') as f:
    data = f.readline()
    lines = 0
    while data:
        lines+=1
        data = f.readline()
       
print(lines)'''

'''with open("sample.txt" , 'r') as f : #char count
    data = f.read()
    words = data.split()
    count = 0 
    for char in data:
        count+=1
print(count)
'''
'''with open("sample.txt" , 'r') as f:
    data = f.read()
    words = data.split()
    count = 0
    for char in words:
        count += 1
print(count)'''

'''try:
    with open("sample.txt" , "r") as f:
        data = f.read()
except FileNotFoundError :
    print("FileNotFoundError")'''

#JSON
'''import json
data = {
    "name": "Anirudh",
    "skill": "Python",
    "level": "Beginner"
}
with open("data.json" , 'w') as f:
    json.dump(data , f)
with open("data.json" , 'r') as f :
    content = json.load(f)
    print(content)
'''

#Last Problem
import json
lst = [1, 2, 2, 3, 4, 4, 5] #Creation of list with duplicates
with open("data.json" , 'w') as f:
    json.dump(lst , f)
with open("data.json" , 'r') as f:
    data = json.load(f)
    lst_2 = []
    for n in data:
        if n not in lst_2:
            lst_2.append(n)
print(lst_2)
with open("data.json" , 'w') as f:
    json.dump(lst_2 , f , indent = 4 , sort_keys=True)






        






        
       
