from collections import Counter

# Input data (your text)
text = """
this bird is gray and black in color, with a large black beak
a large white bird with black wings and long yellow bill
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird has black plumage, with a large head and a large black, curved beak
this is a large grey bird with a black wing and head and a long and pointy black beak
a large bird with large black and white bill, and black wings
this bird has a black head, a long black bill, and a large wingspan
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird has black plumage, with a large head and a large black, curved beak
a large white bird with black wings and long yellow bill
this bird has a black head, a long black bill, and a large wingspan
this is a large grey bird with a black wing and head and a long and pointy black beak
this is a white bird with a black wing and a large beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird is black with big wings and has a long, pointy beak
a large white bird with black wings and long yellow bill
this bird has a black head, a long black bill, and a large wingspan
this is a large grey bird with a black wing and head and a long and pointy black beak
a long black bird with a stubby black beak and a medium sized neck
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird is gray and black in color, with a large black beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird has a black head, a long black bill, and a large wingspan
this bird has black plumage, with a large head and a large black, curved beak
this is a white bird with a black wing and a large beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
a large white bird with black wings and long yellow bill
a large white bird with black wings and long yellow bill
a large white bird with black wings and long yellow bill
this is a white bird with a black wing and a large beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird has black plumage, with a large head and a large black, curved beak
a black bird with a long tail and a large gray beak
this bird has wings that are black and has a long black bill
this bird has a black head, a long black bill, and a large wingspan
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has a black head, a long black bill, and a large wingspan
this bird has a black head, a long black bill, and a large wingspan
this bird has a black head, a long black bill, and a large wingspan
this is a large grey bird with a black wing and head and a long and pointy black beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird has a black head, a long black bill, and a large wingspan
a black bird with a long tail and a large gray beak
this bird has black plumage, with a large head and a large black, curved beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird is black with white and has a very short beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird has a black head, a long black bill, and a large wingspan
this bird has a black head, a long black bill, and a large wingspan
a large white bird with black wings and long yellow bill
this bird has black plumage, with a large head and a large black, curved beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird is black with red and has a very short beak
this bird is black with white and has a very short beak
this is a large grey bird with a black wing and head and a long and pointy black beak
a black bird with a long tail and a large gray beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this is a large grey bird with a black wing and head and a long and pointy black beak
a long black bird with a stubby black beak and a medium sized neck
this bird has black plumage, with a large head and a large black, curved beak
a large white bird with black wings and long yellow bill
this bird has black plumage, with a large head and a large black, curved beak
a black bird with a long tail and a large gray beak
this bird has a black head, a long black bill, and a large wingspan
this bird has black plumage, with a large head and a large black, curved beak
this bird has a black head, a long black bill, and a large wingspan
this bird is black with white and has a very short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has a black head, a long black bill, and a large wingspan
this bird has wings that are grey and has a long black bill
this is a large bird with dark grey wings, a white body and a large bill
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird has a black head, a long black bill, and a large wingspan
this is a large grey bird with a black wing and head and a long and pointy black beak
this is a grey bird with a black head and a large black beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird is black with white and has a very short beak
this bird has a black head, a long black bill, and a large wingspan
this bird has a black head, a long black bill, and a large wingspan
this bird has a black head, a long black bill, and a large wingspan
this bird has a black head, a long black bill, and a large wingspan
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with white and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this is a large grey bird with a black wing and head and a long and pointy black beak
a long black bird with a stubby black beak and a medium sized neck
this bird has a black head, a long black bill, and a large wingspan
this bird has a black head, a long black bill, and a large wingspan
a long black bird with a stubby black beak and a medium sized neck
a large white bird with black wings and long yellow bill
this bird has a black head, a long black bill, and a large wingspan
a long black bird with a stubby black beak and a medium sized neck
this bird has wings that are grey and has a long black bill
this bird has black plumage, with a large head and a large black, curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has wings that are black and has a long black bill
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
