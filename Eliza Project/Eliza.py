#This is my Eliza Program it commands the conversation allowing for easier key phrase searching, the program is broken up into sections, upon completion of a section (or while loop)
#the program moves on to the next section (much like stepping from one boulder to another across a pond) counters are given within each while loop to indicate upon successful completion of a step the program jumps
#foward to the next while loop or section, some sections break off from the original story line allowing sub-story lines to take place however the program will finally
#reach back to the same ending upon completion of 21 turns (a turn being an interaction between Eliza and the user). The program is similar to leading a blind man along a path.

#Example: (Name Identification)
#a) "I am Alex Jonas" -> results in keyword match of "I am" and a register save of whatever is typed afterward which is assumed will be the name of the user.
#b) "My name is Alex Jonas" -> results in keyword match of "name is" and a register save of whatever is typed afterward which is assumed to be the name of the user.
#c) "I'm Alex Jonas -> results in a keyword match of "I'm" and a register save of whatever is typed afterward which is assumed to be the name of the user.
#d) "Alex Jonas" -> this lookup results a match of "(word, word)" which is assumed to be the user simply typing there name, no keywords in this case simply except the 2 words separated by a space.

#Within each while loop "Eliza" searches for a particular response given a question within the previous while loop, depending upon your response you will be given different responses from Eliza
#as well as differing questions. "Eliza" also remembers the users name, placing the register storing the users name into a variable (variables are implied as strings within python) called "name_string",
#the exact same idea is expressed for "new_string" which pertains to how evertying is going at home (a question asked by Eliza) who then brings up there response later during the discussion. The name_string and
#new_string designed to be a basic idea for a memory register for Eliza.

#No priority queue within this Eliza program, however a basic priority is given to abusive language, as Eliza will interact with the user saying "Please refrain from that use of language" instead of
#continuing to look for an expression match.
import re
print("This is Eliza The Academic Advisor, programmed by Alex Jonas" + "\n")
print("-> [Eliza]: Shalum, I'm your Academic Advisor. What is your name")
counter = 100
regex_I = r"(.*)[Ii]\b(.*)"
regex_Im = r"(.*)[Ii]\'?m\b(.*)"
regex_am = r"(.*)am\b(.*)"
regex_my = r"(.*)my\b(.*)"
user_dialogue = input("=> [User]: ")
regex_swear = r"(.*)ass(.*)|(.*)bitch(.*)|(.*)fuck(.*)|(.*)shit(.*)|(.*)piss(.*)|(.*)dick(.*)|(.*)pussy(.*)"
while(user_dialogue != 'exit' and counter == 100):
	#Different possibilities for stating your name to Eliza
	if re.search(regex_swear, user_dialogue) is not None: #looks for abusive language before searching for any other regular expression match
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r".*\b[Ii] am\b (.*)\b", user_dialogue) != None: # Finds I am or i am (name here)
		print(re.sub(r".*\b[Ii] am\b (.*)\b", r"-> [Eliza]: Hi \1. What is your major?", user_dialogue)) 
		counter = 200
		name_string = re.sub(r".*\b[Ii] am\b (.*)\b", r"\1", user_dialogue) #saves name into string variable named "name_string" which will be called upon later, acts as a memory.
	elif re.search(r".*\b[Nn]ame is\b(.*)\b", user_dialogue) != None:
		print(re.sub(r".*\b[Nn]ame is\b(.*)\b", r"-> [Eliza]: Hi \1. what is your major?", user_dialogue))  #Finds my name is (name here)
		counter = 200
		name_string = re.sub(r".*\b[Ii] am\b (.*)\b", r"\1", user_dialogue)
	elif re.search(r".*\b[Ii]'?m\b(.*)\b", user_dialogue) != None:
		print(re.sub(r".*\b[Ii]'?m\b(.*)\b", r"-> [Eliza]: Hi \1. what is your major?", user_dialogue)) # Finds I'm or i'm or im (name here)
		counter = 200
		name_string = re.sub(r".*\b[Ii] am\b (.*)\b", r"\1", user_dialogue)
	elif re.search(r"([A-Za-z]+ [A-Za-z]+)\b", user_dialogue) != None: #finds instance of just name being given
		print(re.sub(r"([A-Za-z]+ [A-Za-z]+)\b", r"-> [Eliza]: Hi \1. Not much of a conversationalist are you. What is your major?", user_dialogue))
		counter = 200
		name_string = re.sub(r".*\b[Ii] am\b (.*)\b", r"\1", user_dialogue)
	
	
	else: 
		print("> I didn't quite catch that")
		
	user_dialogue = input("=> [User]: ")
	
