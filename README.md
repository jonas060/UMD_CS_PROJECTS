# Natural-Language-Processing
A few select projects that I worked on within NLP.

## Eliza Project
A simple implemenation using Python, the Eliza project is a rendition of the famous 1966 Chatbot created by Joseph Weizenbaum nicknamed ELIZA. The purpose of
Eliza was to imitate a Rogerian psychologist.

The eliza implementation created is simple. The Eliza Program takes input text from the user and outputs a response based upon certain "key" words the user inputs.
The key word is found through regular expression searches. The entire program Lasts for 20 inputs with a small memory that caches a specific input line to later ask a
question to the user given the specific input cached.

In interesting future project could be implementing the PARRY project. Unlike Eliza who is programmed a psycotherapist, the program PARRY is a schizophrenic patient
that acts increasingly paranoid or less so depending upon input the user provides.

## Movie Review Sentiment Classifier

The Sentiment Classifier program was developed to classify if a given review was positive or negative. The Sentiment Classifer developed in "understanding" of a positive or negative review through a training phase.

 #Training Phase
Within this training phase the program was fed hundreds of reviews, the program would cache certain keywords within each review along with the rating of the review '1' being a postive review '2' being a negative review. The program was then able to statistically determine if a given keywords were likely to be from a positive or negative review. During the training phase the program determined that certain keywords were given different "weights" or determining leverage as some keywords could be used both in a postive or negative context. This wasn't due to any brilliance from the programming but rather simple arithmetic with additonal adjustment of weight values for keywords.

For example:
"I really liked the show but it was dull at some points."
           This is split into: "'I', 'really', 'liked', 'the', 'show', 'but', 'it', 'was', 'dull', 'at', 'some', 'points'"
           We then go through the list and check if each token is equivalent to a keyword within "Sentiment" list if it is
           such as 'like' == 'like' we then add a +1 to the value of "sentimentCount" if the keyword is also used a negative sentiment we add
           -1.011 to the "sentimentCount" for the same keyword resulting in a sentimentCount of -0.011. Going through and adding
           all sentiment values we then check to see if the total sentimentCount is greater then or less then 0. If it is greater
           then 0, we know we have a positive review. If it is less then 0 we know our review is negative. We then add the result
           (result being a postive or negative review) to a variable labeled accordingly that being "positiveReviews", and "negativeReviews."

Notice how the entire sentence is broken up into keywords. Notice also I state the program "cached certain keywords,"  this is important. Some keywords give not sentiment      value at all such has "I", "it", "at", these keywords are referred to as "stopwords" and have minimal bearing on whether a given review is positive or negative. Therefore they are not considered when determining the sentiment of a given review. The program also prints out a decision list with what keywords are postive and which are negative along with the weighted value of how postive or negative the keyword is.
  
Example of decision list:
  
Total word count in dict: 39410
Positive words in dict: 19689
Negative words in dict: 19721
diner: -9.664552144125853e-05
preparing: -4.076630296878964e-05
cv625tok0573txt: 2.537427048972342e-05
1957: 7.355747272265924e-05
fibe: 2.537427048972342e-05
singular: -7.69601623953311e-06
intellectualized: 2.537427048972342e-05
tragically: -1.2826693732555185e-05
  
Where a negative value pertains to negative sentiment and a postive value a postive sentiment.
  
#Testing Phase
    
Next comes the testing phase in which we feed the program entirely new and unused reviews. Now the Sentiment Classifier must determine what the sentiment of a few hundred  reviews are knowing only the keywords that pertain to a certain sentiment given the decision list.
    
#Gold Phase 
This is where we compare the Sentiment Classifiers result on what the sentiment of each review was against the actual sentiment of the review. The result is a confusion matrix of True Postive, True Negative, False Positive, False Negative. With basic arithmetic (TP+TN)/(FP+FN) we are able to see how accurate our Sentiment Classifier is.
    
## POS-Tag Classifier
The POS-Tag Classifier as with the Sentiment Classifier trains on specific data and determines what POS_TAG (Noun, ADJ, Verb, ...) a given word is. The determination is then placed within a decision list (PA5-log.txt) and compared against a key. The determination list is created within "Tag.py" the resulting score and confusion matrix is created within the "Score.py". Score.py uses the decision list to determine the POS-Tag Classifiers overall accuracy. The program received a 92.87% accuracy rating.
    
