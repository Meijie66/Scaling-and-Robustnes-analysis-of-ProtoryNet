from collections import Counter

# Input data (your text)
text = """
this bird has black plumage, with a large head and a large black, curved beak
this is a black bird with long wings and a black beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black wings and a solid black head
this is a large grey bird with a large downward pointing beak
this bird has black plumage, with a large head and a large black, curved beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this is a grey bird with large feet and a large black beak
this bird has a blunt orange beak with mostly black above the neck, the belly is solid white
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this is a brown bird with a large pointed black beak
this bird has wings that are black with a long orange beak
this small bird has a black & blue colored body, and a black bill
this bird has black plumage, with a large head and a large black, curved beak
this is a black bird with a long tail feather and a large black beak
this bird has a black crown with black belly and black sides
this bird has black plumage, with a large head and a large black, curved beak
a large bird with a white belly, black and white wings with a long beak
this bird has very long black wings, with a long black bill
this is a black bird with a large downward pointing black beak
this is a brown bird with a large pointed black beak
this bird has a large beak and has all black feathers
this bird is white and black in color, with a large white beak
this is a brown bird with a large pointed black beak
this bird has a black head and a gray nape, with a large beak
a large dark brown gray bird with a black beak
this bird has a black bill, a black breast,and a black wing
this bird has long black and white wings, with a very long bill
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has a black head and a gray nape, with a large beak
this is a black bird with a long black tail wing and a pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has black wings and a solid black head
this bird has black plumage, with a large head and a large black, curved beak
this bird has a black crown, black primaries, and a white belly
this bird has very long black wings, with a long black bill
this is a grey bird with a black head and a large black beak
this bird has a black head, a long black bill, and a large wingspan
the bird has a wide wing span, with a grayish body feather with a long beak
this bird has a black crown with a short orange beak and black throat
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
