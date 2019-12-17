import re
print("> Hello. How are you?")
user_dialog = input("< ")


while(user_dialog != 'exit'):
	if re.search(r"[Ii]\b(.*)\bmy\b(.*)\b", user_dialog) != None:
		print(re.sub(r"[Ii]\b(.*)\bmy\b(.*)\b", r"> What makes you say you\1your\2?", user_dialog))
	elif re.search(r"[Yy]ou\b(.*)\bme\b(.*)\b", user_dialog) != None:
		print(re.sub(r"[Yy]ou\b(.*)\bme\b(.*)\b", r"> Why do you say I\1you\2?", user_dialog))
	elif re.search(r"She\b(.*)\bme\b(.*)\b", user_dialog) != None:
		print(re.sub(r"[Ss]he\b(.*)\bme\b(.*)\b", r"> Why do you say she\1your\2?", user_dialog))
	elif re.search(r"[Hh]e\b(.*)\bme\b(.*)\b", user_dialog) != None:
		print(re.sub(r"[Hh]e\b(.*)\bme\b(.*)\b", r"> Why do you say he\1you\2?", user_dialog))
	else:
		print("> Tell me more.")
	user_dialog = input("< ")
   