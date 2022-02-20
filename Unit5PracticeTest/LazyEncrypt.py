#For our final problem we apply the open and close file that we learnt
#in our previous unit.
#We open our two files that we will be getting. We set the outputFile mode
#to write since we will be writing to the file, while the inputFile mode
#is on read.

def lazy_encrypt(outFile, inFile, dictionary):
    outputFile = open(outFile, "w")
    inputFile = open(inFile)

#Next with our files open, we readlines() our input file so that we put it
#into a list.

    read = inputFile.readlines()

#Currently read contains sentences in each index
#read = ['Here is a pretty simple message to encrypt', 'When is a pretty...']
#So we need to for each loop it to access each sentence by itself, and then another
#for each loop to access the individual letters.

    for sentence in read:
        for letter in sentence:

#If you understand it to this step the rest becomes straightforward.
#Now that we have access each letter, we can simply check if that letter
#is a key in our dictionary, and it if is then we write the key's value
#as part of our encryption. If the letter is not in our dictionary
#then we simply just write the letter to our outputFile.

            if letter in dictionary:
                outputFile.write(dictionary[letter])
            else:
                outputFile.write(letter)

#When we are done iterating through all the letters of each sentence and
#done iterating through all the sentences in the read list, then we can
#close both files and return

    outputFile.close()
    inputFile.close()
    return

#We have an empty return which is returning 'None' since we are not returning
#anything and just writing into files.


#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, the contents of anOutputFile.txt after running
#will be:
#Horo is a protty simplo mossago ta oncrypt
#Whon it's oncryptod, it will laak difforont

lazy_encrypt("anOutputFile.txt", "anInputFile.txt", {"e": "o", "o": "a"})
print("Done running! Check anOutputFile.txt for the result.")

