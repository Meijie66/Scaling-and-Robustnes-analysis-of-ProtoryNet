from collections import Counter

# Input data (your text)
text = """
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this is a white bird with black wings and an orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a orange bill
this bird has wings that are black with an orange beak
this bird has wings that are black with a long orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird has wings that are grey and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has a white body, brown wings and an orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are brown and has a long black bill
this bird has wings that are black and has an orange bill
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a orange bill
this bird has wings that are black with a long orange beak
this bird has wings that are black and white with a short orange beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird has wings that are black and has an orange bill
this bird has wings that are grey and has a long black bill
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird has wings that are black and has a orange bill
this bird has wings that are black and has a red and yellow blotch
this bird has wings that are black with a long orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black with a long orange beak
this bird has a white body, brown wings and an orange beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are gray and has a big black bill
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a white body, brown wings and an orange beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird has wings that are grey and has a long black bill
this is a white bird with black wings and an orange beak
this bird has wings that are black and white and has a long bill
a flying albatross with big and long black wings and white body has orange beak and legs
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black with a short black beak
this bird has wings that are black with an orange beak
a grayish black bird with white eyes and orange stubby beak that has a tuft of gray feathers on it
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and has an orange bill
this bird has wings that are black and has a bulky yellow beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird has wings that are black with a long orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black with a long orange beak
this bird has wings that are black and has a orange bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a orange bill
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has wings that are black and has an orange bill
this bird has wings that are black and has a long black bill
this is a white bird with black wings and an orange beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has wings that are black with a long orange beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird has wings that are black and has an orange bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this is a grey bird with black wings and an orange beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird has wings that are black and white with a small orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black with a long orange beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black with a long orange beak
this is a white bird with black wings and an orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird has a white body, brown wings and an orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a long orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black with a long orange beak
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
