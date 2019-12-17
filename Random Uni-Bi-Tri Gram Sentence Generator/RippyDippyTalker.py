#Welcome to the RippyDiddyTalker! The program is designed to take an input of what size n-gram
#you would like from 1-3, how many random sentences you would like generated, as many as you want!
#Lastly the program looks for an input of a text document to train the program, it can be as many
#different text documents as you would like, the more documents though the more tokens that will be
#generated within the training data, and therefore a longer runtime. That being said the more text
#also means the more potential sentences generated.

import sys
import re
import random
wordbank_array = []
tokenCount = 0

#sys.argv[1] specifies the n-gram model you had selected within the command line, while sys.argv[2]
#specifies the number of random sentences you want generated from the given n-gram model.
number_sentences = int(sys.argv[2])
n_gram = int(sys.argv[1])

#If you specify fewer then 4 arguments then the program is unable to run.
#examples being RippyDiddyTalker.py 10 something.txt, the program will see to few arguments
#are given and exit. If the program were to continue the program would assume the 10 is the
#n-value and would exit immediately anyway as there is no 10-gram model created within the
#RippyDiddyTalker.py

if len(sys.argv) < 4:
	print("Not enough arguments.")
	exit()

print("Arguments that were entered: " + str(sys.argv))
print("This is the name of the script: " + sys.argv[0])
print("This is the n-gram model you have selected: " + sys.argv[1])
print("This is the number of randomly selected sentences you want: " + sys.argv[2])
print("This is the name of the files that were selected: ")
#For loop iterates through system arguments given by user and prints out all arguments that have
#".txt" within them, as all files given use .txt format, the goal is simply to output what the user
#inputted for text documents.
x = 4
for x in sys.argv:
	if re.search(r".txt", x):
		print("File: ", x)
		with open(x) as my_file:
			for line in my_file:
				line = line.lower()
				line = re.sub(r'([!.~\),\(_*]+)', r' \1 ', line, 0)
				line = re.sub(r'([\",~_*\(\)])', r'', line, 0)
				content = line.split()
				wordbank_array += content
				for tokens in content:
					tokenCount += 1
					

sentence_counter = 0
sentence_string = ' '
sentence = ' '


#Unigram Model
#Simply checks to make sure that the number of sentences generated so far is less then the sentences
#that have been created, sentence_counter which counts the number of sentences already generated always
#begins at 0. Secondly we check to see that the n-gram number inputted on the command line matches the 
#n-gram model were using in this case n-gram value of 1.
while((sentence_counter < number_sentences) and n_gram == 1):
	sentence = random.choice(wordbank_array)
	sentence_string = str(sentence_counter) + ": "
	while re.search(r'[.!?]', sentence) is None:
		sentence_string += " " + sentence
		sentence = random.choice(wordbank_array)
	sentence_string += sentence
	print(sentence_string)
	sentence_counter += 1