#Example: (Name Identification, above)
#Your Response -> Eliza Response
#a) "I am Alex Jonas" -> results in keyword match of "I am" and a register save of whatever is typed afterward which is assumed will be the name of the user.
#b) "My name is Alex Jonas" -> results in keyword match of "name is" and a register save of whatever is typed afterward which is assumed to be the name of the user.
#c) "I'm Alex Jonas -> results in a keyword match of "I'm" and a register save of whatever is typed afterward which is assumed to be the name of the user.
#d) "Alex Jonas" -> this lookup results a match of "(word, word)" which is assumed to be the user simply typing there name, no keywords in this case simply except the 2 words separated by a space.
#e) "What is going on here?" -> I didn't quite catch that.
#f) "Ah Shit" -> Please refrain from that use of language.

#counter then increases to 200 and waits for user input after input is given Eliza checks the while loop counter finds it doesn't match, so Eliza checks the next while loop finds that it matches and
#looks for a regular expression that matches the input given at the end of the last while loop if it does counter results in an increase to 300 otherwise Eliza responds "Could you repeat that" (or something similar)
#and waits for input from the user within the same while loop, this will continue until the input matches a regular expression within the while loop.
	
while(user_dialogue != 'exit' and counter == 200):
	if re.search(regex_swear, user_dialogue) is not None:
		print("Please refrain from that use of language.")
	elif re.search(r"([A-Za-z]+ [A-Za-z]+\b|[A-Za-z]+\b)", user_dialogue) != None:
		print(re.sub(r"([A-Za-z]+ [A-Za-z]+\b|[A-Za-z]+\b)", r"-> [Eliza]: Are you enjoying \1 as of now?", user_dialogue)) #Finds instance only putting in your name, needs to be fixed
		counter = 300
	
	else: 
		print("> Could you repeat that")
	user_dialogue = input("=> [User]: ")
	
while(user_dialogue != 'exit' and counter == 300):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r"(.*)[Yy]e(.*)\b|(.*)[Ff]ar(.*)\b", user_dialogue) != None:
		print(re.sub(r"(.*)[Yy]e(.*)\b|(.*)[Ff]ar(.*)\b", r"-> [Eliza]: That's good to hear, what's your favorite part about it?", user_dialogue)) # looks for keywords that have a ye or far within them usually indicating good
		counter = 400
	elif re.search(r"(.*)[Nn]o(.*)\b", user_dialogue) != None:
		print(re.sub(r"(.*)[Nn]o(.*)\b", r"-> [Eliza]: I'm sorry to hear your not enjoying it. Where are you from?", user_dialogue)) #Looks for any instance of no or not indicating not enjoying the major
		counter = 400
	elif re.search(r".*I\b.*[Qq]uestion.*\b", user_dialogue) != None:
		print(re.sub(r".*I\b.*[Qq]uestion.*\b", r"-> [Eliza]: Of course. How can I help you today?", user_dialogue))
		counter = 500
	
	else: 
		print("> repeat that again for me.")
	user_dialogue = input("=> [User]: ")
	
