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
from sklearn.multiclass import OneVsRestClassifier

def load_corpus(input_dir):
	from os import listdir
	from os.path import isfile, join
	trainfiles =[ f for f in listdir(input_dir) if isfile(join(input_dir,f))]
	trainset = []
	for f in trainfiles:
		label = f
		df = [line.strip() for line in open(input_dir+"/"+f)]
		for d in df:
			trainset.append({"label":label, "text": d})
	
	return trainset

	#for f in trainfiles:
#		label = f
#		df = pandas.read_csv(input_dir+"/"+f, dtype={'text':object},error_bad_lines=False,sep="\t", header=None)
#		for row in df['text']:
#			if type(row) is str:
#				trainset.append({"label":label, "text":row})
#	return trainset
def train_model(trainset):
	word_vector = TfidfVectorizer(analyzer="word", ngram_range=(2,2), binary = False, max_features= 2000,min_df=1,decode_error="ignore")
#	print word_vector	
	print "works fine"
	char_vector = TfidfVectorizer(ngram_range=(2,3), analyzer="char", binary = False, min_df = 1, max_features = 2000,decode_error= "ignore")
	vectorizer =FeatureUnion([ ("chars", char_vector),("words", word_vector) ])
	corpus = []
	classes = []

	for item in trainset:
		corpus.append(item['text'])
		classes.append(item['label'])

	print "Training instances : ", 0.8*len(classes)
	print "Testing instances : ", 0.2*len(classes) 
	
	matrix = vectorizer.fit_transform(corpus)
	print "feature count : ", len(vectorizer.get_feature_names())
	print "training model"
	X = matrix.toarray()
	y = numpy.asarray(classes)
	model =LinearSVC()
	X_train, X_test, y_train, y_test= train_test_split(X,y,train_size=0.8,test_size=.2,random_state=0)
	y_pred = OneVsRestClassifier(model).fit(X_train, y_train).predict(X_test)
	#y_prob = OneVsRestClassifier(model).fit(X_train, y_train).decision_function(X_test)
	#print y_prob
#	output=open(sys.argv[1],"w")
#	output.write(str(y_pred)+"\n")
#	output.write('y_test:'+str(y_test)+"\n")
	#con_matrix = []
	#for row in range(len(y_prob)):
	#	temp = [y_pred[row]]	
	#	for prob in y_prob[row]:
	#		temp.append(prob)
	#	con_matrix.append(temp)
	#for row in con_matrix:
	#	output.write(str(row)+"\n")
	test=[i for i, j in enumerate(y_pred) if j=='anonEdited'] 
	for i in test:
		print y_test[i]
	cm = confusion_matrix(y_test, y_pred)
	print(cm)
	pl.matshow(cm)
	pl.title('Confusion matrix')
	pl.colorbar()
	pl.ylabel('True label')
	pl.xlabel('Predicted label')
	pl.show()
	print accuracy_score(y_pred,y_test)

if __name__=='__main__':
	print "started"
	corpus = load_corpus("./1000authors800")
	
	#print len(corpus), corpus[0:10]
	train_model(corpus)
