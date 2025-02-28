from collections import Counter

# Input data (your text)
text = """
medium to large grey and black bird with long black beak
this bird is black with a red beak and has a very short beak
this bird is black and gray in color, with a large curved beak
this bird is white and black in color with a large curved beak, and dark eye rings
this bird has black winds and a white body with a long curved beak
this bird is black with grey and has a very short beak
this all-black bird has a long tail and a short black beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has a long black crest and an orange beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has a black head and has a short bright orange pointed bill
this bird has a dark grey crown with a light grey belly and white and black beak
this bird has black plumage, with a large head and a large black, curved beak
this is a large white bird, with dark grey wings, and a curved bill
black head and body, red eyes. wide tail
this mottled white and black bird has white eyes, a white throat, and a stubby dark orange beak
this black bird has a white belly and a small, round beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird is black with white on its stomach and a short beak
this is a grey bird with a white breast and eye and a black beak
this bird has black plumage, with a large orange beak and white stripes on its head
this bird has black plumage, with a large head and a large black, curved beak
this bird has grey black wings, crown and rump, with a short stout beak
this bird is black with red and has a long, pointy beak
a black bird with an orange beak and a white stripe coming from its white eyes
this bird has black plumage, with a large head and a large black, curved beak
this bird has a unique white eye, and a pointed orange beak
this bird has a large beak and is brown with a white ring on its face
this bird has a black head and a gray nape, with a large beak
this bird has black plumage, with a large head and a large black, curved beak
this��bird��has��a��dark��brown��body,��black��wings,��and��a��short,��pointed��bill
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with white on its stomach and a short beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this black bird has a white belly and a small, round beak
this bird has black winds and a white body with a long curved beak
an all black bird with a orange short slightly round bill
this��bird��has��a��dark��brown��body,��black��wings,��and��a��short,��pointed��bill
this bird has black plumage, with a large head and a large black, curved beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this bird is white and gray in color, with a long curled beak
this black bird features a pop of bright orange with its beak and a very pronounced crown feather
a black bird with a long tail and a large gray beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with white on its stomach and has a long, pointy beak
this black and white bird has a white throat, small beak, speckled belly, and white eyering
this bird has black plumage, with a large head and a large black, curved beak
a large white bird with gray wings, a short tail, a long neck, and a long beak with a downward curve
this bird has black plumage, with a large head and a large black, curved beak
this is a black bird with a grey face and a large beak
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
