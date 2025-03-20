import random
import itertools

print("Welcome to the card shuffing program.")

deck = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
cards = list(itertools.product(deck, ["Spade", "Heart", "Diamond", "Clubs"]))

# shuffle the cards 
random.shuffle(cards)

# Draw 5 Cards At Random
print("Your cards are: ")
for i in range (5):
    print(cards[i][0], "of", cards[i][1])

