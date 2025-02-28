from collections import Counter

# Input data (your text)
text = """
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black, and red in color, with a black beak
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird is black with red and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this is a grey bird with black feet and a large beak
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is completely black, except for two adjacent wingbars -- one red, and one yellow
this bird is gray and black in color, with a large black beak
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is grey with black and has a long, pointy beak
this��bird��has��a��dark��brown��body,��black��wings,��and��a��short,��pointed��bill
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
a small bird covered in black feathers except for the small bit of red and orange on its coverts
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is gray and black in color, with a large black beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is gray and black in color, with a large black beak
this bird is grey with black and has a long, pointy beak
this bird is grey with white and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is grey with black and has a long, pointy beak
this bird is gray and black in color, with a large black beak
this bird is gray and black in color, with a large black beak
a bird with a large triangular bill, black covering its body except for the red on its coverts
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
