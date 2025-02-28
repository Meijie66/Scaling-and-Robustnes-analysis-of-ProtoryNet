from collections import Counter

# Input data (your text)
text = """
this bird is black in color, and has a bright orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has black plumage, with a large orange beak and white stripes on its head
this is a black and white bird with a large orange beak
this black and gray bird has a very short orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has wings that are black and white with a short orange beak
this is a black bird with a white eye and a large orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is brown with some white and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this bird has black plumage, with a large orange beak and white stripes on its head
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is brown with some white and has a long, pointy beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has wings that are black and white with a short orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is brown with some white and has a long, pointy beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black in color, and has a bright orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black, white, and brown in color with a stubby beak and black eye rings
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black in color, and has a bright orange beak
this bird is brown with some white and has a long, pointy beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a brown and black bird with a yellow eye and an orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this black colored bird has a bright orange beak and white eyes
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black and gray in color, and has a bright orange beak
this bird has black plumage, with a large orange beak and white stripes on its head
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has black plumage, with a large orange beak and white stripes on its head
this is a black bird with a white eye and a large orange beak
this bird is white and black in color, with a stubby orange and black beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has wings that are black and white with a short orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white eye and a large orange beak
this bird is black and gray in color, and has a bright orange beak
this bird is black and gray in color, and has a bright orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this black and gray bird has a very short orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black and gray in color, and has a bright orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white eye and a large orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill, a black head, and a black and white mottled body
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white eye and a large orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black and white bird with a large orange beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black and gray in color, and has a bright orange beak
this is a brown and black bird with a yellow eye and an orange beak
this bird has wings that are brown and white and has a long bill
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black and gray in color, and has a bright orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black and gray in color, with a large curved beak
this bird is black and gray in color, and has a bright orange beak
this bird has wings that are brown and white and has a long bill
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black with white and has a long, pointy beak
this bird is black, white, and gray in color, with a orange and black beak
this bird is black with white and has a long, pointy beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this bird is gray and black in color, with a large black beak
this black and gray bird has a very short orange beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this bird is brown with some white and has a long, pointy beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has an all black body with a large orange beak and a white eye
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black and gray in color, and has a bright orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black and gray in color, and has a bright orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this bird has black plumage, with a large orange beak and white stripes on its head
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has black plumage, with a large orange beak and white stripes on its head
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this black and gray bird has a very short orange beak
this bird has black plumage, with a large orange beak and white stripes on its head
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black colored bird has a bright orange beak and white eyes
this bird has black plumage, with a large orange beak and white stripes on its head
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black in color, and has a bright orange beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
the bird is black with orange and yellow wingbars and a thin black beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has sparse plumage and a thick brown beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has black plumage, with a large orange beak and white stripes on its head
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black, white, and brown in color with a stubby beak and black eye rings
this bird is all black with an orange beak and a bit of white between the head and beak
this is a black bird with a white eye and a large orange beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has black plumage, with a large orange beak and white stripes on its head
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black with white on its chest and has a very short beak
this bird has wings that are black and white with a short orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black and gray in color, with a large curved beak
this bird is white with black on its head and has a very short beak
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has an all black body with a large orange beak and a white eye
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black and white bird with a large orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black and gray bird has a very short orange beak
this bird has an all black body with a large orange beak and a white eye
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white eye and a large orange beak
this black and gray bird has a very short orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white eye and a large orange beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
this bird has an all black body with a large orange beak and a white eye
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill and a large white eye with a white and brown mottled throat
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
