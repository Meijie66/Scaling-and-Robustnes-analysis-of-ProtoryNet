from collections import Counter

# Input data (your text)
text = """
this bird has white eyes and a bright orange wide beak
the bird is black with an orange bill and white eye
this bird is black with a large, wide beak
this large bird has is all black with white eyes
this bird is black with crazy eyes and has a very short beak
this is a black bird with a white eye and a large orange beak
this bird has an all black body with a large orange beak and a white eye
this bird has white eyes and a bright orange wide beak
this bird is black with crazy eyes and has a very short beak
this bird is black with grey and white on its head with a tan beak
this large bird has is all black with white eyes
this bird is black and white in color, and has a bright orange beak
this is a large grey bird with a black face and beak
this bird has white eyes and a bright orange wide beak
this large bird has is all black with white eyes
this large bird has is all black with white eyes
this is a large grey bird with a black face and beak
this bird has white eyes and a bright orange wide beak
this bird has white eyes and a bright orange wide beak
this is a large bird with dark grey wings, a white body and a large bill
this large bird has is all black with white eyes
this large bird has is all black with white eyes
this medium sized bird is all black with a black beak
this is a black bird with a white eye and a large orange beak
the bird has a black head with a dark green body and white eye rings with a black bill
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with green eyes and has a long, pointy beak
this is a large grey bird with a black face and beak
the bird is black with a yellow eye and long black tarsals
this bird is black with crazy eyes and has a very short beak
this is a black and white bird with a large orange beak
this is a black and white bird with a large orange beak
this bird has a orange beak, black throat, and a black and white belly
this large bird has is all black with white eyes
this bird has a thick black bill, with a black and white breast
this large bird has is all black with white eyes
this bird has white eyes and a bright orange wide beak
this is a black bird with a white eye and a large orange beak
this is a black and white bird with a large orange beak
this large bird has is all black with white eyes
this bird is white with black and has a very short beak
this large bird has is all black with white eyes
this bird has a black head and it also has a black bill
this bird has white eyes and a bright orange wide beak
this is a black bird with a white eye and a large orange beak
this bird has a black and dark orange bill, with white eyes
this bird has white eyes and a bright orange wide beak
this bird has a orange beak, black throat, and a black and white belly
this is a large grey bird with a black face and beak
this bird has a orange beak, black throat, and a black and white belly
this bird has a black head, a long black bill, and a large wingspan
this bird has white eyes and a bright orange wide beak
this is a black bird with a white eye and a large orange beak
this is a black and white bird with a large orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with crazy eyes and has a very short beak
this bird has a black and dark orange bill, with white eyes
this bird has a orange beak, black throat, and a black and white belly
this bird has a orange beak, black throat, and a black and white belly
this bird is black with crazy eyes and has a very short beak
this bird is white and black in color, and has a vivid bright orange beak
this is a black bird with a white eye and a large orange beak
this is a large bird with dark grey wings, a white body and a large bill
this bird has white eyes and a bright orange wide beak
this bird has white eyes and a bright orange wide beak
this large bird has is all black with white eyes
this is a black and white bird with a large orange beak
this large bird has is all black with white eyes
this bird has a orange beak, black throat, and a black and white belly
this is a large grey bird with a black face and beak
this is a dark grey bird with a white eye and a large black beak
this bird is black with green eyes and has a long, pointy beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird has white eyes and a bright orange wide beak
this bird has a orange beak, black throat, and a black and white belly
this large bird has is all black with white eyes
this bird has a orange beak, black throat, and a black and white belly
this bird has white eyes and a bright orange wide beak
this bird is black with crazy eyes and has a very short beak
this bird has white eyes and a bright orange wide beak
this is a black bird with a white eye and a large orange beak
this large bird has is all black with white eyes
this is a large bird with dark grey wings, a white body and a large bill
this bird has a orange beak, black throat, and a black and white belly
this bird has a black head, a long black bill, and a large wingspan
this large bird has is all black with white eyes
this bird has a orange beak, black throat, and a black and white belly
this bird is a very dark blue with a black head and beak, while it's eyes are white
this bird has a black bill and broad, grey wings and a grey body
this bird is black with white and has a long, pointy beak
this bird has a orange beak, black throat, and a black and white belly
this large bird has is all black with white eyes
this bird is black and white in color, and has a bright orange beak
this bird is black it has a very large beak it looks to be a large bird
this bird has a black and dark orange bill, with white eyes
this bird has white eyes and a bright orange wide beak
this bird has white eyes and a bright orange wide beak
this is a black and white bird with a large orange beak
this bird is black and white in color, and has a bright orange beak
this bird is black with crazy eyes and has a very short beak
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
