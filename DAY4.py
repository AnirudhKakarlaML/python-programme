#'''WarmUp--20 mins
'''num  = 25521
num_search = int(input("what number u want frequency of :- "))
count = 0
while (num > 0) :
    ld = num % 10
    if(ld == num_search):
        count +=1
    num = num // 10

print(count)'''
'''#Taking Input
a = int(input("enter : -"))
print(a)'''
'''#string Slicing
word = "Python"
print(word[2:4])'''
'''#Formatting A String
a = 5
b = 10 
s = a + b
print("Sum of {} and {} is {}".format(a , b, s))'''
'''#List Methods And Mutation
marks = [12,21,34,43,56,65]
print(marks)
print(type(marks))
marks[2] = 190
marks.append(23)
print(marks)
marks.insert(2 , 9)
print(marks)
marks.sort()
print(marks)
marks.reverse()'''
'''#Searching The Index Value In A Particular VAlue
marks = [1 , 2 ,3 ,4]
x = int(input("Enter The Number Of Which Index Must Be Found : "))
idx = 0
for value in marks :
    if (value == x):
     print(idx)
     break
    idx=+1'''
'''#Tuple Methods
tup = (1,2,2,3,3,4,5,6,4,6)
print(tup.index(2))
print(tup.count(2))'''
'''#Dictionary Creation And Mutation And Accesing A Particular Valur
dict = {
    "Name" : "Anirudh",
    "CGPA": 9.6
    }
print(dict)
dict["CGPA"] = 9.4
print(dict["Name"])'''
'''#Dictionary Methods:
student_info = {
    "Name" : "Anirudh" ,
    "CGPA" : "9.4"
}
print(student_info)
print(student_info.keys())
print(student_info.values())
print(student_info.get("Ctya"))
student_info.update({
   "Bestie" : "LASYA"
    })
print(student_info)'''
'''#Set Methods
s = {1 ,2 ,3 ,4 }
s_ = {4 ,5 , 6 ,7}
print(s.union(s_))
print(s.intersection(s_))
(s_.add(987))
print(s_)
(s.remove(3))
print(s)
(s_.pop())
print(s_)
'''
'''#q1
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]
''''''courses = set()
for val in info:
    courses.add(val[1])
print(courses)

for name,subject in info:
    if (subject == "English"):
        print(name)'''
'''
#Now Creation Of dictionaries With Courses
dict = {}

for name, course in info:
    if dict.get(name) == None:
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)
print(dict.get("Alice"))'''
'''#PRINTING nUMBERS gREATER tHAN 50 IN THE LIST
l = [50 , 60 , 70 , 80 , 90]
for num in l :
    if(num > 50) :
        print(num)'''
'''#Finding The Second largest in a list
nums = [10, 50, 20, 90, 70]
nums.sort()
print(nums)
print(nums[-2])'''
'''#Without Sorting
nums = [10, 50, 20, 90, 70]
max1 = nums[0]
for n in nums:
    if n > max1:
        max1 = n
        
max2 = nums[0]
for n in nums:
    if n > max2 and n!= max1:
        max2 = n
print(max2)
     '''
'''#Remove duplicates
nums = [10, 20, 10, 30, 20, 40]
unique_list = []
for n in nums:
    if n not in unique_list:
        unique_list.append(n) 
print(unique_list)'''
'''l =list((input("Enter A List")))
l.insert(2 , 9)
print(l)'''
'''#Insertion
l = [1 , 5 , 7 , 9 ,11]
l.insert(2 , 9)
print(l)'''
'''#Square The Given List
l = [1 ,2 ,3 ,5]
square=[]
for n in l :
    if n in l :
        square.append(n*n)
print(square)'''
'''#Seperation Of Even And Odd sum in the list
list = [1 ,5 ,9 , 16 , 8]
even_sum = 0
odd_sum = 0
for n in list:
    if n % 2 == 0:
        even_sum+=n
    elif n % 2 != 0:
        odd_sum+=n
print(even_sum)
print(odd_sum)'''
'''#Printing Only The Name Starting with Vowel
names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Kiran"]

for name in names:
    if name[0].lower() in "aeiou":
        print(name)
'''
