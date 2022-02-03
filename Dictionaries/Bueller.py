#Write a function called students_present. students_present
#should take as input one parameter, a dictionary. The keys
#of the dictionary will be names, and the values will be one
#of three strings: "Here", "Present", or an empty string "".
#
#Return a list of the keys for whom the corresponding value
#is either "Here" or "Present".


#Add your code here!
def students_present(a_dict):
    list = []
    for item in a_dict.items():
        if item[1] == "Here" or item[1] == "Present":
            list.append(item[0])
    return list

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#["David", "Marguerite", "Joshua", "Erica"]

student_list = {"David" : "Here", "Marguerite" : "Here",
                "Jackie": "", "Joshua": "Present",
                "Erica": "Here", "Daniel": ""}
print(students_present(student_list))



#-----------------------------------------------------------
#First we define the function:
def students_present(students):
    
    #Our goal is to return a list of the students who were
    #present, so let's start by creating an empty list so we
    #can add them as we find them:
    present = []
    
    #There are a couple of ways we could iterate through the
    #dictionary. We could do...
    #
    # for student_name in students:
    #     status = students[student_name]
    #
    #However, we can write a slightly more succinct loop that
    #will pull out both student and status automatically:
    for (student, status) in students.items():
        
        #Inside this loop, student will be the student name
        #that was the key in the dictionary, and status will
        #be the value. So, we check if status is "Present" or
        #"Here":
        if status == "Present" or status == "Here":
            
            #And if it is, we add the student to the list:
            present.append(student)
            
         #If not, we don't need to do anything!
        
    #Finally, at the end, we return our list of students who
    #were present:
    return present




student_list = {"David" : "Here", "Marguerite" : "Here",
                "Jackie": "", "Joshua": "Present",
                "Erica": "Here", "Daniel": ""}
print(students_present(student_list))
