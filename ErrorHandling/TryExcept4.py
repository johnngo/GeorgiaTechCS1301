#Right now, the code below will encounter an error when num
#is 0, but it will not print anything when it does, and then
#it will keep running for num = 1, num = 2, and num = 3
#afterwards. Modify this code so that once it hits an error,
#the loop stops altogether.
#
#You still should not print anything when the error is
#encountered, and the loop definition on line 10 should not
#be changed.

try:
    for num in range(-3, 3):
	    print(5 / num)
except:
    pass



#alternative
#There are two ways to do this. This first way is more
#relevant to this chapter's material, but the second way is
#clever enough that we didn't disallow it on this problem.
#
#First, using this chapter's material: the problem with the
#original code is that the error handling occurred inside
#the loop. After the except block ran when an error was
#encountered, the loop continued with its next iteration.
#That happened because 'try' and 'except were indented
#under the loop.
#
#If we instead want the loop to stop once a single error
#is encountered, we should put the loop inside the try
#block:

try:
    for num in range(-3, 3):
        print(5 / num)
except:
    pass

#When an error occurs in the loop, it jumps to the except
#block on line 19. That's outside the loop, though, so the
#loop is now done.
#
#See sample_answer_2.py for the other possible answer.

#alternative2
#In Chapter 3.3, we briefly talked about special keywords
#for loops: pass, continue, and break. In the original code
#here, we used pass to tell Python that there was no code
#in the except block. What if we change it to break?

for num in range(-3, 3):
    try:
	    print(5 / num)
    except:
        break

#'break' forces the loop containing the 'break' to
#terminate. So, if we 'break' when an error is
#encountered, the loop stops.
