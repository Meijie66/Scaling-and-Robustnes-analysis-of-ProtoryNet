from collections import Counter

# Input data (your text)
text = """
this is a black bird that has red and yellow coverts
small black bird with a short beak and long tail feathers
this is a large black bird with a long and pointy black beak
a medium sized brown bird with long wings and a long beak
this bird has wings that are black and has a white belly
this��bird��has��a��dark��brown��body,��black��wings,��and��a��short,��pointed��bill
a small black bird, with a long tarsus, and a sharp bill
the bird has a black bill that is small and a black eyering
the bird has a bright orange bill and light blue eyering
this bird is brown with a long wingspan and has a very short beak
this��bird��has��a��dark��brown��body,��black��wings,��and��a��short,��pointed��bill
a small bird with an all black body, a short curved bill, and long tail feathers
this is a black bird with long tail feathers and a sharp bill
this bird has a curved, thick bill with starkly black feathers
this bird has wings that are black and has a patch of red
this is a brown bird with a white eyering and a long downward pointing beak
this all-black bird has a long tail and a short black beak
this bird is grey and has a very large wing span with a very long beak
a medium sized bird, with black spots on a white belly, a black head and back, and has webbed feet
a dark black bird with long tail feather and a short pointed beak
this bird is brown with a long wingspan and has a very short beak
this small bird has a curved beak and a very long tail
the bird has a black eyering, short throat and a small bill
this bird is brown with a long wingspan and has a very short beak
this bird has a white body, a long wingspan, and a short orange bill
this is a medium sized black bird, with a white belly, and webbed feet
the bird had a white and grey speckled chest with a short orange beak
this all-black bird has a long tail and a short black beak
this particular bird has a white belly with gray spots and white eye rings
this bird has a long pointed beak with a wide wingspan
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
