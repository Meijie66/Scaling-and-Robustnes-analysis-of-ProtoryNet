from collections import Counter

# Input data (your text)
text = """
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a white chest, black wings and small curved orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown with black and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has wings that are black and has an orange bill
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a white chest, black wings and small curved orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a orange beak, black throat, and a black and white belly
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a black head and a gray nape, with a large beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a black bird with a white belly and a large orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown with a black back and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown with black and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a white chest, black wings and small curved orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with white and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a black bird with a white belly and a large orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black in color with a black beak, and black eye rings
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird is brown with black and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has wings that are black and white with a small orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown with black and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is grey with black and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with big wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a black bird with a white belly and a large orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a orange beak, black throat, and a black and white belly
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is grey with black and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a large beak and has all black feathers
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is brown in color, and has a black beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black in color with a black beak, and black eye rings
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with white and has a very short beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has wings that are black and has an orange bill
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
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
