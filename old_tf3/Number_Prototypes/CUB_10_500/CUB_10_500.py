
#import neccesary packages
import tensorflow_hub as hub
import tensorflow as tf
import pickle
import numpy as np
from sklearn_extra.cluster import KMedoids
from tensorflow import keras
from tensorflow.keras.layers import Concatenate, Dense, Input, LSTM, Embedding, Dropout, Activation, GRU, Flatten
from datetime import datetime
from scipy.spatial import distance_matrix
import sys
from protorynet_10_500 import ProtoryNet
import pandas as pd
import re

# Check if GPU is available
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# 加载数据集
dir = "/home/limei/ProtoryNet/CUB_data/"
with open (dir + 'train_data.csv', 'rb') as fp:
    train = pd.read_csv(fp, nrows=300)
    train_shuffled = train.sample(frac=1, random_state=16).reset_index(drop=True)
    #print('shuffle:',train_shuffled)
with open (dir + 'test_data.csv', 'rb') as fp:
    test = pd.read_csv(fp, nrows=243)
    test_shuffled = test.sample(frac=1, random_state=16).reset_index(drop=True)
    print('test shuffle:',len(test_shuffled))



train_not_clean = train_shuffled ['description'].tolist()
y_train = train_shuffled ['label'].tolist()
test_not_clean = test_shuffled ['description'].tolist()
y_test= test_shuffled ['label'].tolist()


def gen_sents(para):
    res = []
    for p in para:
        sents = re.split(r'\.\n|\n',p)
        sents = [s.strip() for s in sents if s.strip()]
        res.append(sents)
    return res


x_train = gen_sents(train_not_clean)
x_test = gen_sents(test_not_clean)

print(x_train[:5])
print(y_train[:5])
print(x_test[:5])
print(y_test[:5])

#import Google Sentence encoder, to convert sentences into vector values
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)
print("module %s loaded" % module_url)

def embed(input):
    return model(input)

#sampling training data (sentences)
sample_sentences = []
#choose with data to sample
for p in x_train:
    sample_sentences.extend(p)

print("sample_sentences:",sample_sentences[0])

#compute vector values of sentences
sample_sent_vect = embed(sample_sentences)
print(sample_sent_vect)

k_protos, vect_size = 500, 512
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

