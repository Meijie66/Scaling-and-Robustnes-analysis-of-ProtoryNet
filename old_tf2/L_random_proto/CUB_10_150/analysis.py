from collections import Counter


text = """
this bird is black in color, with a black beak and a black eye ring
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color with a large brown beak and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird has an all black body with a navy blue crested head and long pointy beak
this bird is black in color with a sharp black beak, and black eye rings
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a large brown beak and black eye rings
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this brown bird has webbed feet and a black beak
this bird is black in color, with a black beak and a black eye ring
this bird has a black crown, an orange bill, and a long neck
this bird is black in color with a sharp black beak, and black eye rings
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color with a large brown beak and black eye rings
this bird is black and red in color with a black beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is black and red in color with a black beak, and black eye rings
this bird is generally black in color, with a strange black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a vibrant orange beak, and black eye rings
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird is black and blue in color with a sharp black beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a large brown beak and black eye rings
this bird is black in color with a large brown beak and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is generally black in color, with a strange black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a vibrant orange beak, and black eye rings
a large bird has a stumpy bill, large tufts of black feathers on its breast, and a black crown
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color with a large brown beak and black eye rings
this bird is generally black in color, with a strange black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black and red in color with a black beak, and black eye rings
this bird is black and blue in color with a sharp black beak, and black eye rings
this bird is generally black in color, with a strange black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a large brown beak and black eye rings
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is generally black in color, with a strange black beak and a black eye ring
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color with a large brown beak and black eye rings
this bird is black with green eyes and has a long, pointy beak
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color with a large brown beak and black eye rings
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is generally black in color, with a strange black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is generally black in color, with a strange black beak and a black eye ring
this bird is black in color with a large brown beak and black eye rings
this bird is black in color with a vibrant orange beak, and black eye rings
this bird has a black crown, an orange bill, and a long neck
this bird is black in color with a large brown beak and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color, with a black beak and a black eye ring
this bird is black, white, and brown in color with a stubby beak and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is black and blue in color with a sharp black beak, and black eye rings
this bird is black in color with a large brown beak and black eye rings
this bird is generally black in color, with a strange black beak and a black eye ring
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird has a black shiny body and feathers, a small pointy black bill and bright yellow eyes
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird has wings that are black and has a big bill
this is a grey bird with a black head and a large black beak
this bird is black in color with a large brown beak and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a large brown beak and black eye rings
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color, with a black beak and a black eye ring
this bird has a black shiny body and feathers, a small pointy black bill and bright yellow eyes
this bird is black in color, with a black beak and a black eye ring
this bird is black and blue in color with a sharp black beak, and black eye rings
this bird is black in color with a large brown beak and black eye rings
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color with a large brown beak and black eye rings
this bird is black and blue in color with a sharp black beak, and black eye rings
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this is a large grey bird with a black wing and head and a long and pointy black beak
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
this bird has a black crown, an orange bill, and black webbed feet
this bird is black in color with a sharp black beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
a large bird has a stumpy bill, large tufts of black feathers on its breast, and a black crown
this bird is black in color, with a black beak and a black eye ring
this bird has a black shiny body and feathers, a small pointy black bill and bright yellow eyes
this bird is black in color with a large brown beak and black eye rings
this bird is black in color with a large brown beak and black eye rings
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color with a vibrant orange beak, and black eye rings
this bird is black in color, with a black beak and a black eye ring
a large bird has a stumpy bill, large tufts of black feathers on its breast, and a black crown
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is all black, with black webbed feet, a black plume, and orange beak
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color, with a black beak and a black eye ring
this bird is black in color with a large brown beak and black eye rings
this bird is black in color, with a black beak and a black eye ring
a large bird has a stumpy bill, large tufts of black feathers on its breast, and a black crown
this bird is black in color with a brown beak, and black eye rings
this bird is black in color with a vibrant orange beak, and black eye rings
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