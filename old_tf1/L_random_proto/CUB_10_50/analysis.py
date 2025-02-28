from collections import Counter

# Input data (your text)
text = """
this bird is black with long tail feathers and has a very short beak
this bird is mostly black and has a red and white covert
this bird is white and gray in color, with a long curled beak
the bird has a white body with a grey rump and white webbed feet
this bird has a very long neck, white belly, and red short beak
this bird has a white and gray speckled belly and breast with a black eyering and short bill
this bird has a long wingspan, a white belly, and a yellow bill
this bird is black with a white belly, has webbed feet and a red beak
this bird is white with grey on its wings and has a long, pointy beak
this is a black bird with a white breast and belly, webbed black feet and a red short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a very short bright orange beak, a white cheek patch and blueish black webbed feet
this is a black bird with a white breast and belly, webbed black feet and a red short beak
this bird is black and red with a red throat and a black crown
this bird is almost all light gray with a white superciliary and an orange beak
this bird has a white belly and breast with an orange bill and webbed feet
this bird is black with long tail feathers and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a white belly, black back, red beak that curves up and webbed white and gray feet
this bird is black with white on its chest and has a very short beak
this bird has a white belly, black back, red beak that curves up and webbed white and gray feet
this bird is black with white on its stomach and a short beak
this bird is black white white on its chest and has a very short beak
this bird is black with a white belly, has webbed feet and a red beak
this bird is black with a white chest and has a very short beak
this bird has a black head and a gray nape, with a large beak
this is a black bird with a white breast and belly, webbed black feet and a red short beak
this crested black bird has spiky plumage, long tail feathers, and a short, thick gray beak
this bird is black with a white belly, has webbed feet and a red beak
this is a black bird with a white breast and belly, webbed black feet and a red short beak
this bird is black with a white belly, has webbed feet and a red beak
this bird has black winds and a white body with a long curved beak
this bird is black white white on its chest and has a very short beak
this bird is black with long tail feathers and has a very short beak
a red and black beak connects to a dark crown with light eyes peering into the distance
this bird has black plumage, with a large head and a large black, curved beak
this bird has a orange beak, black throat, and a black and white belly
this bird has a white belly and breast with an orange bill and webbed feet
this bird has very long wings and is a water bird with white on its head
this bird is black, white, and gray in color, with a orange and black beak
this bird has very long wings and is a water bird with white on its head
this bird is grey with hwite and has a very short beak
this crested black bird has spiky plumage, long tail feathers, and a short, thick gray beak
this is a black bird with a white breast and belly, webbed black feet and a red short beak
this bird has black winds and a white body with a long curved beak
this bird is black with long tail feathers and has a very short beak
this crested black bird has spiky plumage, long tail feathers, and a short, thick gray beak
this bird is black, white, and gray in color, with a orange and black beak
this bird is brown, white, and red in color, with a sharp black beak
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
