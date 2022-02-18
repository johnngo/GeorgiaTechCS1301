#Create a class called Name. Name should have two attributes
#(instance variables): first_name and last_name. Make sure
#the variable names match those words. Both will be strings.
#
#Name should have a constructor with two required parameters,
#one for each of those attributes (first_name and last_name,
#in that order).
#
#Name should also have two methods. The first should be
#called find_printed_name, and should return the first and
#last name with a space in between, e.g. "David Joyner". The
#second method should be called find_sortable_name, and
#should return the last name, then a comma and space, and
#then only the first initial, e.g. "Joyner, D".
#
#Neither sortable_name nor printed_name should be attributes:
#both should be created and returned when those methods are
#called. Neither method will have any parameters besides self.


#Write your class here!
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def find_printed_name(self):
        return self.first_name + " " + self.last_name
    
    def find_sortable_name(self):
        return self.last_name + ", " + self.first_name[0:1]

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print
#David
#Joyner
#David Joyner
#Joyner, D
test_name = Name("David", "Joyner")
print(test_name.first_name)
print(test_name.last_name)
print(test_name.find_printed_name())
print(test_name.find_sortable_name())



#As we learnt, in classes now we will be creating constructors (the __init__ function).
#This is an important concept to grasp for future CS courses so make sure you review
#the videos if you do not understand it!
#
#As asked, our constructor should have two attributes, first_name and last_name
#In Python, we conventionally use the variable name 'self' to identify the instance's
#attributes.

class Name:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

#As shown above, we create a class "Name" and make our constructor
#The instructions tell us to make sure to have first_name first
#in our parameters.
#
#We continue by creating methods within our Name class as told

    def find_printed_name(self):
        return self.first_name + " " + self.last_name
    def find_sortable_name(self):
        return self.last_name + ", " + self.first_name[0]

#Note that for any method that requires us to access any attributes
#of the class we need to have self as the parameter of the method!
#The return statement is simply the current instance's first_name
#and last name with formatting excepted by the problem.
#
#self.first_name[0] is to access only the first character of the first name.