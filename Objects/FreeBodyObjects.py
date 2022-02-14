#Recall in Coding Problem 4.4.4 (and before that, in Coding
#Problem 4.3.9) you built a program for finding the net
#force (magnitude and angle) on an object from several
#individual forces.
#
#In the next two exercises, we're going to convert that
#system into one that uses objects.
#
#To start, create a class called Force. The constructor for
#Force should have two required arguments: magnitude and
#angle. These should be saved to two attributes called
#'magnitude' and 'angle'. You should assume angle is
#initially in degrees, from -180 to 180.
#
#Then, add three methods to Force:
#
# - get_horizontal should return the horizontal component
#   of the force, according to the formula:
#   horizontal = magnitude * cos(angle).
# - get_vertical should return the vertical component of
#   the force, according to the formula:
#   vertical = magnitude * sin(angle).
# - get_angle should return the angle of the force, but
#   should have a keyword parameter called use_degrees.
#   use_degrees should default to True. If use_degrees
#   is true, it should return the angle in degrees; if it
#   is false, it should return the angle in radians.
#
#HINT: Don't overcomplicate this. All we want here is
#a class called Force with four methods: __init__,
#get_horizontal, get_vertical, and get_angle. Note that
#these are not true "getters" even though they have "get"
#in their names: all three will have some reasoning
#beyond just returning a single value.
#
#HINT 2: angle will initially be passed into the
#constructor in degrees. You may store it in either
#degrees or radians. Each approach has different benefits,
#but make sure to keep track of when it's in angles and
#when it's in degrees.

from math import sin, cos, atan2, radians, degrees, sqrt


#Add your code here!
class Force:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = radians(angle)
    def get_horizontal(self):
        horizontal = self.magnitude * cos(self.angle)
        return horizontal
    def get_vertical(self):
        vertical =self.magnitude * sin(self.angle)
        return vertical
    def get_angle(self, use_degrees = True):
        if use_degrees==True:
            d=degrees(self.angle)
            return round(d,3)
        else:
            return self.angle


#Below are some lines of code that will test your object.
#You can change these lines to test your code in different
#ways.
#
#If your code works correctly, this will originally run
#error-free and print (with room for rounding errors):
#Magnitude: 500
#Horizontal: 250.0
#Vertical: 433.0127018922193
#Angle in Degrees: 60.0
#Angle in Radians: 1.0471975511965976
a_force = Force(500, 60)
print("Magnitude:", a_force.magnitude)
print("Horizontal:", a_force.get_horizontal())
print("Vertical:", a_force.get_vertical())
print("Angle in Degrees:", a_force.get_angle())
print("Angle in Radians:", a_force.get_angle(use_degrees = False))

from math import sin, cos, atan2, radians, degrees, sqrt

#First, we define the class:
class Force:
    
    #Then, we define the constructor -- notice it follows
    #the same template as our others. The only difference
    #is that we're converting the angle to radians as soon
    #as it comes in -- you don't have to do that, though:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = radians(angle)
    
    #Then, we define a method for getting the horizontal.
    #Because we converted the angle to radians on line 12,
    #we can just get the cos of the angle -- however, if
    #we had stored it in degrees, we would need to convert
    #it to radians here:
    def get_horizontal(self):
        return self.magnitude * cos(self.angle)
    
    #get_vertical follows the same pattern, but with sin
    #instead of cos:
    def get_vertical(self):
        return self.magnitude * sin(self.angle)
    
    #Finally, we implement get_angle. Note that how this
    #works differs based on what we did in the constructor.
    #Because here we converted it to radians immediately,
    #we have to convert it back to degrees if use_degrees
    #is True:
    def get_angle(self, use_degrees = True):
        if use_degrees:
            return degrees(self.angle)
        else:
            return self.angle
        
    #Notice, though, that in this implementation, we had
    #to remember whether we stored angle in degrees or
    #radians when we implemented get_horizontal and
    #get_vertical. What if we were working on this code
    #with someone else? They might not realize which we
    #did. We can make this a little bit better: check
    #out sample_answer_2.py.