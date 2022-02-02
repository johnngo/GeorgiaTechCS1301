#Recall Coding Problem 4.3.9 (Advanced), the free body
#diagram problem. If you were unable to solve that, we've
#included the sample answer in the dropdown in the top left
#-- feel free to use that to write your answer to this
#problem.
#
#Revise your code from that problem to use a file instead of
#a list as its parameter. Name this new function
#find_net_force_from_file. The function should take one
#parameter, the name of a file. The function should return
#the net magnitude and direction, just as it did in the other
#problem.
#
#Each line of the file will have two numbers, both integers:
#the first number will be the magnitude, and the second
#number will be the angle (in degrees, from -180 to 180).
#There will be a space between them.
#
#HINT: You may have multiple functions in your code if you
#want!
#
#HINT 2: Try to write this such that you can reuse as much
#of your earlier code as possible. Remember, when loading
#from a file, any text you load is initially a string. You'll
#almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#Add your function here!
def find_net_force_from_file(filename):
    read_file = open(filename, "r")
    ListT = []
    
    for item in read_file:
        item = item.rstrip('\n')
       
        item = item.split()
        
        
        item0 = int(item[0])
        
        item1 = int(item[1])
        finalitem = item0,item1
        
       
        tupleitem =tuple(finalitem)
        ListT.append(tupleitem)
  
    
    HC = 0
    VC = 0
    for element in ListT:
        ele0 = element[0]
        ele1 = radians(element[1])
        
        HC +=ele0*cos(ele1)
        VC +=ele0*sin(ele1)
    
    
    net_magnitude = sqrt(HC**2 + VC**2)
    net_magnitude = round(net_magnitude,1)
    
    net_angle = atan2(VC,HC)
    
    net_angle = degrees(net_angle)
    
    net_angle = round(net_angle,1)
    
    return (net_magnitude, net_angle)

    read_file.close()
    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))


from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#First, let's try this the more "natural" way. Note that this
#isn't the best way to do this, but it's the way that probably
#came to mind first.
#
#We already had a function called find_net_force. Let's just
#copy that function and adapt it. Our goal is going to be to
#load the forces in from the file in such a way that we don't
#even have to change the rest of the code.
#
#First, we change its name and parameter:
def find_net_force_from_file(filename):
    
    #Now, we open the file:
    file = open(filename)
    
    #We want to create a list of forces. In our previous code,
    #this list was called forces, so let's keep that variable
    #name. So, we create that empty list:
    forces = []
    
    #For each line in the file...
    for line in file:
        
        #First we want to split it into two parts based on
        #where the space occurs. That's the default behavior
        #for the string's split() method.
        split_line = line.split()
        
        #Now that we've split the line up, the first value will
        #be the magnitude, and the second will be the angle. We
        #want to convert both to integers:
        magnitude = int(split_line[0])
        angle = int(split_line[1])
        
        #This is now a new force tuple, so let's create that
        #tuple:
        new_force = (magnitude, angle)
        
        #And add it to the list:
        forces.append(new_force)
        
    #We're done with the file now, so we close it.
    file.close()
    
    #At this point in our code, we've create a list called forces,
    #and filled it with 2-tuples, each with a magnitude and an
    #angle. So, the rest of our code can remain totally
    #unchanged! Our original function started with the forces
    #list passed in as an argument.
    #
    #But wait, if our previous function started with forces as an
    #argument, and this function created the list forces... why
    #did we modify the function at all? Check out sample_answer_2.py
    #for the better approach!
    
    total_horizontal = 0
    total_vertical = 0
    
    for force in forces:
        magnitude, angle = force
        angle = radians(angle)
        horizontal = magnitude * cos(angle)
        vertical = magnitude * sin(angle)
        total_horizontal += horizontal
        total_vertical += vertical
        
    net_magnitude = sqrt(total_horizontal**2 + total_vertical**2)
    net_magnitude = round(net_magnitude, 1)
    
    print(total_vertical, total_horizontal)
    net_angle = atan2(total_vertical, total_horizontal)
    net_angle = degrees(net_angle)
    net_angle = round(net_angle, 1)
    
    return (net_magnitude, net_angle)




print(find_net_force_from_file("a_few_angles.txt"))


from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#From last time, we had this function:
def find_net_force(forces):
    total_horizontal = 0
    total_vertical = 0
    
    for force in forces:
        magnitude, angle = force
        angle = radians(angle)
        horizontal = magnitude * cos(angle)
        vertical = magnitude * sin(angle)
        total_horizontal += horizontal
        total_vertical += vertical
    
    net_magnitude = sqrt(total_horizontal**2 + total_vertical**2)
    net_magnitude = round(net_magnitude, 1)
    
    net_angle = atan2(total_vertical, total_horizontal)
    net_angle = degrees(net_angle)
    net_angle = round(net_angle, 1)
    
    return (net_magnitude, net_angle)

#Instead of modifying it, why don't we just reuse it as is?
#Let's create a new function called find_net_force_from_file:
def find_net_force_from_file(filename):
    
    #And load the angles from the file exactly as we did
    #in the other sample answer:
    file = open(filename)
    
    forces = []
    for line in file:
        split_line = line.split()
        
        magnitude = int(split_line[0])
        angle = int(split_line[1])
        new_force = (magnitude, angle)
        
        forces.append(new_force)
        
    file.close()
    
    #Now instead of including our net force calculations in
    #this function, let's just call the other one:
    result = find_net_force(forces)
    
    #That result will be the same!
    return result
    

print(find_net_force_from_file("a_few_angles.txt"))