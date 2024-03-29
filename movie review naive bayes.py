from nltk.corpus import movie_reviews

# Total reviews
print (len(movie_reviews.fileids())) # Output: 2000

# Review categories
print (movie_reviews.categories()) # Output: [u'neg', u'pos']

# Total positive reviews
print (len(movie_reviews.fileids('pos'))) # Output: 1000

# Total negative reviews
print (len(movie_reviews.fileids('neg'))) # Output: 1000

positive_review_file = movie_reviews.fileids('pos')[0]
print (positive_review_file) #Output: pos/cv000_29590.txt

documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        #documents.append((list(movie_reviews.words(fileid)), category))
        documents.append((movie_reviews.words(fileid), category))

print (len(documents)) # Output: 2000

# x = [str(item) for item in documents[0][0]]
# print (x)

# print first tuple
print (documents[0])
'''
Output:

(['plot', ':', 'two', 'teen', 'couples', 'go', ...], 'neg')
'''

# shuffle the document list
from random import shuffle
shuffle(documents)

all_words = [word.lower() for word in movie_reviews.words()]

# print first 10 words
print (all_words[:10])
'''
Output:

['plot', ':', 'two', 'teen', 'couples', 'go', 'to', 'a', 'church', 'party']
'''

from nltk import FreqDist

all_words_frequency = FreqDist(all_words)

print (all_words_frequency)
'''
Output:

<FreqDist with 39768 samples and 1583820 outcomes>
'''

# print 10 most frequently occurring words
print (all_words_frequency.most_common(10))
'''
Output:

[(',', 77717), ('the', 76529), ('.', 65876), ('a', 38106), ('and', 35576), ('of', 34123), ('to', 31937), ("'", 30585), ('is', 25195), ('in', 21822)]
'''

from nltk.corpus import stopwords

stopwords_english = stopwords.words('english')
print (stopwords_english)
'''
Output:

['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
'''

# create a new list of words by removing stopwords from all_words
all_words_without_stopwords = [word for word in all_words if word not in stopwords_english]

# print the first 10 words
print (all_words_without_stopwords[:10])
'''
Output:

['plot', ':', 'two', 'teen', 'couples', 'go', 'church', 'party', ',', 'drink']
'''

'''
# Above code is written using the List Comprehension feature of Python
# It's the same thing as writing the following, the output is the same

all_words_without_stopwords = []
for word in all_words:
    if word not in stopwords_english:
        all_words_without_stopwords.append(word)

print (all_words_without_stopwords[:10])
'''

import string

print (string.punctuation)
'''
Output:

!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''

# create a new list of words by removing punctuation from all_words
all_words_without_punctuation = [word for word in all_words if word not in string.punctuation]

# print the first 10 words
print (all_words_without_punctuation[:10])
'''
Output:

[u'plot', u'two', u'teen', u'couples', u'go', u'to', u'a', u'church', u'party', u'drink']
'''

# because we clean stopwords and punctuations from the word list

all_words_clean = []
for word in all_words:
    if word not in stopwords_english and word not in string.punctuation:
        all_words_clean.append(word)

print (all_words_clean[:10])
'''
Output:

['plot', 'two', 'teen', 'couples', 'go', 'church', 'party', 'drink', 'drive', 'get']
'''

all_words_frequency = FreqDist(all_words_clean)

print (all_words_frequency)
'''
Output:

<FreqDist with 39586 samples and 710578 outcomes>
'''

# print 10 most frequently occurring words
print (all_words_frequency.most_common(10))
'''
Output:

[('film', 9517), ('one', 5852), ('movie', 5771), ('like', 3690), ('even', 2565), ('time', 2411), ('good', 2411), ('story', 2169), ('would', 2109), ('much', 2049)]
'''

print (len(all_words_frequency)) # Output: 39586

# get 2000 frequently occuring words
most_common_words = all_words_frequency.most_common(2000)
print (most_common_words[:10])
'''
Output:

