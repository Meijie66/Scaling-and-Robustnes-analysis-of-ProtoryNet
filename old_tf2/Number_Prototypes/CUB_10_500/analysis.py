from collections import Counter

# Input data (your text)
text = """
this bird is black with red and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird has wings that are black and has a white bill
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is brown with black and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with red on its wing and has a very short beak
this bird is all black and has a long, pointy beak
this bird is all black and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and has a thick bill
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with grey and has a long, pointy beak
this bird is brown with black and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black and has a thick bill
this bird is black with a large, wide beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and has a big bill
this bird is white with black and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a very short beak
this bird is black with white and has a very short beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is black with white and has a very short beak
this bird is black with a large, wide beak
this bird is all black and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with white on its chest and has a very short beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is white with black on its head and has a very short beak
this bird is black with white and has a long, pointy beak
this bird is black with a large, wide beak
this bird has wings that are black and has a thick bill
this bird has wings that are black with a short black beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a very short beak
this bird is black with red and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird has wings that are black and has a thick bill
this bird has wings that are black with a short black beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with red and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with white and has a long, pointy beak
this bird is brown with black and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with white and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long bill
this bird has wings that are black and white and has a long bill
this bird has wings that are black and has a long black bill
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with red and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with red and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with big wings and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white with black and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is all black and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with grey and has a very short beak
this bird is black with grey and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is white with black on its head and has a very short beak
this bird is black with white and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with white and has a very short beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with red and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with red and has a long, pointy beak
this bird is black with a large, wide beak
this bird has wings that are black and has a thick bill
this bird is black with a large, wide beak
this bird has wings that are black and has a orange bill
this bird is black with grey and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black and has a thick bill
this bird is black with white and has a very short beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is all black and has a long, pointy beak
this bird has wings that are black and has an orange bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird has wings that are black and has a thick bill
this bird is black with a large, wide beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a very short beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and has a orange bill
this bird is black with a large, wide beak
this bird has wings that are black and has a thick bill
this bird is black with white and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is brown with black and has a long, pointy beak
this bird is white with black and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black and has an orange bill
this bird is black with white and has a very short beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is brown with black and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird has wings that are black and has an orange bill
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird is brown with black and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with grey and has a very short beak
this bird has wings that are black and has a long bill
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird has wings that are black and white with a short orange beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird is black with a large, wide beak
this bird is brown with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with big wings and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird has wings that are black and has a thick bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird has wings that are black and white with a short orange beak
this bird is black with a large, wide beak
this bird has wings that are black and has a long bill
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black and has a long, pointy beak
this bird is white with black and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with white and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird has wings that are black with a short black beak
this bird is brown with black and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird has wings that are black and has a long black bill
this bird has wings that are black with a short black beak
this bird is black with grey and has a long, pointy beak
this bird is all black and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird is black with grey and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a thick bill
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with big wings and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird has wings that are black and has a orange bill
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird has wings that are black and has a orange bill
this bird is black with grey and has a long, pointy beak
this bird is black with grey and has a very short beak
this bird has wings that are black and has a long bill
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird is black with a large, wide beak
this bird is black with red and has a long, pointy beak
this bird is black with a large, wide beak
this bird has wings that are black and has a long black bill
this bird is black with an orange, short, stubby beak
this bird is black with red and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black and has a thick bill
this bird is black with white on its chest and has a very short beak
this bird is white with black and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with white and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with white and has a very short beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird has wings that are black and has a thick bill
this bird is all black and has a very short beak
this bird is black with white and has a very short beak
this bird is black with red and has a long, pointy beak
this bird has wings that are black and has an orange bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a long tail and has a very short beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with grey and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird has wings that are black and has an orange bill
this bird is all black and has a very short beak
this bird is black with a large, wide beak
this bird has wings that are black and has a orange bill
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird has wings that are black and has a thick bill
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird has wings that are black with a short black beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird has wings that are black and white with a short orange beak
this bird is all black and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are black and has a thick bill
this bird is all black and has a very short beak
this bird is black with a large, wide beak
this bird is black with a long tail and has a very short beak
this bird is brown with black and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black with an orange beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is all black and has a very short beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird has wings that are black and has an orange bill
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and has a thick bill
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and has a orange bill
this bird is black with big wings and has a long, pointy beak
this bird is brown with white and has a very short beak
this bird has wings that are black with a long orange beak
this bird is black with a large, wide beak
this bird is black with grey and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with white and has a very short beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and has a thick bill
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has an orange bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird is black with a large, wide beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a very short beak
this bird is black with a large, wide beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird has wings that are black with a short black beak
this bird is black with a large, wide beak
this bird has wings that are black with an orange beak
this bird is completely black and has a very short beak
this bird has wings that are black with a short black beak
this bird has wings that are black and has a thick bill
this bird is black with white and has a very short beak
this bird has wings that are black with a short black beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird has wings that are black with a short black beak
this bird is black, and red in color, with a black beak
this bird is completely black and has a very short beak
this bird is black with a large, wide beak
this bird has wings that are black with a short black beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with a large, wide beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird has wings that are black and has a thick bill
this bird is black with white and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and has a thick bill
this bird is black, and red in color, with a black beak
this bird is black with a large, wide beak
this bird is brown with white and has a very short beak
this bird is black with grey and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is brown with black and has a long, pointy beak
this bird has wings that are white and has a long bill
this bird is black with white and has a very short beak
this bird has wings that are black and has an orange bill
this bird is black with a large, wide beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with white and has a very short beak
this bird is black with grey and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with white and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with white and has a very short beak
this bird is black with white and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a large, wide beak
this bird has wings that are black with an orange beak
this is a large grey bird with a black face and beak
this is a large grey bird with a black face and beak
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
