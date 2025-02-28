from collections import Counter

text = """
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and white with a small orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and has a bulky yellow beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and has a bulky yellow beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and has a bulky yellow beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
a dark grey bird with an orange beak, white eye and long curly feathers at top of beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and white with a small orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and white with a small orange beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this is a white bird with a black wing and a large beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and has a bulky yellow beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
light gray bird with a large wingspan tinged with white that has a black face and beak
this bird has wings that are black and has a bulky yellow beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and white with a small orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black with an orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and white with a small orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this is a white bird with a black wing and a large beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
a medium sized bird with a yellow beak and white feathers around the eye and cheek
this bird is brown with white and has a very short beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and white with a small orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and has a bulky yellow beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this is a white bird with a black wing and a large beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this is a white bird with a black wing and a large beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this is a white bird with black wings and an orange beak
this is a white bird with a black wing and a large beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and has a bulky yellow beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and has a thick bill
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this is a grey bird with black wings and a pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this is a grey bird with black wings and a pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
a strange looking bird with a curved beak and small head in proportion to its body
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and white with a small orange beak
this bird has a white chest, black wings and small curved orange beak
this is a white bird with a black wing and a large beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
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