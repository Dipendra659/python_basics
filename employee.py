#casses in python
#self
#the word self  is used to represent the instance of a class.
#by using the "self" keyword used access the attributes and methods
#of the classes in python.

# **init** method
# **init** is a reserved method in python class.
#init is claed as constructors & this method is called  when an

# object is crested from class
# and its allows the class to initialize the attributes of the class.


class Employee:
     def __init__(self,first, last, email, address):
         self.first = first
         self.last = last
         self.email = email
         self.address = address
     def fullname(self):
      return self.first, self.last

     def emp_email(self):
      return self.email

      def abc(self):
       return self.fullname()

emp_1 = Employee("abc", "xyz", "abc@gmail,com", "npj" )
print(emp_1.fullname())
print(emp_1.emp_email())
