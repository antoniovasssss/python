class Student: # defines a new class called Student
  def __init__(self, name, marks): # the constructor method that runs when you create a new Student object
   self.name = name # creates an instance variable name and assigns the passed-in name to it
   self.marks = marks # creates an instance variable marks and assigns the passed-in markes to it


# Creating Objects
s1 = Student("Ram",85)
s2 = Student("Sita",92)
print(s1.name)
print(s2.name)




