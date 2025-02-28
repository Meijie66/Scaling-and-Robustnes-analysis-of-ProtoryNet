from collections import Counter

# Input data (your text)
text = """
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a big bill
this bird is white with black and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
the bird is all black, medium length pointed beak, with grey feet
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a long neck
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a short bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a white bill
this bird is all black and has a very short beak
this bird has wings that are brown and has a short bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a short bill
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a big bill
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a big bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly
this bird has wings that are black and white with a short orange beak
this bird is mostly dark grey and has a white ring around its bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a white belly and red bill
this bird has wings that are black and has a grey belly
this bird is black with a big wingspan and has a very short beak
this bird has wings that are black and has a white belly
this bird has wings that are black and white with a short orange beak
this bird has a large beak and has all black feathers
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a white belly and red bill
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a short bill
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a yellow bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are brown and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are brown and has a long black bill
this bird has wings that are grey and has a long black bill
this bird has wings that are black and has a big bill
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a big bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a big bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly
this bird has wings that are grey and has a long black bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a white belly
this bird has wings that are black and white with a short orange beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a short bill
this bird has wings that are black and has a thick bill
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and has a grey belly
this bird has wings that are brown and has a long black bill
this bird is brown with black feet and has a very short beak
this bird is brown in color, and has a black beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a big bill
this bird has wings that are black and has a grey belly
this bird has wings that are grey and has a long black bill
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a white belly and red bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a white bill
this bird is brown with black feet and has a very short beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with short wings and has a long, pointy beak
this bird has wings that are black and has a long neck
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a thick bill
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a short bill
this bird is brown with black feet and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown in color, and has a black beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a small bill
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a short bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a white bill
this bird has wings that are black and white with a short orange beak
this bird is brown in color, and has a black beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a short bill
this bird has wings that are black and has a short bill
this bird has wings that are black and has a white belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a short bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black with a big wingspan and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a yellow bill
this bird has wings that are black and has a short bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly and red bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a red bill
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white bill
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is light brown, and has a long neck and a pointy bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a long neck
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a white belly
this bird has a large beak and has all black feathers
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has a long wingspan, a white belly, and a yellow bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a long neck
this bird has wings that are black and white with a short orange beak
this bird is jet black everywhere and has a medium sized beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are brown and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly and red bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a long neck
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly
this bird is black with white and has a long, pointy beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a short bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a flat bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a long neck
this bird has wings that are black and has a white bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and has a big bill
this bird is mostly dark grey and has a white ring around its bill
this bird is mostly dark grey and has a white ring around its bill
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a white belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird is black with a white chest and has a very short beak
this bird has wings that are black and has a yellow bill
this bird has a large beak and has all black feathers
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a short bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a short bill
this bird has wings that are black and white with a short orange beak
this bird is brown with black and has a long, pointy beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird is brown in color, and has a black beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird has wings that are black and white and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white bill
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a orange bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a white belly
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a white belly
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a short bill
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a small bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a long neck
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a long neck
this bird is brown with black feet and has a very short beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black and red in color, and has a black beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a big bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and has a long black bill
this bird has wings that are grey and has a long black bill
this bird is black in color, and has a curved and black beak
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird has wings that are grey and has a long black bill
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are grey and has a long black bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a white belly
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are grey and has a long black bill
this bird is brown in color, and has a black beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and has a grey belly
this bird has wings that are black and has a grey belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are brown and has a large yellow bill
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black feet and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
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
