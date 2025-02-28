from collections import Counter

# Input data (your text)
text = """
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a long wingspan, a white belly, and a yellow bill
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a very short beak
this bird has wings that are black and has a white bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a white bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with white and has a very short beak
this bird has really big wings and has a white belly
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has really big wings and has a white belly
this bird has really big wings and has a white belly
this bird is black with white and has a very short beak
this bird has wings that are grey and has a white belly
this bird has wings that are black and has a white belly and red bill
this bird is black with white and has a very short beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with black and has a very short beak
this bird is black with white and has a very short beak
this bird is black with white and has a long, pointy beak
this bird has really big wings and has a white belly
this bird is black with big wings and has a long, pointy beak
this bird is white with black and has a very short beak
this bird has wings that are black and has a white belly
this bird is black with big wings and has a long, pointy beak
this bird is white with black and has a very short beak
this bird is black with white and has a very short beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and has a white belly and red bill
this bird has really big wings and has a white belly
this bird has a long wingspan, a white belly, and a yellow bill
this bird has a long wingspan, a white belly, and a yellow bill
this bird is black with white and has a very short beak
this bird has wings that are black and has a white belly
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this black and gray bird has a very short orange beak
this bird has wings that are black and white with a short orange beak
this bird has really big wings and has a white belly
this bird is white with black and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a white belly
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a white belly and red bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and has a white belly and red bill
this bird is white with black and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are grey and has a white belly
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its stomach and a short beak
this bird has a long wingspan, a white belly, and a yellow bill
this bird is white with black and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a long wingspan, a white belly, and a yellow bill
this bird has really big wings and has a white belly
this bird has really big wings and has a white belly
this bird has wings that are grey and has a white belly
this bird is white with black and has a long, pointy beak
this bird is black with white and has a very short beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has really big wings and has a white belly
this bird has really big wings and has a white belly
this bird has wings that are black and has a white belly
this bird has wings that are black and white with a short orange beak
this bird is white with black and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly
this bird is white with black and has a very short beak
this bird is white with black and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a white belly and red bill
this bird is black with white and has a very short beak
this bird has wings that are black and has a white belly and red bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and has a white bill
this bird is white with black and has a very short beak
this bird is black with white and has a very short beak
this bird is black with white and has a very short beak
this bird has a long wingspan, a white belly, and a yellow bill
this bird is white with black and has a very short beak
this bird is white with black and has a very short beak
this bird has wings that are black and has a white belly
this bird is white with black and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its stomach and a short beak
this bird is black with white and has a very short beak
this bird is white with black and has a very short beak
this bird has really big wings and has a white belly
this bird has a long wingspan, a white belly, and a yellow bill
this bird has wings that are black and has a white belly and red bill
this bird is grey with white and has a long, pointy beak
this bird has wings that are black and has a white belly
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a white belly and red bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a white bill
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its stomach and a short beak
this bird has wings that are black and white and has a long bill
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has really big wings and has a white belly
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
