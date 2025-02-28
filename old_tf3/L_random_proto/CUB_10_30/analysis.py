from collections import Counter

# Input data (your text)
text = """
this bird has a black crown as well as a black belly
this bird is completely black with the exception of red and yellow on its coverts
a black bird with white spots and small black bill
this water bird has a black crown and back, yellow and black bill and cream colored throat
a small black bird with a vivid red covert and yellow wingbar
a black bird with a white breast and black feet
this bird has a black bill, a black breast,and a black wing
this bird is grey with long wings and has a long, pointy beak
this bird has wings that are black and has a white belly
this bird is completely black with the exception of red and yellow on its coverts
this bird has a white back and a black head
this bird has a black crown with a short orange beak and black throat
this bird has a black crown with yellow and orange coverts and black belly
a black bird with a white breast and black feet
this bird has feathers that are black and has an orange bill
this bird is completely black with a pointy black beak
a black bird with an orange beak and a white stripe coming from its white eyes
this bird is white and black in color, and has a orange beak
a bird with a white belly, and black and white wingbars with a black outer retrices
this bird has a black crown, black primaries, and a black belly
this bird has a black crown, a black belly and a white wingbar
the even black color of this bird is only interrupted by an orange and yellow wingbar
this bird is black in color, with a black beak
this particular bird has a white belly and a black breast
this bird has wings that are black with a black head
a completely black bird except a white and orange wingbar
this is a completely black bird that has some yellow and orange on its coverts
this bird is black witrh blue and has a long, pointy beak
a small black bird, with a sharp yellow bill
this particular bird has a belly that is white and black
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
