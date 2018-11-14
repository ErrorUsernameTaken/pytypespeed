import time
import keyboard

# average - "/prompts/average_prompt.py" (maybe)
# advanced - "/prompts/advanced_prompt.py" (maybe)
# not sure if i should change prompts into just words (no list)

prompt = "walmart gaming yeah"  # placeholder prompt

# lets the user choose the word difficulty
def diffChoice():
    diffi = input("Average or advanced?: ").lower()
    if diffi not in ('average', 'advanced'):
        print("Please pick a valid difficulty.")
        diffChoice()
    else:
        if diffi == 'average':
            pass
            # open average-prompt.py
            # and then, when the user picks the word amount
            # ^ call wordChoice for this
            # select that many words from that file
        elif diffi == 'advanced':
            pass
            # same thing, different files


diffChoice()


# lets the user choose how many words they want to type
def wordChoice():
    wordAmt = int(input("How many words do you want to type? (50-1000): "))
    if wordAmt not in range(50, 1000):
        print("Please pick a valid number.")
        wordChoice()
    else:
        print(wordAmt)
        # select wordAmt words from whatever file
        # need to print out the words so that they aren't in a list format


# keeps track of time
def counter():
    print(prompt)
    input(">> Press ENTER to begin")
    keyboard.block_key("backspace")  # disables backspaces
    global errors
    errors = 0
    # for recording errors:
    # after the user is done, loop through both lists
    # if a character typed isn't equal to a character in the prompt, add an error

    global start_time
    start_time = time.time()
    inp = input("\n")
    global end_time
    end_time = time.time()
    final_time = (end_time - start_time) / 60
    return final_time, inp


# calculates words per minute
def calcWpm(time, line):
    words = line.split()
    word_length = len(words)
    words_per_m = word_length / time
    return words_per_m


# checks for incorrect words
def wordcheck(inp):
    prompts = prompt.split()
    inputs = inp.split()
    errorcount = 0

    idx = 0
    for inp in inputs:
        if inp != prompts[idx]:
            errorcount += 1
            if inp == prompts[idx + 1]:
                idx += 2
            elif inp != prompts[idx - 1]:
                idx += 1
        else:
            idx += 1

    correct = float(len(prompts)) - float(errorcount)
    percentage = float(correct) / float(len(prompts)) * 100

    return percentage


# calculates statistics
tm, line = counter()
tm = round(tm, 2)
hours, rem = divmod(end_time - start_time, 3600)
minutes, seconds = divmod(rem, 60)
wpm = calcWpm(tm, line)
wpm = round(wpm, 2)
print("Total time: {:0>2}:{:05.2f}".format(int(minutes), seconds))
print("Average WPM: {}".format(wpm))
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("Accuracy: {}".format(percentager))
