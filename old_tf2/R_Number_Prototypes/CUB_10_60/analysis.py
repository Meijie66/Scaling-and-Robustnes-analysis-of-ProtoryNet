from collections import Counter

# Input data (your text)
text = """
this bird has white eyes and a bright orange wide beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is brown with some white and has a long, pointy beak
this is a grey bird with a white eye and a large orange beak
this black colored bird has a bright orange beak and white eyes
this bird has black plumage and yellow eyes, with a long and flat beak
this bird has black plumage and yellow eyes, with a long and flat beak
this is a grey bird with a white eye and a large orange beak
this is a grey bird with a white eye and a large orange beak
this bird is brown with some white and has a long, pointy beak
this is a grey bird with a white eye and a large orange beak
this is a grey bird with a white eye and a large orange beak
this bird has black plumage, with a large orange beak and white stripes on its head
this bird has a short orange bill, and a black head
this bird has black plumage and yellow eyes, with a long and flat beak
this bird has black plumage and yellow eyes, with a long and flat beak
this is a grey bird with a white breast and eye and a black beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird is black with white and has a very short beak
this bird is brown in color, and has a black beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird is a very dark blue with a black head and beak, while it's eyes are white
this bird has an all black body with a large orange beak and a white eye
this bird is brown with black feet and has a very short beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this bird has white eyes and a bright orange wide beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this is a grey bird with a white eye and a large orange beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird is all black with a large beak and long tail
this bird has black plumage, with a large orange beak and white stripes on its head
this is a grey bird with a white eye and a large orange beak
this bird has black plumage and yellow eyes, with a long and flat beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a grey bird with a black beak and a white eye
this bird has white eyes and a bright orange wide beak
this is a grey bird with a white eye and a large orange beak
this is a grey bird with a white eye and a large orange beak
this bird has black plumage, with a large orange beak and white stripes on its head
this bird is a very dark blue with a black head and beak, while it's eyes are white
this bird has black plumage and yellow eyes, with a long and flat beak
this bird is black and gray in color, and has a bright orange beak
this bird has black plumage and yellow eyes, with a long and flat beak
this is a grey bird with a white eye and an orange beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird has an all black body with a large orange beak and a white eye
this bird has white eyes and a bright orange wide beak
this bird is a very dark blue with a black head and beak, while it's eyes are white
this bird has black plumage, with a large orange beak and white stripes on its head
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this bird has black plumage, with a large orange beak and white stripes on its head
this bird is a very dark blue with a black head and beak, while it's eyes are white
this bird is black with big wings and has a long, pointy beak
this bird has white eyes and a bright orange wide beak
this black colored bird has a bright orange beak and white eyes
this is a grey bird with a white eye and a large orange beak
this bird is a very dark blue with a black head and beak, while it's eyes are white
this bird is black with white and has a very short beak
this bird is white and gray in color, and has a bright orange beak
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
