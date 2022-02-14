#Below we have given you the code for three classes: Owner,
#Pet, and Name.
#
#An Owner is defined by two attributes: a Name and a list of
#Pets. The list of pets is initially empty; it can be added
#to later.
#
#A Pet is defined by two attributes: a Name and an Owner.
#
#A Name is defined by two attributes, both strings,
#representing first and last name.
#
#Write a function called get_owner_string that will take as
#input a single instance of Pet. The function should then print
#out the Pet's Owner's name using the following format:
#
#Boggle Joyner's owner is David Joyner.
#
#You will need to access the Pet's first name, pet's last name,
#pet's owner's first name, and pet's owner's last name to
#accomplish this. You may NOT modify the Name, Pet, or Owner
#classes (we will test your code with our own copies of these
#classes, so any changes you make will not be part of our
#grading code).
#
#HINT: To access a pet's name, you would use the_pet.name. So,
#to access only the pet's first name, you would use
#the_pet.name.first. To access a pet's owner's, you would use
#the_pet.owner. So, how would you access the pet's owner's
#first and last name?

class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        
class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

#Add your get_owner_string function here!
def get_owner_string(pet): 
    return pet.name.first + " " + pet.name.last + "'s owner is " + pet.owner.name.first + " " + pet.owner.name.last + "."
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Boggle Joyner's owner is David Joyner.
#Artemis Joyner's owner is David Joyner.
#Pippin Hepburn's owner is Audrey Hepburn.
owner_1 = Owner(Name("David", "Joyner"))
owner_2 = Owner(Name("Audrey", "Hepburn"))

pet_1 = Pet(Name("Boggle", "Joyner"), owner_1)
pet_2 = Pet(Name("Artemis", "Joyner"), owner_1)
pet_3 = Pet(Name("Pippin", "Hepburn"), owner_2)

owner_1.pets.append(pet_1)
owner_1.pets.append(pet_2)
owner_2.pets.append(pet_3)

print(get_owner_string(pet_1))
print(get_owner_string(pet_2))
print(get_owner_string(pet_3))


class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        
class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []


#First, we define our function. Its name is get_owner_string,
#and it has one parameter, an instance of Pet:
def get_owner_string(a_pet):
    #Next, we want to find the four names that we care about:
    #the pet's first and last name, and the owner's first and
    #last name.
    #
    #The pet's first and last name are contained in the attribute
    #name, so let's grab that first:
    pets_name = a_pet.name
    
    #Now, we can grab the first and last name from pets_name:
    pets_first = pets_name.first
    pets_last = pets_name.last
    
    #We can do the same thing for the owner's name. First, we get
    #the owner out of a_pet:
    owner = a_pet.owner
    
    #Then we get the owner's name:
    owners_name = owner.name
    
    #Then we get their first and last name:
    owners_first = owners_name.first
    owners_last = owners_name.last
    
    #Finally, we knit that all together into the final string:
    result = pets_first + " " + pets_last + "'s owner is " + owners_first + " " + owners_last + "."
    
    #And return that!
    return result

    #There's a more efficient way to do this though. Check out
    #the other sampe answer to see!


owner_1 = Owner(Name("David", "Joyner"))
owner_2 = Owner(Name("Audrey", "Hepburn"))
pet_1 = Pet(Name("Boggle", "Joyner"), owner_1)
pet_2 = Pet(Name("Artemis", "Joyner"), owner_1)
pet_3 = Pet(Name("Pippin", "Hepburn"), owner_2)

print(get_owner_string(pet_1))
print(get_owner_string(pet_2))
print(get_owner_string(pet_3))



class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        
class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []


def get_owner_string(a_pet):
    #There are two ways we can make the other solution better.
    #First, we do not need to unpack the objects one step at
    #a time; for example, we can access the owner's first name
    #directly using: a_pet.owner.name.first.
    #
    #Second, we can use the string method format() to make this
    #easier to format as a string.
    #
    #Put these two together, and we get this:
    
    #Finally, we knit that all together into the final string:
    result = "{0} {1}'s owner is {2} {3}.".format(a_pet.name.first, a_pet.name.last, a_pet.owner.name.first, a_pet.owner.name.last)
    
    #And return that!
    return result


owner_1 = Owner(Name("David", "Joyner"))
owner_2 = Owner(Name("Audrey", "Hepburn"))
pet_1 = Pet(Name("Boggle", "Joyner"), owner_1)
pet_2 = Pet(Name("Artemis", "Joyner"), owner_1)
pet_3 = Pet(Name("Pippin", "Hepburn"), owner_2)

print(get_owner_string(pet_1))
print(get_owner_string(pet_2))
print(get_owner_string(pet_3))
