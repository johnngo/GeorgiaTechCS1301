#and CatchingMultipleSpecificErrors-5.py from 3.5.3.4.
#
#Write a function called get_integer that takes as input one
#variable, my_var. If my_var can be converted to an integer,
#do so and return that integer. If my_var cannot be converted
#to an integer, return the error message that results from
#attempting to do so.
#
#Do not use any conditionals or the type() function.


#Write your function here!
def get_integer(my_var):
    try:
        return int(my_var)
    except Exception as error:
        return error
    except ValueError as error:
        return error


#You can use the lines below to test out your function. When
#the function is written correctly, the output of these three
#lines should be:
#5
#invalid literal for int() with base 10: 'Boggle.'
#5
print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))
