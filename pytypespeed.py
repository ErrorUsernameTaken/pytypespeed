from time import time #removing from time breaks the program for some reason
#import average-prompt
#import advanced-prompt
#import random
#import keyboard
import os
import sys

prompt = "This is a placeholder prompt."

#since english-master files are out of order, do something with random module maybe?
#have the user control how many words they type (todo)
#fix some errors with typing (todo)
#fix accuracy and wpm (todo)
#how do i test if wpm is correcT?
#fix calculating errors (todo)
#prevent backspaces (either use pynput or keyboard module)

#Errors -
"""
This is aplceholder repmopt. -
File "/Users/Trent/Desktop/Programming/Python/!!!WIP Projects/TypingTest.py", line 83, in <module>
words_per_minute = wpm(tm, line)
File "/Users/Trent/Desktop/Programming/Python/!!!WIP Projects/TypingTest.py", line 54, in wpm
words_per_m = word_length / time
ZeroDivisionError: float division by zero

this is a placehodler prompt
File "/Users/Trent/Desktop/Programming/Python/!!!WIP Projects/TypingTest.py", line 125, in <module>
percentage = wordcheck(line)
File "/Users/Trent/Desktop/Programming/Python/!!!WIP Projects/TypingTest.py", line 105, in wordcheck
if inp == prompts[idx + 1]:
IndexError: list index out of range
"""

print("Notice: backspaces are disabled. (or will be)\n")

"""
while True:

"""
def choices():
    global diff
    diff = input("Choose a difficulty: Average/Advanced ")
    diff = diff.lower()
    x = 0
    while x > 1:
        if diff == 'average':
            x = x + 1
        elif diff == 'advanced':
            x = x + 1

    if diff not in ('average', 'advanced'):
        print('Your input is invalid. Please try again.')
        choices()

choices()

def deathchoice():
    global death
    death = input("Would you like sudden death to be enabled? (Y/N) ")
    death = death.lower()
    z = 0
    while z > 1:
        if death == 'y':
            z = z + 1
        elif death == 'n':
            z = z + 1

    if death not in ('y', 'n'):
        print('Your input is invalid. Please try again.')
        deathchoice()

deathchoice()

#checks if the user has the files
#maybe use try/catch statement?

def file():
    global filepath
    filepath = input("Where is the prompt file located?: ")
    #personal is /Users/Trent/Desktop/Future\ Reference/google-10000-english-master/10k-english-usa-no-swears-medium.txt
    #/Users/Trent/Desktop/Future\ Reference/google-10000-english-master/10k-english-usa-no-swears-long.txt
    #I DON'T KNOW HOW TO DO THIS ANY OTHER WAY =)
    if diff == 'average':
        if os.path.exists(average-prompt):
            #run prompts (call counter() )
            #seems to work without calling counter(), which is interesting. might change later
            print("h")
        else:
            print("The file does not exist. \nPlease download the file here - https://bit.ly/2M8205X")
            print("Alternatively, if you have already downloaded the file, please restart the program and try again.")
    elif diff == 'advanced':
        if os.path.exists(advanced-prompt):
            #run prompts (call counter() )
            print("h")
        else:
            print("The file does not exist. \nPlease download the file here - https://bit.ly/2M8205X")
            print("Alternatively, if you have already downloaded the file, please restart the program and try again.")

file()

#keeps track of the user's word amount
"""
wordamt = int(input("How many words do you want to type?\n(Must be in the range 1-10000) "))
#have random module
if wordamt < 1 or wordamt > 10000:
    print("What did I just tell you?")
"""

"""
lines = open("../WordsForGames.txt").readlines() 
line = lines[0] 

words = line.split() 
myword = random.choice(words)
"""

#keeps time
def counter():
    print(prompt)
    input("Press enter to begin. Once you have finished, press enter.")
    begin_time = time()
    inp = input("\n")
    end_time = time()
    final_time = (end_time - begin_time)
    return final_time, inp

#calculates wpm
def wpm(time, line):
    words = line.split()
    word_length = len(words)
    words_per_m = word_length / time
    return words_per_m

#checks if words are correct
def wordcheck(inp):
    prompts = prompt.split()
    inputs = inp.split()
    error_count = 0

    idx = 0 #what does idx mean?
    #maybe this limits you to having one error.
    #calculates errors
    #i need to fix this
    for inp in inputs:
        if inp != prompts[idx]:
            error_count += 1
            if inp == prompts[idx + 1]:
                idx += 2
            elif inp != prompts[idx - 1]:
                idx += 1
        else:
            idx += 1

    words_left = len(prompts) - len(inputs)
    correct = float(len(prompts)) - float(error_count)
    percentage = (((float(correct) / float(len(prompts))) - float(words_left) / float(len(prompts))) * 100)

    return percentage

#calculates results
tm, line = counter()
tm = round(tm, 2)
words_per_minute = wpm(tm, line)
words_per_minute = round(words_per_minute, 2) * 100
print("Time: {} seconds".format(tm))
print("Average WPM: {} ".format(words_per_minute))
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("Accuracy: {0:.2f}% ".format(percentager))

name = input("Please enter a name to save your data: ") #for future file thing
