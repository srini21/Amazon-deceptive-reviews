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
    
    def calculate(self, review):
        r = re.compile(r'[{}]'.format(punctuation))
        modifiedSentence = r.sub(' ', review)
        self.featureValue = len(modifiedSentence.split())

class NumberOfWordsPerSentence(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 2
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, review):
        r = re.compile(r'''[.!?]['"]?\s{1,2}(?=[A-Z])''')
        sentences = r.sub('\t', review).split("\t")
        sum = 0
        for sentence in sentences:
            sum += len(sentence.split())
        self.featureValue = sum *1.0/len(sentences)

class LengthOfReview(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 3
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, reviewdatum):
        self.featureValue = len(review)

class NumberOfNumericals(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 4
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, review):
        numbers = ''.join(c for c in review if c.isdigit())
        self.featureValue = len(numbers)

class NumberOfCapitals(Feature):
    
    def __init__(self,reviewdatum): 
        self.featureNumber = 5
        self.featureValue = None 
        self.calculate(reviewdatum)

    def calculate(self, review):
        numbers = ''.join(c for c in review if c.upper())
        self.featureValue = len(numbers)

class NumberOfAllCapitals(Feature):
    
    def __init__(self, reviewdatum):
        self.featureNumber = 6
        self.featureValue = None
        self.calculate(reviewdatum)

    def calculate(self, review):
        r = re.compile(r'[{}]'.format(punctuation))
        sentences = r.sub(' ', review)
        sentences = sentences.split()
        capitalWords = [word for word in sentences if word.isupper()]
        self.featureValue = len(capitalWords)

class NumberOfJJ(Feature):
    
    def __init__(self, tagged):
        self.featureNumber = 7
        self.featureValue = None
        self.calculate(tagged)

    def calculate(self, tagged):
        count = 0
        print tagged
        for tag in tagged:
            if tag[1] == "JJ":
                count+=1
        self.featureValue = count
        
class NumberOfNN(Feature):
    
    def __init__(self, tagged):
        self.featureNumber = 8
        self.featureValue = None
        self.calculate(tagged)

    def calculate(self, tagged):
        count = 0
        print tagged
        for tag in tagged:
            if tag[1] == "NN":
                count+=1
        self.featureValue = count

class NumberOfNNP(Feature):
    
    def __init__(self, tagged):
        self.featureNumber = 9
        self.featureValue = None
        self.calculate(tagged)

    def calculate(self, tagged):
        count = 0
        print tagged
        for tag in tagged:
            if tag[1] == "NNP":
                count+=1
        self.featureValue = count

class NumberOfIN(Feature):
    
    def __init__(self, tagged):
        self.featureNumber = 10
        self.featureValue = None
        self.calculate(tagged)

    def calculate(self, tagged):
        count = 0
        print tagged
        for tag in tagged:
            if tag[1] == "IN":
                count+=1
        self.featureValue = count

class NumberOfDT(Feature):
    
    def __init__(self, tagged):
        self.featureNumber = 11
        self.featureValue = None
        self.calculate(tagged)

    def calculate(self, tagged):
        count = 0
        print tagged
        for tag in tagged:
            if tag[1] == "DT":
                count+=1
        self.featureValue = count

class NumberOfDT(Feature):
    
    def __init__(self, tagged):
        self.featureNumber = 11
        self.featureValue = None
        self.calculate(tagged)

    def calculate(self, tagged):
        count = 0
        print tagged
        for tag in tagged:
            if tag[1] == "DT":
                count+=1
        self.featureValue = count

sent = "My stay was quick but awesome. After a long day, seeing a substantial line at check-in was a bit of a groaner, but then i saw the self-serve kiosks. i was checked in with keys in hand in under 3 minutes. in the morning i was able to check out on the TV in my room. the hotel is a beautiful historic landmark with all the amenities of a modern hotel and all the charm of its 1927 origins. The bed was FABULOUSLY comfortable. i wish i could live there. they have many rooms wtih 2 bathrooms. i stayed in a room like that once with a friend and we didn't know ahead of time that we had two bathrooms. talk about squeals of delight. that was about 7 years ago in virginia beach. i was by myself at the hilton and had no need for a room with two bathrooms, but it's the first time i've seen this since. what a great feature! "
tagged = nltk.pos_tag(nltk.word_tokenize(sent))
print NumberOfJJ(tagged).getValue()
#f = open(sys.argv[1], "r")
#feature_file = open(sys.argv[2],"w")
#reviewdata = [line.strip() for line in f]
#for reviewdatum in reviewdata:
#    feature_file.write("+1\t")
#    feature_file.write(NumberOfWords(reviewdatum).getFeature()+":"+NumberOfWords(reviewdatum).getValue()+"\t")
#    feature_file.write(NumberOfWordsPerSentence(reviewdatum).getFeature()+":"+NumberOfWords(reviewdatum).getValue()+"\t")
#    feature_file.write(NumberOfWordsPerSentence(reviewdatum).getFeature()+":"+NumberOfWords(reviewdatum).getValue()+"\t")
#    feature_file.write(LengthOfReview(reviewdatum).getFeature()+":"+LengthOfReview(reviewdatum).getValue()+"\t")
#    feature_file.write(NumberOfNumericals(reviewdatum).getFeature()+":"+NumberOfNumericals(reviewdatum).getValue()+"\t")
#    feature_file.write(NumberOfCapitals(reviewdatum).getFeature()+":"+NumberOfCapitals(reviewdatum).getValue()+"\t")
#    feature_file.write(NumberOfAllCapitals(reviewdatum).getFeature()+":"+NumberOfAllCapitals(reviewdatum).getValue()+"\t")
#    tagged = nltk.pos_tag(nltk.word_tokenize(reviewdatum))
#    feature_file.write(NumberOfJJ(tagged).getFeature()+":"+NumberOfJJ(tagged).getValue()+"\t")
#    
#    feature_file.write("\n")
#    print reviewdatum 
