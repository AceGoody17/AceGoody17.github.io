import random

movies = {1: "Shawshank Redemption", 2: "Forrest Gump", 3: "Seven", 4: "Life is Beautiful", 5: "Kill Bill: Vol. 1", 6: "Kill Bill: Vol. 2", 7: "Spirited Away", 8: "12th Fail", 9: "How to lose a guy in 10 days", 10: "Band Baaja Bhaarat", 11: "Drishyam", 12: "Laapata Ladies", 13: "Bachna Ae Haseeno" , 14: "Rang de Basanti", 15: "A Wednesday", 16: "Parasite", 17: "The Prestige", 18: "Spider Man: Into the Spider Verse", 19: "Wall E", 20: "Good Will Hunting", 21: "Coco", 22: "American Beauty", 23: "Requiem for a Dream", 24: "Eternal Sunshine of the Spotless Mind", 25: "The Mask", 26: "Up", 27: "Andhadhun", 28: "Tumbbad", 29: "Swades", 30: "Kahaani"}
movies_copy = movies
number = random.randint(1, len(movies_copy))
print(f"Today's movie is: {movies_copy[number]}")
del movies_copy[number]
print(movies_copy)




