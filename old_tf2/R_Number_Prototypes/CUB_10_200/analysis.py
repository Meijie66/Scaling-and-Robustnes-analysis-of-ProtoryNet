from collections import Counter

text = """
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black back, white eye and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a grey bird with large feet, a white eye and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black back, white eye and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black back, white eye and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black wings and head and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this bird has a grey body with black wings speckled with white dots, and an orange bill
this is a bird with a white belly, black back, white eye and an orange beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
a black bird with an orange beak and a white stripe coming from its white eyes
this is a bird with a white belly, black back, white eye and an orange beak
a black bird with an orange beak and a white stripe coming from its white eyes
a bird with a large beak, grey head with a white belly and dark grey wings
this is a black bird with a white spot on the head and a white breast with an orange beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a grey bird with a white breast and eye and a black beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a bird with a large beak, grey head with a white belly and dark grey wings
this is a bird with a white belly, black back, white eye and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black wings and head and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black back, white eye and an orange beak
this bird has a short, bright orange bill with a long black neck and a white breast and belly
this bird has a short, bright orange bill with a long black neck and a white breast and belly
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black back, white eye and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a black bird with an orange beak and a white stripe coming from its white eyes
a small bird with an orange bill, white belly and breast, and black wings and back
this bird has a grey body with black wings speckled with white dots, and an orange bill
a small bird with an orange bill, white belly and breast, and black wings and back
this bird has a grey body with black wings speckled with white dots, and an orange bill
this is a bird with a white belly, black wings and head and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this bird has a white belly and grey wings and crown with an orange bill
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this bird has a dark brown and white belly with grey feet and dark brown crown
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this bird has a grey body with black wings speckled with white dots, and an orange bill
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a grey bird with a white eye and a large orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this bird has a white breast and belly with grey wings and a grey crown
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
a bird with a large beak, grey head with a white belly and dark grey wings
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a black bird with an orange beak and a white stripe coming from its white eyes
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black back, white eye and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black back, white eye and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this bird has black plumage, with a large orange beak and white stripes on its head
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black back, white eye and an orange beak
this is a bird with a white belly, black back, white eye and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
bird has a short wide orange beak with white eyes, and a plume of feathers arching over the bill
this bird has a grey body with black wings speckled with white dots, and an orange bill
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black wings and head and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black wings and head and an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this bird has a grey body with black wings speckled with white dots, and an orange bill
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a black bird with a white spot on the head and a white breast with an orange beak
a small bird with an orange bill, white belly and breast, and black wings and back
this is a bird with a white belly, black back, white eye and an orange beak
this is a bird with a white belly, black wings and head and an orange beak
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