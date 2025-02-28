from collections import Counter

# Input data (your text)
text = """
this bird is black in color, and has a bright orange beak
this bird has a white body and head with black feathers and a long pointy beak
this bird is black with white and has a long, pointy beak
this bird is gray and brown in color, and has a large curved beak
this bird has wings that are grey and has a white belly
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is white and brown in color, with a stubby beak
this bird is black and gray in color, and has a bright orange beak
this bird is grey and has a very large wing span with a very long beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black and gray in color, and has a bright orange beak
this bird is all black with long tail feathers and a large rounded beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and has an orange and yellow patch
this bird is grey with white and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird has a wide wing span covered in brown, grey and white feathers with a broad, blunt beak
this bird is black with a white belly, has webbed feet and a red beak
this bird has a large beak and has all black feathers
this bird is gray and brown in color, and has a large curved beak
a black bird with a long tail and a large gray beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with a white belly, has webbed feet and a red beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird has a large beak and has all black feathers
this bird has a large beak and has all black feathers
this small bird has a white breast and a small orange beak
this bird has a white belly and breast with an orange bill and webbed feet
this bird has black plumage and yellow eyes, with a long and flat beak
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
