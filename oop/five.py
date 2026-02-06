class Student: # Student is the class name, this is the blueprint for creating student objects
   def greet(self): # create a method called greet() that takes self as a parameter 
      print("Hello student")

s1 = Student()
s1.greet() # this now becomes Student.greet(s1)
