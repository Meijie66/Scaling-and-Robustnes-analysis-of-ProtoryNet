from collections import Counter

# Input data (your text)
text = """
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird is brown with white and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird is brown with white and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is grey with white and has a long, pointy beak
this bird is gray and brown in color, and has a large curved beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird has wings that are black and has a thick bill
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is gray and brown in color, and has a large curved beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is gray and brown in color, and has a large curved beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is grey with white and has a long, pointy beak
this bird is black with grey on its chest and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this bird is grey with black and has a long, pointy beak
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is gray and brown in color, and has a large curved beak
this bird is black with grey on its chest and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is black with grey on its chest and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is grey with white and has a long, pointy beak
this bird is black with white on its stomach and a short beak
this bird has wings that are black and has a yellow bill
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is gray and brown in color, and has a large curved beak
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird is brown with white and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is gray and brown in color, and has a large curved beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is gray and brown in color, and has a large curved beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with white and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with white and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is gray and brown in color, and has a large curved beak
this bird is brown with black feet and has a very short beak
this bird is gray and brown in color, and has a large curved beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is black with grey and has a long, pointy beak
this bird is brown with black and has a very short beak
this bird is brown with a black back and has a long, pointy beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with white and has a long, pointy beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black and has a very short beak
this bird has a orange beak, black throat, and a black and white belly
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is black with grey on its chest and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is grey with white and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with white and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is grey with black and has a long, pointy beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with white and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is gray and brown in color, and has a large curved beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is grey with black and has a very short beak
this bird is brown with white and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is grey with white and has a long, pointy beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with white and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with white and has a long, pointy beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is grey with white and has a very short beak
this bird is gray and brown in color, and has a large curved beak
this bird is black in color with a black beak, and black eye rings
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with white and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with a black back and has a long, pointy beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head, orange beak, and white breast and belly
this bird is brown with black feet and has a very short beak
this bird has wings that are black and has a yellow bill
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with white and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a black head, orange beak, and white breast and belly
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with white and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is gray and brown in color, and has a large curved beak
this bird is brown with black feet and has a very short beak
this bird is brown with white and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is grey with black and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird is grey with black and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has wings that are black and has a thick bill
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with white and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is black with grey on its chest and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with white and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with white and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is black with white on its stomach and a short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird has a black head and a gray nape, with a large beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird is black with white on its stomach and a short beak
this bird is brown with black and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is black in color with a black beak, and black eye rings
this bird is black with white on its stomach and a short beak
this bird is black with grey and has a long, pointy beak
this bird is brown with white and has a very short beak
this bird is brown with black feet and has a very short beak
this bird is brown with black feet and has a very short beak
this bird has a gray and white belly and a small orange beak
this bird is black with white on its stomach and a short beak
this bird is gray and brown in color, and has a large curved beak
this bird is black with white on its stomach and a short beak
this bird is gray and brown in color, and has a large curved beak
this bird is black with white on its stomach and a short beak
this bird is brown with black feet and has a very short beak
this bird has a black head and a gray nape, with a large beak
this bird is brown with black feet and has a very short beak
this bird is gray and brown in color, and has a large curved beak
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
