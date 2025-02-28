from collections import Counter

# Input data (your text)
text = """
this bird has wings that are grey and has a long black bill
this bird has wings that are black and has a red and yellow blotch
this bird has wings that are grey and has a long black bill
this bird has wings that are grey and has a long black bill
this bird has wings that are brown and has a long black bill
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black and has a long black bill
this bird has wings that are grey and has a long black bill
this bird has a white body and black wings, this bird's bill is long and slightly curved downward
this bird has wings that are black and has an orange bill
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are grey and has a long black bill
this bird has wings that are brown and has a long black bill
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are grey and has a long black bill
this bird has a black bill and broad, grey wings and a grey body
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird is black and orange in color, with a black beak
this bird has wings that are grey and has a long black bill
this bird has wings that are brown and has a black bill
this bird has wings that are grey and has a long black bill
this bird has wings that are grey and has a long black bill
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are grey and has a long black bill
this bird has a white belly with a black back and face
this bird has wings that are brown and has a long black bill
this bird has wings that are grey and has a long black bill
this bird has wings that are grey and has a long black bill
this bird has wings that are grey and has a long black bill
this bird has wings that are brown and has a long black bill
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are grey and has a long black bill
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are grey and has a long black bill
this small bird has a black & blue colored body, and a black bill
this bird has wings that are grey and has a long black bill
this black and white bird has a white throat, small beak, speckled belly, and white eyering
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
