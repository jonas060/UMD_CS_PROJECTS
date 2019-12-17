#Authors: Alex Jonas and Joseph Winfield
#A note regarding the format of the program, although it was suppose to be broken up into three separate
#programs passing in text files to the next piece of the program i have condensed it down to one functioning
#program. I have given comments descring each part of the process as well as what part would have been the second
#and third parts of the program.
import string
import operator
import math

data = ""
Sentiment = {}
stopList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#truncate to within 5 decimal places when discovering ratio of keyword frequency given total occurence
#of all keywords, this was removed as it negatively impacted performance.
def truncate(n):
	return int(n*100000)/100000
	
#Method to check for words that don't help in classification of sentiment if found remove from list thereby
#allowing us to create a list with keywords that contain sentiment only.
def checkStopList(word):
    for bannedWord in stopList:
        if word == bannedWord:
            return True
    return False

#After keyword list has been created sift through raw review data line by line looking for review words that
#match word in sentiment list
def checkSentimentList(word):
    for data in Sentiment:
        if word == data:
            return True
    return False
    
#Method to remove punctuation from keyword list, by sifting through raw review text line by line.
def nomorePunctuation(line):
    noPunct = ""
    for token in line:
        if token not in punctuations:
            noPunct+=token
    return noPunct


try:
    data = open("sentiment-train.txt", "r", encoding = 'utf = 8',errors = 'ignore')
except:
    print("Error opening training file")

#Sift through raw data line by line, remove punctuation and lower all character's to lower case, after which we
#split the raw data into a list of "tokens" if review is postive and the token is not a stoplist word, continue,
#placing the non-stoplist word into a set call "Sentiment" which will act as a keyword set. Same idea with negative reviews,
#as indicated by the first "else," meaning if negative review place within a set called Sentiment as well with a negative value
#given value of -1.1101 as there are more positive then negative reviews within "sentiment-training.txt"

for line in data:
    line = nomorePunctuation(line)
    line.lower()
    tokens = line.split()
    if(str(tokens[1]) == str(1)):
        for word in tokens:
            if checkStopList(word) is True:
                continue
            elif word in Sentiment:
                Sentiment[word] += 1
            else:
                Sentiment[word] = 1
    else:
        for word in tokens:
            if checkStopList(word) is True:
                continue
            elif word in Sentiment:
                Sentiment[word] -= 1.1011
            else:
                Sentiment[word] = -1.1011
print("\nDone processing training data\n")

#close raw text data file
data.close()

#Open raw text data "sentiment-test.txt," at this point we would be entering the second program determining
#from our trained data what review would be positive as well as what part would be negative.
try:
    data = open("sentiment-test.txt",'r',encoding = 'utf = 8', errors = 'ignore')
except:
    print("Error opening test file")

#Count sentiment of keyword, how many times is it used in a postive sense? How many times in a negative sense?
negative = 0
positive = 0
for word in Sentiment:
    if (Sentiment[word] > 0):
        positive+=1
    elif (Sentiment[word] < 0):
        negative+=1

#Print out how many keywords in set as well as how often the keyword is used in both a postive and negative sense,
#as well as used in general throughout all review text.
print("Total word count in dict: " + str(len(Sentiment)))
print("Positive words in dict: " + str(positive))
print("Negative words in dict: " + str(negative))


#Add weights to keywords therefore a keyword with a smaller sentiment value does not hold as much value as a word with a
#sentiment rating of a higher sentiment value. Truncating was removed from this.
for word in Sentiment:
    Sentiment[word] = Sentiment[word]/len(Sentiment)

for entry in Sentiment:
	print(entry + ": " + str(Sentiment[entry]))



