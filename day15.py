'''f = open("sample.txt" , "r")
data = f.read() # Open and close and read
print(data)
f.close()
'''

'''#read line by line
f = open("sample.txt" , "r")
data = f.readline()
print(data)# The Space That comes in the output is to show that that it moves to the next line start after reading
data = f.readline()
print(data)
f.close()
'''

'''#Overwriting the file
f = open("sample.txt" , "w")
f.write("Overwriting the file")
f.close()'''

'''#Addition Of New Text
f = open("sample.txt" , "a")
f.write("\n New Text is Being added......")
f.close()'''

'''#Creation Of New Files
f = open("sample2.txt" , "x")
f.write("I do what ever i want")
f.close()'''

#Multiple Operations
'''#operation 1 read and overwrite the first position
f = open("sample.txt" , "r+")
f.write("Operation Done")
f.close()'''

'''#operation 2 overwrite and read
f = open("sample2.txt" , "w+")
f.write("Hi bro")
f.close()

'''

'''#operation 3 - read and append
f = open("sample.txt" , "a+")
f.write("hi")
f.seek(0)
print(f.read())
f.close()
'''

'''#With keyword
with open("sample.txt" , "r") as f:
    data = f.read()
    print(len(data))'''

'''#Deletion of files
import os
os.remove("sample2.txt")'''

'''#Practice # Word Search
line = 1
with open("sample.txt", "r") as f:
    data = f.readline()
    while data:
        if "Python" in data:
            print(f"The word is found in line {line}")
            break
        line += 1
        data = f.readline()
'''
#Exception Handling
'''try:
    x = int(input())
    ans = 10 /x
except ZeroDivisionError:
    print("Not Possible")
except ValueError:
    print("invalid input")
else:
    print(f"ans = {ans}")'''

'''#finally which we need to execute no matter what
try:
    x = int(input())
    ans = 10 /x
except ZeroDivisionError:
    print("Not Possible")
except ValueError:
    print("invalid input")
else:
    print(f"ans = {ans}")
finally:
    print("end")'''

#List comprehensions
'''sq = [i*i for i in range(6)]
print(sq)'''

'''sq = [i*i for i in range(6) if i%2!=0]
print(sq)'''

'''nums = [ -1 , 2 , -3]
nums = [0 if val<0 else val for val in nums]
print(nums)'''

'''with open("names.txt" , "w+") as f:
    f.write("Anirudh\nRohith\nYash\nLasya\nLasya.S")
    f.seek(0)
    data = f.read()
    print(data)'''

'''with open("log.txt" , "a+") as f:
    f.write("Program Runned Succesfully")
    f.seek(0)
    print(f.read())'''

'''numbers = [5, 10, 15, 20, 25]
numbers = [ val for val in numbers if val > 15 ] 
print(numbers)'''

'''import os
os.remove("log.txt")
os.remove("sample.txt")'''

'''with open("intro.txt" , "w") as f:
    f.write("Anirudh\nDay 15\nMl")
    f.seek(0)
with open("intro.txt" , "r") as f:
    data = f.read()
    print(data)'''

'''lines = 0
with open("intro.txt" , "r") as f:
    data = f.readline()
    while data:
        lines+=1
        data = f.readline()
        
print(lines)'''

'''with open("sample.txt" , "r") as f: #Words
    data = f.read()
    print(len(data))'''

'''#Characters Count
with open("sample.txt" , "r") as f:
    data = f.read()
    words = data.split()
    print(len(words))
'''
'''data = True
lines = 1
with open("sample.txt" , "r") as f:
    data = f.readline()
    data = f.readline()
    data = f.readline()
    data = f.readline()
    data = f.readline()#Wrong
    data = f.readline()


    while data:
        if "Python" in data:
            data = f.readline()
            print(data)'''

'''lines = 1
with open("sample.txt" , "r") as f:
    for line in f:
        if "Python" in line:
            print(f"Line {lines}: {line.strip()}")
        lines+=1'''

'''with open("sample.txt" , "a+") as f:
    f.write("File handling is now clear.")
    f.seek(0)
    data = f.read()
    print(data)'''

'''try :
    with open("intro.txt" , "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found")'''


'''try :
    with open("intro.txt" , "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found")
finally:
    print("Programme ended")'''

            
    
