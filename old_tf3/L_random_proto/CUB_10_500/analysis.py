from collections import Counter

# Input data (your text)
text = """
this bird is black with white and has a long, pointy beak
this is a black bird with a white eye and a yellow beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is white and black in color with a odd shaped orange beak and black eye rings
this bird is black with white and has a long, pointy beak
this bird is completely black with a yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is completely black with a yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this is a black bird with a white eye and a yellow beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a black head and has a short bright orange pointed bill
this bird is white and black in color with a odd shaped orange beak and black eye rings
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a vivid bright orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is white and black in color with a red beak, and black eye rings
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird has a black shiny body and feathers, a small pointy black bill and bright yellow eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a black head and has a short bright orange pointed bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird has wings that are black and white and has a long bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with red and blue and has a very short beak
this bird has a black and dark orange bill, with white eyes
this bird is white and black in color with a odd shaped orange beak and black eye rings
this funny looking bird is black with white eyes and an orange beak
this bird has wings that are black and white with a short orange beak
this bird is black with white and has a long, pointy beak
this bird has a orange beak, black throat, and a black and white belly
this bird is white and black in color with a odd shaped orange beak and black eye rings
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird is black with white and has a long, pointy beak
this bird is black and white in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
a black bird with an orange beak and a white stripe coming from its white eyes
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird has wings that are black and has a orange and yellow spot
this is a black bird with a white eye and an orange beak
this bird is black with red and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is white and black in color with a odd shaped orange beak and black eye rings
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird has a short orange bill, a black head, and a black and white mottled body
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is completely black with a yellow eye and pointy bill
this bird is completely black with a yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and has a red and yellow blotch
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and has a white belly
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird is black with white and has a very short beak
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a orange beak, black throat, and a black and white belly
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is completely black with a yellow eye and pointy bill
this bird is black with white on its chest and head and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this funny looking bird is black with white eyes and an orange beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird has a short orange bill, a black head, and a black and white mottled body
this bird has a black head and has a short bright orange pointed bill
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this is a grey bird with a black head and a pointy orange beak
this bird has a black and dark orange bill, with white eyes
this funny looking bird is black with white eyes and an orange beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a black head and has a short bright orange pointed bill
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird is black and white in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird has black eyes with a white throat and a red beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white on its chest and head and has a long, pointy beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird is black with white and has a long, pointy beak
this bird has a orange beak, black throat, and a black and white belly
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with red and blue and has a very short beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird has a black shiny body and feathers, a small pointy black bill and bright yellow eyes
this bird has a black and dark orange bill, with white eyes
this bird has a black head and has a short bright orange pointed bill
this bird is white and black in color, and has a orange beak
this bird is completely black witha yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a very short beak
this is a black bird with a white eye and an orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this is a black bird with a white eye and an orange beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird is white and black in color, and has a orange beak
this bird has wings that are brown and has a long black bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is white and black in color with a odd shaped orange beak and black eye rings
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
a black bird with an orange beak and a white stripe coming from its white eyes
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has wings that are black and has a red and yellow blotch
this bird is black with white and has a long, pointy beak
this is a black bird with a white eye and an orange beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird has a black and dark orange bill, with white eyes
this is a grey bird with a black head and a pointy orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this is a black bird with a white eye and an orange beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this bird is completely black with a yellow eye and pointy bill
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with red and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this is a black bird with a white eye and a large orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is black with small eyes and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is white and black in color, and has a orange beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird has a short orange bill, and a black head
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is completely black with a yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird has wings that are black and white and has a yellow bill
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is completely black witha yellow eye and pointy bill
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is white and black in color with a odd shaped orange beak and black eye rings
this bird is black with white and has a long, pointy beak
this bird is white and black in color with a odd shaped orange beak and black eye rings
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird has a short orange bill, and a black head
this bird is completely black with a yellow eye and pointy bill
this bird has a orange beak, black throat, and a black and white belly
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird is small and black with a pointy orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this is a black bird with a white eye and a yellow beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird has black eyes with a white throat and a red beak
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird has a black head and has a short bright orange pointed bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this is a black bird with a white eye and a pointy black beak
this bird is black with white and has a long, pointy beak
this bird has a black shiny body and feathers, a small pointy black bill and bright yellow eyes
this bird has a black head and has a short bright orange pointed bill
this is a black bird with a white eye and a pointy black beak
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
a black bird with an orange beak and a white stripe coming from its white eyes
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is completely black with a yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird has a short orange bill, and a black head
this bird is completely black with a yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird has a black head and has a short bright orange pointed bill
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is completely black with a yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a black and dark orange bill, with white eyes
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is dark black and featherless around is eyes, and has a short black beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird is black with white and has a long, pointy beak
this bird is black with red and blue and has a very short beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is all black with an orange beak and a bit of white between the head and beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is completely black witha yellow eye and pointy bill
this bird is completely black with a yellow eye and pointy bill
this bird has wings that are black and white and has a yellow bill
this bird is black with white and has a long, pointy beak
this funny looking bird is black with white eyes and an orange beak
this bird is black in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird has a short orange bill, a black head, and a black and white mottled body
this bird is black and white in color, and has a bright orange beak
this bird is black with white and has a long, pointy beak
this bird is mostly black with a small head, white eye, and small orange bill
this bird is completely black with a yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is completely black witha yellow eye and pointy bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black in color, and has a bright orange beak
this bird has a black and dark orange bill, with white eyes
this bird is mostly black with a small head, white eye, and small orange bill
this bird is mostly black with a small head, white eye, and small orange bill
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is black with white and has a long, pointy beak
this bird is white and black in color, and has a orange beak
this bird is black with white and has a long, pointy beak
this black bird has white eyes and black plumage on top of a bright orange shortened beak
this bird is black with red and has a long, pointy beak
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
