class Student:
    school_name = "ABC School"
    
    def __init__(self, name):  
        self.name = name

s1 = Student("Ram")
s2 = Student("Sita")

print(s1.school_name) 
print(s2.school_name)  


# Changing Instance variable
s1.name ="Hari"
print(s2.name)

 
# Changing Class variable
Student.school_name ="XYZ School"