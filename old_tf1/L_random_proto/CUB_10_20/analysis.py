from collections import Counter

# Input data (your text)
text = """
the wholly black bird features a strong, thick beak and beady black eyes
this bird has wings that are black and has a rotund body
this big bird has a long, black wingbars, and black thigh, body and feet
this is a plump dark gray bird with a thick beak that is yellow
medium to large grey and black bird with long black beak
this bird has wings that are black and has a orange bill
this bird has wings that are black and has a thick bill
the bird has orange coverts, black wingbars and a black back
this black bird has a sharp beak and white eyering
the bird has a black eyering, short throat and a small bill
gray spooky looking bird with tuft of hair on top of head with irange beak
this black bird has a straight beak, black tarsus & feet, and a bright orange covert
the bird is grey and black with an orange bill and white eyes
this bird is gray and black in color, with a orange beak
this is a large grey bird with a large grey beak
a dark gray bird with white eyes and an orange beak
this bird has wings that are black and has ahwite eyes
this bird has gray and white tarsus along with a white belly and black crown
brown duck playing on the lake making a poodle
brown duck playing on the lake making a poodle
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
