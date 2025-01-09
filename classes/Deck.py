from classes.Card import Card
import random

class Deck:
    cards = []
    def __init__(self):
        suits = ["Spade", "Club", "Heart", "Diamond"]

        for suit in suits:
            for i in range(2, 11):
                card = Card(suit, i)
                self.cards.append(card)
            self.cards.append(Card(suit, "J"))
            self.cards.append(Card(suit, "Q"))
            self.cards.append(Card(suit, "K"))
            self.cards.append(Card(suit, "A"))

        random.shuffle(self.cards)
        print(self.cards[1].number)
        print(self.cards[1].suit)

        