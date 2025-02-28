from collections import Counter

# Input data (your text)
text = """
a black and white bird with white eyes
and all black bird with red and yellow side
a small bird with a black and white coloring and short beak
this water bird has a black crown and back, yellow and black bill and cream colored throat
birds beak is small and flat black head and feet are small secondaries is tand orange and brown
a medium size bird with a short, pointed, orange beak
this bird has wings that are black and has a thick bill
this bird is completely black, with a blunt beak
this bird has wings that are black and has a thickbill
the bird is light brown in color and has a head that is brown with a thick bill
this bird is brown with black and has a long, pointy beak
this bird has wings that are black with a black head
this is a completely black bird with red and yellow covarts
this bird has wings that are black and has a yellow and orange patch
this bird has wings that are grey and has a yellow bill
the bird has a thick brown neck with a grey beak and a white head
this gray bird has large webbed feet, a white belly, a white eye, and a short orange bill
this bird is black with white and has a very short beak
this particular bird has a belly that is gray and black
this particular bird has a white belly and breast and black secondaries
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
