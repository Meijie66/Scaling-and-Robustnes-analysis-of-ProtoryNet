from collections import Counter

# Input data (your text)
text = """
this is a black bird with a white eye and a large orange beak
this bird is black with white and has a long, pointy beak
a small bird with a black and white coloring and short beak
this bird has a black crown as well as a small black bill
this is a large grey bird with a large grey beak
a medium size bird with a short, pointed, orange beak
this bird has wings that are black and has a thick bill
this bird has a white body and head with black feathers and a long pointy beak
a large bird with a white belly, black and white wings with a long beak
the bird has a white eyering and a small peach bill
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
