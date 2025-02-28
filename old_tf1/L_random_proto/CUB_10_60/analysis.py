from collections import Counter

# Input data (your text)
text = """
this bird is small and black with a pointy orange beak
this bird is white and black in color, and has a orange beak
this black and white bird is mostly black with flecks of white on the head, chest, throat and feet
this bird is small and black with a pointy orange beak
a medium bird with gray feathers and a black beak
this is a mostly black bird with a bright orange bill, a gray breast, and webbed feet
a solid black bird with a small head and flat, black beak
this bird is gray and black in color, with a orange beak
this bird is black with an orange, short, stubby beak
this bird is white and black in color with a large black beak curved at the end
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with an orange, short, stubby beak
this is a black bird with a white breast and belly, webbed black feet and a red short beak
this bird is black with grey on its chest and has a very short beak
this bird is small and black with a pointy orange beak
this bird is black with white on its chest and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with an orange, short, stubby beak
this bird is black with an orange, short, stubby beak
this bird is black with a white chest and has a very short beak
this bird has a gray and white belly and a small orange beak
small black bird with a short black beak and bright orange wingbars
this bird is black with an orange, short, stubby beak
this bird is black with grey on its chest and has a very short beak
this bird is black white white on its chest and has a very short beak
this bird is black, white, and gray in color, with a orange and black beak
this bird is black with a white chest and has a very short beak
this bird is mostly gray with a bright orange bill
this bird is black with grey on its chest and has a very short beak
this bird is black with a white chest and has a very short beak
this bird is dark blue and purple with a black beak
this bird is black with an orange, short, stubby beak
medium grey and black bird with medium to long black beak
this bird is black with grey on its chest and has a very short beak
bird with a black body with a thick dark grey beak
this bird is black with an orange, short, stubby beak
a long bodied bird with gray legs, black & white body and a stubby orange beak
the bird had a white and grey speckled chest with a short orange beak
medium to large grey and black bird with long black beak
this bird is small and black with a pointy orange beak
this bird is black and blue in color, with a large stubby and curved beak
this bird is black, white, and gray in color, with a orange and black beak
this bird is black with white on its chest and has a very short beak
this bird is black with grey on its chest and has a very short beak
this bird is black with an orange, short, stubby beak
this bird is completely a color between blue and black, with a small dark purple head
this bird is white and black in color, with a stubby orange and black beak
this bird is black with grey on its chest and has a very short beak
this bird is brown with white on its chest and has a long, pointy beak
this small bird has a white breast and a small orange beak
this bird is black with grey on its chest and has a very short beak
this bird is black witrh blue and has a long, pointy beak
bird with a black body with a thick dark grey beak
this is a black bird with a white breast and belly, webbed black feet and a red short beak
this bird is small and black with a pointy orange beak
this bird has a short, stubby gray beak, and webbed gray feet
this bird is brown with black feet and has a very short beak
this bird is black with an orange, short, stubby beak
this bird is black with grey on its chest and has a very short beak
this bird is black with white on its chest and has a very short beak
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
