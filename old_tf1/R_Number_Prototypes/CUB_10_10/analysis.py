from collections import Counter

# Input data (your text)
text = """
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird has a wide wing span covered in brown, grey and white feathers with a broad, blunt beak
this bird is grey with white and has a long, pointy beak
a long black bird with a stubby black beak and a medium sized neck
this bird has wings that are black and has an orange and yellow patch
this bird has wings that are black and has a thick bill
this bird has a black overall body color aside from a white line around it's bill
the bird has a white eyering and long secondaries that are dark grey
the bird has a black eyering, short throat and a small bill
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
