from collections import Counter

# Input data (your text)
text = """
this is a black bird with a long black tail feather and a large beak
this bird has a short orange bill, a black head, and a black and white mottled body
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this is a plump dark gray bird with a thick beak that is yellow
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a thick bill
this bird is black with white on its feathers and has a long, pointy beak
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this is a black bird with a long black tail feather and a large beak
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this is a black bird with a long black tail feather and a large beak
this bird is grey and has a very large wing span with a very long beak
this bird is black with a white belly, has webbed feet and a red beak
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this bird is grey and has a very large wing span with a very long beak
this bird is black with white and has a long, pointy beak
this bird has smooth brown feathers and a large, long black bill
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
