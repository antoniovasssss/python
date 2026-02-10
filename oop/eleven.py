class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def display_info(self): # is an instance method, it works with object data using self
      print("Name:",self.name)
      print("Marks:",self.marks)

# instance methods are called using objects
s1 = Student("Ram",85)
s1.display_info()


# Class method example
class Student:
    school_name = "ABC School"

    @classmethod
    def show_school(cls): # is a class method, cls refers to the class itself
        print("School:", cls.school_name)  

Student.show_school()

s1.show_school() # object calling class method s1: Student