import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import tensorflow
import tflearn
import numpy
import json
import random

#open the json and store it in a var
#tokenize the 
#tokenize and stem the patterns
#sort the patterns and remove duplicates
#append patterns and tags to a combined list

with open("training_data.json") as file:
    data = json.load(file)

patterns = []
tags = []
patterns_pattern = []
patterns_tags = []

for d in data["training_data"]:
    tag = data["tag"]
    tags.append(tag)
    for p in data["patterns"]:
        words = nltk.word_tokenize(p)
        patterns.extends(words)
        patterns_pattern.append(words)
        patterns_tags.append(tags)

tags = sorted(tags)

ignore_case = ['?','!','$','@','#','&']
patterns = sorted(list(set([stemmer.stem(w) for w in patterns if w not in ignore_case])))

training = []
output = []

op_empty = [0 for _ in range(len(tags))]

for num, doc in enumerate(patterns_pattern):
    bag = []
    bag_of_wrds = [stemmer.stem(w) for w in doc]

    for w in bag_of_wrds:
        if w in bag_of_wrds:
            bag.append(1)
        else:
            bag.append(0)
    
    op_row = op_empty[:]
    op_row[tags.index(patterns_tags[num])] = 1

    training.append(bag)
    output.append(op_row)

training = numpy.array(training)
output = numpy.array(output)