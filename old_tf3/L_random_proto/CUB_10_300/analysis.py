from collections import Counter

# Input data (your text)
text = """
the bird is black with a long wing span and short beak
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this is a bird with black and white feathers and a small straight beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and a stumpy bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird is black and red in color with a black beak, and blackeye rings
this bird has wings that are black and white and has a long bill
this bird has a white body and black wings, this bird's bill is long and slightly curved downward
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird is black with red on its wing and has a very short beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this is a bird with black and white feathers and a small straight beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are brown and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has feathers that are black and has an orange bill
this bird has wings that are black and white and has a long bill
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this is a bird with black and white feathers and a small straight beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and has a short bill
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a small bill
this is a bird with black and white feathers and a small straight beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird is black with white and has a very short beak
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and has a big bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has black wings and tail while the remainder of it is white, with a pointy bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this is a white bird with black and white wings and a long and pointy black beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this is a black bird with a long black tail wing and a pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird is black with big wings and has a long, pointy beak
this bird is brown with white on its head and tail and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a long wing, a brown bill, and a short tail
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird is brown with black and has a very short beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has a pink beak, white body and brown wings
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird is black with long tail feathers and has a very short beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a long bill
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
