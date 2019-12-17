#Author: Alex Jonas
#Overall Basic Tag Accuracy: 92.13%, Overall Inhanced Accuracy: 92.84%
#Welcome To the Tag.py the best POS tagger in town! The goal of this project was given a corpus where each line consisted of a word and correct POS tag such as: 'Word/NN' read in all lines for the training file
#and based on the words and POS tags read decide a words POS tag given only a word, the only word with no POS tag being the test corpus that your program applies POS tags too. Due to the fact that words may have
#multiple differing POS tags given a specific word we count of the occurence of each differing POS tag given a specific word and generalize that the most common POS tag will be used as the POS tag when applying POS
#tags to the same word given no POS tag if found in the test corpus. The basic and Inhanced versions of this project (before I forget to mention there are two versions to this project) both implement this strategy,
#the only difference being with inhanced we also add 5 rules to increase our Overall Tagging accuracy. Overall tagging accuracy is determined by a gold corpus in which we test our output against.
#
#How the program actually works: Tag.py is the algorithm that creates a decision list for POS tags for a given word. We then send this decision list to an ouput file called: "pos-test-with-tags-basic.txt" for basic
#and "pos-test-with-tags-inhanced.txt" for the inhanced algorithm. We then read in this decision list as well as the "pos-key.txt" into the program scorer.py and place the output into a file called either "basic-tagger-scores.txt"
#or "enhanced-tagger-scores.txt" which will then output the total number of correct and incorrect POS tags, Overall Accuracy of the algorithm in regards to correctly indentifying POS tags given a word, and finally a confusion matrix
#for what the POS tags that were correct were, as well as a confusion matrix for incorrect POS tags and a confusion matrix for what the incorrect POS tags should have been.
#
#Tag.py creates a decision list which is then read into scorer.py for an Overall Accuracy rating as well as confusion matrix for correct, incorrect, and should have been confusion matrixs for the POS tags
#
#Commands:
#
#python3 Tag.py pos-train.txt pos-test.txt simple/(any other phrase) > pos-test-with-tags-basic/enhanced.txt (basic and enhanced depending on what algorithm you want to run, simple/(any other phrase) argument decides what program you
#would like to run with 'simple' being the simple algorithm and '(any other phrase)' being the enhanced version of the algorithm
#
#python3 Scorer.py pos-test-with-tags-basic/enhanced.txt pos-key.txt > basic/enhanced-tagger-scores.txt
#
#Bam! All Done!
#
import os
import sys
import re
import math
from collections import Counter

