from collections import Counter

# Input data (your text)
text = """
this bird is black with big wings and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black and white and has a long bill
this is a dark grey bird with a long black beak and white feet
this bird is black with big wings and has a long, pointy beak
this is a dark grey bird with a long black beak and white feet
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a blunt orange beak and dark brown wings
this bird is entirely black with a long, sharp beak and a broad wingspan
this is a grey bird with black feet and a large beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has wings that are black and white with a short orange beak
this is a grey bird with black feet and a large beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has wings that are brown and has a long neck
this bird is brown with short wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is completely black and has a very short beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
a large bird with a white belly, black and white wings with a long beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is black with white on its stomach and a short beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with weird eyes and has a very short beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has a large beak and has all black feathers
this is a dark grey bird with a long black beak and white feet
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown with black feet and has a very short beak
this is a grey bird with black wings and a pointy beak
this bird is brown with black and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown with black feet and has a very short beak
this is a brown bird with long wings and a large beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is all black with an orange beak and a bit of white between the head and beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is brown with short wings and has a long, pointy beak
this bird is white with black and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this is a dark grey bird with a long black beak and white feet
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black and white with a short orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a brown bird with long wings and a large beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with white and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is grey with black and has a very short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with white on its feathers and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a white bird with a black wing and a large beak
this is a dark grey bird with a long black beak and white feet
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is brown with black and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is brown with short wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is grey with black and has a very short beak
this bird has wings that are black and white with a short orange beak
this is a large grey bird with a black face and beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this bird appears black with very long wings, and a long bill
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with white and has a very short beak
this is a grey bird with black feet and a large beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this is a grey bird with large feet, a white eye and an orange beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is completely black and has a very short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is grey with long wings and has a long, pointy beak
this bird has a wide wing span covered in brown, grey and white feathers with a broad, blunt beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with white on its feathers and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is brown with black and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown with short wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this bird is brown with black feet and has a very short beak
this bird is brown with black and has a very short beak
this bird is brown with short wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
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
