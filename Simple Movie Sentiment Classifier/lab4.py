import string
import operator

data = ""
totalS = {}

try:
	data = open("sentiment-train.txt", "r", encoding = 'utf-8', errors = 'ignore')
except:
	print("File could not be opened.")
#Adding our original training data

for line in data:
	line.translate(str.maketrans('', '', string.punctuation))
	tokens = line.split()
	if(str(tokens[1]) == str(1)):
	#postive reviews
		for word in tokens:
			if word in totalS:
				totalS[word] += 1
			else:
				totalS[word] = 1
	else:
	#negative reviews
		for word in tokens:
			if word in totalS:
				totalS[word] -= 1
			else:
				totalS[word] = -1
print("\nTraining is complete.\n")
sorted = sorted(totalS.items(), key = lambda x : x[1])
	
for x in sorted[0:10]:
	print(x)
for y in sorted[len(sorted)-11:len(sorted)-1]:
	print(y)