while(user_dialogue != 'exit' and counter == 400):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	#elif re.search(r"([A-Za-z., ]+)\b", user_dialogue) != None:
		#print(re.sub(r"([A-Za-z., ]+)\b", r"> \1 you say? Interesting. So how can I help you today?", user_dialogue)) #iterates first word user types out then repeats the output for as many words that were entered by the user
	elif re.search(r"(.*)I\b(.*)", user_dialogue) is not None:
		new_quote = user_dialogue
		new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_I, new_quote)) is not None: #looks for any instance of "I" within a statement and changes the I to a "you", while loop is used in case there are multiple instances of I within the statement
			new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_Im, new_quote)) is not None: #looks for any instance of "Im" within a statement and changes the Im to "your", while loop is used in case there are mulitple instances of Im within the statement
			new_quote = re.sub(regex_Im, r"\1your\2", new_quote)
		while(re.search(regex_am, new_quote)) is not None: #looks for any instance of "am" within a statement and changes the am to a "are", while loop is used in case there are multiple instances of am within the statement
			new_quote = re.sub(regex_am, r"\1are\2", new_quote)
		while(re.search(regex_my, new_quote)) is not None: #looks for any instance of "my" within a statement and changes the my to a "your", while loop is used in case there are multiple instances of my within the statement
			new_quote = re.sub(regex_my, r"\1your\2", new_quote)
		print("-> [Eliza: " + new_quote + ". Interesting! So how can I help you today?")
		counter = 500
	
	else: 
		print("-> [Eliza]: Sorry, can you say that again?")
	user_dialogue = input("=> [User]: ")
	
while(user_dialogue != 'exit' and counter == 500): #This is the start of actual advisement help or sorta help since the advisor doesn't know anything about your academics
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza}: Please refrain from that use of language.")
	elif re.search(r"(.*)[Cc]redits?(.*)[Gg]raduate(.*)\b|(.*)[Gg]raduate(.*)[Cc]redits?(.*)\b", user_dialogue) != None:
		print(re.sub(r"(.*)[Cc]redits?(.*)[Gg]raduate(.*)\b|(.*)[Gg]raduate(.*)[Cc]redits?(.*)\b", r"-> [Eliza]: How many credits do you think you need to graduate?", user_dialogue)) #checks for keywords credits and graduate
		counter = 600
	
	else:
		print("-> {Eliza]: Could you repeat that for me?")
	user_dialogue = input("=> [User]: ")

while(user_dialogue != 'exit' and counter == 600):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r".*[Nn]ot sure.*\b|.*[Dd]on'?t know.*\b|.*[Tt]hink.*\b", user_dialogue) != None:
		print(re.sub(r".*[Nn]ot sure.*\b|.*[Dd]on'$t know.*\b|.*[Tt]hink.*\b", r"-> [Eliza]: I'm concerned you don't know. Students need to understand they are responsible for themeselves.", user_dialogue)) #checks for keywords not sure, don't know, or think, assuming think means the user is not completely sure
		counter = 700
	elif re.search(r".*[0-9]+.*", user_dialogue) != None:
		print(re.sub(r".*([0-9]+).*", r"-> [Eliza]: You only need \1 more credits? Good for you. What classes are you taking?", user_dialogue)) #need to figure out number bug
		counter = 700
	
	else:
		print("-> [Eliza]: I seem to have troube understanding what your saying, could you repeat that?")
	user_dialogue = input("=> [User]: ")

while(user_dialogue != 'exit' and counter == 700):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	#elif re.search(r"(.*)", user_dialogue) != None:
		#print(re.sub(r"(.*)", r"-> [Eliza]: \1? Hm. How are things at home?", user_dialogue)) #takes any input and repeats it back to the user along with a question
	elif re.search(r"(.*)I\b(.*)", user_dialogue) is not None:
		new_quote = user_dialogue
		new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_I, new_quote)) is not None:
			new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_Im, new_quote)) is not None:
			new_quote = re.sub(regex_Im, r"\1your\2", new_quote)
		while(re.search(regex_am, new_quote)) is not None:
			new_quote = re.sub(regex_am, r"\1are\2", new_quote)
		while(re.search(regex_my, new_quote)) is not None:
			new_quote = re.sub(regex_my, r"\1your\2", new_quote)
		print("-> [Eliza]: " + new_quote + "? Hm. How are things at home?")
		counter = 800
	
	else:
		print("-> [Eliza]: I seem to have trouble understanding what your saying, could you repeat that?")
	user_dialogue = input("=> [User]: ")
