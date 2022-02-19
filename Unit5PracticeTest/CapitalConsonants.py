#Write a function called count_capital_consonants. This
#function should take as input a string, and return as output
#a single integer. The number the function returns should be
#the count of characters from the string that were capital
#consonants. For this problem, consider Y a consonant.
#
#For example:
#
# count_capital_consonants("Georgia Tech") -> 2
# count_capital_consonants("GEORGIA TECH") -> 6
# count_capital_consonants("gEOrgIA tEch") -> 0


#Write your function here!
def count_capital_consonants(string: str) -> int:
    # sol 1:
    consonants_count = 0
    for char in string:
        if char not in 'AEIOU':
            if 'B' <= char < 'Z':
                consonants_count += 1
    return consonants_count


#The lines below will test your code. Feel free to modify
#them. If your code is working properly, these will print
#the same output as shown above in the examples.
print(count_capital_consonants("Georgia Tech"))
print(count_capital_consonants("GEORGIA TECH"))
print(count_capital_consonants("gEOrgIA tEch"))


#For this problem, our initial thought process should be to start with a count
#variable that will hold the number of capital consonants.

def count_capital_consonants (string):
    count = 0

#We are given a string and we should iterate through each character of that string
#so that we can see whether or not it is a capital consonant
#Since we now have access to each individual character, we can now filter through
#and count how many are capital consonants.

    for char in string:
        if char not in "AEIOU":
            if 'A' < char < 'Z':
                count += 1
    return count

#The order of the two conditionals don't really matter, it is up to you.
#We check to see if the 'char' is not a capital vowel, and see if the 'char'
#is within the appropriate range.
#If both those conditions pass then we increment count since we found our
#capital consonant.
#And at the end, of course, we return our count.
