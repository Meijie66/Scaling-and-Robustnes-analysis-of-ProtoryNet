from collections import Counter

# Input data (your text)
text = """
this medium-sized bird has spiky crown with black feathers
tan and brown body with a white body, dark brown feathers and an orange beak
a small bird with black coloring and an orange wingbar
this bird has smooth dark-brown feathers and a thick yellowish beak
this dark colored bird has quite a small head and beak compared to the sized of the rest of its body
a medium size bird with a short, pointed, orange beak
this bird has wings that are blue and has yellow eyes
a big bird with gray feathers and a big gray beak
this��bird��has��a��dark��brown��body,��black��wings,��and��a��short,��pointed��bill
the bird has a white eyering and a white breast and belly
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