#Bigram Model
if((sentence_counter < number_sentences) and n_gram == 2):
	#initialize empty second array for wordbank_array to copy data into
	wordbank_twos_array = []
	wordbank_array_Bigram = wordbank_array[:-1] #subtract one entry from end of wordbank_array
	wordbank_twos_array = wordbank_array[1:] #subtract one entry from beginning of wordbank_array
	
	while(sentence_counter < number_sentences):
		#creates new array called 'tuples_array' that zips (combines two entries from different arrays
		#into a single entry) the wordbank_array_Bigram and wordbank_twos_array together as both arrays
		#have been shifted by deleting the first entry of wordbank_twos_array and the last entry of 
		#wordbank_array_Bigram this allows us match the previous word say "the cat", the cat being previous
		#with the next word such as (cat, sat) combining the two entries results in "the cat sat", however if
		#the previous word cannot match the next word, we throw a random word from the original text array into
		#the sentence as the next entry and try to find a next word given the new previous random word. This results
		#in the sentence making less sense but that's the drawback of a bigram.
		
		#There are instances when more then one word matches the previous word such as: (the, cat), cat being the previous
		#word and (cat, had) or (cat, attacked) or (cat, sat), as any of the next words could potentially be our next word
		#within the generation of a sentence we place all the possibilites into an array called 'match_list' we then call
		#random on the match_list and whatever word is chosen becomes our next word within the sentence we continue in this pattern
		#unless there are no matches within the match_list, at this point we simply call random upon the training array and
		#place a random word within the sentence and begin searching for matches based on this random word.
		tuples_array = list(zip(wordbank_array_Bigram, wordbank_twos_array)) #zipped array cast as list otherwise can't print entries
		sentence = random.choice(wordbank_array_Bigram)
		sentence_string = str(sentence_counter) + ": "
		while re.search(r'[.!?]', sentence) is None:
			sentence_string += " " + sentence
			match_list = []
			for bigram in tuples_array:
				if bigram[0] == sentence:
					match_list.append(bigram[1])
			if len(match_list) == 0:
				sentence = random.choice(wordbank_array)
			else:
				sentence = random.choice(match_list)
		sentence_string += sentence
		print(sentence_string)
		sentence_counter += 1
	
#Trigram Model
#Same idea takes place here as with the Bigram model however in this case there are two other words we need
#to shift within separate arrays in order to create a an entry with 3 words that would appear together within a
#a sentence from the .txt files that were inputted.
if((sentence_counter < number_sentences) and n_gram == 3):
	#We create three separate arrays from the original wordbank_array, prev_word_array deletes two entries from
	#the last entries of wordbank_array while current_word_array deletes one entry from the beginning and one entry
	#from the ending of the wordbank_array while next_word_array deletes two entries from the beginning of wordbank_array
	#this again allows us to shift our entries to match the next occuring entry an another array which we again sandwich
	#together using the zip() method. We again typecast the zipped array as a list as otherwise we cannot print entries from
	#the zipped list.
	prev_word_array = wordbank_array[:-2]
	current_word_array = wordbank_array[1:-1]
	next_word_array = wordbank_array[2:]
	triples_array = list(zip(prev_word_array, current_word_array, next_word_array)) #Here we zip all three arrays that have been shifted into a single array called "triples_array"
	sentence_counter = 0 #Sentence count
	while(sentence_counter < number_sentences): #While generated sentences are less then total number of sentences to generate, generate another sentence within while loop.
		random_index = random.randint(0, len(triples_array) - 1) #begin our sentence with a random entry within our newly created triple word entry array
		prev_word = triples_array[random_index][0] 
		while re.search(r'[!.\?]', prev_word): #Search for punctuation within previous three word entry array if punctuation call random on index of prev_word in order to find new index position without punctuation
											   #prev_word being first word in three zipped word entry
			random_index = random.randint(0, len(triples_array) - 1)
			prev_word = triples_array[random_index][0]
		sentence = triples_array[random_index][1]
		sentence_string = str(sentence_counter) + ": " + prev_word #add prev_word entry to our sentence_string
		while re.search(r'[.!?]', sentence) is None:
			sentence_string += " " + sentence #add a space to sentence
			match_list = []
			for trigram in triples_array:
				if trigram[0] == prev_word and trigram[1] == sentence: #if our trigram is in proper order append third entry of trigram
					match_list.append(trigram[2])
			if len(match_list) == 0: #If no possible matches
				rand_index = random.randint(0, len(triples_array) - 1) #Find new random index point as no match was found to append new entry to existing entry of words
				prev_word = triples_array[random_index][0] #Call random on triple zipped word array entry and get entry for sentence
				while re.search(r'[.!?]', prev_word):
					rand_index = random.randint(0, len(triples_array) - 1)
					prev_word = triples_array[rand_index][0]
				sentence = triples_array[rand_index][1]
				sentence_string += " " + prev_word		
			else:
				prev_word = sentence
				sentence = random.choice(match_list)
		sentence_string += sentence
		sentence = ' '
		print(sentence_string)
		sentence_counter += 1
	


	

