from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest
from sklearn import svm
import logging
import numpy, random
from pprint import pprint
import sys

positivefile = open(sys.argv[1], "r")
unverifiedfile = open(sys.argv[2], "r")
poscorpus = [line for line in positivefile]
positivecorpus = random.sample(poscorpus, 500)
test1 = random.sample(poscorpus, 50)
unvcorpus = [line for line in unverifiedfile]
unverifiedcorpus = random.sample(unvcorpus, 500)
test2 = random.sample(unvcorpus, 50)
corpus = []
target = []
for i in range(1000):
    a = random.randint(1,50)
    if a <= 10 and len(positivecorpus) > 0:
        random.shuffle(positivecorpus)
        corpus.append(positivecorpus.pop())
        target.append(1)
    elif len(unverifiedcorpus) > 0:
        random.shuffle(unverifiedcorpus)
        corpus.append(unverifiedcorpus.pop())
        target.append(-1)
    else:
        random.shuffle(positivecorpus)
        corpus.append(positivecorpus.pop())
        target.append(1)
target = numpy.array(target)

pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('sbest', SelectKBest(k=1)),
    ('clf', SGDClassifier()),
])
parameters = {
    'vect__max_df': (0.5, 0.75, 1.0),
    'vect__max_features': (None, 5000, 10000, 50000),
    'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
    'tfidf__use_idf': (True, False),
    'tfidf__norm': ('l1', 'l2'),
    'clf__alpha': (0.00001, 0.000001),
    'clf__penalty': ('l2', 'elasticnet'),
}
vect = CountVectorizer()
x = vect.fit_transform(corpus)
print x.toarray()
#print vect.get_feature_names()
grid_search = GridSearchCV(pipeline, parameters, n_jobs=1, verbose=1)
#csv = svm.SVC()
#csv.fit(corpus, target)
#print csv.predict(test1)
grid_search.fit(corpus, target)
best_parameters = grid_search.best_estimator_.get_params()
print grid_search.predict(test1)
print grid_search.predict(test2)
#print corpus[11:14]
#print target[11:14]
