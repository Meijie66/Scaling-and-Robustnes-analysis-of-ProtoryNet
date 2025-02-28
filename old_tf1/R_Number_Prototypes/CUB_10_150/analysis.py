from collections import Counter

# Input data (your text)
text = """
this bird has feathers that are black and has a thick black bill
this bird has wings that are brown and has a large yellow bill
this bird has wings that are black and has a big bill
this bird has wings that are black and has a big bill
this bird has feathers that are black and has a thick black bill
this bird has wings that are black and has an orange bill
this bird has wings that are grey and has a long black bill
this bird has wings that are grey and has a long black bill
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are brown and white and has a long bill
this bird has feathers that are black and has a thick black bill
this bird has a large, orange bill, a grey breast, and black wings
this bird has wings that are grey and has a long black bill
this bird has wings that are brown and has a long black bill
this bird has feathers that are black and has a thick black bill
this bird is black with white on its stomach and a short beak
this bird has wings that are brown and has a large yellow bill
this bird has a large, orange bill, a grey breast, and black wings
this bird has wings that are brown and has a long black bill
this is a black bird with a white belly and a large orange beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and has a white bill
this bird has wings that are brown and has a long black bill
this bird has wings that are grey and has a long black bill
this bird has a orange and black bill and a white breast
this bird has a very short orange bill with a black spot and a white eye
this bird has wings that are brown and has a large yellow bill
this bird has feathers that are black and has a thick black bill
this bird has wings that are brown and has a large yellow bill
this bird has wings that are brown and white and has a long bill
this bird has feathers that are black and has a thick black bill
this bird has a black head and has a short bright orange pointed bill
this bird has a black head and has a short bright orange pointed bill
this bird has feathers that are black and has a thick black bill
this bird has a white superciliary and brown all around its body with a long bill
this bird has wings that are grey and has a long black bill
this bird has wings that are grey and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white and has a yellow bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are grey and has a long black bill
this bird has wings that are brown and has a large yellow bill
this bird has a very short orange bill with a black spot and a white eye
this bird has a black head and has a short bright orange pointed bill
this bird has wings that are grey and has a long black bill
this bird is brown with black on its wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black and has a big bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and white and has a yellow bill
this bird is black with big wings and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird has wings that are black and white and has a yellow bill
this bird has wings that are brown and has a large yellow bill
this bird has wings that are brown and has a large yellow bill
this bird has wings that are brown and has a long black bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are black and has a thick bill
this bird has wings that are grey and has a long black bill
this bird has a large, orange bill, a grey breast, and black wings
this bird has wings that are black and has a thick bill
this bird has wings that are grey and has a long black bill
this bird has feathers that are black and has a thick black bill
this bird has wings that are grey and has a long black bill
this is a black bird with a white belly and a large orange beak
this bird has wings that are black and has a big bill
this bird has a orange and black bill and a white breast
this bird has feathers that are black and has a thick black bill
this bird has wings that are black and has a big bill
this bird has feathers that are black and has a thick black bill
this bird has a orange and black bill and a white breast
this bird has wings that are black with a long orange beak
this bird has wings that are grey and has a long black bill
this bird has wings that are brown and white and has a long bill
this bird has wings that are black and white with a short orange beak
this bird has a black head and has a short bright orange pointed bill
this bird has a large, orange bill, a grey breast, and black wings
this bird has wings that are black and has an orange bill
this bird has a very short orange bill with a black spot and a white eye
this bird has wings that are black and white and has a yellow bill
this bird has wings that are black and white with a short orange beak
this bird has a large, orange bill, a grey breast, and black wings
this bird has wings that are brown and has a large yellow bill
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are black with an orange bill
this bird has wings that are gray and has a big black bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are black and has a orange bill
this bird has wings that are black and has a yellow bill
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are black and white and has a yellow bill
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird has wings that are black and has a thick bill
this bird has wings that are grey and has a long black bill
this bird has a black head and has a short bright orange pointed bill
this bird has wings that are brown and has a long black bill
this bird has wings that are black and has a thick bill
this bird has wings that are grey and has a long black bill
this bird has a very short orange bill with a black spot and a white eye
this bird is black with white on its stomach and a short beak
this bird has wings that are brown and has a large yellow bill
this bird has a black head and has a short bright orange pointed bill
this bird has wings that are brown and white and has a long bill
this bird has wings that are black and white with a short orange beak
this bird has a very short orange bill with a black spot and a white eye
this bird is black with big wings and has a long, pointy beak
this bird has a black head and has a short bright orange pointed bill
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are grey and has a long black bill
this bird has wings that are brown and has a long black bill
this bird has wings that are brown and has a long black bill
this is a black bird with a white belly and a large orange beak
this bird has wings that are black and has a orange bill
this bird has wings that are black and white and has a yellow bill
this bird is gray and black in color, with a large black beak
this bird has a orange beak, black throat, and a black and white belly
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are gray and has a big black bill
this bird has wings that are black and white and has a yellow bill
this bird has wings that are brown and has a large yellow bill
this bird has a large, orange bill, a grey breast, and black wings
this bird has a large, orange bill, a grey breast, and black wings
this bird has wings that are black and white and has a yellow bill
this bird has wings that are grey and has a long black bill
this bird has wings that are black and has a big bill
this bird has wings that are brown and has a long black bill
this bird has feathers that are black and has a thick black bill
this bird has feathers that are black and has a thick black bill
this bird has feathers that are black and has a thick black bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and has a white bill
this bird has a large, orange bill, a grey breast, and black wings
this bird has a large, orange bill, a grey breast, and black wings
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white and has a yellow bill
this bird has a large, orange bill, a grey breast, and black wings
this bird has wings that are brown and white and has a long bill
this bird has wings that are black and white with a small orange beak
this bird has a very short orange bill with a black spot and a white eye
this bird has wings that are grey and has a long black bill
this bird has feathers that are black and has a thick black bill
this bird has wings that are black and has a big bill
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