while(user_dialogue != 'exit' and counter == 800):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r".*([Gg]ood).*\b|.*([Ff]ine).*\b|.*([Nn]ot [Bb]ad).*\b|.*([Tt]errific).*\b|.*([Ww]onderful).*\b|.*([Ee]xceptionall?y?).*\b|.*([Ee]xcellent).*|.*([Ff]antastic).*\b", user_dialogue) != None: #searches for any instance of good as the keyword or a synonym of the word
		print(re.sub(r".*([Gg]ood).*\b|.*([Ff]ine).*\b|.*([Nn]ot [Bb]ad).*\b|.*([Tt]errific).*\b|.*([Ww]onderful).*\b|.*([Ee]xceptionall?y?).*\b|.*([Ee]xcellent).*\b|.*([Ff]antastic).*\b", r"-> [Eliza]: Oh Good! Have you thought about what you'll do after you graduate?", user_dialogue))
		counter = 900
		new_string = re.sub(r".*([Gg]ood).*\b|.*([Ff]ine).*\b|.*([Nn]ot [Bb]ad).*\b|.*([Tt]errific).*\b|.*([Ww]onderful).*\b|.*([Ee]xceptionall?y?).*\b|.*([Ee]xcellent).*\b|.*([Ff]antastic).*\b", r"\1\2\3\4\5\6\7\8", user_dialogue)
	elif re.search(r".*([Nn]ot.*[Gg].*)\b|.*([Bb]ad).*\b|.*([Oo]kay).*\b|.*([Tt]erribly?).*\b|.*([Aa]wful).*\b", user_dialogue) != None: #searches for any instance of bad as the keyword or a synonym of the word
		print(re.sub(r".*([Nn]ot.*[Gg]ood).*\b|.*([Bb]ad).*\b|.*([Oo]kay).*\b|.*([Tt]erribly?).*\b|.*([Aa]wful).*\b", r"I'm sorry to hear things are \1\2\3\4\5 at home. Have you thought about what you'll do after you graduate?", user_dialogue))
		counter = 900
		new_string = re.sub(r".*([Nn]ot.*[Gg]ood).*\b|.*([Bb]ad).*\b|.*([Oo]kay).*\b|.*([Tt]erribly?).*\b|.*([Aa]wful).*\b", r"\1\2\3\4\5", user_dialogue)
		
		
	else:
		print("-> [Eliza]: Could you repeat that?")
	user_dialogue = input("=> [User]: ")
	
while(user_dialogue != 'exit' and counter == 900):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r".*[Aa]m [Nn]ot.*\b|.*[Nn]o.*\b|.*[Dd]on'?t.*\b|.*[Kk]ind.*\b", user_dialogue) != None:
		print(re.sub(r".*[Aa]m [Nn]ot.*\b|.*[Nn]o.*\b|.*[Dd]on'?t.*\b|.*[Kk]ind.*\b", r"-> [Eliza]: You sound discouraged, college is hard work but you can do it.", user_dialogue)) #Looks for no or a synonym of no as a keyword
		counter = 1000
	elif re.search(r".*[Yy]es.*\b|.*[Ss]orta ?\b|.*[Ss]ort of.*\b|.*[Ii] [Hh]ave.*\b", user_dialogue) != None:
		print(re.sub(r".*[Yy]es.*\b|.*[Ss]orta ?\b|.*[Ss]ort of.*\b|.*[Ii] [Hh]ave.*\b", "r-> [Eliza]: I am glad to hear you are not discouraged, college is hard work but you can do it.", user_dialogue)) #Looks for yes or a synonym of yes as a keyword
		counter = 1000
	
	else:
		print("-> [Eliza]: Sorry?")
	user_dialogue = input("=> [User]: ")

while(user_dialogue != 'exit' and counter == 1000):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r"\b.*\b", user_dialogue) != None:
		print(re.sub(r"\b.*\b", r"-> [Eliza]: I'm only trying to encourage you. Before I forget what year are you currently in?", user_dialogue))
		counter = 1100
	
	else:
		print("-> [Eliza]: Could you repeat that?")
	
	user_dialogue = input("=> [User]: ")
	
