from collections import Counter

# Input data (your text)
text = """
this bird is black with red and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with white and has a long, pointy beak
a black bird with a long tail and a large gray beak
this bird has wings that are black and has a white belly
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
this bird is all black with a large beak and long tail
this bird is black with grey and has a long, pointy beak
a black bird with a long tail and a large gray beak
this bird is gray and black in color, with a large black beak
a black bird with a long tail and a large gray beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and has a red and yellow patch
this bird is black with grey and has a long, pointy beak
this bird is gray and black in color, with a large black beak
a black bird with a long tail and a large gray beak
this is a black bird with a white belly, a red beak, and small webbed feet
this bird is black with grey and has a very short beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
this bird is black with grey and has a very short beak
this bird is black with grey and has a long, pointy beak
a black bird with a long tail and a large gray beak
this bird is black with grey and has a long, pointy beak
this bird is black with grey and has a very short beak
this bird is black with grey and has a very short beak
this bird is all black with a large beak and long tail
this bird is black with grey and has a long, pointy beak
this bird is black with long tail feathers and has a very short beak
a black bird with a long tail and a large gray beak
this bird is black with grey and has a very short beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with grey and has a very short beak
this bird is black with grey and has a long, pointy beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
this is a grey bird with large feet and a large black beak
this bird is black with grey and has a very short beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
this bird is grey with black and has a long, pointy beak
this bird is all black with a large beak and long tail
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
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
