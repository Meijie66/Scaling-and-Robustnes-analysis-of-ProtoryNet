from collections import Counter

# Input data (your text)
text = """
this bird is grey with long wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird has wings that are black and has an orange bill
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird has a very large wing span with dark colored wings and a white body
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a very large wing span with dark colored wings and a white body
this bird is grey with long wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
the bird is made up of thick black feathers and a has a short black beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is grey with long wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is grey with long wings and has a long, pointy beak
this bird is brown with short wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird has a very large wing span with dark colored wings and a white body
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
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
