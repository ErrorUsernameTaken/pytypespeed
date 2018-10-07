import time

prompt = "walmart gaming yeah" #placeholder prompt

#lets the user choose the word difficulty
def diffChoice():
        diffi = input("Average or advanced?: ").lower()
        if diffi not in ('average', 'advanced'):
                print("Please pick a valid difficulty.")
                diffChoice()
        else:
                if diffi == 'average':
                        print("advanced")
                        #open average-prompt.py
                        #and then, when the user picks the word amount
                        #^ call wordChoice for this
                        #select that many words from that file
                elif diffi == 'advanced':
                        print("advanced")
                        #same thing, different files

diffChoice()

#lets the user choose how many words they want to type
def wordChoice():
        wordAmt = int(input("How many words do you want to type? (50-1000): "))
        if wordAmt not in range(50, 1000):
                print("Please pick a valid number.")
                wordChoice()
        else:
                print(wordAmt)
                #select wordAmt words from whatever file
                #need to print out the words so that they aren't
                #in a list format
        
#keeps track of time
def counter():
	print(prompt)
	input(">> Press ENTER to begin")
	global start_time
	start_time = time.time()
	inp = input("\n")
	global end_time
	end_time = time.time()
	final_time = (end_time - start_time) / 60
	return final_time, inp

#calculates words per minute
def calcWpm(time, line):
	words = line.split()
	word_length = len(words)
	words_per_m = word_length / time
	return words_per_m

#checks for incorrect works
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

	words_left = len(prompts) - len(inputs)
	correct = float(len(prompts)) - float(errorcount)
	percentage = (((float(correct) / float(len(prompts))) - float(words_left) / float(len(prompts))) * 100)

	
	return percentage


tm, line = counter()
tm = round(tm, 2)
hours, rem = divmod(end_time - start_time, 3600)
minutes, seconds = divmod(rem, 60)
wpm = calcWpm(tm, line)
wpm = round(wpm, 2)
print("Total time: {:0>2}:{:05.2f}".format(int(minutes),seconds))
print("Average WPM: {}".format(wpm))
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("Accuracy: {}".format(percentager))
