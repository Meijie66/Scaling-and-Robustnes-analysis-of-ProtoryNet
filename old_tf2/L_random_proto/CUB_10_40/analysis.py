from collections import Counter

# Input data (your text)
text = """
a small bird has a short neck with a black breast, a black crown, and black secondaries
bird has black body feathers, black breast feather, and pointed beak
this is a black bird with a white belly and a red beka
this is a dark black bird with a white breast and a short, squat bright orange bill
the bird had a white and grey speckled chest with a short orange beak
this bird is mostly grey with a short bright orange bill
this bird has a black crown as well as a black belly
this is a brown bird with a short white tail and a large brown beak
this is a dark black bird with a white breast and a short, squat bright orange bill
the bird has a white eyering and white breast, belly, abdomen area but with a lot of black patches
a larger bird with a white belly and breast, a longer wingspan, and a long, narrow bill
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this bird is black it has a very large beak it looks to be a large bird
this bird has smooth brown body, with a black bill and a white eyering
this bird is mostly grey with webbed feet, and blunt orange bill
this bird is brown with a long wingspan and has a very short beak
this is a dark black bird with a white breast and a short, squat bright orange bill
this is a bird with a white breast, black back and a large pointed beak
this bird is mostly gray with a long hooked black bill
this bird has a black head, orange beak, and white breast and belly
this bird has a grey body with black wings speckled with white dots, and an orange bill
this gull is a muddy brown in color, with a long, thick, hooked brown beak and white rectrices
this is a dark black bird with a white breast and a short, squat bright orange bill
this is a black bird with a thick orange beak that has a white piece at the base of it
this bird has a black overall color, with the exception of its eyering, feet and base of the bill
this large bird has a large bill and is light brown to tan in color with darker primaries
this bird has smooth brown feathers and a large, long black bill
this is a bird with a white belly, black back and a black head
this bird is white and black in color with a long dull ended beak and black eye rings
this bird is a very dark blue with a black head and beak, while it's eyes are white
this bird has a blunt orange beak with mostly black above the neck, the belly is solid white
an exotic looking brown bird with a white highlight on its face and orange beak
this is a black bird with a white belly and a red beka
a bird with a brown bill, white eyering, and brown secondaries
this bird has a black head and body with a white belly
this is a dark black bird with a white breast and a short, squat bright orange bill
this is a brown and black bird with a brown bill and a white side
this is a black bird with a white belly and a white eye
this is a dark black bird with a white breast and a short, squat bright orange bill
this is a dark black bird with a white breast and a short, squat bright orange bill
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
