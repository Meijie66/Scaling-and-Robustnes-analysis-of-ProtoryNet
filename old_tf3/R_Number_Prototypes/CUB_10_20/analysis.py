from collections import Counter

# Input data (your text)
text = """
this is a black bird with a white eye and an orange beak
this bird is black with red and has a long, pointy beak
this bird has a white belly and breast with a black wing and crown
this bird is brown with a black back and has a long, pointy beak
this bird has a large and slightly curved brown beak and broad brown wings
this bird is black with a red beak and has a very short beak
this bird has wings that are black and has a thick bill
this bird has a white body and head with black feathers and a long pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are grey and has a long black bill
this bird is brown with black and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird has a black crown as well as a small black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are grey and has a yellow bill
this bird is grey with white and has a long, pointy beak
this bird has a white belly and grey wings and crown with an orange bill
this bird is black with white and has a very short beak
this bird is black with grey and has a long, pointy beak
this bird has a white belly and breast with a black wing and crown
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
