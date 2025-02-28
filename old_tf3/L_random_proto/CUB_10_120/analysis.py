from collections import Counter

# Input data (your text)
text = """
this bird is large with a white head and chest and brown wings and an orange beak
this bird is black, white, and gray in color, with a orange and black beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird has a white chest, black wings and small curved orange beak
this black bird has a white belly and a small, round beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has wings that are black and white and has a long bill
this is a grey bird with black wings and an orange beak
the bird is black with a white eye and black beak and grey tarsals and feet
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird is white and black in color, and has a orange beak
this is a white bird with a black back and head and an orange beak
this bird is black with white on its stomach and a short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird is large with a white head and chest and brown wings and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird is large with a white head and chest and brown wings and an orange beak
this bird is black, white, and gray in color, with a orange and black beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is black with white on its chest and has a very short beak
this bird is white and black in color, with a large white beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird is large with a white head and chest and brown wings and an orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is large with a white head and chest and brown wings and an orange beak
this bird has wings that are black and white with a short orange beak
this is a white bird with black wings and an orange beak
this bird has wings that are black and white with a short orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird is black, white, and gray in color, with a orange and black beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird has a white chest, black wings and small curved orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird is large with a white head and chest and brown wings and an orange beak
this is a white bird with black wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white chest, black wings and small curved orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are white and has a long bill
this bird is black with a white chest and has a very short beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and has a big bill
this bird has a white chest, black wings and small curved orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has wings that are black and white with a small orange beak
this bird has a white chest, black wings and small curved orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a white crown, yellow beak and brown wings
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a long yellow bill and a white crown and breast with black wings
this bird is large with a white head and chest and brown wings and an orange beak
this bird is black with a white chest and has a very short beak
this is a white bird with black wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is large with a white head and chest and brown wings and an orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black white white on its chest and has a very short beak
this bird is black with a white chest and has a very short beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird is large with a white head and chest and brown wings and an orange beak
this bird has wings that are black and white with a short orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has a white body and head with black feathers and a long pointy beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird is black with a white chest and has a very short beak
this bird has a white head and body, brown wings and a somewhat long, pink beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird has a white body, brown wings and an orange beak
this bird has a black back, wings and head, with a white belly and speckled nape
this bird is black with a white chest and has a very short beak
this bird is black with a white chest and has a very short beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
the bird has a white head and rump with grey body and wings
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird has a white chest, black wings and small curved orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white and gray in color, and has a bright orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is white and black in color, and has a orange beak
this is a white bird with black and white wings and a long and pointy black beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is large with a white head and chest and brown wings and an orange beak
this bird has a white belly and breast, black wings and head, and a white striped superciliary
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