trainfile = {}
testfile = {}
#array that temporarily holds all files from sys.argv[1] or the 'path' which we have designated to argument 2 which leads to the directory full of the 2,000 files which are to be read in.
#Sift through each word within each dictionary within wordMatrix to get count of each words occurence as well as total amount of words within each dictionary.
#Current file be read in to matrix
#This will be our wordMatrix as discussed above.
trainingfile = sys.argv[1]
testingfile = sys.argv[2]
inhanced = sys.argv[3]
#Verb Rule
Verb_array = ["accept", "add", "admire", "admit", "advise", "afford", "agree", "alert", "allow", "amuse", "analyse", "fall", "announce", "annoy", "answer", "apologise", "appear", "applaud", "appreciate", "approve", "argue", "arrange", "arrest", "arrive", "ask", "attach", "attack", "attempt", "attend", "attract", "avoid", "back", "bake", "balance", "ban", "bang", "bare", "bat", "bathe", "battle", "beam", "beg", "behave", "belong", "bleach", "bless", "blind", "blink", "blot", "blush", "boast", "boil", "bolt", "bomb", "book", "bore", "borrow", "bounce", "bow", "box", "brake", "branch", "breathe", "bruise", "brush", "bubble", "bump", "burn", "bury", "buzz", "calculate", "call", "camp", "care", "carry", "carve", "cause", "challenge", "change", "charge", "chase", "cheat", "check", "cheer", "chew", "choke", "chop", "claim", "clap", "clean", "clear", "clip", "close", "coach", "coil", "collect", "colour", "comb", "command", "communicate", "compare", "compete", "complain", "complete", "concentrate", "concern", "confess", "confuse", "connect", "consider", "consist", "contain", "continue", "copy", "correct", "cough", "count", "cover", "crack", "crash", "crawl", "cross", "crush", "cry", "cure", "curl", "curve", "cycle", "dam", "damage", "dance", "dare", "decay", "deceive", "decide", "decorate", "delay", "delight", "deliver", "depend", "describe", "desert", "deserve", "destroy", "detect", "develop", "disagree", "disappear", "disapprove", "disarm", "discover", "dislike", "divide", "double", "doubt", "drag", "drain", "dream", "dress", "drip", "drop", "drown", "drum", "dry", "dust", "earn", "educate", "embarrass", "employ", "empty", "encourage", "end", "enjoy", "enter", "entertain", "escape", "examine", "excite", "excuse", "exercise", "exist", "expand", "expect", "explain", "explode", "extend", "face", "fade", "fail", "fancy", "fasten", "fax", "fear", "fence", "fetch", "file", "fill", "film", "fire", "fit", "fix", "flap", "flash", "float", "flood", "flow", "flower", "fold", "follow", "fool", "force", "form", "found", "frame", "frighten", "fry", "gather", "gaze", "glow", "glue", "grab", "grate", "grease", "greet", "grin", "grip", "groan", "guarantee", "guard", "guess", "guide", "hammer", "hand", "handle", "hang", "happen", "harass", "harm", "hate", "haunt", "head", "heal", "heap", "heat", "help", "hook", "hop", "hope", "hover", "hug", "hum", "hunt", "hurry", "identify", "ignore", "imagine", "impress", "improve", "include", "increase", "influence", "inform", "inject", "injure", "instruct", "intend", "interest", "interfere", "interrupt", "introduce", "invent", "invite", "irritate", "itch", "jail", "jam", "jog", "join", "joke", "judge", "juggle", "jump", "kick", "kill", "kiss", "kneel", "knit", "knock", "knot", "label", "land", "last", "laugh", "launch", "learn", "level", "license", "lick", "lie", "lighten", "like", "list", "listen", "live", "load", "lock", "long", "look", "love", "man", "manage", "march", "mark", "marry", "match", "mate", "matter", "measure", "meddle", "melt", "memorise", "mend", "mess up", "milk", "mine", "miss", "mix", "moan", "moor", "mourn", "move", "muddle", "mug", "multiply", "murder", "nail", "name", "need", "nest", "nod", "note", "notice", "number", "obey", "object", "observe", "obtain", "occur", "offend", "offer", "open", "order", "overflow", "owe", "own", "pack", "paddle", "paint", "park", "part", "pass", "paste", "pat", "pause", "peck", "pedal", "peel", "peep", "perform", "permit", "phone", "pick", "pinch", "pine", "place", "plan", "plant", "play", "please", "plug", "point", "poke", "polish", "pop", "possess", "post", "pour", "practise", "pray", "preach", "precede", "prefer", "prepare", "present", "preserve", "press", "pretend", "prevent", "prick", "print", "produce", "program", "promise", "protect", "provide", "pull", "pump", "punch", "puncture", "punish", "push", "question", "queue", "race", "radiate", "rain", "raise", "reach", "realise", "receive", "recognise", "record", "reduce", "reflect", "refuse", "regret", "reign", "reject", "rejoice", "relax", "release", "rely", "remain", "remember", "remind", "remove", "repair", "repeat", "replace", "reply", "report", "reproduce", "request", "rescue", "retire", "return", "rhyme", "rinse", "risk", "rob", "rock", "roll", "rot", "rub", "ruin", "rule", "rush", "sack", "sail", "satisfy", "save", "saw", "scare", "scatter", "scold", "scorch", "scrape", "scratch", "scream", "screw", "scribble", "scrub", "seal", "search", "separate", "serve", "settle", "shade", "share", "shave", "shelter", "shiver", "shock", "shop", "shrug", "sigh", "sign", "signal", "sin", "sip", "ski", "skip", "slap", "slip", "slow", "smash", "smell", "smile", "smoke", "snatch", "sneeze", "sniff", "snore", "snow", "soak", "soothe", "sound", "spare", "spark", "sparkle", "spell", "spill", "spoil", "spot", "spray", "sprout", "squash", "squeak", "squeal", "squeeze", "stain", "stamp", "stare", "start", "stay", "steer", "step", "stir", "stitch", "stop", "store", "strap", "strengthen", "stretch", "strip", "stroke", "stuff", "subtract", "succeed", "suck", "suffer", "suggest", "suit", "supply", "support", "suppose", "surprise", "surround", "suspect", "suspend", "switch", "talk", "tame", "tap", "taste", "tease", "telephone", "tempt", "terrify", "test", "thank", "thaw", "tick", "tickle", "tie", "time", "tip", "tire", "touch", "tour", "tow", "trace", "trade", "train", "transport", "trap", "travel", "treat", "tremble", "trick", "trip", "trot", "trouble", "trust", "try", "tug", "tumble", "turn", "twist", "type", "undress", "unfasten", "unite", "unlock", "unpack", "untidy", "use", "vanish", "visit", "wail", "wait", "walk", "wander", "want", "warm", "warn", "wash", "waste", "watch", "water", "wave", "weigh", "welcome", "whine", "whip", "whirl", "whisper", "whistle", "wink", "wipe", "wish", "wobble", "wonder", "work", "worry", "wrap", "wreck", "wrestle", "wriggle", "x-ray", "yawn", "yell", "zip", "zoom"]
#Adjective Rule
JJ_array = ['Defiant', 'Homeless', 'Adorable', 'Delightful', 'Homely', 'Quaint', 'Adventurous', 'Depressed', 'Horrible', 'Aggressive', 'Determined', 'Hungry', 'Real', 'Agreeable', 'Different', 'Hurt', 'Relieved', 'Alert', 'Difficult', 'I', 'Repulsive', 'Alive', 'Disgusted', 'Ill', 'Rich', 'Amused', 'Distinct', 'Important', 'Angry', 'Disturbed', 'Impossible', 'Scary', 'Annoyed', 'Dizzy', 'Inexpensive', 'Selfish', 'Annoying', 'Doubtful', 'Innocent', 'Shiny', 'Anxious', 'Drab', 'Inquisitive', 'Shy', 'Arrogant', 'Dull', 'Itchy', 'Silly', 'Ashamed', 'Sleepy', 'Attractive', 'Eager', 'Jealous', 'Smiling', 'Average', 'Easy', 'Jittery', 'Smoggy', 'Awful', 'Elated', 'Jolly', 'Sore', 'Elegant', 'Joyous', 'Sparkling', 'Bad', 'Embarrassed', 'Splendid', 'Beautiful', 'Enchanting', 'Kind', 'Spotless', 'Better', 'Encouraging', 'Stormy', 'Bewildered' 'Energetic', 'Lazy', 'Strange', 'Black', 'Enthusiastic', 'Light', 'Stupid', 'Bloody', 'Envious', 'Lively', 'Successful', 'Blue', 'Evil', 'Lonely', 'Super', 'Blue-eyed', 'Excited', 'Long', 'Blushing', 'Expensive', 'Lovely', 'Talented', 'Bored', 'Exuberant', 'Lucky', 'Tame', 'Brainy', 'Tender', 'Brave', 'Fair', 'Magnificent', 'Tense', 'Breakable', 'Faithful', 'Misty', 'Terrible', 'Bright', 'Famous', 'Modern', 'Tasty', 'Busy', 'Fancy', 'Motionless', 'Thankful', 'Fantastic', 'Muddy', 'Thoughtful', 'Calm', 'Fierce', 'Mushy', 'Thoughtless', 'Careful', 'Filthy', 'Mysterious', 'Tired', 'Cautious', 'Fine', 'Tough', 'Charming', 'Foolish', 'Nasty', 'Troubled', 'Cheerful', 'Fragile', 'Naughty', 'Clean', 'Frail', 'Nervous', 'Ugliest', 'Clear', 'Frantic', 'Nice', 'Ugly', 'Clever', 'Friendly', 'Nutty', 'Uninterested', 'Cloudy', 'Frightened', 'Unsightly', 'Clumsy', 'Funny', 'Obedient', 'Unusual', 'Colorful', 'Obnoxious', 'Upset', 'Combative', 'Gentle', 'Odd', 'Uptight', 'Comfortable', 'Gifted', 'Old-fashioned', 'Concerned', 'Glamorous', 'Open', 'Vast', 'Condemned', 'Gleaming', 'Outrageous', 'Victorious', 'Confused', 'Glorious', 'Outstanding', 'Vivacious', 'Cooperative', 'Good', 'Courageous', 'Gorgeous', 'Panicky', 'Wandering', 'Crazy', 'Graceful', 'Perfect', 'Weary', 'Creepy', 'Grieving', 'Plain', 'Wicked', 'Crowded', 'Grotesque', 'Pleasant', 'Wide-eyed', 'Cruel', 'Grumpy', 'Poised', 'Wild', 'Curious', 'Poor', 'Witty', 'Cute', 'Handsome', 'Powerful', 'Worrisome', 'Happy', 'Precious', 'Worried', 'Dangerous', 'Healthy', 'Prickly', 'Wrong', 'Dark', 'Helpful', 'Proud', 'Dead', 'Helpless', 'Putrid', 'Zany', 'Defeated', 'Hilarious', 'Puzzled' ,'Zealous']
#CD rule
if inhanced == 'simple':
	print("Simple is always better!")
	print("\n")
	print("\nRunning script name: " + sys.argv[0]+ "\n")
	try:
		print("Processing files from " + sys.argv[1] + "\n")
		#"Python method listdir() returns a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special 
		#entries '.' and '..' even if they are present in the directory." - Taken from: https://www.tutorialspoint.com/python/os_listdir.htm
		trainfile = open(trainingfile, "r", encoding = 'utf-8', errors = 'ignore')
	except:
		print("Error reading first argument from command line\nInclude path to files to be processed")
	d = {}
	thedictionary = {}
	
	for line in trainfile:
		#line = line.lower()
		line = line.strip()
		lineContent = line.rsplit("/", 1)
		#Line read in has format Fight/VB, we therefore read the line in and split along the '/' thereby we are left we two values: value 0 being 'Fight' (our word) and value 1 being 'VB' (our POS tag)
		#lineContent has two values value 0 is the the word while value 1 is the the POS_Tag we then place each value into its own string variable, word going in string variable 'word' while
		#POS tag is placed within string variable POS_Tag.
		word = lineContent[0]
		POS_Tag = lineContent[1]
		
		#We then place both the word and POS tag within a dictionary, the POS tag being our value, while word is our key, if the word has occured for the first time as represented by the else statment we place our first POS tag within the word key,
		#after a word has recurred we append the POS tag value to the existing word (key).
		#
		#																						Example:
		#																				  Read in first Line
		# 																				  WORD/NN is read in
		# 																			    This is then split into:
		#																					{'Word', 'NN'}
		#											We then set 'Word' (word) = (string variable) word and 'NN' (POS tag) = (string variable) POS_tag
		#										We then check to see if word is already in our word dictionary (d), this is represented by "if word in d"
		#										If the word is not within dictionary we then place the word within the dictionary represented by "d[word]"
		#						We then set our POS tag as the value to the key (the key being the word we have just placed within dictionary (represented as d[word] = [POS_Tag]
		#						If however the word is already present within the dictionary we add the POS tag value to the existing key entry (word entry) to which the value belongs
		#				We then have reached the bottom of the for loop so therefore we read in the next line of the file (only 1,232,276 more lines to go!), until we have reached the end of the file
		#
		#																						Visual:
		#																				WORD/NN -> {'WORD', 'NN'}
		#																	d (dictionary) = {(key) WORD : (Value) 'NN'}
		#																			  SPEAR/NN -> {'SPEAR', 'NN'}
		#																	d (dictionary) = {{(key) WORD : (Value) 'NN'}, {(key) SPEAR : (Value) 'NN'}}
		#																				WORD/NN -> {'WORD', 'NN'}
		#																	d (dictionary) = {(key) WORD : (Value) 'NN', 'NN'}, {(key) SPEAR : (Value) 'NN'}}
		#																				WORD/JJ -> {'WORD', 'JJ'}
		#																	d (dictionary) = {{(key) WORD : (Value) 'NN', 'NN', 'JJ'}, {(key) SPEAR : (Value) 'NN'}}
		if word in d:
			d[word].append(POS_Tag)
		else:
			d[word] = [POS_Tag]
	    #From the example above you may notice a problem that begins to develop a key word such as 'WORD' might have more then one type of value (POS tag) such as: 'NN' and 'JJ'. If we are trying to train a program
		#to append a POS tag given only a word how do we decide which POS tag to pick? As you probably have already guessed we will pick the most common POS tag within a key value such as 'WORD', therefore when assigning
		#a POS tag to a word within the test set, the program will assign the most common POS tag of that specific word, which it learned within the Tag.py program!
		#So how do we go about finding the most common POS tag (value) given a word (key)?
	    #After we have loaded our dictonary with every word placed as keys along with the POS tags that are a part of each word as a value, we then sift through each word in the dictionary, looking at all the values we call
		#the method 'Counter' which simply counts all occurences of each POS tag given a word, we then call 'most_common(1)' which picks the highest frequency POS tag given a word. The highest frequencey is indicated by the '1' within
		#the most_common() argument, if we passed in a two we would receive the two highest occurring words, if we passed in a three the three highest occurring words, and so on. Once we have our most occuring word we place into a 1x2 matrix
		#called d_count where the 1x1 part of the matrix is the POS tag, we therefore take this value and place within a string variable called 'tag'. It is this tag string variable value we then assign to our word (key) value. To sum up, what is
		#happening is we take our dictionary (d) with all the words (keys) and there POS Tag values and dump then one by one into a 'cleaner' this cleaner counts up all the differing POS tags given a particular word and disposes of all POS tags 
		#except for the highest occuring POS tag. The cleaner the highest occuring POS tag back into the keys (words) value spot (which the cleaner had originally taken all the POS tags in order to count and dispose of) and sends the word (key) on its
		#merry way. The cleaner does this for every word within the dictionary resulting in a dictionary with words (keys) and one value (Highest occuring POS tag) for that word (key).
		#
		#																								Example:
		#																							Before Mr.Clean
		#													d (dictionary) -> {{(key) 'Tremendous' : (Value) ('NN' : 4), ('JJ' : 3), ('NNP' : 1), ('VB' : 2)} ... }
		#																					 Dump 'Tremendous' into Cleaner
		#																					 		After Mr. Clean
		#																	  thedictionary (dictionary) -> {{(key{ 'Tremendous' : (Value) 'NN'} ... )
	for word in d:
		d_count = Counter(d[word]).most_common(1)
		tag = d_count[0][0]
		thedictionary[word] = tag
		
		
		#print(thedictionary[word]))
		

		
	print("\nRunning script name: " + sys.argv[0]+ "\n")
	try:
		print("Processing files from " + sys.argv[2] + "\n")
		#"Python method listdir() returns a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special 
		#entries '.' and '..' even if they are present in the directory." - Taken from: https://www.tutorialspoint.com/python/os_listdir.htm
		testfile = open(testingfile, "r", encoding = 'utf-8', errors = 'ignore')
	except:
		print("Error reading first argument from command line\nInclude path to files to be processed")
		#Read in line from testfile if (remember testfile is words without POS tags that being said a line from a test file will contain a single word or number of some sort. After reading the line we check to see
		#if the word within the line is contained within our dictionary, if it is, represented by the if statement "if line in thedictionary", we extract the POS tag (value) from the word (key) in our dictonary ('thedictionary')
		#that is equivalent to the word being read in from the test file. Therefore WORD == WORD, yes! Now extract the POS tag of 'WORD' from the key within our dictionary which occurred most frequently, which we found out was 'NN' (thanks Mr.Clean!).
		#After we have extracted the POS tag, assign extracted POS tag to string variable 'tag', then apply said tag to line (word) that was read in along with a '/'. Represented by line = line + "/" + tag, however if the case arises that we don't know
		#what the word being read in is (word being read in wasn't in training corpus) simply slap on a 'NN' POS tag, as open class words are predominately Nouns.
	for line in testfile:
		line = line.strip()
		if line in thedictionary:
			#add POS from thedictionary to line word
			tag = thedictionary[line]
			line = line + "/" + tag
		else:
			line = line + "/" + "NN"
		print(line)
		
		#BOOM! 
		#92.132% accuracy, not bad!
