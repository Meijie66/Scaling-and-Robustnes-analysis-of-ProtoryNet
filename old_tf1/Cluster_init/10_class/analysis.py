from collections import Counter

# Input data (your text)
text = """
this is a black bird with a long black tail feather and a large beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this bird is black with white on its feathers and has a long, pointy beak
this is a plump dark gray bird with a thick beak that is yellow
this bird has black plumage, with a large head and a large black, curved beak
this bird has a black head and has a short bright orange pointed bill
this is a black bird with a long black tail feather and a large beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with long tail feathers and has a very short beak
this is a white bird with a black wing and a large beak
this bird is black with long tail feathers and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with long tail feathers and has a very short beak
this bird is gray and black in color, with a large black beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this is a black bird with a white eye and a large beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with white on its stomach and a short beak
this bird has smooth brown feathers and a large, long black bill
this is a black bird with a long black tail feather and a large beak
this bird is white and gray in color, with a long curled beak
this bird is black with white on its feathers and has a long, pointy beak
this is a black bird with a long black tail feather and a large beak
this is a white bird with a black wing and a large beak
this bird is black with red on its wing and has a very short beak
this is a black bird with a long black tail feather and a large beak
this bird is black with long tail feathers and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this black bird has a white belly, a white stripe trailing from its eye and a distinctive red beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this is a black bird with a long black tail feather and a large beak
this bird has feathers that are black and has a long yellow bill
the bird has a long black bill that is curved and large
this bird is black with long tail feathers and has a very short beak
this is a white bird with a black wing and a large beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this bird is black with red on its wing and has a very short beak
this is a black bird with a long tail feather and a large black beak
this is a black bird with a white belly and a large orange beak
this bird is black with red on its wing and has a very short beak
this black bird has a white belly, a white stripe trailing from its eye and a distinctive red beak
this is a black bird with a long black tail feather and a large beak
this is a black bird with a long tail feather and a pointy black beak
this black bird has a white belly, a white stripe trailing from its eye and a distinctive red beak
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
