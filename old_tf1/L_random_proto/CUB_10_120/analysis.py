from collections import Counter

# Input data (your text)
text = """
this bird is black with red on its wing and has a very short beak
this bird is black with white and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is black in color, and has a black beak
this bird is black with white on its chest and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird is black with white and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is black with red on its wing and has a very short beak
this bird is black with white on its chest and has a very short beak
this unique black bird is glossy and features serious, yellow eyes and a long, sharp beak
this bird is black in color, and has a curved and black beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is black with weird eyes and has a very short beak
this bird is black with red and blue and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is black with red on its wing and has a very short beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird is one solid color, black, with black tarus and feet, and bright yellow eyes
this bird is black with white and has a very short beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is black with white and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is black with white and has a very short beak
this bird is one solid color, black, with black tarus and feet, and bright yellow eyes
this bird is black with white on its chest and has a very short beak
this bird is black with white and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is all black with a short beak and buggy yellow and black eyes
this bird is black in color, and has a bright orange beak
this bird is black with white and has a very short beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is black in color, and has a bright orange beak
this bird is black with white on its chest and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with white and has a very short beak
this bird is black in color, and has a bright orange beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white and has a very short beak
this bird is black and orange in color, with a black beak
this bird is black with white and has a very short beak
this bird is brown with black and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird has wings that are black and has a bulky yellow beak
this bird is black with red on its wing and has a very short beak
this bird is black with weird eyes and has a very short beak
this bird is black and orange in color, with a black beak
this bird is black with red on its wing and has a very short beak
this bird is black with grey and has a very short beak
this bird is black with white and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is black in color, and has a curved and black beak
this bird is black in color, and has a curved and black beak
this bird is brown with black feet and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with weird eyes and has a very short beak
this bird is black in color, and has a bright orange beak
this bird is black with red on its wing and has a very short beak
this bird is black with white and has a very short beak
this bird has wings that are black and has an orange bill
this bird is black in color, and has a bright orange beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird is brown with black feet and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is black all over, has a short pointed bill, and bright yellow and red wingbars
this bird is black with white on its chest and has a very short beak
this bird is black and orange in color, with a black beak
this bird is black with white on its chest and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black in color, and has a black beak
this bird has a short beak and is black everywhere
this bird is black with white on its chest and has a very short beak
this bird is black with white and has a very short beak
this bird has wings that are black and has a short bill
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is black with grey on its chest and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with white on its chest and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black in color, and has a bright orange beak
this bird is brown with black feet and has a very short beak
this bird is black with white and has a very short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with weird eyes and has a very short beak
this bird is black in color, and has a curved and black beak
this bird is black and gray in color, and has a bright orange beak
this bird is black with red on its wing and has a very short beak
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is black in color, and has a curved and black beak
this bird is black with white and has a long, pointy beak
this bird is black and orange in color, with a black beak
this bird is black with white and has a very short beak
this bird is black with white and has a very short beak
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