else:
	#Now for our inhanced Program
	#Everything within code is identical except for when assigning tags to the test file, so lets skip down to there.
	print("Let's complicate things!")
	print("\n")
	print("\nRunning script name: " + sys.argv[0]+ "\n")
	try:
		print("Processing files from " + sys.argv[1] + "\n")
		#"Python method listdir() returns a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special 
		#entries '.' and '..' even if they are present in the directory." - Taken from: https://www.tutorialspoint.com/python/os_listdir.htm
		trainfile = open(trainingfile, "r", encoding = 'utf-8', errors = 'ignore')
	except:
		print("Error reading first argument from command line\nInclude path to files to be processed")
	d = {}
	thedictionary = {}
	tagdictionary = {}
	previous_tagged = ""
	for line in trainfile:
		#line = line.lower()
		line = line.strip()
		lineContent = line.rsplit("/", 1) #I believe this has to do with the fact that tokens is not a set therefore doesn't display word and POS as separate items, Nope.
		#for word in matrix.dictionaryHeader[tokens[word]] #might not need this as I believe the if statement will sift through all words occuring within array
		word = lineContent[0]
		POS_Tag = lineContent[1]
		
		if word in d:
			d[word].append(POS_Tag)
		else:
			d[word] = [POS_Tag]
	   
	   #Tag dictionary (POS Tag file): After adding tag to word for thedictionary, add tag along to previous tag to create a dictionary list of tags that come after one another.
	   #Example:
	   #
	   #NN/CD, previous was 'CD'
	   #JJ/NN previous was 'NN'
	   #NNP/JJ previous was 'JJ'
	   #NNP/NNP previous was 'NNP'
	   #NN/NNP previous was 'NNP'
	   #
	   #This will continue with all word POS tags giving us the most common POS tag given a previous POS tag, which is then outputted to a file in which we can deduce a common pattern, such as 'NNP' happens to follow
	   #'NNP' more frequently then any other 'POS tag', which we then used as rule and gave us a 0.313% Increase in Overall Accuracy.
	for word in d:
		d_count = Counter(d[word]).most_common(1)
		tag = d_count[0][0]
		thedictionary[word] = tag
		tagdictionary[word] = previous_tagged + " " + tag #Used to find next most common tag given previous tag, unigram model, used in rule #4, if previous tag was 'NNP' the tag 'NNP' is likely to follow
		previous_tagged = tag
		
		#common_follow_tag = Counter(tagdictionary[word]).most_common(2)
		#print(tagdictionary[word]) #Creates viewable POS Tag file
		#print("\n")
		#print(common_follow_tag)
		
	#And We have arrived! Welcome to the inhanced algorithm! The Inhanced algorithm is identical to the Basic algorithm except that the inhanced differs in two key spots
	#the first spot has already been mentioned (an output text file was created that demonstrated what POS tag came next given a previous POS tag). The second inhancement as shown below occurs when
	#reading in the test file line (test word) and comparing it to our dictionary ('thedictionary') the if case remains the same as the basic version (if test word is in thedictionary slap on the POS tag
	#that thedictionary holds for the specific word onto the test word. However the difference between the basic and inhanced lies within the case that the test word does not appear within the thedictionary,
	#represented by the numberous elif' as well as the else statement. In these cases 5 Rules were incorporated in order to inhance the overall accuracy of the POS tagging algorithm (Overall increase of 0.708%, Overall Accuracy increased from 92.132% to 92.84%)
	#
	#The First Two rules: involve creating an Adjective and Verb array and filling said array with appropiate values (Adjective values in the Adjective array, Verb values in the Verb array). We then compare the unknown test word
	#to each array (Adjective and Verb), if it matches an entry withhin the Adjective array we assign the unknown word a 'JJ' POS tag, if it matches an entry within the Verb array we assign the unknown word a 'VB' POS tag.
	#The overall increase for the first two rules combined was an increase of 0.012%, hardly noticeable (more statistical information below).
	#
	#Example: (Verb)
	#fight (unknown word) == verb_array[pounce, smile, run, fight, play] Yes!
	#fight/VB (add Verb POS tag)
	#
	#Example: (Adjective)
	#Hot (unknown word) == Verb_array[pounce, smile, run, fight, play] No!
	#Hot (unknown word) == Adjective_array[Hot, Cold, wet, dry, sharp] Yes!
	#Hot/JJ (add Adjective POS tag)
	#
	#Third rule: applied cardinal digits increased our Overall Accuracy by
	#0.123% far surpassing the first two rules combined. For the third rule all it does is use regular expressions and searches for either a digit or written out form of a number within the unknown word, if the search is successful
	#we apply a 'CD' POS tag to the unknown word. The reason the third rule had a dramatic increase on overall accuracy is due to the fact that the training corpus can only train SPECIFIC number sequences as cardinal digits,
	#however a test corpus may have differing number sequences that will not directly match the number sequences that the algorithm was trained on. Therefore to counteract this the third rule generalizes and searches for any instance
	#of a number therefore being able to correctly identify any number sequence instead of a specific number sequence, resulting in a 0.123% overall increase.
	#
	#Example:
	#4 == re.search(r"[0-9]|[Oo]ne|[Tt]wo|[Tt]hree|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|[Nn]ine|[Ee]leven|[Tt]welve|[Tt]een", line) is not None: Yes!
	#4/CD (add Cardinal Digit POS tag)
	#
	#Fifteen == re.search(r"[0-9]|[Oo]ne|[Tt]wo|[Tt]hree|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|[Nn]ine|[Ee]leven|[Tt]welve|[Tt]een", line) is not None: Yes!
	#Fifteen/CD (add Cardinal Digit POS tag)
	#
	#smile == re.search(r"[0-9]|[Oo]ne|[Tt]wo|[Tt]hree|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|[Nn]ine|[Ee]leven|[Tt]welve|[Tt]een", line) is not None: No!
	#(As this is the last rule before base case, use base case, add 'NNP' POS tag to unknown word)
	#
	#Fourth Rule: A simple unigram model that keeps track of the previous_tag that was given to the last word, given this tag and the output POS_Tag file that was created (read section on POS_Tag file) we were able to determine
	#that if a previous tag was 'NNP' the most likely tag to follow would also be 'NNP' so therefore apply this tag if the word is unknown and the previous tag was 'NNP'. Increased accuracy by: 0.313% the highest overall accuracy increase
	#given any rule implemented.
	#
	#Example:
	#Gym/NNP (last POS tag, last POS tag was therefore 'NNP'), therefore appy POS tag to next word IF UNKNOWN therefore Tree (unknown word) results in: Tree/NNP.
	#Pounce/VB since the last POS tag was not 'NNP', rule 4 is not used and therefore 'NNP' is not applied unless not other rule is used for the unknown word in which case we do apply 'NNP' as this is the base case.
	#
	#Fifth Rule: Within our basic implementation if we were unable to find the test word within out dictionary we would simply add a 'NN' POS tag to the unknown word. This functionality worked quite well however after analyzing
	#the POS Tag file that was generated (again read section on POS_Tag file), we determined that in fact 'NNP' was more more common then 'NN' so therefore we switched the base case (if no other case of deducing the unknown word
	#POS tag works) to add a 'NNP' POS tag rather then a 'NN' POS tag. Increased accuracy by 0.29%.
	#
	#Example:
	#Waffle (unknown word), last POS tag was NN, Waffle is an unknown word and does not appear in the Adjective or Verb arrays, it's also not a cardinal digit and would not prove true in cardinal search (rule #3), lastly
	#the last POS tag was NOT 'NNP' therefore we cannot add 'NNP' due to rule #4, therefore we go with base case in which we do apply 'NNP' as this is the most common case in the test corpus. Therefore the result would be
	#Waffle/NNP.
	#
	#Overall Accuracy Increase due to 5 rules mentioned resulted in a 0.708% increase in Overall Accuracy, Overall Accuracy Basic being: 92.132% and Inhanced being: 92.84% for Overall Accuracy.
	print("\nRunning script name: " + sys.argv[0]+ "\n")
	try:
		print("Processing files from " + sys.argv[2] + "\n")
		#"Python method listdir() returns a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special 
		#entries '.' and '..' even if they are present in the directory." - Taken from: https://www.tutorialspoint.com/python/os_listdir.htm
		testfile = open(testingfile, "r", encoding = 'utf-8', errors = 'ignore')
	except:
		print("Error reading first argument from command line\nInclude path to files to be processed")
	previous_tag = ""
	for line in testfile:
		line = line.strip()
		if line in thedictionary:
			#add POS from thedictionary to line word
			tag = thedictionary[line]
			line = line + "/" + tag
			previous_tag = tag
		elif previous_tag == 'NNP': #Rule 4: Use this as unigram, in order to determine most likely next POS tag if unknown word occurs, If previous tag was NNP next tag is likely to be NNP, increased by 0.313%, 92.612%, incorrect cases: 4198
			line = line + "/" + "NNP"
			previous_tag = tag
		elif line == JJ_array: # and previous_tag != "DT" (Something along those lines)
			line = line + "/" + "JJ"
			previous_tag = tag #Rule 5: Use this as unigram, in order to determine most likely next POS tag if unknown word occurs
		elif line == Verb_array: #Rule2 + Rule1: Increase of 0.012%, 92.147%
			line = line + "/" + "VB"
			previous_tag = tag 
		elif re.search(r"[0-9]|[Oo]ne|[Tt]wo|[Tt]hree|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|[Nn]ine|[Ee]leven|[Tt]welve|[Tt]een", line) is not None: #Rule 3: Increase of 0.123%, 92.28%, fixed 113 cases
		#Introduction of written Cardinal Numbers results in an Increase of 0.011% increase, 92.299%
			line = line + "/" + "CD"
			previous_tag = tag
		else:
			line = line + "/" + "NNP" #Rule #5 instead of switching everything we can't determine to a noun swith it to a Noun Phrase, increases by 0.29%, 92.89%, incorrect cases: 4040
		print(line)
	#Overall Accuracy 92.84%
	#Overall Accuracy Increase of: 0.708% 

