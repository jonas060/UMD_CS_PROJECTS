#Author: Alex Jonas
#Welcome to Scorer.py! Where we test your decision list created in Tag.py and see how well the algorithm did indicated by: Number of correct and Incorrect POS tags, Overall Accuracy in Percentage, as well as
#Confusion Matrixes created for Correct, Incorrect, and Should have been POS tags with counts for each.
import os
import sys
import re
from collections import Counter
#trainedcorpus = {}
keycorpus = {}
success = 0
notsuccess = 0
trainedcorpusfile = sys.argv[1]
keycorpusfile = sys.argv[2]
POS_array = []
POS_array_wrong = []
POS_array_Correct = []
print("\nRunning script name: " + sys.argv[0]+ "\n")

#Zip files lines so we may read both line in simulatenously, in both cases strip the extra "\n" that occurs when reading in line1 (we read in line1 as that is our POS tag value we have given the test word
#doesnt matter when line1 is equivalent to line2 (learnedcorpus being line1 and keycorpus being line2) however it is of importance when the POS tag is incorrect, for when we construct our confusion matrix.
#After line has been cleaned of "\n" with rstrip split word from POS tag assign POS tag string variable POS_Tag and append POS tag to POS array (POS_array for correct POS tags, POS_array_wrong for wrong POS Tags,
#POS_tags_corrected for what they should have been). We then use the 'Counter' method to count the occurance of all 46 POS tags within the within the POS tag arrays, as well as counting up all successful taggings as
#well as unsuccessful taggings. the 'Counter' method helps produce our confusion matrix (example shown) below while the 'success' and 'notsuccess' variables are used to distinguish our total accuracy, adding both success
#and not success together to get a total which we refer to as 'overall' then simply divide success by overall and multiply by 100 to get a overall correct percentage value.
#
with open(trainedcorpusfile) as trainedcorpus, open(keycorpusfile) as keycorpus:
	for line1, line2 in zip(trainedcorpus, keycorpus):
		#Correct POS Tags
		if line1 == line2:
			line1 = line1.rstrip("\n")
			lineContent = line1.rsplit("/", 1)
			word = lineContent[0]
			POS_Tag = lineContent[1]
			POS_array.append(POS_Tag)
			d_count = Counter(POS_array).most_common(46)
			#print("Success!")
			#print(line1 + line2)
			success = success + 1
		else:
			#Erroneous POS tags
			line1 = line1.rstrip("\n")
			lineContent = line1.rsplit("/", 1)
			word = lineContent[0]
			POS_Tag = lineContent[1]
			POS_array_wrong.append(POS_Tag)
			d_wrong_count = Counter(POS_array_wrong).most_common(46)
			
			#Array of what POS tags should have been
			line2 = line2.rstrip("\n")
			lineContentCorrect = line2.rsplit("/", 1)
			POS_Tag_Correct = lineContentCorrect[1]
			POS_array_Correct.append(POS_Tag_Correct)
			d_Corrected_Count = Counter(POS_array_Correct).most_common(46)
			#print("Not Similar!")
			#print(line1 + line2)
			notsuccess = notsuccess + 1

print("number of correct: " + str(success))
print("number incorrect: " + str(notsuccess))
print("\n")
overall = 0
overall = success + notsuccess
percentage = 0.0
percentage = (success/overall) * 100

print("Overall Percentage: " + str(percentage))
print("\n")
print("Confusion Matrix:")
print("________________________________")
print("Correct POS Tags: " + str(d_count))
print("\n")
print("Incorrect POS Tags: " + str(d_wrong_count))
print("\n")
print("Incorrect POS tags should have been: " + str(d_Corrected_Count))
#
#Confusion Matrix Output Looks like:
#
#Number of Correct: x
#Number of Incorrect: y
#
#Overall Percentage: z
#
#Confusion Matrix:
#____________________________
#
#Correct POS Tags: {('NN', 7010), ('IN', 5830), ('NNP', 5664), ('DT', 4747), ('NNS', 3314), ... }
#
#Incorrect POS Tags: ...
#
#Incorrect POS tags should have been: ...
#
#And Hoila! Project Finished!
#