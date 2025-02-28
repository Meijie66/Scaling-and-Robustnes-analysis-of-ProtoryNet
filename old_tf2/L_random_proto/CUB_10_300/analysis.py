from collections import Counter

# Input data (your text)
text = """
this bird is primarily black with an orange marking on its wing and a short beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with red on its wing and has a very short beak
this bird is primarily black with an orange marking on its wing and a short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is white with grey on its wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has wings that are gray and has a big black bill
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
a black bird with a long pointy beak and wings with one orange and one yellow wingbar
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with a red beak and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with a big wingspan and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are gray and has a big black bill
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with a red beak and has a very short beak
this bird has wings that are black and white with a small orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this is a white bird with a black wing and a large beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with a red beak and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird is grey with long wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has wings that are black and white with a short orange beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is large with a white head and chest and brown wings and an orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with red on its wing and has a very short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has wings that are black and white with a short orange beak
this bird is black with a red beak and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has a black head and rectrices with white in its wings, a yellow ey, and a pointed beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with white and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird is black with red on its wing and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has wings that are black and white with a short orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with white and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has a grey body with black wings speckled with white dots, and an orange bill
this bird is large with a white head and chest and brown wings and an orange beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with a red beak and has a very short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has wings that are black and white with a short orange beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is black with red on its wing and has a very short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is white with grey on its wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
a brown and white speckled bird with a long neck and a short beak
this bird has wings that are black and white with a short orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are brown and has a short bill
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is black with big wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with a red beak and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
a black bird with a short orange beak, a white eye, and a black feather on the top of its head
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are gray and has a big black bill
this bird is black with big wings and has a long, pointy beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black with big wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are gray and has an orange bill
this is a gray bird that has a white eye, and a bright red short beak
this bird has wings that are black and white with a short orange beak
this bird is black with white on its chest and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has wings that are black and white with a small orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
a brown and white speckled bird with a long neck and a short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has black plumage, with a large head and a large black, curved beak
this bird is black with a red beak and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird has wings that are black and white with a short orange beak
this bird is black with a red beak and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a short orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is white with grey on its wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is brown with short wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird has wings that are black and white with a short orange beak
this bird is black with a red beak and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has black plumage and yellow eyes, with a long and flat beak
this bird is grey with long wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
a black bird with a red circle on its wing and a sharp thin beak
this bird is black with big wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with a red beak and has a very short beak
this bird is primarily black with an orange marking on its wing and a short beak
this is a gray bird that has a white eye, and a bright red short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is black with a red beak and has a very short beak
this bird is black with small eyes and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with red on its wing and has a very short beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with white and has a long, pointy beak
this bird has wings that are gray and has a big black bill
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are grey and has a white belly
this bird has wings that are gray and has a big black bill
this bird is primarily black with an orange marking on its wing and a short beak
this bird has black plumage, with a large head and a large black, curved beak
this bird has wings that are black and white with a short orange beak
this bird has wings that are black and white with a short orange beak
this bird is black with red on its wing and has a very short beak
this bird is primarily black with an orange marking on its wing and a short beak
this bird is black with red on its wing and has a very short beak

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
