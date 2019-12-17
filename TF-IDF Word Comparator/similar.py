import os
import sys
import re
import math
#Author: Alex Jonas
#Hello! And Welcome to similar.py! Two files were used to create this project that being similar.py, and wordMatrix.py. The goal of this project was to compare two random words inputted by the user, to see how
#similar the two words were, given a corpus of 2,000 files of random movie reviews. Sentiment evaluation was not used, simply TF-IDF calculations. The random words are inputted by the user, once prompted to,
#the IDF of each word is then displayed as well as the resulting similarity of the given words. The command to start is:
#separate file created that creates empty set in which we can read file files into each file having its own dictionary, therefore the empty set becomes our matrix which holds our dictionaries,
#each dictionary pertaining to a different file.
#example:
#wordMatrix is equal to empty set {}
#read in file 1, file 1 is now added to its own dictionary -> {file1}, this dictionary containing file1 is now added to wordMatrix empty set{} -> resulting in: wordMatrix -> {{file1}}
#we can then read in another file (file2) and a third file (file3), now our wordMatrix looks like this: wordMatrix -> {{file1}, {file2}, {file3}}, we will keep doing this until all 2,000 files are contained
#within wordMatrix.
import wordMatrix


fileList = []
#array that temporarily holds all files from sys.argv[1] or the 'path' which we have designated to argument 2 which leads to the directory full of the 2,000 files which are to be read in.
everyWord = {}
#Sift through each word within each dictionary within wordMatrix to get count of each words occurence as well as total amount of words within each dictionary.
currentFile = ""
#Current file be read in to matrix
matrix = wordMatrix.wordMatrix()
#This will be our wordMatrix as discussed above.


print("\nRunning script name: " + sys.argv[0]+ "\n")
try:
    print("Processing files from " + sys.argv[1] + "\n")
    #"Python method listdir() returns a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special 
    #entries '.' and '..' even if they are present in the directory." - Taken from: https://www.tutorialspoint.com/python/os_listdir.htm
    fileList = os.listdir(sys.argv[1])
except:
    print("Error reading first argument from command line\nInclude path to files to be processed")

    #This is where we have each new file placed within a dictionary and then added as a "newKey" (method addNewDictionary applies our new file dictionary to the larger wordMatrix, look within wordMatrix.py for more details)
    #after the dictionaryHeader of the wordMatrix (dictionaryHeader is used as a sort of placeholder, to keep to keep track of how many dictionary "newKey's" have been created and where each is, therefore we don't run the risk 
    #of going out-of-range.
    #In simpler terms what is happening is a file is taken and placed inside a red box, this red box can be thought of as a dictionary a sort of organizational container to keep the file contained within in which we write information about the
    #word count and instances of each word on the outside of the red box, which will be used later to determine the TF-IDF of a specific word were looking for, this red box is placed inside a giant crate called 'wordMatrix' which acts as a container
    #for all the red boxes, and in turn the file in which each red box holds.
for file in fileList:
    print("processing file: " + str(file))
    matrix.addNewDictionary(file)
    strFile = "Pang-Lee-PA4/"+file
    try:
        currentFile = open(strFile, "r")
    except:
        print("Error opening file " + fileCount)
    for line in currentFile:
    #Simply cleaning up words within each file re.sub(r'\W+', ' ', line) replaces any non-word character with empty space, we then lower all words within file and split into separate items with wordArray = line.split(" "), which means split at each
    #occurence of empty space, these items are placed an a temporary array called 'wordArray', we then sift through the items counting how often each specific word occurs in the file (such as: the occurs 12 times), explain addOccurance more thorougly!
        line = re.sub(r'\W+', ' ',line)
        line.lower()
        wordArray = line.split(" ")
        for word in wordArray:
            if word == '':
                continue
            if word in everyWord:
                everyWord[word] += 1.0
            else:
                everyWord[word] = 1.0
            matrix.addOccurance(file,word)
            
#Count every word in each file and place within variable everyWordCount, again this can be thought of as opening the large crate (wordMatrix) sifting through each red box (dictionary) within the crate and placing the total
#amount of contents within all redboxes on the outside of the crate.
#Here we also sift through each file looking for cases of a word occuring only once if so, place word within separate array called popList (still within large crate, wordMatrix), we then pass this to the popList within the
#large crate (wordMatrix), once pased to method removeKey (within wordMatrix.py) if word within wordMatrix is within popList remove from wordMatrix.
popList = []
everyWordCount = 0.0
for key in everyWord:
    if everyWord[key] == 1.0:
        popList.append(key)
    everyWordCount += everyWord[key]
for col in fileList:
    matrix.removeKey(popList, col)

#Let's try this again. The user inputs two words in which they would like to see compared to each other computed through TF-IDF (Explain how this is done and your done). If the user would like to exit the program the
#user must type 'exit' for both the first and second word within the prompt. If the program has decided the user does not want to exit the program (either by successful typing of two words or perhaps an unsuccessful typing
#of 'exit' twice) the progarm continues and does not break the while loop. At this point we create two variables 'word1IDF' and 'word2IDF' which will contain the computed IDF values of word1 as well as word2. We then set the 'word1IDF'
#as well as 'word2IDF' to the variable findIDF which searches through the wordMatrix (giant crate, however it is referred to as 'tempMatrix' however it is a copy of wordMatrix or for as shown within the code simply 'matrix'), sifting 
#through each dictionary (red box) for the specific word (more details on this method can be found within wordMatrix.py). After we have computed the IDF values for word1 and word2 we print them out for debugging purposes as well as for
#the user to see.

#How to compute IDF:
#IDF = Log_e(total number of documents/total number of documents with term t in it

