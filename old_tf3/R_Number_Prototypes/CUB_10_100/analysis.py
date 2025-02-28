from collections import Counter

# Input data (your text)
text = """
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this is a grey bird with a black head and a large black beak
a large gray and white bird with a long neck, a short tail and a wide beak with a gray tip
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this bird has a white chest, black wings and small curved orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird is grey with white and has a long, pointy beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
the bird had a white and grey speckled chest with a short orange beak
this bird is black with a white chest and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
the bird has a thick brown neck with a grey beak and a white head
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird is black with a white chest and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this is a grey bird with large feet and a large black beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this is a dark grey bird with a long black beak and white feet
a large bird with a long curved downward beak, with a gray and white body and a white face
a bird with a large beak, grey head with a white belly and dark grey wings
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
the bird had a white and grey speckled chest with a short orange beak
this bird is black with a red beak and has a very short beak
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a orange beak, black throat, and a black and white belly
a large bird with a white belly, black and white wings with a long beak
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird is grey with black and has a very short beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a white breast, a black head, a short red beak, and webbed feet
this bird has a gray and white belly and a small orange beak
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
the bird has a grey body and a white and grey speckled chest along with an orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a gray and white belly and a small orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird is black with grey on its chest and has a very short beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird is black with a red beak and has a very short beak
this is a grey bird with large feet and a large black beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black and white bird has a white throat, small beak, speckled belly, and white eyering
the bird had a white and grey speckled chest with a short orange beak
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has a gray and white belly and a small orange beak
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