while(user_dialogue != 'exit' and counter == 1100):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r".*([1-2]).*\b|.*([Ff]reshmen).*\b|.*([Ss]ophmore).*\b", user_dialogue) != None:
		print(re.sub(r".*([1-2]).*\b|.*([Ff]reshmen).*\b|.*([Ss]ophmore).*\b", r"-> [Eliza]: You still have most your college experience ahead of you! How do you feel about that?", user_dialogue))
		counter = 1200
	elif re.search(r".*([3-4]).*\b|.*([Jj]unior).*\b|.*([Ss]enior).*\b", user_dialogue) != None:
		print(re.sub(r".*([3-4]).*\b|.*([Jj]unior).*\b|.*([Ss]enior).*\b", r"-> [Eliza]: Your almost out of here! How does that make you feel?", user_dialogue))
		counter = 1200
	
	else:
		print("-> [Eliza]: Say that again?")
	user_dialogue = input("=> [User]: ")
	
while(user_dialogue != 'exit' and counter == 1200):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r".*[Ii].*[Ff]eel (.*)", user_dialogue) != None:
		print(re.sub(r".*[Ii].*[Ff]eel (.*)", r"-> [Eliza]: What makes you feel \1?", user_dialogue)) 
		counter = 1300
	elif re.search(r".*[Gg]ood.*\b|.*[Ff]ine.*\b|.*[Nn]ot [Bb]ad.*\b|.*[Tt]errific.*\b|.*[Ww]onderful.*\b|.*[Ee]xceptionall?y?.*\b|.*[Ee]xcellent.*|.*[Ff]antastic.*\b", user_dialogue) != None: #searches for any instance of good as the keyword or a synonym of the word
		print(re.sub(r".*([Gg]ood).*\b|.*([Ff]ine).*\b|.*([Nn]ot [Bb]ad).*\b|.*([Tt]errific).*\b|.*([Ww]onderful).*\b|.*([Ee]xceptionall?y?.*)\b|.*([Ee]xcellent).*\b|.*([Ff]antastic).*\b", r"-> [Eliza]: What makes you feel \1\2\3\4\5\6\7 about it?", user_dialogue))
		counter = 1300
	elif re.search(r".*[Nn]ot.*[Gg].*\b|.*[Bb]ad.*\b|.*[Oo]kay.*\b|.*[Tt]erribly?.*\b|.*[Aa]wful.*\b", user_dialogue) != None: #searches for any instance of bad as the keyword or a synonym of the word
		print(re.sub(r".*([Nn]ot.*[Gg]ood).*\b|.*([Bb]ad).*\b|.*([Oo]kay).*\b|.*([Tt]erribly?).*\b|.*([Aa]wful).*\b", r"-> [Eliza]: What makes you feel \1\2\3\4\5 about it?", user_dialogue))
		counter = 1300
	
	else:
		print("-> [Eliza]: Not sure what you meant")
		
	user_dialogue = input("=> [User]: ")
	
while(user_dialogue != 'exit' and counter == 1300): #needs work
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	#elif re.search(r"(.*)[Ii]'?m(.*)\b|.*[Ii].*[Ff]eel(.*)|.*[Ii].*[Gg]uess(.*)\b", user_dialogue) != None:
		#print(re.sub(r"(.*)[Ii]'?m(.*)\b|.*[Ii].*[Ff]eel(.*)|.*[Ii].*[Gg]uess(.*)", r" You say you feel, \1\2 about it. Why is that?", user_dialogue))
	elif re.search(r"(.*)I\b(.*)", user_dialogue) is not None:
		new_quote = user_dialogue
		new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_I, new_quote)) is not None:
			new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_Im, new_quote)) is not None:
			new_quote = re.sub(regex_Im, r"\1your\2", new_quote)
		while(re.search(regex_am, new_quote)) is not None:
			new_quote = re.sub(regex_am, r"\1are\2", new_quote)
		while(re.search(regex_my, new_quote)) is not None:
			new_quote = re.sub(regex_my, r"\1your\2", new_quote)
		print("-> [Eliza]: You stated that: " + new_quote + ", Why is that?")
		counter = 1400
	#elif re.search(r".*[Ii].*[Dd]on'?t.*[Kk}now.*\b", user_dialogue) != None:
		#print(re.sub(r".*[Ii].*[Dd]on'?t.*[Kk]now.*\b", r"-> [Eliza]: You sound like your unsure, why is that?", user_dialogue))
		#counter = 1400
	
	else:
		print("-> [Eliza]: Could you repeat that?")
		
	user_dialogue = input("=> [User]: ")
		
