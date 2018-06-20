from time import time
import random
import os
i = 0
prompt = "This is a placeholder prompt."

#since english-master files are out of order, do something with random module maybe?

#file exists but it says there's no path. learn more (todo)
#have the user control how many words they type (todo)
#fix some errors with typing (todo)
"""
This is aplceholder repmopt. -
  File "/Users/Trent/Desktop/Programming/Python/!!!WIP Projects/TypingTest.py", line 83, in <module>
    words_per_minute = wpm(tm, line)
  File "/Users/Trent/Desktop/Programming/Python/!!!WIP Projects/TypingTest.py", line 54, in wpm
    words_per_m = word_length / time
ZeroDivisionError: float division by zero
"""

diff = input("Choose a difficulty: Average/Advanced ")
diff = diff.lower()
if diff == 'average':
    print('The difficulty of your test has been set to average.')
elif diff == 'advanced':
    print('The difficulty of your test has been set to advanced.')
else:
    print('Invalid input.')

#checks if the user has the files
def filecheck():
    if diff == 'average':
        if os.path.exists("10k-english-usa-no-swears-medium.txt"):
            #run prompts
            print("h")
        else:
            print("The file does not exist. \nPlease download the file here - https://bit.ly/2M8205X")
    elif diff == 'advanced':
        if os.path.exists("10k-english-usa-no-swears-long.txt"):
            #run prompts
            print("h")
        else:
            print("The file does not exist. \nPlease download the file here - https://bit.ly/2M8205X")

filecheck()

#keeps time
def counter():
    print(prompt)
    input("Press enter to begin. Once you have finished, press enter.")
    begin_time = time()
    inp = input("\n")
    end_time = time()
    final_time = (end_time - begin_time) / 100
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

    idx = 0
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
words_per_minute = round(words_per_minute, 2)
print("Time: {} seconds".format(tm)) #not true seconds
#it does 0.05 instead of 5.xx or whatever
print("Average WPM: {} ".format(words_per_minute))
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("Accuracy: {0:.2f}% ".format(percentager))

name = input("Please enter a name to save your data: ") #for future file thing
