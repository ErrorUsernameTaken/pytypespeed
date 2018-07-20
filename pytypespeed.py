from time import time #removing from time breaks the program for some reason
#import random
#import keyboard

#have the user control how many words they type (todo)
#fix some errors with typing (todo)
#fix accuracy and wpm (todo)
#how do i test if wpm is correcT?
#fix calculating errors (todo)
#prevent backspaces (either use pynput or keyboard module)

prompt = "This is a placeholder prompt."

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
    disable backspaces
"""

def choices():
    global diff
    diff = input("Choose a difficulty: Average/Advanced ")
    diff = diff.lower()
    x = 0
    while x > 1:
        if diff == 'average':
            #change prompt assignment to average_prompt
            x = x + 1
        elif diff == 'advanced':
            global prompt2
            #change prompt assignment to advanced prompt
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
            #change yeah
            z = z + 1
        elif death == 'n':
            #don't need to assign here
            z = z + 1

    if death not in ('y', 'n'):
        print('Your input is invalid. Please try again.')
        deathchoice()

deathchoice()

#keeps track of the user's word amount
def words():
    wordamt = int(input("How many words do you want to type?\n(Must be in the range 1-10000) "))
    if wordamt < 1 or wordamt > 10000:
        print('Your input is invalid. Please try again.')

    #global prompt reassignment broken
    #prompt = random.sample(prompt, wordamt)


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
    global error_count
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
