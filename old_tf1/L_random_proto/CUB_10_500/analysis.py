from collections import Counter

# Input data (your text)
text = """
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has a orange beak, black throat, and a black and white belly
this bird has wings that are black and white with a small orange beak
this bird has wings that are black and white with a small orange beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is brown with black feet and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are grey and has a long black bill
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with an orange beak
this bird is black with big wings and has a long, pointy beak
this bird has black winds and a white body with a long curved beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black with an orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is grey with long wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with big wings and has a long, pointy beak
this bird has a white body and head, brown wings, and a long slightly curved orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black with a long orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and has a thick bill
this bird has wings that are black with an orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black and has a orange bill
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with an orange beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with white and has a very short beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a small orange beak
this bird has a white chest, black wings and small curved orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are black and white with a small orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird has wings that are black and white with a short orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black with an orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with an orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are black and white with a small orange beak
this bird is black with big wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with an orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a small orange beak
this bird is black with red on its wing and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has a short bill, a red patch on its wing, and a black breast
this bird has wings that are black with a long orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has black plumage, with a large orange beak and white stripes on its head
this bird is black with big wings and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and white with a small orange beak
this bird has wings that are black with an orange beak
this bird has wings that are black and white with a small orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with grey and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black and gray in color, and has a bright orange beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has large black wings and a white underbelly as well as a medium sized beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a white body, brown wings and an orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are grey and has a long bill
this bird is black with big wings and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with red on its wing and has a very short beak
this bird has a white chest, black wings and small curved orange beak
this bird has wings that are black and white with a small orange beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with an orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with an orange beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this is a large bird with a mostly grey bird with a yellow beak and black and white wings
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has wings that are black and white with a small orange beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird has a black head and back, with gray wings, tail, and beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this crested black bird has spiky plumage, long tail feathers, and a short, thick gray beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with black and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with red on its wing and has a very short beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with shiny feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has a white chest, black wings and small curved orange beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with red on its wing and has a very short beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a short black beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is white with grey on its wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird has wings that are black with a long orange beak
this bird is black with white on its feathers and has a long, pointy beak
this bird has wings that are black with a long orange beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with white on its feathers and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is black with big wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
this bird is brown with black on its wings and has a long, pointy beak
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
