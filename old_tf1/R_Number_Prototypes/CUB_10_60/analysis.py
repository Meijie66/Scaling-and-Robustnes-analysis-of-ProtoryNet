from collections import Counter

# Input data (your text)
text = """
this bird is black with a red beak and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is black with a red beak and has a very short beak
this bird is small and black with a pointy orange beak
this bird has wings that are black and white with a short orange beak
this bird is black with grey and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird is black with white and has a long, pointy beak
this bird is brown with white and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with red and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with red on its wing and has a very short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a very short beak
this bird is white with black and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with a red beak and has a very short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with red and has a very short beak
this bird is black with a red beak and has a very short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a orange beak, black throat, and a black and white belly
this bird is brown with red and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is black with a red beak and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird has wings that are black and has a yellow bill
this bird is black with red on its wing and has a very short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with red and has a very short beak
this bird is small and black with a pointy orange beak
this bird is black with white and has a long, pointy beak
this bird is small and black with a pointy orange beak
this bird is black with white and has a very short beak
this bird is grey with black and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird is black with red and has a very short beak
this bird is small and black with a pointy orange beak
this bird is black with a red beak and has a very short beak
this bird is grey and has a very large wing span with a very long beak
this bird is black with a red beak and has a very short beak
this bird is black in color, and has a black beak
this bird is black with white on its stomach and a short beak
this bird is black with red on its wing and has a very short beak
this bird is black with white and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird is black in color, and has a bright orange beak
this bird is black with a red beak and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird has wings that are black and has a white belly and red bill
this bird is black with red on its wing and has a very short beak
this bird has wings that are grey and has a long black bill
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
