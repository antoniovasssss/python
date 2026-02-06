class Student:
   def set_name(self, name): # stores a name in the instance variable
      self.name = name

   def show_name(self):
      print(self.name) # prints the stored name


s1 = Student() # these are the two seperate Student objects s1 and s2
s2 = Student()

s1.set_name("Alex")
s2.set_name("John")

s1.show_name()
s2.show_name()