from collections import Counter

# Input data (your text)
text = """
'this bird has wings that are black and has a thick bill'
'bird has black body feathers, white breast feather, and short beak'
'this bird is black with white and has a long, pointy beak'
'a large grey bird, with a white head and belly, and a large curved bill'
'this bird has wings that are black and has a white belly'
'this black bird has white eyes and black plumage on top of a bright orange shortened beak'
'this bird has a black crown as well as a small black bill'
'a medium sized bird with black feet and a black breast and belly with a orange and black beak'
'this bird has a large grey head with a orange pointed bill'
'this bird is grey and has a very large wing span with a very long beak'

'this is a black bird with a white eye and a large orange beak'
'this bird is black with white and has a long, pointy beak'
'a small bird with a black and white coloring and short beak'
'this bird has a black crown as well as a small black bill'
'this is a large grey bird with a large grey beak'
'a medium size bird with a short, pointed, orange beak'
'this bird has wings that are black and has a thick bill'
'this bird has a white body and head with black feathers and a long pointy beak'
'a large bird with a white belly, black and white wings with a long beak'
'the bird has a white eyering and a small peach bill'




"""

# Step 1 Split the text into individual sentences
sentences = text.strip().split('\n')

# Step  Count the occurrences of each sentence
sentence_counts = Counter(sentences)

# Step 3 Display unique sentences and their counts
print("Unique Sentences and Their Occurrences")
for sentence, count in sentence_counts.items():
    print(f"'{sentence}' {count} ")

# Step 4 Calculate duplicate counts
total_sentences = len(sentences)
unique_sentences = len(sentence_counts)
duplicates = total_sentences - unique_sentences

print("\nSummary")
print(f"Total Sentences {total_sentences}")
print(f"Unique Sentences {unique_sentences}")
print(f"Duplicated Sentences {duplicates}")
