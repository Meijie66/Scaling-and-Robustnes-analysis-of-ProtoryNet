from collections import Counter

# Input data (your text)
text = """
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this mottled white and black bird has white eyes, a white throat, and a stubby dark orange beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this is a black bird with a white eye and a large orange beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this is a white bird with a black wing and a large beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this is a white bird with a black wing and a large beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is white and black in color, with a large white beak
this bird is black with white and has a very short beak
this bird is black with white and has a very short beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is black and red in color, and has a black beak
this bird is black with white and has a very short beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird has a white chest, black wings and small curved orange beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is grey with white and has a long, pointy beak
this bird is black with white on its stomach and a short beak
this bird is white and black in color, with a large white beak
this is a white bird with a black wing and a large beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this is a bird with a white belly, black back, white eye and an orange beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, and has a orange beak
this is a bird with a white belly, black back, white eye and an orange beak
this bird is brown in color, and has a black beak
this is a white bird with a black wing and a large beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
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