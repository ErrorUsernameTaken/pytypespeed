from time import time
prompt = "hey, this is a placeholder"

def counter():
	print(prompt)
	input(">> Press ENTER to begin")
	begin_time = time()
	inp = input("\n")
	end_time = time()
	final_time = (end_time - begin_time) / 60
	return final_time, inp

#calculates words per minute
def calcWpm(time, line):
	words = line.split()
	word_length = len(words)
	words_per_m = word_length / time
	return words_per_m


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
wpm = calcWpm(tm, line)
wpm = round(wpm, 2)
print("Total time: {} minutes".format(tm))
print("Average WPM: {}".format(wpm))
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("Accuracy: {}".format(percentager))
