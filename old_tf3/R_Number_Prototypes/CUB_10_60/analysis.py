from collections import Counter

# Input data (your text)
text = """
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this is a black bird with a white belly and a large orange beak
this is a black bird with a long tail feather and a pointy black beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this bird is brown with black feet and has a very short beak
this bird has a black head and has a short bright orange pointed bill
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a long tail feather and a large black beak
this is a black bird with a white belly and a large orange beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a black head and has a short bright orange pointed bill
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this is a black bird with a long tail feather and a pointy black beak
this is a black bird with a long tail feather and a pointy black beak
this bird has wings that are black and has a yellow bill
this bird has black plumage, with a large head and a large black, curved beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a brown bird with a short white tail and a large brown beak
this is a black bird with a long tail feather and a large black beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a long tail feather and a large black beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this is a black bird with a white belly and a large orange beak
this is a brown bird with a short white tail and a large brown beak
this is a black bird with a white belly and a large orange beak
this is a brown bird with a short white tail and a large brown beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a long tail feather and a pointy black beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a long tail feather and a large black beak
this bird has a white belly, black head and back with a short orange bill
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
the bird has a thick brown neck with a grey beak and a white head
this bird is brown with a white tail and has a long, pointy beak
this is a black bird with a long tail feather and a large black beak
this is a black bird with a white belly and a large orange beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this bird has a black head and has a short bright orange pointed bill
this is a black bird with a long tail feather and a large black beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a long tail feather and a large black beak
this is a black bird with a long black tail feather and a large beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a long tail feather and a pointy black beak
this is a black bird with a white eye and a large orange beak
this is a brown bird with a short white tail and a large brown beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this is a black bird with a white belly and a large orange beak
this bird is brown with a white tail and has a long, pointy beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white belly and a large orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a white belly, black head and back with a short orange bill
this bird has an all black body with a large orange beak and a white eye
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this is a black bird with a white belly, white eye and a small black beak
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
