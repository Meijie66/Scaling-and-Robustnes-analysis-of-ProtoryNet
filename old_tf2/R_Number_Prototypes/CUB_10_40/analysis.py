from collections import Counter

# Input data (your text)
text = """
this bird is black with red on its wing and has a very short beak
this bird has a white body and head with black feathers and a long pointy beak
this bird is black with white on its feathers and has a long, pointy beak
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this large bird has a small orange bill, white belly, and grey feathers
this bird has gray feathers, large feet, white eyes and a bright orange beak
this bird has a orange beak, black throat, and a black and white belly
this is a grey bird with large feet and a large black beak
this bird has gray feathers, large feet, white eyes and a bright orange beak
this bird is brown with black feet and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has feathers that are black and has a long yellow bill
this bird has a large beak and has all black feathers
this bird has wings that are black and has a thick bill
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with white on its feathers and has a long, pointy beak
this is a grey bird with black feet and a large beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with a white belly, has webbed feet and a red beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is brown with black feet and has a very short beak
this bird is black with a large, wide beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with a white chest and has a very short beak
this bird has a white belly and breast with an orange bill and webbed feet
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a white body and head with black feathers and a long pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with a large, wide beak
this bird has a large beak and has all black feathers
this is a grey bird with black feet and a large beak
the bird has a short, thick orange bill and brown feathers on its head and white eyes
this is a black bird with a white eye and an orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a black head and a gray nape, with a large beak

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
