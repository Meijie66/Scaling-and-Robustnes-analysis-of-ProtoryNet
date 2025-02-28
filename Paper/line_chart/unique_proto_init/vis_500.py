import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# List of sentences
sentences = [
    " this bird is black with white and has a long, pointy beak",
    " this bird is grey with white and has a long, pointy beak" ,
    " this bird is black with white on its stomach and has a long, pointy beak",
    " this bird is black with white on its stomach and a short beak" ,
    " this bird is brown with some white and has a long, pointy beak" ,
    " this is a black bird with a white belly and a large orange beak" ,
    " this bird is white with grey and has a long, pointy beak ",
    " this bird has wings that are black and white with a short orange beak" ,
    " this bird has a gray and white belly and a small orange beak" ,
    " this bird is brown with white and has a long, pointy beak" ,
    " this bird is white with black and has a long, pointy beak",
    " this bird is brown with black on its wings and has a long, pointy beak",
    " this bird has wings that are black and has a white belly",
    " this bird has wings that are black and has an orange and yellow patch",
    " this bird is all black and has a long, pointy beak",
    " this bird has a black crown as well as a orange bill",
    " this bird has wings that are black and has a long black bill",
    " this bird is grey with black and has a long, pointy beak",
    " this bird is black with white on its feathers and has a long, pointy beak",
    " this bird is white with black and has a very short beak"
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
plt.savefig("vis_500.pdf", dpi=300, bbox_inches='tight')
plt.grid(True)
plt.show()
