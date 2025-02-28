from collections import Counter

# Input data (your text)
text = """
this bird is black with big wings and has a long, pointy beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this bird has a curved orange beak and a black body
this bird is black with big wings and has a long, pointy beak
this is a grey bird with black wings and an orange beak
this is a black and white bird with a large orange beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird has a curved orange beak and a black body
this is a black bird with a white belly and a large orange beak
this bird is black and gray in color, and has a bright orange beak
this bird has wings that are black with a long orange beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this is a black and white bird with a large orange beak
this bird has a large, orange bill, a grey breast, and black wings
this is a brown bird with a large pointed black beak
this bird has a curved orange beak and a black body
this bird is gray and black in color, with a large black beak
this is a black and white bird with a large orange beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this bird has a curved orange beak and a black body
this is a brown bird with a large pointed black beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this is a black bird with an orange wing and a small beak
this is a grey bird with black wings and an orange beak
this bird has wings that are black and has a thick bill
this bird is black in color, and has a bright orange beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this bird has an all black body with a large orange beak and a white eye
this bird has an all black body with a large orange beak and a white eye
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird has wings that are black and white with a short orange beak
this is a black bird with a white eye and a large orange beak
this bird has a curved orange beak and a black body
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this is a grey bird with black feet and a large beak
this bird is gray and black in color, with a large black beak
this is a brown bird with a large pointed black beak
this is a grey bird with black wings and an orange beak
this is a black and white bird with a large orange beak
this is a black bird with an orange wing and a small beak
this is a black and white bird with a large orange beak
this is a grey bird with black wings and an orange beak
this is a grey bird with black wings and an orange beak
this is a black and white bird with a large orange beak
this bird is brown with black and has a long, pointy beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black wings and an orange beak
this is a black and white bird with a large orange beak
this bird has black plumage, with a large head and a large black, curved beak
this is a brown bird with a large pointed black beak
this bird has wings that are black with a long orange beak
this is a black and white bird with a large orange beak
this bird is grey with black and has a long, pointy beak
this bird is brown with black and has a long, pointy beak
this is a grey bird with black wings and an orange beak
this is a black bird with an orange wing and a small beak
this bird is gray and black in color, with a large black beak
this bird is black in color, and has a bright orange beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black feet and a large beak
this is a black bird with an orange wing and a small beak
this bird is black with white and has a very short beak
this is a black bird with long wings and a black beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this bird is black and gray in color, with a large curved beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this is a brown bird with a large pointed black beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black wings and an orange beak
this bird has a curved orange beak and a black body
this bird is black in color, and has a bright orange beak
this bird is black in color, and has a bright orange beak
this is a black and white bird with a large orange beak
this bird has wings that are black with a long orange beak
this is a grey bird with black wings and an orange beak
this bird is black with white and has a very short beak
this bird has an all black body with a large orange beak and a white eye
this bird is black in color, with a bright orange beak
this is a grey bird with black wings and an orange beak
this is a black and white bird with a large orange beak
this is a black bird with a white belly and a large orange beak
this is a grey bird with black feet and a large beak
this is a black bird with an orange wing and a small beak
this is a brown bird with a large pointed black beak
this is a black and white bird with a large orange beak
this is a grey bird with black feet and a large beak
this is a brown bird with a large pointed black beak
this is a grey bird with black wings and an orange beak
this is a black bird with an orange wing and a small beak
this is a grey bird with black wings and an orange beak
this is a black and white bird with a large orange beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this is a grey bird with black wings and an orange beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black in color, with a bright orange beak
this bird is black with big wings and has a long, pointy beak
this is a black bird with an orange wing and a small beak
this is a black and white bird with a large orange beak
this is a black bird with an orange wing and a small beak
this bird is brown with black and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black in color, and has a bright orange beak
this is a grey bird with black wings and an orange beak
this bird has wings that are black with a long orange beak
this is a black and white bird with a large orange beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this is a black bird with an orange wing and a small beak
this bird has an all black body with a large orange beak and a white eye
this bird has a curved orange beak and a black body
this bird is gray and black in color, with a large black beak
this is a black bird with an orange wing and a small beak
this bird has wings that are black with a long orange beak
this bird is black in color, and has a bright orange beak
this bird is black in color, and has a bright orange beak
this bird has wings that are black with a long orange beak
this is a black bird with an orange wing and a small beak
this is a black bird with an orange wing and a small beak
this is a black and white bird with a large orange beak
this is a brown bird with a large pointed black beak
this is a brown bird with a large pointed black beak
this bird is gray and black in color, with a large black beak
this bird is black and gray in color, with a large curved beak
this is a black and white bird with a large orange beak
this is a grey bird with black wings and an orange beak
this bird has wings that are black with a long orange beak
this bird is black in color, and has a bright orange beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this is a black and white bird with a large orange beak
this bird has wings that are black with a long orange beak
this is a black bird with an orange wing and a small beak
this bird is gray and black in color, with a large black beak
this bird is black with big wings and has a long, pointy beak
this is a black bird with a white belly and a large orange beak
this is a grey bird with black feet and a large beak
this is a black and white bird with a large orange beak
this is a black bird with long wings and a black beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black wings and an orange beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this is a black bird with a white belly and a large orange beak
this bird has a curved orange beak and a black body
this is a black and white bird with a large orange beak
this bird has wings that are black and has a thick bill
this bird has wings that are black with a long orange beak
this is a black bird with a white belly and a large orange beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black wings and an orange beak
this is a brown bird with a large pointed black beak
this is a black bird with an orange wing and a small beak
this bird is black in color, and has a bright orange beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this bird is brown with black and has a long, pointy beak
this is a grey bird with black wings and an orange beak
this bird has a large, orange bill, a grey breast, and black wings
this bird is gray and black in color, with a large black beak
this bird is black in color, with a bright orange beak
this is a grey bird with black feet and a large beak
this is a grey bird with black feet and a large beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this bird has a curved orange beak and a black body
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this is a grey bird with black wings and an orange beak
this bird is black in color, and has a bright orange beak
this bird is gray and black in color, with a large black beak
this bird is black in color, and has a bright orange beak
this bird has wings that are black with a long orange beak
this bird is black in color, and has a bright orange beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black with a long orange beak
this bird has an all black body with a large orange beak and a white eye
this bird is black in color, with a bright orange beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black wings and an orange beak
this bird has wings that are black with a long orange beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black in color, with a bright orange beak
this is a black bird with an orange wing and a small beak
this bird is gray and black in color, with a large black beak
this bird is black with a red beak and has a very short beak
this is a grey bird with black wings and an orange beak
this bird is black in color, and has a bright orange beak
this is a black bird with an orange wing and a small beak
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird is brown with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this is a black bird with an orange wing and a small beak
this is a brown bird with a large pointed black beak
this is a black bird with an orange wing and a small beak
this is a grey bird with black wings and an orange beak
this bird has wings that are black and has a thick bill
this is a grey bird with black wings and an orange beak
this is a black and white bird with a large orange beak
this bird is black with big wings and has a long, pointy beak
this is a brown bird with a large pointed black beak
this is a black bird with an orange wing and a small beak
this bird has wings that are black with a long orange beak
this bird is black in color, and has a bright orange beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this bird has a large, orange bill, a grey breast, and black wings
this is a grey bird with black wings and an orange beak
this bird is black in color, and has a bright orange beak
this is a grey bird with black wings and an orange beak
this is a brown bird with a large pointed black beak
this is a black bird with a white eye and a large orange beak
this is a grey bird with black wings and an orange beak
this is a black bird with an orange wing and a small beak
this bird is black with big wings and has a long, pointy beak
this is a grey bird with black wings and an orange beak
this bird is black in color, and has a bright orange beak
this is a grey bird with black feet and a large beak
this bird has wings that are black with a long orange beak
this bird is black in color, and has a bright orange beak
this is a brown bird with a large pointed black beak
this is a black bird with an orange wing and a small beak
this is a grey bird with black feet and a large beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this bird is black with big wings and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black feet and a large beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this is a brown bird with a large pointed black beak
this is a black bird with an orange wing and a small beak
this bird is gray and black in color, with a large black beak
this bird has a curved orange beak and a black body
this bird has black plumage, with a large head and a large black, curved beak
this is a black bird with an orange wing and a small beak
this bird has a large, orange bill, a grey breast, and black wings
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird is gray and black in color, with a large black beak
this bird has a curved orange beak and a black body
this is a grey bird with black feet and a large beak
this is a grey bird with black wings and an orange beak
this bird is gray and black in color, with a large black beak
this is a black bird with an orange wing and a small beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this is a brown bird with a large pointed black beak
this bird is gray and black in color, with a large black beak
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
