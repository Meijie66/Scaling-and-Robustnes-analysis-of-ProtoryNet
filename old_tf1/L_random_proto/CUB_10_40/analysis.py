from collections import Counter

# Input data (your text)
text = """
this bird has a black and dark orange bill, with white eyes
this bird has a black and dark orange bill, with white eyes
this bird has a black and dark orange bill, with white eyes
this is a plump dark gray bird with a thick beak that is yellow
this is a black bird with white feet and an orange bill
this bird has a gray and white belly and a small orange beak
this bird has feathers that are black and has an orange bill
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and a long yellow bill
this bird has a white belly and a long yellow bill
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a black and dark orange bill, with white eyes
this bird has a black and dark orange bill, with white eyes
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a black and dark orange bill, with white eyes
this bird has a white belly and grey wings and crown with an orange bill
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white head and a big orange bill
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and breast, black/webbed feet and a brightly orange colored bill
this gray winged bird has a white head and rump and black retrices
this bird has a black and dark orange bill, with white eyes
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and a long yellow bill
this bird has a black and dark orange bill, with white eyes
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and breast with an orange bill and webbed feet
this bird has a white belly and breast, black/webbed feet and a brightly orange colored bill
this bird has a black and dark orange bill, with white eyes
this bird is white and black in color, and has a orange beak
this bird has a black and dark orange bill, with white eyes
this bird has a white belly and breast with an orange bill and webbed feet
this bird is white and black in color, and has a orange beak
this bird has a white belly and a long yellow bill
this bird has a black and dark orange bill, with white eyes
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
