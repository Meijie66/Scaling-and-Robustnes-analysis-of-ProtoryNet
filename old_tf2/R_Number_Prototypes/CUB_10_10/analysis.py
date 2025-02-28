from collections import Counter

# Input data (your text)
text = """
this bird has wings that are black and has a thick bill
bird has black body feathers, white breast feather, and short beak
this bird is black with white and has a long, pointy beak
a large grey bird, with a white head and belly, and a large curved bill
this bird has wings that are black and has a white belly
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a black crown as well as a small black bill
a medium sized bird with black feet and a black breast and belly with a orange and black beak
this bird has a large grey head with a orange pointed bill
this bird is grey and has a very large wing span with a very long beak
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
