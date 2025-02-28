from collections import Counter

# Input data (your text)
text = """
this bird is black and gray in color, and has a bright orange beak
this bird has wings that are brown and has a large yellow bill
this bird is brown and has a black bill with a white bit surrounding it
this bird has a black shiny body and feathers, a small pointy black bill and bright yellow eyes
this bird has a gray and white belly and a small orange beak
this bird has a white body, brown wings and an orange beak
this bird has a gray and white belly and a small orange beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with a big wingspan and has a very short beak
this funny looking bird is black with white eyes and an orange beak
this bird is grey and has a very large wing span with a very long beak
a large bird with an orange bill, white crown, and black eyering
a larger black and grey bird with an orange beak
this bird has wings that are brown and has a large yellow bill
this bird has a gray and white belly and a small orange beak
this is a large bird with dark grey wings, a white body and a large bill
this bird is black with white and has a very short beak
this bird has a white belly and breast, black/webbed feet and a brightly orange colored bill
this bird has webbed feet and a grey bill and throat with a white belly
this bird has a white body, brown wings and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is gray and brown in color, and has a large curved beak
this bird has webbed feet and a grey bill and throat with a white belly
the bird has a black head with a grey and white body and a bright orange bill
this is a dark grey bird with a white eye and an orange beak
a large, gray bird with black wings, orange feet, and a yellow bill
this bird has a large, curved, black bill, a blue throat, and a yellow eyering
this is a bird with a white belly, black back and an orange beak
this is a black bird with a white belly and a large orange beak
this bird has wings that are black and white with a small orange beak
this is a white and gray bird that has webbed feet and a beak that turns down at the tip
this bird has gray tarsus and feet with an orange beak and white eyes
this bird is primarily black with an orange marking on its wing and a short beak
the bird has grey webbed feet and a bright orange beak
a small black bird with light yellow eyes and a black beak
this is a black bird with a grey belly, a white eye and an orange bill
this bird is white and gray in color, and has a vivid orange beak
this is a large bird, brown in color, with a thick beak
this bird is black, white, and gray in color, with a orange and black beak
this bird is completely black with the exception of red and yellow on its coverts
this bird has gray tarsus and feet with an orange beak and white eyes
this bird has gray tarsus and feet with an orange beak and white eyes
a large grey bird, with webbed feet, and a curved bill
a larger black and grey bird with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this funny looking bird is black with white eyes and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is white and brown in color with a curved orange beak and white eye ring
this is a bird with a white belly, black back, white eye and an orange beak
this is a large white bird, with dark grey wings, and a curved bill
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
