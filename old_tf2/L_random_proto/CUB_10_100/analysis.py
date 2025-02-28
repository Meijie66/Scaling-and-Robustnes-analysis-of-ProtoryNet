
from collections import Counter
text = """
this bird has a black head and back, with gray wings, tail, and beak
a black bird with a long tail and a large gray beak
this bird has a long beak with a black and white body
a bird with an orange beak, black head and neck with black wings
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and a gray nape, with a large beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
a dark black and grey feathered bird with a bright beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and a gray nape, with a large beak
a black bird with a long tail and a large gray beak
this bird has a black head and back, with gray wings, tail, and beak
a black and white bird with a short blunt orange beak
a dark black and grey feathered bird with a bright beak
this bird has a black head and back, with gray wings, tail, and beak
a nearly all black bird with a hit of orange on its wing, and a short white beak
this bird has a black head and back, with gray wings, tail, and beak
black bird with a short pointed back beak and long black tail feathers
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
a grey bird with a black back and a small white beak
a black bird with a long tail and a large gray beak
this bird with white eyerings is a sleek black on its head, body, wings, tail, and bill
a dark grey bird with wiry feathers and a curved beak
a black bird with a long tail and a large gray beak
this bird has a black head and back, with gray wings, tail, and beak
the bird is grey with a black head and a black beak with a small eye
a black bird with a long tail and a large gray beak
a grey bird with a black back and a small white beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
a black bird with a long tail and a large gray beak
this bird has large black wings and a white underbelly as well as a medium sized beak
a grey bird with a black back and a small white beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and a gray nape, with a large beak
a grey bird with a black back and a small white beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
a black bird with a long tail and a large gray beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this is a black bird with a large white beak
a black bird with a sharp black beak and red and white on its wingbars
this bird is white with black on its head and has a very short beak
this bird has a black head and a gray nape, with a large beak
a dark black and grey feathered bird with a bright beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
a black bird with a long tail and a large gray beak
this is a black bird with a large white beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and a gray nape, with a large beak
this bird has a black head and back, with gray wings, tail, and beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
a black bird with a long tail and a large gray beak
a dark black and grey feathered bird with a bright beak
this bird has a black head and back, with gray wings, tail, and beak
this is a small grey bird with a large curved beak
a grayish black bird with white eyes and orange stubby beak that has a tuft of gray feathers on it
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
a grayish black bird with white eyes and orange stubby beak that has a tuft of gray feathers on it
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
a large bird with a white belly, black and white wings with a long beak
light gray bird with a large wingspan tinged with white that has a black face and beak
small black bird with long tail feathers and a short beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has a long beak with a black and white body
this bird has a black head and back, with gray wings, tail, and beak
a black bird with a long tail and a large gray beak
a grayish black bird with white eyes and orange stubby beak that has a tuft of gray feathers on it
this bird has a black head and back, with gray wings, tail, and beak
a black bird with a long tail and a large gray beak
a dark black and grey feathered bird with a bright beak
a grey bird with a black back and a small white beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a long beak with a black and white body
this bird has black plumage, with a large head and a large black, curved beak
this bird has a black head and back, with gray wings, tail, and beak
a grey bird with a black back and a small white beak
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