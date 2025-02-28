
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
from protorynet_10_10 import ProtoryNet
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Check if GPU is available
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# 加载数据集
dir = "/home/limei/ProtoryNet/CUB_data/"
with open (dir + 'train_data.csv', 'rb') as fp:
    train = pd.read_csv(fp, nrows=300)
    train_shuffled = train.sample(frac=1, random_state=28).reset_index(drop=True)
    #print('shuffle:',train_shuffled)
with open (dir + 'test_data.csv', 'rb') as fp:
    test = pd.read_csv(fp, nrows=243)
    test_shuffled = test.sample(frac=1, random_state=28).reset_index(drop=True)
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

k_protos, vect_size = 10, 512

kmedoids = KMedoids(n_clusters=k_protos,random_state=28, init='random').fit(sample_sent_vect)

# Get cluster labels and medoids
labels = kmedoids.labels_
k_cents = kmedoids.cluster_centers_


medoids = np.array(kmedoids.medoid_indices_)  # Ensure it's a NumPy array

# Reduce the 512-dimensional embeddings to 2D using PCA
pca = PCA(n_components=2, random_state=28)
sample_sent_vect_2d = pca.fit_transform(sample_sent_vect.numpy())


# Create a scatter plot for visualization
plt.figure(figsize=(16,14))
unique_labels = np.unique(labels)
print("labels:",unique_labels)

# You might want to choose a colormap that supports a larger number of clusters.
colors = plt.cm.get_cmap('turbo', len(unique_labels))

for k in unique_labels:
    # Get the 2D points for cluster k
    cluster_points = sample_sent_vect_2d[labels == k]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1],
                s=50, color=colors(k), label=f'Cluster {k}', alpha=0.8, zorder=1)
    
    # Get the medoid for this cluster
    # Convert the medoid index to an integer if it's not already one.
    medoid_index = int(medoids[k])
    medoid_point = sample_sent_vect_2d[medoid_index]
    plt.scatter(medoid_point[0], medoid_point[1],
                marker='*', s=3000, color=colors(k), edgecolor='black', linewidth=2, zorder=2)

#plt.title("K-Medoids Clusters Visualization")
#plt.xlabel("Principal Component 1")
#plt.ylabel("Principal Component 2")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',prop={'size': 10})
plt.tight_layout()
plt.xticks([])  # Hide x-axis ticks and labels
plt.yticks([])  # Hide y-axis ticks and labels
plt.savefig("random_10proto.pdf", dpi=600, bbox_inches='tight')
plt.show()



