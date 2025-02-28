from collections import Counter

# Input data (your text)
text = """
this is a black bird with a white belly and a large orange beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has wings that are black and white with a short orange beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with a white chest and has a very short beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has a white belly and breast with an orange bill and webbed feet
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has black plumage, with a large head and a large black, curved beak
this is a black bird with a white belly and a large orange beak
this bird is brown with some white and has a long, pointy beak
this brown bird has a distinctive long sharp bill and this is a large bird
this bird is black with a big wingspan and has a very short beak
this bird is grey with long wings and has a long, pointy beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this is a black bird with a long black tail feather and a large beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this is a black bird with a white belly and a large orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is grey with long wings and has a long, pointy beak
this bird is one solid color, black, with black tarus and feet, and bright yellow eyes
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a black bird with a white belly and a large orange beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is grey with long wings and has a long, pointy beak
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
