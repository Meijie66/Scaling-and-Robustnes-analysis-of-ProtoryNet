import tensorflow_hub as hub
import tensorflow as tf
import pickle
from keras import backend as K
import numpy as np
from sklearn_extra.cluster import KMedoids
from tensorflow import keras
from keras.layers import Concatenate, Dense, Input, LSTM, Embedding, Dropout, Activation, GRU, Flatten
from datetime import datetime
from scipy.spatial import distance_matrix
import sys

import pandas as pd
import re

with open('embedding_train_lama2.pkl', 'rb') as f:
    train_vectors = pickle.load(f)
    print('train_vectors:',len(train_vectors),train_vectors[0])

with open('embedding_test_lama2.pkl', 'rb') as f:
    test_vectors = pickle.load(f)
    print('test_vectors:',len(test_vectors),test_vectors[0])

for p in train_vectors:
    sample_sent_vect.extend(p)

print(sample_sent_vect)
breakpoint()
k_protos, vect_size = 50, 512
kmedoids = KMedoids(n_clusters=k_protos,random_state=0).fit(sample_sent_vect)
k_cents = kmedoids.cluster_centers_
print(k_cents.shape)

#import protoryNet, we recommend you download the protoryNet.py file from Github to have the most updated version

pNet = ProtoryNet() 

model = pNet.createModel(k_cents)

pNet.train(x_train,y_train,x_test,y_test)

#test giving a prediction value to an input

testS = ['the medium sized bird has a dark grey color, a black downward curved beak, and long wings', 'the bird is dark grey brown with a thick curved bill and a flat shaped tail', 'bird has brown body feathers, white breast feathers and black beak', 'this bird has a dark brown overall body color, with a small white patch around the base of the bill', 'the bird has very long and large brown wings, as well as a black body and a long black beak', 'it is a type of albatross with black wings, tail, back and beak, and has a white ring at the base of its beak', 'this bird has brown plumage and a white ring at the base of its long, curved brown beak', 'the entire body is dark brown, as is the bill, with a white band encircling where the bill meets the head', 'this bird is gray in color, with a large curved beak', 'a large gray bird with a long wingspan and a long black beak']

pNet.predict(testS)
#show the list of prototypes
Prototypes = pNet.showPrototypes(sample_sentences,sample_sent_vect)
print('list of prototypes:', Prototypes)

#the number of closest sentences to each prototypes
freq = pNet.protoFreq(sample_sent_vect)
print('the number of closest sentences to each prototypes:',freq)

#list of prototypes
pNet.mappedPrototypes
print('mapped prototypes:',pNet.mappedPrototypes)

