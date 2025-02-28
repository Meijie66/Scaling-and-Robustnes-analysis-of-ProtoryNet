from collections import Counter

# Input data (your text)
text = """
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
a small all black bird, there is one orange and red wing bar, the bird has a short black bill
this bird has wings that are black with a short black beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird is black with grey and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this is a black bird with long wings and a black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is brown with black feet and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this is a black bird with long wings and a black beak
this bird has wings that are black with a short black beak
this is a brown bird with a large pointed black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black with a short black beak
this is a black bird with an orange wing and a small beak
this bird has wings that are black with a short black beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this is a black bird with long wings and a black beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is gray and black in color, with a large black beak
"""

# Step 1: Split the text into individual sentences
sentences = text.strip().split('\n')

# Step 2: Count the occurrences of each sentence
sentence_counts = Counter(sentences)

# Step 3: Display unique sentences and their counts
print("Unique Sentences and Their Occurrences:")
for sentence, count in sentence_counts.items():
    print(f"'{sentence}': {count} times")

# Step 4: Calculate duplicate counts
total_sentences = len(sentences)
unique_sentences = len(sentence_counts)
duplicates = total_sentences - unique_sentences

print("\nSummary:")
print(f"Total Sentences: {total_sentences}")
print(f"Unique Sentences: {unique_sentences}")
print(f"Duplicated Sentences: {duplicates}")