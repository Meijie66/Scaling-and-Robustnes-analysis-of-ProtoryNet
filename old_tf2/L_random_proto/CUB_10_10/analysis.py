from collections import Counter

# Input data (your text)
text = """
a medium sized bird with a bill that curves downwards, and a white belly
bird has brown body feathers, brown breast feathers, and brown beak
this��bird��has��a��dark��brown��body,��black��wings,��and��a��short,��pointed��bill
a large grey bird, with a white head and belly, and a large curved bill
this bird has wings that are black and has a thickbill
a strange looking black bird,the bird eyes are white
this bird has a black crown as well as a black bill
a medium sized grey bird with a bright orange bill
this grey bird has very long wings
this bird is grey and has a very large wing span with a very long beak
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
