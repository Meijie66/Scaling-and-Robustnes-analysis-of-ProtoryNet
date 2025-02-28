from collections import Counter

# Input data (your text)
text = """
a black bird with a long tail and a large gray beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is nearly all black with a short pointy bill
this bird is black with a red beak and has a very short beak
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this bird is black with big wings and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has wings that are grey and has a long black bill
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird has very long black wings, with a long black bill
this bird has long black and white wings, with a very long bill
this bird is black with long tail feathers and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this is a large bird with dark grey wings, a white body and a large bill
this bird is black with a red beak and has a very short beak
a black bird with a long tail and a large gray beak
this bird has very long black wings, with a long black bill
this is a black bird with a long black tail feather and a large beak
this bird is black with long tail feathers and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this large bird has a white body, black wing and tail, and long hooked bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
a black bird with a long tail and a large gray beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this is a dark grey bird with a long black beak and white feet
a small black bird with light yellow eyes and a black beak
this bird is black with a red beak and has a very short beak
this bird is black with long tail feathers and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
a black bird with a long tail and a large gray beak
this is a dark grey bird with a long black beak and white feet
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with big wings and has a long, pointy beak
this bird is grey with black and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with a red beak and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this is a dark grey bird with a long black beak and white feet
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is brown with short wings and has a long, pointy beak
this large bird has a white body, grey wing, and long hooked yellow bill
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird is black with a big wingspan and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is grey with long wings and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is grey with black and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is grey with black and has a long, pointy beak
a dark grey bird with white eyes and a very short red beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this is a black bird with a long black tail feather and a large beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this is a black bird with a long black tail wing and a pointy beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has large feet with a shorter beak and a white and black body
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with a red beak and has a very short beak
a black bird with a long tail and a large gray beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
a black bird with a large round beak
a black bird with a long tail and a large gray beak
this is a black bird with a long black tail wing and a pointy beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird is black with a red beak and has a very short beak
this is a grey bird with black feet and a large beak
this bird is black with a red beak and has a very short beak
this is a dark brown bird, with short wings, and a yellow bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has a mostly dark grey body, long neck, and short pointy bill
this bird is black with a red beak and has a very short beak
a large dark brown gray bird with a black beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is brown with short wings and has a long, pointy beak
this bird has very long black wings, with a long black bill
this is a grey bird with black feet and a large beak
this bird has wings that are black and has a long black bill
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird has very long black wings, with a long black bill
this bird has very long black wings, with a long black bill
this bird has very long black wings, with a long black bill
this bird is black with a red beak and has a very short beak
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