#What's the importane of IDF?
#measures how important a term is. While computing TF, all terms are considered equally important. However it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. 
#Thus we need to weigh down the frequent terms while scale up the rare ones. However not to rare as if a word occurs only once we remove it from wordMatrix.

#How to compute TF:
#TF = Number of time t appears in a document/total number of terms in a document

#What's the importance of TF?
#measures how frequently a term occurs in a document. Since every document is different in length, it is possible that a term would appear much more times in long documents than shorter ones. Thus, the term frequency is often divided 
#by the document length (aka. the total number of terms in the document) as a way of normalization:

#Example:
#Consider a document containing 100 words wherein the word cat appears 3 times. The term frequency (i.e., tf) for cat is then (3 / 100) = 0.03. Now, assume we have 10 million documents and the word cat appears in one thousand of these. 
#Then, the inverse document frequency (i.e., idf) is calculated as log(10,000,000 / 1,000) = 4. Thus, the Tf-idf weight is the product of these quantities: 0.03 * 4 = 0.12. - Taken From: tfidf.com

#Side Note: There are a few drawbacks to this program however the first being that if a user types exit but does not type exit for the second word the program will compute TF-IDF for 'exit' along with the second word typed
#and compute the similarity between the two words. Also if a user accidently hits enter within one of the word input options the program will crash as all whitespaces have been removed within the 2,000 dictionary list of items
#(words). If you misspell a word the program will most likely exit (crash) as a misspelled word is unlikely to be within the 2,000 different dictionaries. For example: If I type in 'chrismas' as word one but I meant 'christmas'
#it is unlikely the word 'chrismas' appears within any of the 2,000 separate dictionaries, however if on the off chance it does with more then one occurence, congradulations! the program will continue run, as it is an item within
#a dictionary (red box) or dictionaries (red boxes) within the wordMatrix (large crate). Lastly there is a chance the word you typed does not appear in the 2,000 separate dictionaries, this is more common then one may think, if this
#is the case the program will crash as zero occurence of a word would result in division by zero within the IDF calculation, and as python does not want to get theoritical with calculation it will simply exit (crash).
while(True):

    print("Enter your two word pair")
    tempMatrix = matrix
    word1 = ""
    word2 = ""
    print("Enter word 1:")
    word1 = input("")
    print("Enter word 2:")
    word2 = input("")
    if(word1 == "exit" and word2 == "exit"):
        break
    word1IDF = 0.0
    word2IDF = 0.0
    word1IDF = tempMatrix.findIDF(word1,fileList)
    word2IDF = tempMatrix.findIDF(word2,fileList)
    print("word 1 Inverse Document Frequency: " + str(word1IDF))
    print("word 2 Inverse Document Frequency: " + str(word2IDF))

    
    #Call applyTF on word1TF (an empty array), applyTF will return a vector with frequency of occurence for word1 within each file (more detail in wordMatrix.py, as this will be used to compute TF-IDF.
    word1TF = []
    word1TF = tempMatrix.applyTF(word1,fileList)
    #Call TFIDF and pass in word1TF vector values along with word1IDF value, word1IDF value is multplied by each word1TF value within the vector, returning a vector of TF-IDF values for word1 (more detail in
    #wordMatrix.py).
    word1TFIDF = tempMatrix.TFIDF(word1TF,word1IDF)

    tempMatrix = matrix
    
    #Call TFIDF and pass in word2TF vector values along with word2IDF value.
    word2TF = []
    word2TF = tempMatrix.applyTF(word2,fileList)
    word2TFIDF = tempMatrix.TFIDF(word2TF,word2IDF)
    
    #Now we compute the dot-product! Take vector word1TFIDF and cycle through each numerical value multiply by the same numerical value position by the vector for word2TFIDF and add to a variable called 'dotProduct'
    #that was set at 0 inititally.
    #Example:
    #word1TFIDF = [ 1, 3, 5, 7 ]
    #word2TFIDF = [ 0, 2, 4, 6 ]
    #start with element 0 in each word1TFIDF
    # 1 * 0 = 0, now add this value to our dotProduct sum, so 0 + 0 = 0.
    #Now sift through the rest of both word1TFIDF and word2TFIDF following the same process
    # 3 * 2 = 6, 6 + dotProduct (0) = 6
    # 5 * 4 = 20, 20 + dotProduct (6) = 26
    # 7 * 6 = 42, 42 + dotProduct (26) = 68
    #Hoila! 68 is our dotProduct for vectors word1TFIDF and word2TFIDF.
    dotProduct = 0.0
    for element in range(len(word1TF)):
        dotProduct += (word1TFIDF[element] * word2TFIDF[element])
    word1Length = 0.0
    word2length = 0.0
    #for each numerical value in word1TFIDF square the numerical value and add to variable 'word1Length.'
    #Example:
    #word1TFIDF = [ 1, 3, 5, 7]
    #1*1 = 1, now add to word1Length, 1 + word1Length (0) = 1
    #3*3 = 9, 9 + word1Length (1) = 10
    #5*5 = 25, 25 + word1Length (10) = 35
    #7*7 = 49, 49 + word1Length (35) = 85
    #Now we have our word1Length! Repeat the same process for word2Length
    for word1ele in word1TFIDF:
        word1Length += word1ele*word1ele
    word1Length = math.sqrt(word1Length)
    for word2ele in word2TFIDF:
        word2length += word2ele*word2ele
    #We then square root the sum of squares for word2.
    word2length = math.sqrt(word2length)
    #Then apply our dotProduct value over our word1Length multiplied by our square-rooted sum of squares for word2Length resulting in our consine value, which is our value of how similar the two words are to one another.
    cosine = dotProduct/(word2length * word1Length)
    print(str(cosine))
print("\n\n")
print("Well Done!")
