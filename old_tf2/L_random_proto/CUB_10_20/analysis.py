from collections import Counter

# Input data (your text)
text = """
a medium sized bird with a black crown and a bill that curves downwards
this large bill is covered in black feathers with a bright orange bill
this bird is black with white and has a long, pointy beak
a medium sized bird with a grey belly, and a bill that curves downwards
this bird has wings that are black and has a white belly
a medium sized bird, with a bill that curves downwards, and a black crown
a medium sized bird, with a bill that curves downwards, and a black crown
a red and black beak connects to a dark crown with light eyes peering into the distance
a big rounded yellow bill, long white eyebrow, eyering, long neck
this bird is grey and has a very large wing span with a very long beak
a red and black beak connects to a dark crown with light eyes peering into the distance
this large bird has a small orange bill, white belly, and grey feathers
the bird is black with a curved head and a long black tail as well as a black short beak
this bird has wings that are grey and has a long orange bill
this bird has wings that are black and has a red and yellow patch
a medium sized bird with a black crown and a bill that curves downwards
a beautiful grey bird with a black head, and a small black eye with a white eye ring
a larger bird with a long beak that curves downwards at the end, and a white head with smokey eyes
the bird has a white eyering and a white breast and belly
a bird with a long wingspan and a long beak with a bill curves downward at the end
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
