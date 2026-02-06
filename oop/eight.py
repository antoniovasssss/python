# adding attributes to objects
class Student:
 def set_name(self, name):
   self.name = name

 def show_name(self):
  print(self.name)

# create objects
s1 = Student()
s2 = Student()

s1.set_name("Alex")
s2.set_name("John")

# now display the names
s1.show_name()
s2.show_name()


# you can access atributes directly like this
# print(s1.name)
# print(s2.name)

