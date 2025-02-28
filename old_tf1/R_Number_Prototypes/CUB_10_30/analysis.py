from collections import Counter

# Input data (your text)
text = """
this is a black bird with a long black tail feather and a large beak
this bird is black with grey and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is grey and has a very large wing span with a very long beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are grey and has a long orange bill
this bird has wings that are black and has a thick bill
this bird is grey and has a very large wing span with a very long beak
this bird is black and gray in color, and has a bright orange beak
this is a black bird with a long black tail feather and a large beak
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this bird is black with grey and has a long, pointy beak
this bird is grey and has a very large wing span with a very long beak
this bird is black with a white chest and has a very short beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this bird is black with grey and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is grey and has a very large wing span with a very long beak
this bird is black with grey and has a long, pointy beak
this bird is grey with white and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is grey with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red and has a very short beak
this bird is black with grey and has a long, pointy beak
this bird is grey and has a very large wing span with a very long beak
this is a black and white bird with a large orange beak
this bird is black and gray in color, and has a bright orange beak
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
