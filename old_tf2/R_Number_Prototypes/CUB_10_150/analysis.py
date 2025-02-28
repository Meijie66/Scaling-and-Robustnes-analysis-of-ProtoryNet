from collections import Counter


text = """
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with big wings and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a large grey bird with a black face and beak
this is a large grey bird with a black face and beak
this bird is black with white and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a white bird with black wings and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this bird is white with black and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this bird is black with white and has a long, pointy beak
this is a white bird with a black wing and a large beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a large grey bird with a black face and beak
this is a large grey bird with a black face and beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with grey and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a white bird with a black wing and a large beak
this is a black bird with a white belly and a large orange beak
this bird is black with big wings and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this bird is black with big wings and has a long, pointy beak
this is a large grey bird with a black face and beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a large grey bird with a black face and beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with big wings and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a grey bird with black feet and a large beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with white and has a long, pointy beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a large grey bird with a black face and beak
this bird is black with red and has a very short beak
this bird is black with white on its feathers and has a long, pointy beak
this is a large grey bird with a black face and beak
this bird is black with big wings and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with white and has a long, pointy beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a grey bird with black feet and a large beak
this is a white bird with a black wing and a large beak
this bird is brown with white and has a long, pointy beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is brown with white and has a long, pointy beak
this is a white bird with a black wing and a large beak
this is a large grey bird with a black face and beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black back, white eye and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a large grey bird with a black face and beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a white bird with a black wing and a large beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a white bird with a black wing and a large beak
this is a large grey bird with a black face and beak
this is a black bird with a white belly and a large orange beak
this bird is black with big wings and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with white and has a long, pointy beak
this is a white bird with a black wing and a large beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with big wings and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this bird is grey with black and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with white and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white belly and a large orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black with big wings and has a long, pointy beak
this is a large grey bird with a black face and beak
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