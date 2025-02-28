from collections import Counter

# Input data (your text)
text = """
this bird is white with black on its head and has a very short beak
this bird has a black head and a gray nape, with a large beak
this is a black bird with a large black beak
this bird has a black head and a gray nape, with a large beak
this is a black and blue bird with a white eye and a pointed beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and a gray nape, with a large beak
this bird is black with green and has a long, pointy beak
this bird has a orange and black bill and a white breast
this bird has a orange and black bill and a white breast
this bird has a short, rounded bill, and a dark brown head
this bird has a black head and a gray nape, with a large beak
this bird has a white belly, black head and back with a short orange bill
this bird is black and gray in color, with a large curved beak
this bird is completely black with a bright yellow eye
this bird is black with green and has a long, pointy beak
this bird has a black head and a gray nape, with a large beak
this is a black bird with a white eye and a large beak
this bird has a black head and a gray nape, with a large beak
this bird has a short, rounded bill, and a dark brown head
this bird is black and gray in color, with a large curved beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a white belly, black head and back with a short orange bill
this bird has a black head and a gray nape, with a large beak
this bird has a black head and back, with gray wings, tail, and beak
this is a black bird with a gray bill with a orange and white on the wingbar
this bird has a pointed black and white bill, with a black breast
this bird has a black head and a gray nape, with a large beak
this bird has a white head and a big orange bill
this bird is black and gray in color, with a large curved beak
this bird is white and brown in color with a curved orange beak and white eye ring
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this is a black and blue bird with a white eye and a pointed beak
this grey bird has white on his wingtips when in flight and a darker gray curved beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has a black head and a gray nape, with a large beak
this bird has a long black bill and a brown body
this black bird has a large set of eyes and a long, curving beak
this bird is black with white on its chest and head and has a long, pointy beak
this black bird has a large set of eyes and a long, curving beak
this bird has a black head and back, with gray wings, tail, and beak
this bird has a black head and a gray nape, with a large beak
this is a black bird with a gray bill with a orange and white on the wingbar
this bird is black with white on its chest and head and has a long, pointy beak
this bird is black with green eyes and has a long, pointy beak
this black colored bird has a bright orange beak and white eyes
this bird is black and gray in color, with a large curved beak
this bird has a short, rounded bill, and a dark brown head
this bird is grey with white and has a long, pointy beak
this bird has a black head and a gray nape, with a large beak
this is a black bird with a white eye and a large beak
this is a black bird with a large black beak
duck with brown body brown head
this bird has a black head and a gray nape, with a large beak
this bird has black wings and a solid black head
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird has a short, rounded bill, and a dark brown head
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
