from collections import Counter

# Input data (your text)
text = """
this bird is black with red and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this is a black bird with an orange wing and a pointy beak
this bird is black with red and has a long, pointy beak
this is a bird with a white belly, black wings and head and an orange beak
this bird has wings that are black with a long orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird has a orange beak, black throat, and a black and white belly
this bird is black with red and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this is a black bird with an orange wing and a pointy beak
this bird is black with red and has a long, pointy beak
this bird has a orange beak, black throat, and a black and white belly
this is a black bird with an orange wing and a pointy beak
this is a black bird with a white belly and a large orange beak
this bird is brown with black on its wings and has a long, pointy beak
this is a black bird with a long black tail wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this bird has wings that are black and white with a short orange beak
this is a black bird with an orange wing and a pointy beak
this bird has wings that are black with a long orange beak
this is a black bird with an orange wing and a pointy beak
this bird has wings that are black and white with a small orange beak
this bird is black with red and has a long, pointy beak
this bird is all black with a large beak and long tail
this bird has wings that are black with a long orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with an orange wing and a pointy beak
this bird is black and red in color, and has a black beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with a long black tail wing and a pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a black bird with an orange wing and a pointy beak
this bird is black with a red beak and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is black with red and has a long, pointy beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with red and has a long, pointy beak
this bird is black and red in color, and has a black beak
this bird has wings that are black with a long orange beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this bird is black with red and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white with a short orange beak
this is a black bird with an orange wing and a pointy beak
this bird has a orange beak, black throat, and a black and white belly
this bird is black with red and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird has a orange beak, black throat, and a black and white belly
this is a black bird with an orange wing and a pointy beak
this bird has wings that are black with a long orange beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this bird has wings that are black and white with a short orange beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
this bird has a orange beak, black throat, and a black and white belly
this bird is brown with black on its wings and has a long, pointy beak
this is a black bird with an orange wing and a pointy beak
this bird has wings that are black with a long orange beak
this bird is black with red on its wing and has a very short beak
this is a black bird with an orange wing and a pointy beak
this is a black bird with an orange wing and a pointy beak
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
