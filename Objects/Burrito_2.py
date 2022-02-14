#Our initial class definition and constructor header are
#the same as before:
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        
        #Note, though, that inside the constructor, we're
        #now calling self.set_meat and the other setters.
        #This way, we only have to have our data validation
        #in one place, inside the setters. When we create a
        #new instance of Burrito, we automatically call the
        #methods that check whether the input is valid.
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
        
    #All our getters just return the corresponding values:
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
    
    #Each setter first compares the new value to a list of
    #acceptable values. If the new value is in that list, it
    #sets its value for that attribute equal to the new value.
    #If not, it sets its value for that attribute equal to
    #False:
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