
from collections import Counter
text = """
this is a grey bird with black feet and a large beak
this bird is black with long tail feathers and has a very short beak
this is a grey bird with black feet and a large beak
this is a black bird with a white belly and a large orange beak
this bird has a white body and head with black feathers and a long pointy beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white belly and a large orange beak
this is a grey bird with black feet and a large beak
this is a grey bird with black feet and a large beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a grey bird with black feet and a large beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black with long tail feathers and has a very short beak
this is a grey bird with black feet and a large beak
this is a grey bird with black feet and a large beak
this bird is black with long tail feathers and has a very short beak
this bird has a orange beak, black throat, and a black and white belly
this is a grey bird with black feet and a large beak
this is a black bird with a white belly and a large orange beak
this bird is black with long tail feathers and has a very short beak
this is a grey bird with black feet and a large beak
this bird is all black with a large beak and long tail
this is a grey bird with black feet and a large beak
this is a black bird with a white eye and a large orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white belly and a large orange beak
this is a grey bird with black feet and a large beak
this is a black bird with a white belly and a large orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a grey bird with black feet and a large beak
this bird is all black with a large beak and long tail
this is a grey bird with black feet and a large beak
this is a black bird with a white belly and a large orange beak
this is a grey bird with black feet and a large beak
this is a dark grey bird with a long black beak and white feet
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white belly and a large orange beak
this bird is black with long tail feathers and has a very short beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black with white on its stomach and a short beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a grey bird with black feet and a large beak
this is a black bird with a white belly and a large orange beak
this bird has black plumage, with a large head and a large black, curved beak
this is a grey bird with black feet and a large beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with long tail feathers and has a very short beak
this bird has a black head and a gray nape, with a large beak
this is a black bird with a white belly and a large orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a grey bird with black feet and a large beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a grey bird with black feet and a large beak
this is a grey bird with black feet and a large beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a grey bird with black feet and a large beak
this bird is black with long tail feathers and has a very short beak
this is a grey bird with black feet and a large beak
this bird is black with long tail feathers and has a very short beak
this is a grey bird with black feet and a large beak
this is a black bird with a white eye and a large orange beak
this bird is black and gray in color, and has a bright orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with long tail feathers and has a very short beak
this is a black bird with a white belly and a large orange beak
this is a grey bird with black feet and a large beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black with long tail feathers and has a very short beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a grey bird with black feet and a large beak
this is a grey bird with black feet and a large beak
this bird has a black head and a gray nape, with a large beak
this is a grey bird with black feet and a large beak
this is a black bird with a white belly and a large orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a grey bird with black feet and a large beak
this is a grey bird with black feet and a large beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a grey bird with black feet and a large beak
this is a grey bird with black feet and a large beak
this bird is black in color, and has a bright orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with long tail feathers and has a very short beak
this is a white bird with a black wing and a large beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is brown with some white and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a grey bird with a black head and a large black beak
this bird is brown with white and has a long, pointy beak
this is a black bird with a white belly and a large orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a grey bird with black feet and a large beak
this is a black bird with a white belly and a large orange beak
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