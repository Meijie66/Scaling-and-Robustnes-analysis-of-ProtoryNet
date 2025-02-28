import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from scipy.spatial.distance import pdist

# First set of sentences
sentences_set1 = [
    "this bird is black with white and has a long, pointy beak",
    "this bird is grey with white and has a long, pointy beak",
    "this bird is black with white on its stomach and has a long, pointy beak",
    "this bird is black with white on its stomach and a short beak",
    "this bird is brown with some white and has a long, pointy beak",
    "this is a black bird with a white belly and a large orange beak",
    "this bird is white with grey and has a long, pointy beak",
    "this bird has wings that are black and white with a short orange beak",
    "this bird has a gray and white belly and a small orange beak",
    "this bird is brown with white and has a long, pointy beak",
    "this bird is white with black and has a long, pointy beak",
    "this bird is brown with black on its wings and has a long, pointy beak",
    "this bird has wings that are black and has a white belly",
    "this bird has wings that are black and has an orange and yellow patch",
    "this bird is all black and has a long, pointy beak",
    "this bird has a black crown as well as a orange bill",
    "this bird has wings that are black and has a long black bill",
    "this bird is grey with black and has a long, pointy beak",
    "this bird is black with white on its feathers and has a long, pointy beak",
    "this bird is white with black and has a very short beak"
]

sentences_set2 = [    
    "this bird has wings that are black and has a thick bill",
    "bird has black body feathers, white breast feather, and short beak",
    "this bird is black with white and has a long, pointy beak",
    "a large grey bird, with a white head and belly, and a large curved bill",
    "this bird has wings that are black and has a white belly",
    "this black bird has white eyes and black plumage on top of a bright orange shortened beak",
    "this bird has a black crown as well as a small black bill",
    "a medium sized bird with black feet and a black breast and belly with a orange and black beak",
    "this bird has a large grey head with a orange pointed bill",
    "this bird is grey and has a very large wing span with a very long beak"
    ]

# Load the Universal Sentence Encoder
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Encode the first set of sentences
vectors_set1 = embed(sentences_set1).numpy()  # Convert to numpy array

# Encode the second set of sentences
vectors_set2 = embed(sentences_set2).numpy()

# Step 1: Compute pairwise distances
pairwise_distances = pdist(vectors_set1, metric='euclidean')

# Step 2: Calculate the mean distance
mean_distance = np.mean(pairwise_distances)


# Step 1: Compute pairwise distances
pairwise_distances_1 = pdist(vectors_set2, metric='euclidean')

# Step 2: Calculate the mean distance
mean_distance_1 = np.mean(pairwise_distances_1)

print(f"Mean distance of vectors in Set 500: {mean_distance}, of set 10: {mean_distance_1}")