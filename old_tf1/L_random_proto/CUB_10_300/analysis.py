from collections import Counter

# Input data (your text)
text = """
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has feathers that are black and has a thick black bill
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has feathers that are black and has a thick black bill
this bird is black with white and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a big bill
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has very long wings and is a water bird with white on its head
this bird has feathers that are black and has a thick black bill
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a thick bill
this bird is black with big wings and has a long, pointy beak
this bird has a white body and head with black feathers and a long pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is brown with a white tail and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a white belly and red bill
this bird has wings that are black and has a big bill
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a white bill
this bird has wings that are black and has a long black bill
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with white on its head and tail and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a white bill
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a thick bill
a large brown bird with long wings and a white line around the base of the blunt and black beak
this bird has wings that are black and has a big bill
this bird has feathers that are black and has a thick black bill
this bird is black with white and has a very short beak
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a big bill
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a flat bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with white on its stomach and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has feathers that are black and has a thick black bill
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a flat bill
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this is a white bird with black and white wings and a long and pointy black beak
this bird has wings that are black and has a big bill
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a white bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a big bill
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has feathers that are black and has a thick black bill
this bird has wings that are black and has a white bill
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a spotted belly
this bird has a white belly, black wings and crown, and a small red bill
this bird has wings that are black and has a white bill
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a big bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its chest and head and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird is brown with white on its head and tail and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has black plumage, with a large head and a large black, curved beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has feathers that are black and has a thick black bill
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a long black bill
this bird has very long wings and is a water bird with white on its head
a gray bird with very long wings, a black head, and a white back
this bird is black with big wings and has a long, pointy beak
this bird with white eyerings is a sleek black on its head, body, wings, tail, and bill
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a white bill
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird has a white belly, black wings and crown, and a small red bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is all dark gray
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a big bill
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a white belly and red bill
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a white bill
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a white bill
this bird has wings that are black and has a big bill
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a big bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a long black bill
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this is a black bird with a long black tail wing and a pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird is black with big wings and has a long, pointy beak
this bird has a black shiny body and feathers, a small pointy black bill and bright yellow eyes
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird has smooth brown feathers and a large, long black bill
this bird has wings that are black and has a big bill
this bird is black with big wings and has a long, pointy beak
this bird has very long wings and is a water bird with white on its head
this bird has feathers that are black and has a thick black bill
this bird has wings that are black and has a long black bill
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a big bill
this bird has feathers that are black and has a thick black bill
this bird has very long wings and is a water bird with white on its head
this bird has very long wings and is a water bird with white on its head
this bird has wings that are black and has a grey belly
this bird is black in color with a black beak, and black eye rings
this bird has wings that are black and has a long black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
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
