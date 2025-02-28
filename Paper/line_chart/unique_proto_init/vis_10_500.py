import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# First set of sentences (to be plotted in one color)
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

# Second set of sentences (to be plotted in another color)
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

# Encode both sets of sentences
embeddings_set1 = embed(sentences_set1)
embeddings_set2 = embed(sentences_set2)

# Combine embeddings for PCA
all_embeddings = tf.concat([embeddings_set1, embeddings_set2], axis=0)

# Reduce dimensionality using PCA for visualization
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(all_embeddings)

# Split the reduced embeddings back into the two sets
reduced_set1 = reduced_embeddings[:len(sentences_set1)]
reduced_set2 = reduced_embeddings[len(sentences_set1):]

# Plot the embeddings
plt.figure(figsize=(10, 8))

# Plot the first set of sentences in one color (e.g., blue)
for i, (x, y) in enumerate(reduced_set1):
    plt.scatter(x, y, color='blue',  marker='o',label='Set 1' if i == 0 else "")
    plt.text(x, y, f'{i+1}', fontsize=12, ha='right', color='blue')

# Plot the second set of sentences in another color (e.g., red)
for i, (x, y) in enumerate(reduced_set2):
    plt.scatter(x, y, color='orange',  marker='*',label='Set 2' if i == 0 else "")
    plt.text(x, y, f'{i+1}', fontsize=12, ha='right', color='red')

plt.title('Visualization of unique prototypes')
plt.xticks([])  # Hide x-axis ticks and labels
plt.yticks([])  # Hide y-axis ticks and labels
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig("vis_10_500.pdf", dpi=300, bbox_inches='tight')
plt.grid(True)
plt.show()