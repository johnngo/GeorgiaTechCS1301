#Write a class called Thing. The constructor for Thing should
#have two required parameters: its mass and its volume, in
#that order. These should be saved as the object's mass and
#volume attributes, respectively.
#
#Additionally, the object should have two other attributes,
#weight and density. weight should be calculated by multiplying
#the mass by the gravity on earth, 9.8, and rounding to the
#nearest tenth. density should be calculated by dividing mass
#by volume and rounding to the nearest tenth.
#
#When the constructor has finished initalizing the object, it
#should thus have four attributes: mass, volume, weight, and
#density. mass and volume will have the same values given to
#the constructor, and weight and density will be calculated
#based on those values.


#Add your class here!
class Thing:
    def __init__(self, mass, volume):
        self.mass = float(mass)
        self.volume =float(volume)
        self.weight = round(mass *9.8,1)
        self.density = round(mass/volume,1)


#The following lines of code will test your object. If it
#is written correctly, they will print:
#10
#5
#98.0
#2.0
#14.0
#75.0
#137.2
#0.2
thing_1 = Thing(10.0, 5.0)
thing_2 = Thing(14.0, 75.0)

print(thing_1.mass)
print(thing_1.volume)
print(thing_1.weight)
print(thing_1.density)
print(thing_2.mass)
print(thing_2.volume)
print(thing_2.weight)
print(thing_2.density)



#First we define the class. Classes are defined with the
#keyword class, followed by the name of the class:
class Thing:
    
    #Next, we need to give it the __init__ method. This is
    #where the initial parameters are sent. The instructions
    #called for a Thing to be defined by two initial
    #parameters: mass and volume. All methods require the
    #first parameter to be 'self'. So, we define __init__ with
    #these three parameters:
    def __init__(self, mass, volume):
        
        #Then, we first need to save the mass and volume to
        #attributes in the object. Attributes are always
        #prefaced by self. Note that the directions called for
        #the attributes to be named mass and volume, so we must
        #define these as self.mass and self.volume. However, we
        #could have named the parameters to __init__ something
        #else; by convention we often give them the same name.
        self.mass = mass
        self.volume = volume
        
        #Once we have saved mass and volume, the directions
        #wanted us to also create two additional attributes:
        #weight and density. These are calculated based on mass
        #and volume. We define weight like this:
        self.weight = round(mass * 9.8, 1)
        
        #...and density like this:
        self.density = round(mass * volume, 1)
        
        #Because these are still attributes, they are preceded
        #by self. as well. Note also that we could have used
        #self.mass and self.volume in these calculations if we
        #wanted to; they are identical to mass and volume since
        #we set them equal earlier in the method.


