from collections import Counter

# Input data (your text)
text = """
a medium sized bird with a bill that curves downward, with a brown body
a bird with an orange thick bill and a black coat with white at its throat
this bird has a medium black bill, black tarsuses and feet, and a dark blue crown
a medium sized bird with a bill that curves downward, with a brown body
a bird with an orange beak, black head and neck with black wings
the bird has a black body with a white chest and grey webbed feet
a bird with a large triangular bill, black covering its body except for the red on its coverts
a white and black bird with black eyes sitting on the ground
a bird with a large triangular bill, black covering its body except for the red on its coverts
a bird with a very large downward hooked triangular bill and ruffled black covering its body
a bird with a very large downward hooked triangular bill and ruffled black covering its body
medium to large grey and black bird with long black beak
the bird has a puffy black belly and black back
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is all black, with black webbed feet, a black plume, and orange beak
this large bird has a grey body, black crown, and long hooked bill
this bird is all black, with black webbed feet, a black plume, and orange beak
the bird spreads its wings while gliding over the surface of the water
a bird with an all black body with bright red coverts, and black tarsus
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black with red and has a long, pointy beak
a bird with a large triangular bill, black covering its body except for the red on its coverts
a bird with a very large downward hooked triangular bill and ruffled black covering its body
a bird with a very large downward hooked triangular bill and ruffled black covering its body
this bird is grey with long wings and has a long, pointy beak
a medium sized bird that has a shiny coat with a medium sized bill
a bird with a very large downward hooked triangular bill and ruffled black covering its body
the bird entire body is black and eyes are yellow
this bird has black eye with brown color body and black feet
a medium bird with with black crown and black throat with grey breast and side and orange bill
a large bird with a black head and rump and grey body
the bird has a puffy black belly and black back
this bird is all black, with black webbed feet, a black plume, and orange beak
the birds has a black head with a grey throat, nape, back and side
this large bird has a white dorsal with a black belly, while flying above the water
the bird has black crown, throat and rectrices, remaining part of the body are covered in gray
a bird with an orange beak, black head and neck with black wings
a bird with a large, downward curved orange bill, white breast and black wings
medium sized all black bird with spots of dark blue and medium sized black bill
a close up of a bird face with a large downward curved yellow beak, the head and chest are white
the wholly black bird features a strong, thick beak and beady black eyes
this bird has a black body with an orange beak
a bird with a red vovert, large triangular bill and all black plumage
this large bird has a grey body, black crown, and long hooked bill
this bird has mainly black feathers, with an orange and yellow splash on its shoulders
this bird is completely black with the exception of red and yellow on its coverts
a medium sized bird with a grey belly, and a bill that curves downwards
the belly and chest are primarily white with brown speckles that stop at the a white throat
the bird has a black body and nape, as well as black tarsus and feet
a large bird with a white body and black wings
this bird has mainly black feathers, with an orange and yellow splash on its shoulders
a medium sized bird with a with a long bill,and black wings
this bird has mainly black feathers, with an orange and yellow splash on its shoulders
a bird that looks like it is partly feathers and partly fur and is grey witha large beak
a bird with an orange beak, black head and neck with black wings
a bird with a large, downward curved orange bill, white breast and black wings
a medium sized bird with a bill that curves downward, with a brown body
the bird has black crown, throat and rectrices, remaining part of the body are covered in gray
the bird has a black body and nape, as well as black tarsus and feet
a large bird with a white body and black wings
this larger bird has a white breast with black spots and a red beak
this bird has a medium black bill, black tarsuses and feet, and a dark blue crown
the birds has a black head with a grey throat, nape, back and side
a bird with an orange thick bill and a black coat with white at its throat
a brown bird with a long black beak and brown breast
a close up of a bird face with a large downward curved yellow beak, the head and chest are white
a medium sized bird with a bill that curves downward, with a brown body
this bird is black with red and has a long, pointy beak
this large bird has a grey body, black crown, and long hooked bill
a close up of a bird face with a large downward curved yellow beak, the head and chest are white
the birds has a black head with a grey throat, nape, back and side
a bird with a large triangular bill, black covering its body except for the red on its coverts
black head and body, red eyes. wide tail
this bird is black with grey and has a long, pointy beak
a black bird with a round body, yellow eyes, black bill, and black tarsus
a large bird with a black head and rump and grey body
a medium sized bird with a with a long bill,and black wings
this is a black bird with a prominent feather on its head and a long neck
this is a grey bird with a white breast and eye and a black beak
a large bird with a grey belly, and large black wings
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
