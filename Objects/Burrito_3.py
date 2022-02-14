#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        
        
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
        
    
    def get_meat(self):
        return self.meat
    
    def get_to_go(self):
        return self.to_go
    
    def get_rice(self):
        return self.rice
    
    def get_beans(self):
        return self.beans
    
    def get_extra_meat(self):
        return self.extra_meat
    
    def get_guacamole(self):
        return self.guacamole
    
    def get_cheese(self):
        return self.cheese
    
    def get_pico(self):
        return self.pico
    
    def get_corn(self):
        return self.corn

    def set_meat(self, new_value):
        if new_value in ["chicken", "steak", "pork", "tofu", False]:
            self.meat = new_value
        else:
            self.meat = False
            
    def set_to_go(self, new_value):
        if new_value in [True, False]:
            self.to_go = new_value
        else:
            self.to_go = False
    
    def set_rice(self, new_value):
        if new_value in ["white", "brown", False]:
            self.rice = new_value
        else:
            self.rice = False
    
    def set_beans(self, new_value):
        if new_value in ["black", "pinto", False]:
            self.beans = new_value
        else:
            self.beans = False
    
    def set_extra_meat(self, new_value):
        if new_value in [True, False]:
            self.extra_meat = new_value
        else:
            self.extra_meat = False
    
    def set_guacamole(self, new_value):
        if new_value in [True, False]:
            self.guacamole = new_value
        else:
            self.guacamole = False
    
    def set_cheese(self, new_value):
        if new_value in [True, False]:
            self.cheese = new_value
        else:
            self.cheese = False
    
    def set_pico(self, new_value):
        if new_value in [True, False]:
            self.pico = new_value
        else:
            self.pico = False
    
    def set_corn(self, new_value):
        if new_value in [True, False]:
            self.corn = new_value
        else:
            self.corn = False
            
    def get_cost(self):
        self.cost = 5.0
        if self.get_meat() in ["chicken", "pork", "tofu"]:
            self.cost += 1.0
        if self.get_meat() == "steak":
            self.cost += 1.5
        if self.get_extra_meat() == True and self.get_meat() != False:
            self.cost += 1
        if self.get_guacamole() == True:
            self.cost += 0.75

        return self.cost
#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75


#Because get_cost sounds like a getter, you might be tempted
    #to make cost an attribute. Note, though, that cost should
    #always be calculated dynamically, and so we really don't need
    #to save it once the method is over. So, first we define our
    #method:
    def get_cost(self):
        
        #Next, we initialize cost:
        cost = 5.0
        
        #Next, we check the meats and guacamole attributes. Note
        #that it's best practice to use getters here: on the next
        #problem, you'll find you'll have an easier time if you use
        #getters here instead of accessing self.meat directly:
        if self.get_meat() in ["chicken", "pork", "beef"]:
            cost += 1.0
        if self.get_meat() == "steak":
            cost += 1.5
        if self.get_extra_meat() and self.get_meat():
            cost += 1.0
        if self.get_guacamole():
            cost += 0.75
            
        #Finally at the end, we return the cost:
        return cost
    
        #Note that this really wasn't any different than writing
        #a function that calculates the cost from a burrito parameter.
        #In fact, you could copy this method outside the class and
        #run it as-is if you use an instance of Burrito as the argument
        #into the function (e.g. get_cost(burrito_1)).




a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())