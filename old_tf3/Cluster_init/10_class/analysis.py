from collections import Counter

# Input data (your text)
text = """
this bird has a short orange bill, and a black head
this bird is black with red and has a very short beak
this bird has a white head and a big orange bill
this bird has a orange beak, black throat, and a black and white belly
this bird is brown with a black back and has a long, pointy beak
this bird has a black head and has a short bright orange pointed bill
this bird has wings that are black and has a thick bill
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has wings that are black with a long orange beak
this is a grey bird with a black head and a large black beak
this bird has a black head and has a short bright orange pointed bill
this bird has a black head, a long black bill, and a large wingspan
this bird has a black crown as well as a small black bill
this bird has a black head and has a short bright orange pointed bill
this bird has wings that are black and has a yellow bill
this bird has a black crown with a short orange beak and black throat
this bird has a black head and has a short bright orange pointed bill
this bird has a orange beak, black throat, and a black and white belly
this bird is primarily black with an orange marking on its wing and a short beak
this bird has a orange beak, black throat, and a black and white belly
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this bird has a black head and has a short bright orange pointed bill
this bird has a black head and has a short bright orange pointed bill
this bird is brown with white and has a very short beak
this bird has a black head and has a short bright orange pointed bill
this is a grey bird with a black head and a large black beak
this bird has a large beak and is brown with a white ring on its face
this bird has a black head and a gray nape, with a large beak
this bird has a short orange bill, and a black head
this bird is black with long tail feathers and has a very short beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with a black back and has a long, pointy beak
this bird has a white belly, black head and back with a short orange bill
this bird has a black head and a gray nape, with a large beak
this bird has a black head and has a short bright orange pointed bill
this bird has a black head, a long black bill, and a large wingspan
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this bird has a short orange bill, and a black head
this is a large grey bird with a black face and beak
this bird has a orange beak, black throat, and a black and white belly
this bird has a black crown with a short orange beak and black throat
this bird is black with long tail feathers and has a very short beak
this bird has a short orange bill, and a black head
this bird has a black head and a gray nape, with a large beak
this is a brown bird with a large orange beak
this bird has a black crown with a short orange beak and black throat
this bird is gray and brown in color, and has a large curved beak
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
