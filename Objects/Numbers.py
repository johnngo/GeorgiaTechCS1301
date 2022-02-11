#Write a class named "Number" with one attribute called 
#"value" which defaults to 0 and another attribute called 
#"even" which defaults to True.
#
#Next, create an instance of this class and assign it to
#a variable called "number_instance".
#
#Then, set the value attribute to 101 and the even
#attribute to False.


#Write your code here!


#Note that this exercise does not print anything by
#default. You're welcome to add print statements to debug
#your code when running it. Note that the autograder
#will check both your value for number_instance and your
#definition of the class Number.

class Number:
    def __init__(self):
        self.value = 0
        self.even = True

number_instance= Number()

number_instance.value = 101
number_instance.even = False

#First, we name the class:
class Number:
    
    #Next, we create the constructor. There are no additional
    #parameters, so we only include one: self, which is
    #included in every method inside a class.
    def __init__(self):
        
        #By default, we set a new instance of Number to have
        #an attribute 'value' with a value of 0. Because this
        #is an attribute that should persist after this method
        #is done, we call this self.value:
        self.value = 0
        
        #Then, we do the same for even:
        self.even = True

#Now, outside the class, we create a new instance of Number:
number_instance = Number()

#Then, we change its value attribute:
number_instance.value = 101

#And its even attribute:
number_instance.even = False
