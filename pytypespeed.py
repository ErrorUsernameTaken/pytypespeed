from time import time
i = 0
cs = False
prompt = "This is a placeholder prompt."

def counter():
	i = 0 
	print(prompt)
	input("Press enter to begin. Once you have finished, press enter.")
	begin_time = time()
	inp = input("\n")
	end_time = time()
	final_time = (end_time - begin_time) / 60
	return final_time, inp


def wpm(time, line):
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
words_per_minute = wpm(tm, line)
words_per_minute = round(words_per_minute, 2)
print("Total time: {} minutes".format(tm))
print("Average WPM: {} words per minute".format(words_per_minute))
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("Accuracy: {}% accuracy".format(percentager))
