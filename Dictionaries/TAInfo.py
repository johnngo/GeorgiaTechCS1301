#We've defined a list of tuples below. Each tuple follows
#the format: (name, home state).
#
#Create a dictionary called ta_dict in the space below, where
#the keys are each TA's name, and the values are their home
#state.

ta_info = [("Joshua", "Georgia"),
          ("Jackie", "Vermont"),
          ("Marguerite", "Tennessee")]

#Add your code to create the dictionary as described!
#The first item in each tuple should be a key, and
#the second item in each tuple should be its value.
#Note that you may create this either by reading and
#using the ta_info list of tuples, or you can create
#the dictionary from scratch:


#Create your dictionary here!
ta_dict = {}
for info in ta_info:
    ta_dict[info[0]] =info[1]


#Now, create three variables: josh_val, jack_val, and
#marg_val. Set josh_val equal to Josh's dictionary value,
#then jack_val equal to Jackie's, then marg_val equal to
#Marguerite's. Remember how to properly access the value
#corresponding to a dictionary key!
#
#Make sure you use dictionary-access syntax to do this.
#Don't create the variables based on new values.


#Create your variables here!
josh_val = ta_dict["Joshua"]
jack_val = ta_dict["Jackie"]
marg_val = ta_dict["Marguerite"]


#If your code works as intended, the following three lines
#will run and print Georgia, Vermont, and Tennessee:
print(josh_val)
print(jack_val)
print(marg_val)


ta_info = [("Joshua", "Georgia"),
          ("Jackie", "Vermont"),
          ("Marguerite", "Tennessee")]

#The problem said you could either create the dictionary
#from scratch, create it based on ta_info, or create it
#dynamically. Let's look at all three!
#
#Here's creating it from scratch:

ta_dict = {"Joshua":"Georgia", "Jackie":"Vermont", "Marguerite":"Tennessee"}

#To create it from ta_info, we'd just replace the string
#literals in the dictionary definition with the list
#and tuple indices:

ta_dict = {ta_info[0][0]:ta_info[0][1], ta_info[1][0]:ta_info[1][1], ta_info[2][0]:ta_info[2][1]}

#To create it dynamically, we would look over all the keys
#and add the new key-value pair to the dictionary:

ta_dict = {}
for ta_tuple in ta_info:
    ta_dict[ta_tuple[0]] = ta_tuple[1]

#Any of these three approaches would crate ta_dict with the
#right values. The first method only works with these three
#names and states, the second method works with any values of
#ta_info as long as there are exactly three, and the third
#works for any values of ta_info no matter how many names.
#   
#
#Now, we just need to pull the data back out of the dictionary:

josh_val = ta_dict['Joshua']
jack_val = ta_dict["Jackie"]
marg_val = ta_dict["Marguerite"]

#And print it:

print(josh_val)
print(jack_val)
print(marg_val)