while(user_dialogue != 'exit' and counter == 1400):#check this one
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r"(.*)I\b(.*)", user_dialogue) is not None:
		new_quote = user_dialogue
		new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_I, new_quote)) is not None:
			new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_Im, new_quote)) is not None:
			new_quote = re.sub(regex_Im, r"\1your\2", new_quote)
		while(re.search(regex_am, new_quote)) is not None:
			new_quote = re.sub(regex_am, r"\1are\2", new_quote)
		while(re.search(regex_my, new_quote)) is not None:
			new_quote = re.sub(regex_my, r"\1your\2", new_quote)
		print("-> [Eliza]: " + new_quote + "? Okay, would you be interested in a group advising session?")
		counter = 1500
	
	else:
		print("-> [Eliza]: I didn't quite catch that")
		
	user_dialogue = input("=> [User]: ")

while(user_dialogue != 'exit' and counter == 1500):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r".*[Nn]o.*\b|.*[Dd]on'?t.*\b", user_dialogue) != None:
		print(re.sub(r".*[Nn]o.*\b|.*[Dd]on'?t.*\b", r"-> [Eliza]: Before your to quick to say no, at least allow me to tell you about it.", user_dialogue))
		counter = 1600
	elif re.search(r".*[Yy]es.*\b|.*[Ss]ure.*\b|.*[Ww]hy [Nn]ot.*\b|.*[Gg]o.*\b|.*[Aa]bsolutely.*\b", user_dialogue) != None:
		print(re.sub(r".*[Yy]es.*\b|.*[Ss]ure.*\b|.*[Ww]hy [Nn]ot.*\b|.*[Gg]o.*\b|.*[Aa]bsolutely.*\b", r"-> [Eliza]: Great! I'll set up the meeting. First let me tell you about it.", user_dialogue))
		counter = 1600
	elif re.search(r".*[Dd]on'?t.*[Kk]now.*\b|.*[Mm]ay.*\b|.*[Pp]erhap.*\b|.*[Mm]ight.*\b|.*[Cc]ould.*\b|.*[Ss]hould.*\b", user_dialogue) != None:
		print(re.sub(r".*[Dd]on'?t.*[Kk]now.*\b|.*[Mm]ay.*\b|.*[Pp]erhap.*\b|.*[Mm]ight.*\b|.*[Cc]ould.*\b|.*[Ss]hould.*\b", r"-> [Eliza]: Let me tell you about it, before making any final decisions.", user_dialogue))
		counter = 1600
	
	else:
		print("-> [Eliza]: Could you repeat that again?")
		
	user_dialogue = input("=> [User]: ")

while(user_dialogue != 'exit' and counter == 1600):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r".*\b", user_dialogue) != None:
		print(re.sub(r".*\b", r"->[Eliza]: The Advising Sessions sponsored by yours truly is a time to reflect. You, " + name_string + " will be asked a question pertaining to you an important "
		+ "personal detail about oneself, if we believe you are lying you are subject to ever increasing excrutiatingly painful, physical penalties. Sound fun? Are you interested?", user_dialogue))
		counter = 1700
	
	else:
		print("-> [Eliza]: I can't quite hear you")
	
	user_dialogue = input("=> [User]: ")
	
