class Student:
    school_name = "ABC School" # shared by all students
    total_students = 0 # counts how many students are created

    # Initialize student data
    def __init__ (self, name, marks):
        self.name = name # instance variable
        self.marks = marks # instance variable
        Student.total_students += 1 # everytime an object is created total_students increases

# Instance method to display student info
    def display_info(self): # instance method (self)
        print("Name:", self.name)
        print("Marks:", self.marks)

# Class method to show school name
    @classmethod
    def show_school(cls): # class method (cls)
        print("School:", cls.school_name)

# Create student objects
s1 = Student("Ram", 85)
s2 = Student("Sita", 92)

# Call instance methods
s1.display_info()
print("-------")
s2.display_info()

# call class method
Student.show_school()

# Show total students
print("Total Students:", Student.total_students)