#Split raw text of "sentiment-test.txt" into a list of tokens, go through one line at at time:
#example: "I really liked the show but it was dull at some points."
#         This is split into: "'I', 'really', 'liked', 'the', 'show', 'but', 'it', 'was', 'dull', 'at', 'some', 'points'"
#         We then go through the list and check if each token is equivalent to a keyword within "Sentiment" list if it is
#         such as 'like' == 'like' we then add a +1 to the value of "sentimentCount" if the keyword is also used an negative sentiment we add
#         -1.011 to the "sentimentCount" for the same keyword resulting in a sentimentCount of -0.011. Going through and adding
#         all sentiment values we then check to see if the total sentimentCount is greater then or less then 0. If it is greater
#         then 0, we know we have a positive review. If it is less then 0 we know our review is negative. We then add the result
#         (result being a postive or negative review) to a variable labeled accordingly that being "positiveReviews", and "negativeReviews."
positiveReviews = 0
negativeReviews = 0
reviewCount = 0
for line in data:
    line = nomorePunctuation(line)
    line.lower()
    tokens = line.split()
    sentimentCount = 0
    reviewCount += 1
    for word in tokens:
        if checkSentimentList(word) is False:
            continue
        else:
            sentimentCount += Sentiment[word]
    if sentimentCount > 0:
        positiveReviews +=1
    else:
        negativeReviews +=1
print("\n\n")
print("Within sentiment-test.txt: ")
print("_______________________________________________________________________________")
print("\nTotal number of postive reviews: " + str(positiveReviews))
print("Total number of negative reviews: " + str(negativeReviews))
print("\n\n")

#third part of program which compares what our program regarded as postive or negative sentiment given a review
#to the actual sentiment of of the review given "sentiment-gold.txt"

#Each line is a single review so as soon as we read in a line add one to the variable "reviewCount" we also set
#sentimentCount to 0 refreshing sentimentCount each time a new line (or review is read in). We read in the value of sentiment
#from "sentiment-gold.txt" by the variable 'tokens[1]' and place this sentiment value within the variable name sentimentValue.
#Next Sentiment[word] checks to see what value we placed for the review against the correct review sentiment value given by
#sentiment-gold.txt" and places it within a variable that either states it was a true postive meaning if our program gave the review a 
#1 and the gold gave it a 1 it was correct as a true postive, same idea with true negative (Program: 0 == Gold: 0), we then add up the 
#true postive and true negative and see how correct our program was given 200 reviews. We also figure out how many false positives (Program: 1 != Gold: 0)
#as well a false negative (Program: 0 != Gold: 1), we then add these up and divide by total number of reviews to determine the percentage
#of incorrect indentifications how program made. This is the confusion matrix.
print("Within sentiment-gold.txt: ")
try:
    data = open("sentiment-gold.txt",'r', encoding = 'UTF = 8', errors = 'ignore')
except:
    print("gold failed to open")
truePositives = 0
trueNegatives = 0
falsePositives = 0
falseNegatives = 0
correctReviews = 0
incorrectReviews = 0
reviewCount = 0
totalReviews = 0
for line in data:
    totalReviews +=1
    line = nomorePunctuation(line)
    line.lower()
    tokens = line.split()
    sentimentValue = tokens[1]
    sentimentCount = 0
    reviewCount += 1
    for word in tokens:
        if checkSentimentList(word) is False:
            continue
        else:
            sentimentCount += Sentiment[word]
	#Confusion Matrix
    if(float(sentimentCount) > 0.0 and float(sentimentValue) > 0.0):
        truePositives += 1
    elif(float(sentimentCount) < 0.0 and float(sentimentValue) == 0.0):
        trueNegatives += 1
    elif(float(sentimentCount) < 0.0 and float(sentimentValue) > 0.0):
        falsePositives += 1
    elif (float(sentimentCount) > 0.0 and float(sentimentValue) == 0.0):
        falseNegatives += 1

#Total Correct and Total Incorrect Reviews
correctReviews = truePositives + trueNegatives
incorrectReviews = falsePositives = falseNegatives

#Output of Confusion Matrix Along With Percentage Correct and Incorrect
print("________________________________________________________________________________")
print("\n")
print("| True Postives: " + str(truePositives) + "               " + "False Postives: " + str(falsePositives) + " |")
print("+------------------------------------------------------------------------------+")
print("| True Negatives: " + str(trueNegatives) + "              " + "False Negatives: " + str(falseNegatives) + " |")
print("________________________________________________________________________________")
print("\n\n")
print("Total Correct Reviews: " + str(correctReviews))
print("Total Incorrect Reviews: " + str(incorrectReviews))
print("Percent correct: " + str((correctReviews/totalReviews)*100))
print("Percent Incorrect: " + str((incorrectReviews/totalReviews)*100))
