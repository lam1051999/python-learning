import random


class Card:
    """
--------suit---------
    Spades ↦ 3
    Hearts ↦ 2
    Diamonds ↦ 1
    Clubs ↦ 0
--------rank---------
    Jack ↦ 11
    Queen ↦ 12
    King ↦ 13
    """
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        # suit is more important
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(1, 14):
                c = Card(i, j)
                self.cards.append(c)

    def __str__(self):
        card_names = []
        for card in self.cards:
            card_names.append(str(card))
        return '\n'.join(card_names)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)
        return len(self.cards)

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def sort_cards(self):
        return self.cards.sort()

    def move_card(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    def __init__(self, label=""):
        self.cards = []
        self.label = label


hand = Hand("My hand")
d = Deck()
c = d.pop_card()
hand.add_card(c)
print(hand)
