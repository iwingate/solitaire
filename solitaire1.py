class Deck(object):
    """Denote a deck to play cards with"""
    
    def __init__(self):
        """Initialize deck as a list of all 52 cards: 13 cards in each of 4 suits"""
        self.__deck = [Card(j, i) for i in "CSHD" for j in range(1,14)] # list comprehension
deck = Deck()
print(deck)
