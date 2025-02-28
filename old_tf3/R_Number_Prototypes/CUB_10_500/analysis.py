from collections import Counter

# Input data (your text)
text = """
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and has a orange and yellow spot
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is black with white on its stomach and a short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black with an orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is black in color with a black beak, and black eye rings
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird is all black and has a long, pointy beak
this bird has wings that are black with an orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is black in color, and has a bright orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and has a orange and yellow spot
this bird is black and orange in color, with a black beak
this bird is black and orange in color, with a black beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and has a orange bill
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has a curved orange beak and a black body
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and has a short bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is black in color, and has a bright orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and has a white belly
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird is black with white on its stomach and a short beak
this bird is black and orange in color, with a black beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and has a orange bill
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a orange and yellow spot
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is all black and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black with an orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black in color with a black beak, and black eye rings
this bird is black with white on its stomach and a short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, and has a orange beak
this bird is white and black in color, and has a orange beak
this bird is black and orange in color, with a black beak
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
