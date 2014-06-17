import os, sys
import subprocess
import re
from string import punctuation
import nltk
import json
from pprint import pprint
import  math
from collections import Counter
import urllib

class Feature:
    
    def __init__(self, reviewdatum):
        featureNumber = None
        featureValue = None
   
    def calculate(self):
        self.featureValue = None

    def getFeature(self):
        return str(self.featureNumber)

    def getValue(self):
        return str(self.featureValue)

    def getFeatureValue(self):
        return (self.featureNumber, self.featureValue)

class NumberOfWords(Feature):
    
    def __init__(self, reviewdatum):
        self.featureNumber = 1
        self.featureValue = None 
        self.calculate(reviewdatum)
    
    def calculate(self, reviewdatum):
        review = reviewdatum[11]
        r = re.compile(r'[{}]'.format(punctuation))
        modifiedSentence = r.sub(' ', review)
        self.featureValue = len(modifiedSentence.split())

class NumberOfWordsPerSentence(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 2
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        review = reviewdatum[11]
        r = re.compile(r'''[.!?]['"]?\s{1,2}(?=[A-Z])''')
        sentences = r.sub('\t', review).split("\t")
        sum = 0
        for sentence in sentences:
            sum += len(sentence.split())
        self.featureValue = sum *1.0/len(sentences)

class NumberOfHelpfulFeedbacks(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 3
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        self.featureValue = reviewdatum[8]

class NumberOfFeedbacks(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 4
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        self.featureValue = reviewdatum[9]

class PercentageOfHelpfulFeedbacks(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 5
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        if reviewdatum[9] is '0':
            self.featureValue = 0
        else:
            self.featureValue = int(reviewdatum[8])*1.0/int(reviewdatum[9])

class LengthOfTitle(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 6
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        self.featureValue = len(reviewdatum[10])

class LengthOfReview(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 7
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        self.featureValue = len(reviewdatum[11])

class NegativeSentiment(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 8
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        try:
            params={}
            params['text']=str(reviewdatum[11])
            urlencoder = urllib.urlencode(params)
            f=urllib.urlopen("http://text-processing.com/api/sentiment/", urlencoder)
            analysis = f.read()
            analysis = analysis[analysis.find('neg'):]
            neg = analysis[analysis.find(": ")+2:analysis.find(",")]
            self.featureValue = float(neg)
        except:
            self.calculate(reviewdatum)

class PositiveSentiment(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 9
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        try:
            params={}
            params['text']=str(reviewdatum[11])
            urlencoder = urllib.urlencode(params)
            f=urllib.urlopen("http://text-processing.com/api/sentiment/", urlencoder)
            analysis = f.read()
            analysis = analysis[analysis.find('pos'):]
            pos = analysis[analysis.find(": ")+2:analysis.find("}")]
            self.featureValue = float(pos)
        except:
            self.calculate(reviewdatum)

class CosineSimilarity(Feature):
        
    def __init__(self,reviewdatum):
        self.featureNumber = 10
        self.featureValue  = None
        self.calculate(reviewdatum)
            

    def getCosine(self, vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator
    
    def text_to_vector(self, text):
        WORD = re.compile(r'\w+')
        words = WORD.findall(text)
        return Counter(words)
    
    def calculate(self, reviewdatum):
        text1 = reviewdatum[11]
        text2 = "TRIAL:"#TODO
        vector1 = self.text_to_vector(text1)
        vector2 = self.text_to_vector(text2)
        self.featureValue = self.getCosine(vector1, vector2)

class NumberOfNumericals(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 11
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        numbers = ''.join(c for c in reviewdatum[11] if c.isdigit())
        self.featureValue = len(numbers)


class NumberOfCapitals(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 12
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        numbers = ''.join(c for c in reviewdatum[11] if c.upper())
        self.featureValue = len(numbers)

class NumberOfAllCapitals(Feature):
    
    def __init__(self, reviewdatum):
        self.featureNumber = 13
        self.featureValue = None
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        review = reviewdatum[11]
        r = re.compile(r'[{}]'.format(punctuation))
        sentences = r.sub(' ', review)
        sentences = sentences.split()
        capitalWords = [word for word in sentences if word.isupper()]
        self.featureValue = len(capitalWords)

class Rating(Feature):
    
    def __init__(self, reviewdatum):
        self.featureNumber = 14
        self.featureValue = None
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        self.featureValue = reviewdatum[7]

f = open(sys.argv[1], "r")
feature_file = open(sys.argv[2],"w")



feature_array=["NumberOfWords","NumberOfWordsPerSentence","NumberOfHelpfulFeedbacks","NumberOfFeedbacks","PercentageOfHelpfulFeedbacks","LengthOfTitle","LengthOfReview","NegativeSentiment","PositiveSentiment","CosineSimilarity","NumberOfNumericals","NumberOfCapitals","NumberOfAllCapitals","Rating"]
reviewdata = [line.strip().split("\t") for line in f]
print len(reviewdata[0][11])
for reviewdatum in reviewdata:
    try:
        if reviewdatum[11] is None:
            continue
    except:
        continue
    feature_file.write("+1\t")
    feature_file.write(NumberOfWordsPerSentence(reviewdatum).getFeature()+":"+NumberOfWords(reviewdatum).getValue()+"\t")
    feature_file.write(NumberOfHelpfulFeedbacks(reviewdatum).getFeature()+":"+NumberOfHelpfulFeedbacks(reviewdatum).getValue()+"\t")
    feature_file.write(NumberOfFeedbacks(reviewdatum).getFeature()+":"+NumberOfFeedbacks(reviewdatum).getValue()+"\t")
    feature_file.write(PercentageOfHelpfulFeedbacks(reviewdatum).getFeature()+":"+PercentageOfHelpfulFeedbacks(reviewdatum).getValue()+"\t")
    feature_file.write(LengthOfTitle(reviewdatum).getFeature()+":"+LengthOfTitle(reviewdatum).getValue()+"\t")
    feature_file.write(LengthOfReview(reviewdatum).getFeature()+":"+LengthOfReview(reviewdatum).getValue()+"\t")
    #feature_file.write(NegativeSentiment(reviewdatum).getFeature()+":"+NegativeSentiment(reviewdatum).getValue()+"\t")
    #feature_file.write(PositiveSentiment(reviewdatum).getFeature()+":"+PositiveSentiment(reviewdatum).getValue()+"\t")
    feature_file.write(CosineSimilarity(reviewdatum).getFeature()+":"+CosineSimilarity(reviewdatum).getValue()+"\t")
    feature_file.write(NumberOfNumericals(reviewdatum).getFeature()+":"+NumberOfNumericals(reviewdatum).getValue()+"\t")
    feature_file.write(NumberOfCapitals(reviewdatum).getFeature()+":"+NumberOfCapitals(reviewdatum).getValue()+"\t")
    feature_file.write(NumberOfAllCapitals(reviewdatum).getFeature()+":"+NumberOfAllCapitals(reviewdatum).getValue()+"\t")
    #feature_file.write(Rating(reviewdatum).getFeature()+":"+Rating(reviewdatum).getValue()+"\t")
    feature_file.write("\n")
    print reviewdatum 
