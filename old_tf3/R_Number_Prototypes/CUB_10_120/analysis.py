from collections import Counter

# Input data (your text)
text = """
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has wings that are black and has a big bill
this bird has black plumage, with a large head and a large black, curved beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with white on its stomach and a short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is grey and has a very large wing span with a very long beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has wings that are black and has a big bill
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has a white body and head with black feathers and a long pointy beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with big wings and has a long, pointy beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has black plumage, with a large head and a large black, curved beak
this bird has a white body and head with black feathers and a long pointy beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has wings that are brown and has a long black bill
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has wings that are brown and has a long black bill
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
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
