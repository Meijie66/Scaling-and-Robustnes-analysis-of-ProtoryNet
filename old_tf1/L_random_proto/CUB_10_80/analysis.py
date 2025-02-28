from collections import Counter

# Input data (your text)
text = """
this bird is black with a red beak and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is grey with white and has a very short beak
this bird is black white white on its chest and has a very short beak
this bird is grey with white and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is black white white on its chest and has a very short beak
this bird is grey with white and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird has black plumage, with a large orange beak and white stripes on its head
this bird is black with white and has a very short beak
this bird is mostly white grey wings, and a long snubbed bill
this bird has a black crown with a short orange beak and black throat
this bird is black and has a very short beak
this bird has very long wings and is a water bird with white on its head
this bird is grey with white and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its chest and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is grey with white and has a very short beak
this bird has very long wings and is a water bird with white on its head
this bird is black with white and has a very short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with white and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is grey with white and has a very short beak
this bird is black with a red beak and has a very short beak
this is a white bird with a black wing and a large beak
this bird is white with black on its head and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has very long wings and is a water bird with white on its head
this bird is white with black on its head and has a very short beak
this bird has wings that are black and white and a stumpy bill
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with white and has a very short beak
this bird has a white crown, a long neck, and an orange bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is grey with white and has a very short beak
this bird is black with a red beak and has a very short beak
this is a white bird with a black wing and a large beak
this bird is black with white on its chest and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is primarily black with a white belly and a short beak
this bird is black with grey and has a very short beak
this bird has very long wings and is a water bird with white on its head
this bird is grey with white and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is grey with white and has a very short beak
this bird is grey with white and has a very short beak
this bird is grey with black and has a very short beak
this bird is white and black in color, with a large white beak
this bird is black white white on its chest and has a very short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black and gray in color, with a large curved beak
this bird is grey with white and has a very short beak
this bird has a white crown, yellow beak and brown wings
this bird is black white white on its chest and has a very short beak
this bird is grey with white and has a very short beak
this bird is black with white and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with white and has a very short beak
this is a black bird with a long black tail feather and a large beak
this bird is black with white and has a very short beak
this bird is white with black and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has a white crown, yellow beak and brown wings
this is a white bird with a black wing and a large beak
this bird is black and has a very short beak
this is a white bird with a black wing and a large beak
this bird is black with a red beak and has a very short beak
this bird is black white white on its chest and has a very short beak
this bird is white with black and has a very short beak
this bird is grey with white and has a very short beak
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
