import math
class wordMatrix:
    dictionaryHeader = {}

    def __init__(self):
        dictionaryHeader = {}
        return

    #Sifts through wordMatrix (giant crate) looking within each file (red box) for particular word, if the word we are searching for (word that has been inputted) occurs within the file we append frequency of the word to an
    #array named TFList if the term does not appear within the file we append a 0 count to the file within the array TFList. After we have searched through all the files we return the array 'TFList' which is a vector of the occurence
    #of the target word within all files. This will be used to compute the TF-IDF value.
    def applyTF(self,word,files):
        count = 0.0
        TFList = []
        for dictionary in files:
            subDictionary = self.dictionaryHeader[dictionary]
            if word in subDictionary:
                TFList.append(subDictionary[word])
            else:
                TFList.append(0.0)
        return TFList
        
        #Sift through dictionaries (subDictionary also are red boxes, 2,000 in total) if the word we are searching for appears within a dictionary, add one to the occurence of times the word occurs throughout all
        #dictionaries (placed within term DF). After we have sifted through the entire wordMatrix (giant crate) checking every dictionary to see if the word occurs within each dicitonary (red box) we compute the IDF
        #by diving the wordMatrix length (wordMatrix being fileList, which is worth a value of 2,000 due to there being 2,000 files) by the DF (number of files with the target word occuring within), this will be placed within
        #a temporary variable IDF. We then take the log of the IDF value with base 10, giving us our final answer for the IDF value.
    def findIDF(self,word,fileList):
        DF = 0.0
        for dictionary in fileList:
            subDictionary = self.dictionaryHeader[dictionary]
            if word in subDictionary:
                DF += 1.0
        IDF = (len(fileList)/DF)
        return math.log(IDF,10)

    #Add a dictionary (file) to the larger wordMatrix (giant crate), think of it has placing a red box (dictionary or file) within a large crate (giant crate).
    def addNewDictionary(self, newKey):
        self.dictionaryHeader[newKey] = {}
        return
    
    #Add a numerical value for the occurence of a specfic word within a file
    def addOccurance(self,dictionary,word):
        subDictionary = self.dictionaryHeader[dictionary]
        if word in subDictionary:
            subDictionary[word] += 1.0
        else:
            subDictionary[word] = 1.0
        return
    
    #Remove items from wordMatrix that only occur one time.
    def removeKey(self, popList, dictionary):
        for item in popList:
            if item in self.dictionaryHeader[dictionary]:
                self.dictionaryHeader[dictionary].pop(item)
        return
        
    #Multipy TF vector by IDF value given to specific word inputted, resulting an a vector of TF-IDF values, which is then returned to similar.py.
    #Example:
    #word1TF = [[ 0.02 (TF) * 1.68 (IDF) = TF-IDF Value for Dictionary 1 (or file or red box) ]
    #          [ 0.0 (TF) * 1.68 (IDF) = TF-IDF Value for Dictionary 2   ]
    #          [ 0.1 (TF) * 1.68 (IDF) = TF-IDF Value for Dictionary 3   ]
    #          [ 0.04 (TF) * 1.68 (IDF) = TF-IDF Value for Dictionary 4  ]
    #          [ ...       * ...        = ...                            ]
    #          [ 0.03 (TF) * 1.68 (IDF = TF-IDF Value for Dictionary 2000]]
    def TFIDF(self,list,IDF):
        for element in range(len(list)):
            list[element] = (list[element]*IDF)
        return list
