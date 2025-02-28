from collections import Counter

# Input data (your text)
text = """
this is a completely black bird with red and yellow covarts
this large bird has a small orange bill, white belly, and grey feathers
this bird is black with white and has a very short beak
this large bird has a small orange bill, white belly, and grey feathers
this bird has wings that are black and has a white belly and red bill
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a black crown as well as a small black bill
this bird has a orange beak, black throat, and a black and white belly
this bird is mostly grey with a short bright orange bill
this bird is grey and has a very large wing span with a very long beak
this bird has black plumage and yellow eyes, with a long and flat beak
this large bird has a small orange bill, white belly, and grey feathers
this bird is all black with long tail feathers and a large rounded beak
this bird has wings that are black and has a black bill
this bird has wings that are black and has a red and yellow patch
this bird is mostly dark grey with a sharp pointy bill
this bird has a small black bill, with a black and white breast
this bird has a dark grey crown with a light grey belly and white and black beak
this bird has a black crown as well as a small black bill
this bird is brown in color, and has a black beak
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
