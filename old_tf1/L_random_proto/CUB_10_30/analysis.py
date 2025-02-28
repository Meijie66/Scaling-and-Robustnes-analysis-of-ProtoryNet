from collections import Counter

# Input data (your text)
text = """
this all-black bird has a long tail and a short black beak
this bird is black all over with shiny feathers and a little bit of red on the coverlet
this bird has a short beak and is black everywhere
this is a black bird with a white belly and a white eye
this is a black bird with a long black tail feather and a large beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and has a thick bill
this bird is black with white on its stomach and a short beak
the bird has black secondaries, a red wingbar and black crown
the impressive wingspan on this bird is brown and the body is white. the bill is long
this bird is entirely black, with a rounded beak and lengthy tail feathers
this bird is white with black on its head and has a very short beak
this bird is black and white in color with a sharp black beak and black eye ring
this bird is black and gray in color, with a black beak
this bird is grey and has a very large wing span with a very long beak
this bird has a short beak and is black everywhere
this is a black bird with white stripes and a white throat and eye
this black bird has a sharp beak and white eyering
this bird is all black and has a long, pointy beak
this is a medium sized brown bird, with a long pointed bill
this bird has a short beak and is black everywhere
this bird is white and gray in color, with a long curled beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this bird is entirely black with a long, sharp beak and a broad wingspan
the bird has a black crown and a black breast as well
the bird is black with a long wing span and short beak
the bird has a white eyering, long outer rectrices, black breast and black back
this black bird has a thick, dark beak and sparse, spiked head feathers
a larger black and grey bird with an orange beak
this bird is black and white in color with a orange beak, and white eye rings
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
