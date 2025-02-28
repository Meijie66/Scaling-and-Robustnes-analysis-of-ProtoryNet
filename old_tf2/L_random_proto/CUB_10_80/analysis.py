from collections import Counter

# Input data (your text)
text = """
this bird has a white body, brown wings and an orange beak
a mostly brown colored bird with white head and long beak
this bird has brown wings and a white head with an orange beak
a mostly brown colored bird with white head and long beak
this bird is large with a white head and chest and brown wings and an orange beak
this black bird has an orange beak slightly pointing downwards, and a white malar stripe
a mostly brown colored bird with white head and long beak
this bird has a white body, brown wings and an orange beak
this bird has brown wings and a white head with an orange beak
this bird has brown wings and a white head with an orange beak
this bird has brown wings and a white head with an orange beak
a mostly brown colored bird with white head and long beak
this bird has brown wings and a white head with an orange beak
this is a bird with a white breast, black back and an orange beak
this bird is white and brown in color, with a stubby beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has brown wings and a white head with an orange beak
a mostly brown colored bird with white head and long beak
a mostly brown colored bird with white head and long beak
this bird is brown, white, and red in color, with a sharp black beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
a black bird with an orange beak and a white stripe coming from its white eyes
this bird has a white body, brown wings and an orange beak
this bird has brown wings and a white head with an orange beak
this bird has a white body, brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
a mostly brown colored bird with white head and long beak
this bird is large with a white head and chest and brown wings and an orange beak
a mostly brown colored bird with white head and long beak
this bird is large with a white head and chest and brown wings and an orange beak
a mostly brown colored bird with white head and long beak
this bird has brown wings and a white head with an orange beak
this bird has brown wings and a white head with an orange beak
this bird is black with big wings and has a long, pointy beak
this bird has a unique white eye, and a pointed orange beak
this bird has brown wings and a white head with an orange beak
a black bird with an orange beak and a white stripe coming from its white eyes
this is a black bird with a white belly and a large orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
a mostly brown colored bird with white head and long beak
a mostly brown colored bird with white head and long beak
this bird has brown wings and a white head with an orange beak
this bird has brown wings and a white head with an orange beak
this bird has a unique white eye, and a pointed orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has brown wings and a white head with an orange beak
this bird has brown wings and a white head with an orange beak
a mostly brown colored bird with white head and long beak
this bird has black plumage, with a large head and a large black, curved beak
a mostly brown colored bird with white head and long beak
this bird has a white body, brown wings and an orange beak
this bird has a white body, brown wings and an orange beak
this bird has brown wings and a white head with an orange beak
a mostly brown colored bird with white head and long beak
this bird has brown wings and a white head with an orange beak
a mostly brown colored bird with white head and long beak
this bird has black plumage, with a large head and a large black, curved beak
this is a black and blue bird with a white eye and a pointed beak
this bird has a white body, brown wings and an orange beak
a mostly brown colored bird with white head and long beak
a mostly brown colored bird with white head and long beak
this bird has brown wings and a white head with an orange beak
a black bird with an orange beak and a white stripe coming from its white eyes
this is a black bird with a white eye and a large orange beak
this bird is grey and has a very large wing span with a very long beak
a mostly brown colored bird with white head and long beak
this bird has black winds and a white body with a long curved beak
this bird has brown wings and a white head with an orange beak
a mostly brown colored bird with white head and long beak
this bird has brown wings and a white head with an orange beak
a black bird with an orange beak and a white stripe coming from its white eyes
this is a black bird with a white spot on the head and a white breast with an orange beak
a black bird with an orange beak and a white stripe coming from its white eyes
this bird has brown wings and a white head with an orange beak
a mostly brown colored bird with white head and long beak
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird has brown wings and a white head with an orange beak
a mostly brown colored bird with white head and long beak
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
