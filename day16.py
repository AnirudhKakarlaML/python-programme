'''with open("numbers.txt" , "w+") as f: # Creation Of File And Adding 50 Numbers In Different Lines
    for i in range (1 , 51):
        f.write(f"{i}\n")'''

'''lines = 0
count_e = 0
count_o = 0
with open("numbers.txt", "r") as f: #Counting Number Of Lines And Counting Even And Odd Out Of it
    for line in f:
        lines += 1
        if int(line) % 2==0:
            count_e+=1
        else:
            count_o+=1

    
print(lines)
print(count_o)
print(count_e)
'''

'''with open("numbers.txt" , "a") as f:
    for i in range(101 , 121): #Adding Some more numbers in the same file without replacing the numbers as in write
        f.write(f"{i}\n")'''

'''with open("numbers.txt" , "r+") as f:
  f.readline()
  f.readline()
  f.readline()
  f.readline()
  f.readline()
  f.write("REPLACED")
  '''

'''with open("numbers.txt" , "a") as f:
    for i in range(101 , 121): #Adding Some more numbers in the same file without replacing the numbers as in write
        f.write(f"{i}\n")
'''

'''lines = 0 
count_e = 0
count_o = 0
with open("numbers.txt" , "r") as f:
    for line in f: #Even count and odd count and no.of lines
        lines+=1
        if int(line) % 2 == 0:
            count_e+=1
        else : 
            count_o +=1
print(lines)
print(count_e)
print(count_o)'''

'''#File Creation And Handling
import os
with open("temp.txt" , "w") as f :
      f.write("Hi") #Here we create a file and handle it in a proper way so that program dosnt crash
try :
        
     os.remove("temp.txt")
except FileNotFoundError:
    print("No file found")'''

'''filename = str(input("enter the file name"))
try :
    with open(filename , "r") as f: #Here We Take file name as input and do the following operations
        print(f.read())
except FileNotFoundError:
    print("File not found")
finally :
    print("Program end")'''

#8  Data Analysis Problems Till Now

#Exception Handling
'''num_1 = (input("Enter The Number : "))
num_2 = (input("Enter The Number : "))
try :
    ans = int(num_1)/int (num_2) 
    print(ans)
except ZeroDivisionError :  #Usage Of Built In Errors
        print("Divison By Zero")
except ValueError:
      print("Divison By String")'''

'''#File Handling -- HOT[Higher Order Thinking]
filename = str(input("enter The file Name : "))
try : 
    with open(filename , "r") as f:
        content = f.read()
        if content ==  "" :
            print("empty file")
        else : 
            print(content)
except FileNotFoundError:
    print("file not found")'''

'''def safe_int_input():
    while True:
        value = input("Enter an integer: ")
        try:
            return int(value) #
        except ValueError:
            print("Invalid input")'''

'''def safe_int_in_range(min_val, max_val):
    while min_val <= n <=max_val:
        n = input("Enter Number")
        try :
            return int(n) # Wrong
        except ValueError:
            print("Enter Valid Input")'''


'''def safe_int_in_range(min_val, max_val):
    
    while True:
        n = input("Enter The Number : ")
        try : 
            num = int(n)
            if min_val<= num <=max_val:
             return num
            else :
               print("Out Of Range")
        except ValueError:
           print("Enter Valid Input")'''

#List Comprehensions
'''numbers = [val**2 for val in range(1 , 51) if val % 2==0]
print(numbers)
odd_cubes = [val**3 for val in range(1, 51) if val % 2 != 0]
print(odd_cubes)'''

'''names = ["Anil", "sunil", "RAVI", "Meena"]
n = []
for m in names: #Must Use List Comprehension
    n.append(m.capitalize())
print(n)
        '''

'''names = ["Anil", "sunil", "RAVI", "Meena"]
names = [val.capitalize() for val in names]
print(names)'''

'''import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])'''

'''import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps("data.json")

# the result is a JSON string:
print(y)'''

'''import json
d = {
    "name"  : "Anirduh"
}
with open("data.json" , "w") as f:
    json.dump(d , f)'''
'''import json
students = [
    {"name": "A", "marks": [70, 80, 90]},
    {"name": "B", "marks": [60, 75, 85]}
]

with open("Students.json" , "w") as f:
    json.dump(students , f)

with open("Students.json" , "r") as f:
    content = json.load(f)

topper_name = ""
highest_avg = 0

for student in content:
    avg = sum(student["marks"]) / len(student["marks"])
    student["average"] = avg
    if avg > highest_avg:
        highest_avg = avg
        topper_name = student["name"]
print("Topper:", topper_name)

# Step 6: Write updated data back to JSON
with open("students.json", "w") as f:
    json.dump(content, f, indent=4)'''







        



    




  
  
    
    