[('film', 9517), ('one', 5852), ('movie', 5771), ('like', 3690), ('even', 2565), ('time', 2411), ('good', 2411), ('story', 2169), ('would', 2109), ('much', 2049)]
'''

print (most_common_words[1990:])
'''
Output:

[('genuinely', 64), ('path', 64), ('eve', 64), ('aware', 64), ('bank', 64), ('bound', 64), ('eric', 64), ('regular', 64), ('las', 64), ('niro', 64)]
'''

# the most common words list's elements are in the form of tuple
# get only the first element of each tuple of the word list
word_features = [item[0] for item in most_common_words]
print (word_features[:10])
'''
Output:

['film', 'one', 'movie', 'like', 'even', 'time', 'good', 'story', 'would', 'much']
'''

def document_features(document):
    # "set" function will remove repeated/duplicate tokens in the given list
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# get the first negative movie review file
movie_review_file = movie_reviews.fileids('neg')[0]
print (movie_review_file)
'''
Output:

neg/cv000_29416.txt
'''

#print (document_features(movie_reviews.words(movie_review_file)))
'''
Output:

{'contains(waste)': False, 'contains(lot)': False, 'contains(rent)': False, 'contains(black)': False, 'contains(rated)': False, 'contains(potential)': False, .............................................................................
.............................................. 'contains(smile)': False, 'contains(cross)': False, 'contains(barry)': False}
'''

# print first tuple of the documents list
print (documents[0])
'''
Output:

(['plot', ':', 'two', 'teen', 'couples', 'go', ...], 'neg')
'''

feature_set = [(document_features(doc), category) for (doc, category) in documents]
print (feature_set[0])
'''
Output:

({'contains(waste)': False, 'contains(lot)': False, 'contains(rent)': False, 'contains(black)': False, 'contains(rated)': False, 'contains(potential)': False, ...........................................................................
............................................................. 'contains(good)': False, 'contains(live)': False, 'contains(synopsis)': False, 'contains(appropriate)': False, 'contains(towards)': False, 'contains(smile)': False, 'contains(cross)': False, 'contains(barry)': False}, 'neg')
'''

'''
# In the above code, we have used list-comprehension feature of python
# The same code can be written as below:
feature_set = []
for (doc, category) in documents:
    feature_set.append((document_features(doc), category))
print (feature_set[0])
'''

print (len(feature_set)) # Output: 2000

test_set = feature_set[:400]
train_set = feature_set[400:]

print (len(train_set)) # Output: 1600
print (len(test_set)) # Output: 400

from nltk import NaiveBayesClassifier

classifier = NaiveBayesClassifier.train(train_set)

from nltk import classify

accuracy = classify.accuracy(classifier, test_set)
print (accuracy) # Output: 0.77

from nltk.tokenize import word_tokenize
 
custom_review = "I hated the film. It was a disaster. Poor direction, bad acting."
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = document_features(custom_review_tokens)
print (classifier.classify(custom_review_set)) # Output: neg
# Negative review correctly classified as negative
 
# probability result
prob_result = classifier.prob_classify(custom_review_set)
print (prob_result) # Output: <ProbDist with 2 samples>
print (prob_result.max()) # Output: neg
print (prob_result.prob("neg")) # Output: 0.999989264571
print (prob_result.prob("pos")) # Output: 1.07354285262e-05
 
custom_review = "It was a wonderful and amazing movie. I loved it. Best direction, good acting."
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = document_features(custom_review_tokens)
 
print (classifier.classify(custom_review_set)) # Output: neg
# Positive review is classified as negative
# We need to improve our feature set for more accurate prediction
 
# probability result
prob_result = classifier.prob_classify(custom_review_set)
print (prob_result) # Output: <ProbDist with 2 samples>
print (prob_result.max()) # Output: neg
print (prob_result.prob("neg")) # Output: 0.999791868552
print (prob_result.prob("pos")) # Output: 0.000208131447797
