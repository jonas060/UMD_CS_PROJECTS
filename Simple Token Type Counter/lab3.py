file = input("")
tokenCount = 0
types = set([])
#f = open(file, "r")
#for line in f:
with open(file, 'rb') as f:
	contents = f.read()
	content = contents.split()
	for tokens in content:
		tokens.lower()
		if tokens.isalpha:
			tokenCount += 1
			types.add(tokens)
ratio = tokenCount/len(types)
print("File: " + file + "\n")
print("Tokens: " + str(tokenCount) + "\n")
print("Types: " + str(len(types)) + "\n")
print("Token / Type Ratio: " + str(ratio))