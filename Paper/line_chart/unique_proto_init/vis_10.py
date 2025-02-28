import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# List of sentences
sentences = [
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

# Encode the sentences
sentence_embeddings = embed(sentences)

# Reduce dimensionality using PCA for visualization
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(sentence_embeddings)

# Plot the embeddings with sentence numbers as labels
plt.figure(figsize=(10, 10))
for i, (x, y) in enumerate(reduced_embeddings):
    plt.scatter(x, y, s=200, label=f'Sentence {i+1}')  # Label as Sentence 1, 2, 3, etc.
    plt.text(x, y, f'{i+1}', fontsize=20, ha='right')  # Add text label for each point

plt.xlim(-0.4, 0.6)  # Set x-axis range from -0.4 to 0.6
plt.ylim(-0.4, 0.6)  # Set y-axis range from -0.4 to 0.6
plt.xticks([])  # Hide x-axis ticks and labels
plt.yticks([])  # Hide y-axis ticks and labels
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig("vis_10.pdf", dpi=300, bbox_inches='tight')
plt.grid(True)
plt.show()