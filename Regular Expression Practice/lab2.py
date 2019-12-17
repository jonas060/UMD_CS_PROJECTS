import re

print("Here we go: ")
user_dialogue = input("=> [User]: ")
new_string = "No Match"
checker = False

regex_tommy = r"(.*)\b[Tt]homas [Jj]\. [Hh]ill\b(.*)"
regex_punct = r"(.*)[.,?!](.*)"
regex_catbear = r"[Cc]at\b|[Bb]ear\b"
regex_integer = r"^\d+|\b\d+$"

while(user_dialogue != 'exit'):
	new_string = user_dialogue
	new_string = re.sub(regex_tommy, r"\1Tommy Hill\2", user_dialogue)
	while(re.search(regex_punct, new_string)) is not None:
		new_string = re.sub(regex_punct, r"\1X\2", new_string)
	new_string = re.sub(regex_integer, r"INT", new_string)
		
	if new_string == user_dialogue and re.search(regex_catbear, user_dialogue) is None:
		print("No Match")
		
	else:
		print(new_string)
		
	user_dialogue = input("=> [User]: ")
		
	