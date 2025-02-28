from collections import Counter

# Input data (your text)
text = """
this bird has a white chest, black wings and small curved orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a large beak and has all black feathers
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has a large beak and has all black feathers
this web-footed bird has a short beak, white eyes, and grey and white mottled feathers
this bird has a white chest, black wings and small curved orange beak
this bird has a short orange bill, and a black head
this bird has a short orange bill, and a black head
this bird has wings that are black and white with a short orange beak
this bird has a black crown as well as a small black bill
this bird has a large beak and has all black feathers
this bird has wings that are black and white and has a yellow bill
this bird has a black head and a gray nape, with a large beak
this bird has gray feathers, large feet, white eyes and a bright orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a large beak and has all black feathers
this bird has a large beak and has all black feathers
a large bird with a brown coloring and orange beak
this bird is grey and has a very large wing span with a very long beak
this bird has a large beak and has all black feathers
this bird has a large beak and has all black feathers
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a white chest, black wings and small curved orange beak
this bird has a large beak and has all black feathers
this bird is black with white on its feathers and has a long, pointy beak
this bird has a large beak and has all black feathers
this bird has a large beak and has all black feathers
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
