'''#OOP + Strings + Tuples + Lists + Dictionaries + Sets + Loops + Functions
class Movie:
    def __init__(self , title , rating , duration):
        self.title = title
        self.rating = rating
        self.duration = duration
    def is_long(self):
        if self.duration > 150 and self.rating > 8 :
             return True
        else:
            return False
    def show(self):
         
         print(f"{self.title}")
         print(f"{self.rating}")
         print({self.duration})

   
m1 =Movie("Inception" , 8.8 , 148)
m2 = Movie("Interstellar" , 8.6 , 169)
m3 = Movie("The Dark Knight" , 9.0 , 152)
m4 = Movie("Avvatar" , 7.8 , 162)
m5 = Movie("RRR" , 9.8 ,182)
Movies = [m1 , m2 ,m3 , m4 , m5]      
for m in Movies:
    if m.is_long():
        m.show()'''

'''class Movie:
    def __init__(self, title, rating, duration):
        self.title = title
        self.rating = rating
        self.duration = duration

    def is_long(self):
        return self.duration > 150

    def show(self):
        print(f"Title: {self.title}")
        print(f"Rating: {self.rating}")
        print(f"Duration: {self.duration}")
        print("------------------------")

# Movie objects
m1 = Movie("Inception", 8.8, 148)
m2 = Movie("Interstellar", 8.6, 169)
m3 = Movie("The Dark Knight", 9.0, 152)
m4 = Movie("Avatar", 7.8, 162)
m5 = Movie("RRR", 9.8, 182)

movies = [m1, m2, m3, m4, m5]

# Filtering logic: rating > 8 AND duration > 150
for m in movies:
    if m.rating > 8 and m.is_long():
        m.show()
'''
'''class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # list of 5 numbers

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"

    def show(self):
        print(f"{self.name} → Avg: {self.average():.2f} → Grade: {self.grade()}")


# Creating 3 students
s1 = Student("Anirudh", [95, 88, 92, 90, 85])
s2 = Student("Ravi", [70, 65, 68, 72, 75])
s3 = Student("Kiran", [55, 60, 58, 62, 50])

students = [s1, s2, s3]

# Display results
for s in students:
    s.show()

'''
'''class Employee:
    def __init__(self, name, base_salary, bonus):
        self.name = name
        self.base_salary = base_salary
        self.bonus = bonus

    def total_salary(self):
        return self.base_salary + self.bonus

emps = [
    Employee("A", 30000, 5000),
    Employee("B", 25000, 3000),
    Employee("C", 40000, 8000),
    Employee("D", 28000, 4000),
    Employee("E", 35000, 7000),
]

highest = emps[0]
for e in emps:
    if e.total_salary() > highest.total_salary():
        highest = e

print("Highest Earner:", highest.name, highest.total_salary())
'''

