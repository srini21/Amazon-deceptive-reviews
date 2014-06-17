import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import NuSVC
import sys
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.pipeline import FeatureUnion
from sklearn import cross_validation
from sklearn import metrics
from sklearn.cross_validation import KFold
import pandas
import pylab as pl
from sklearn.cross_validation import train_test_split
import sklearn
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_curve
from sklearn.multiclass import OneVsRestClassifier
import random
from sklearn.metrics import classification_report
from sklearn.svm import libsvm

def load_corpus(posfile, decfile, numberof):
	#trainfiles =[ f for f in listdir(input_dir) if isfile(join(input_dir,f))]
	trainset = []
	count = 0
	for line in open(posfile,"r"):
		if count < numberof:
			label = +1
        		df = line.strip()
	    		trainset.append({"label":label, "text": df})	
			count += 1
	count = 0
    	for line in open(decfile, "r"):
		if count < numberof:
        		label = -1
        		df = line.strip()
			trainset.append({"label":label, "text": df})
			count +=1

#	print trainset
	random.shuffle(trainset)
	return trainset

	#for f in trainfiles:
#		label = f
#		df = pandas.read_csv(input_dir+"/"+f, dtype={'text':object},error_bad_lines=False,sep="\t", header=None)
#		for row in df['text']:
#			if type(row) is str:
#				trainset.append({"label":label, "text":row})
#	return trainset
def train_model(trainset, testset):
	word_vector = TfidfVectorizer(analyzer="word", ngram_range=(2,2), binary = False, max_features= 2000,min_df=1,decode_error="ignore")
#	print word_vector	
#	print "works fine"
	char_vector = TfidfVectorizer(ngram_range=(2,3), analyzer="char", binary = False, min_df = 1, max_features = 2000,decode_error= "ignore")
	vectorizer =FeatureUnion([ ("chars", char_vector),("words", word_vector) ])
	corpus = []
	classes = []
        testclasses = []
        testcorpus = []
	for item in trainset:
		corpus.append(item['text'])
		classes.append(item['label'])
	
	for item in testset:
		testcorpus.append(item['text'])
		testclasses.append(item['label'])

#	print "Training instances : ", len(classes)
#	print "Testing instances : ", len(set(classes)) 
	
	matrix = vectorizer.fit_transform(corpus)
	testmatrix = vectorizer.fit_transform(testcorpus)
#	print "feature count :. ", len(vectorizer.get_feature_names())
#	print "training model"
	X = matrix.toarray()
	TX = testmatrix.toarray()
	Ty= numpy.asarray(testclasses)
	y = numpy.asarray(classes)
	X_train, X_test, y_train, y_test= train_test_split(X,y,train_size=0.9999,test_size=.00001,random_state=0)
	model = LinearSVC(dual=True, loss='l1')
#	model = SVC()
#	model = NuSVC()
#	model = RandomForestClassifier() 
	#scores=cross_validation.cross_val_score(model,X,y)
	#print "Accuracy "+ str(scores.mean())
#	print y_pred
	y_prob = model.fit(X_train, y_train).predict(TX)
#	y_prob = OneVsRestClassifier(model).fit(X_train, y_train).predict(X_test)
#	print(y_prob)
#	cm = confusion_matrix(y_test, y_pred)
#	cr = classification_report(y_test, y_pred)
#	print cr
#	print(cm)
#	pl.matshow()
#	pl.title('Confusion matrix#')
#	pl.colorbar()
#	pl.ylabel('True label')
#	pl.xlabel('Predicted label')
#	pl.show()
        print accuracy_score(y_prob,Ty)

if __name__=='__main__':
	corpus = load_corpus(sys.argv[1], sys.argv[2], sys.argv[3])	
	testcorpus = load_corpus(sys.argv[4], sys.argv[5], sys.argv[6])
	#print len(corpus), corpus[0:10]
	train_model(corpus, testcorpus)
