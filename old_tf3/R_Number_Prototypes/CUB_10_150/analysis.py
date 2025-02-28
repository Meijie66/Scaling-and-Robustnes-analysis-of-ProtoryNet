from collections import Counter

# Input data (your text)
text = """
this is a black bird with a white belly and a large orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird has brown wings and a white head with an orange beak
this bird is white and brown in color, with a stubby beak
this bird has wings that are black and has a big bill
this bird has a orange beak, black throat, and a black and white belly
this bird has a white chest, black wings and small curved orange beak
this bird is white and black in color, with a large white beak
this bird has a white body, brown wings and an orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is white and black in color, with a large white beak
this bird has a white body, brown wings and an orange beak
this bird is white and black in color, with a large white beak
this bird is brown with some white and has a long, pointy beak
this is a black bird with a white belly and a large orange beak
this is a black bird with a white belly and a large orange beak
this bird is brown with some white and has a long, pointy beak
this bird has a orange beak, black throat, and a black and white belly
this bird has a white chest, black wings and small curved orange beak
this is a black bird with a white belly and a large orange beak
this bird has wings that are black and white with a short orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird has brown wings and a white head with an orange beak
this is a black bird with a white belly and a large orange beak
this bird has wings that are black and white with a short orange beak
this bird is black with white on its stomach and a short beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white body, brown wings and an orange beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with white on its stomach and a short beak
this bird has a white body, brown wings and an orange beak
this bird has a white body, brown wings and an orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and black in color, with a large white beak
this bird has a orange beak, black throat, and a black and white belly
this bird is brown with white and has a long, pointy beak
this is a black bird with a white belly and a large orange beak
this bird has wings that are black and white with a short orange beak
this is a black bird with a white belly and a large orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with white on its stomach and a short beak
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and brown in color, with a stubby beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white body, brown wings and an orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and brown in color, with a stubby beak
this bird is black with white on its stomach and a short beak
this bird is white and black in color, with a large white beak
this bird is white and brown in color, with a stubby beak
this bird has wings that are black and white with a short orange beak
this bird has a white chest, black wings and small curved orange beak
this is a black bird with a white belly and a large orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with white on its stomach and a short beak
this is a black bird with a white belly and a large orange beak
this bird has wings that are black and white with a short orange beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is brown with white and has a long, pointy beak
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird has wings that are black and has a big bill
this bird is white and black in color, with a large white beak
this bird has a white body, brown wings and an orange beak
this bird is white and brown in color, with a stubby beak
this bird is white and brown in color, with a stubby beak
this bird has wings that are black and white with a short orange beak
this bird has an all black body with a large orange beak and a white eye
this bird has a white chest, black wings and small curved orange beak
this bird is brown with some white and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and black in color, with a large white beak
this bird has a white chest, black wings and small curved orange beak
this bird is white and brown in color, with a stubby beak
this bird has a white body, brown wings and an orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird is brown with white and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this is a black bird with a white belly and a large orange beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has a white body, brown wings and an orange beak
this bird has wings that are black and white with a short orange beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this is a black bird with a white belly and a large orange beak
this bird has wings that are brown and has a long bill
this bird has a orange beak, black throat, and a black and white belly
this is a black bird with a white belly and a large orange beak
this bird is black with white on its stomach and a short beak
this bird is white and brown in color, with a stubby beak
this bird is white and black in color, with a large white beak
this bird has wings that are black and white with a small orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird is brown with some white and has a long, pointy beak
this bird is brown with some white and has a long, pointy beak
this bird is white and black in color, with a large white beak
this is a black bird with a white belly and a large orange beak
this bird has wings that are brown and has a long bill
this bird has a white body, brown wings and an orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is brown with some white and has a long, pointy beak
this bird has a orange beak, black throat, and a black and white belly
this is a black bird with a white belly and a large orange beak
this bird has a white body, brown wings and an orange beak
this bird has wings that are black and white with a short orange beak
this is a black bird with a white belly and a large orange beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird is white and black in color, with a large white beak
this bird has a orange beak, black throat, and a black and white belly
this bird has a white body, brown wings and an orange beak
this bird is white and black in color, with a large white beak
this bird has wings that are black and white with a short orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and black in color, with a large white beak
this is a black bird with a white belly and a large orange beak
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird is white and black in color, with a large white beak
this bird has a white chest, black wings and small curved orange beak
this bird has a white body, brown wings and an orange beak
this is a black bird with a white belly and a large orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is white and black in color, with a large white beak
this bird is black with white on its stomach and a short beak
this bird has a white chest, black wings and small curved orange beak
this bird is white and brown in color, with a stubby beak
this bird is white and brown in color, with a stubby beak
this bird is brown with some white and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has a orange beak, black throat, and a black and white belly
this bird has a white body and head with black feathers and a long pointy beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and brown in color, with a stubby beak
this bird is white and black in color, with a large white beak
this bird has a white body, brown wings and an orange beak
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird is white and black in color, with a large white beak
this bird is brown with some white and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this is a black bird with a white belly and a large orange beak
this bird is white and brown in color, with a stubby beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has a white body, brown wings and an orange beak
this bird has black plumage, with a large head and a large black, curved beak
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
