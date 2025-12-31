#Last Day ---> Numpy from jan 1st
'''class student:
    def __init__(self , name , marks ):
        self.name = name
        self.marks = marks
        self.grade = self.grade_rules()
        
    def grade_rules(self):
        if self.marks<0:
            raise ValueError("Negative Marks Are Not Valid")
        elif(self.marks >= 90):
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'D'
    def show_details(self):
        print(f"Name : {self.name}\nMarks : {self.marks}\nGrade : {self.grade}")
s1 = student("Anirudh" , 96)
s1.show_details()'''


'''class student:
    def __init__(self , name , marks ):
        self.name = name
        self.marks = marks
        self.grade = self.grade_rules()
        
    def grade_rules(self):
        if self.marks<0:
            raise ValueError("Negative Marks Are Not Valid")
        elif(self.marks >= 90):
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'D'
    def show_details(self):
        print(f"Name : {self.name}\nMarks : {self.marks}\nGrade : {self.grade}")
s1 = student("Anirudh" , 96)
s2 = student("Rahul" , 98)
s3 = student("Yash" , 97)
students = [s1 , s2 , s3]
for name in students:
    print(name.show_details())'''

'''#Displaying All Students In A Order
class student:
    def __init__(self , name , marks ):
        self.name = name
        self.marks = marks
        self.grade = self.grade_rules()
        
    def grade_rules(self):
        if self.marks<0:
            raise ValueError("Negative Marks Are Not Valid")
        elif(self.marks >= 90):
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'D'
    def show_details(self):
        print(f"Name : {self.name} | Marks : {self.marks} | Grade : {self.grade}\n")
s1 = student("Anirudh" , 96)
s2 = student("Rahul" , 98)
s3 = student("Yash" , 97)
students = [s1 , s2 , s3]
for name in students:
    (name.show_details())'''

#Displaying All Students In A Order
'''class student:
    def __init__(self , name , marks ):
        self.name = name
        self.marks = marks
        self.grade = self.grade_rules()
        
    def grade_rules(self):
        if self.marks<0:
            raise ValueError("Negative Marks Are Not Valid")
        elif(self.marks >= 90):
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'D'
    def show_details(self):
        print(f"Name : {self.name} | Marks : {self.marks} | Grade : {self.grade}\n")
s1 = student("Anirudh" , 96)
s2 = student("Rahul" , 98)
s3 = student("Yash" , 97)
marks = 0
name = ""
grade = ""
students = [s1 , s2 , s3]
for name in students:
    if name.marks > marks:
        marks = name.marks
for name in students:
    if marks == name.marks:
        print(f"Topper:\n Name : {name.name} | Marks : {name.marks} | Grade : {name.grade}")'''

'''class BankAccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self , amount):
        if amount <= 0:
            print("Invalid Deposit Amount")
        else:
            self.__balance+=amount
    def get_balance(self):
        return self.__balance
b1 = BankAccount("Anirudh" , 200000)
b1.deposit(20000)
print(b1.get_balance())'''

#Bank Account Problems
'''class BankAccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self , amount):
        if amount <= 0:
            print("Invalid Deposit Amount")
        else:
            self.__balance+=amount
    def withdraw(self , amount):
        if amount <= 0:
            print("Invalid Withdraw Amount")
        elif amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance-=amount
    def get_balance(self):
        return self.__balance
b1 = BankAccount("Anirudh" , 200000)
b1.deposit(20000)
b1.withdraw(50000)
print(b1.get_balance())'''

'''class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary
class Manager(Employee):
    def __init__(self , name , base_salary , bonus):
        super().__init__(name , base_salary)
        self.bonus = bonus
    def caluculate_salary(self):
        return self.base_salary+self.bonus'''

#Function Over Riding
'''class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def calculate_salary(self):
        return self.base_salary
class Manager(Employee):
    def __init__(self , name , base_salary , bonus):
        super().__init__(name , base_salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.base_salary+self.bonus
e1 = Employee("Anirudh" , 250000)
m1 = Manager("Karthik" , 320000 , 24000 )
print(m1.calculate_salary())'''


'''f = open("file.txt" , 'r') #Problem Statement--->two files mergement
x = open("file2.txt" , 'r')
data = f.read()
content = x.read()
with open("merged.txt" , 'w') as y:
    y.write(data)
with open("merged.txt" , 'a') as z:
    z.write(content)
f.close()
x.close()'''


    