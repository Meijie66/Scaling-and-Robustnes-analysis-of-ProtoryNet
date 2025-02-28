from collections import Counter

# Input data (your text)
text = """
this bird has wings that are black and has a thickbill
this is a black bird with a gray bill with a orange and white on the wingbar
the breast and body of the bird is most white, with brown speckles throughout
this bird is entirely black and has a large curved bill
a long black bird with a stubby black beak and a medium sized neck
the bird has a long curved bill that is ambered color
this bird has wings that are black with a bulky bill
the crown of this exotic bird is made to attract eligible females
the bird has a white eyering and long secondaries that are dark grey
the bird has a black eyering, short throat and a small bill
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