while(user_dialogue != 'exit' and counter == 1700):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r".*[Nn]o.*\b|.*[Dd]on'?t.*\b", user_dialogue) != None:
		print(re.sub(r".*([Nn]o).*\b|(.*[Dd]on'?t.*)\b", r"-> [Eliza]: \1? Very well. Earlier you stated that things at home were" + new_string + ". How do you feel about that?", user_dialogue))
		counter = 1800
	elif re.search(r".*[Yy]es.*\b|.*[Ss]ure.*\b|.*[Ww]hy [Nn]ot.*\b|.*[Gg]o.*\b|.*[Aa]bsolutely.*\b", user_dialogue) != None:
		print(re.sub(r".*[Yy]es.*\b|.*[Ss]ure.*\b|.*[Ww]hy [Nn]ot.*\b|.*[Gg]o.*\b|.*[Aa]bsolutely.*\b", r"-> [Eliza]: Great! I think your going to enjoy it. Earlier you stated that things at home were " + new_string + ". How do you feel about that?", user_dialogue))
		counter = 1800
	elif re.search(r".*[Dd]on'?t.*[Kk]now.*\b|.*[Mm]ay.*\b|.*[Pp]erhap.*\b|.*[Mm]ight.*\b|.*[Cc]ould.*\b|.*[Ss]hould.*\b", user_dialogue) != None:
		print(re.sub(r".*[Dd]on'?t.*[Kk]now.*\b|.*[Mm]ay.*\b|.*[Pp]erhap.*\b|.*[Mm]ight.*\b|.*[Cc]ould.*\b|.*[Ss]hould.*\b", r"-> [Eliza]: We can circle back to that later. Earlier you stated that things at home were " + new_string + ". How do you feel about that?", user_dialogue))
		counter = 1800
	
	else:
		print("-> [Eliza]: Could you repeat that? ")
	
	user_dialogue = input("=> [User]: ")
	#Repeat if they want to go or if they don't

while(user_dialogue != 'exit' and counter == 1800):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	#elif re.search(r"[Ii] [Ff]eel (.*)", user_dialogue) != None:
	elif re.search(r"(.*)I\b(.*)", user_dialogue) is not None:
		new_quote = user_dialogue
		new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_I, new_quote)) is not None:
			new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_Im, new_quote)) is not None:
			new_quote = re.sub(regex_Im, r"\1your\2", new_quote)
		while(re.search(regex_am, new_quote)) is not None:
			new_quote = re.sub(regex_am, r"\1are\2", new_quote)
		while(re.search(regex_my, new_quote)) is not None:
			new_quote = re.sub(regex_my, r"\1your\2", new_quote)
		
		print("-> [Eliza]: " + new_quote + "? Why is that?")
		counter = 1900
	
	else:
		print("=> [User]: I want you to state this as 'I feel a certain way' it causes you to reflect.")
		
	user_dialogue = input("=> [User]: ")
		
while(user_dialogue != 'exit' and counter == 1900): #fix this and were done, fixed!
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
	elif re.search(r"(.*)I\b(.*)", user_dialogue) is not None:
		new_quote = user_dialogue
		new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_I, new_quote)) is not None:
			new_quote = re.sub(regex_I, r"\1you\2", new_quote)
		while(re.search(regex_Im, new_quote)) is not None:
			new_quote = re.sub(regex_Im, r"\1your\2", new_quote)
		while(re.search(regex_am, new_quote)) is not None:
			new_quote = re.sub(regex_am, r"\1are\2", new_quote)
		while(re.search(regex_my, new_quote)) is not None:
			new_quote = re.sub(regex_my, r"\1your\2", new_quote)
		print("-> [Eliza]: " + new_quote + ". I enjoyed talking to you today " + name_string + " now get out of my office.")
		counter = 2000
	
	else:
		print("=> [Eliza]: Remember when reflecting use I to start with.")
		
	user_dialogue = input("=> [User]: ")
	

while(user_dialogue != 'exit' and counter == 2000):
	if re.search(regex_swear, user_dialogue) is not None:
		print("-> [Eliza]: Please refrain from that use of language.")
		user_dialogue = input("=> [User]: ")
	elif re.search(r".*", user_dialogue) is not None:
		print("=> [Eliza]: Until next time.")
	
	else:
		print("=> [Eliza]: Thanks.")
		
	print("=> [Eliza]: End of program.")
	exit() #ends the program
	



		
