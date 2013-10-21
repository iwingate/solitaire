import cards

deck = cards.Deck()

deck.shuffle()



tableau = {}

for n in range(0,7):
    card1 = deck.deal()
    card2 = deck.deal()
    card2.set_hidden()
    card3 = deck.deal()
    card3.set_hidden()
    tableau[n] = [card1, card2, card3]   
    print(tableau[n])



stock = {}


for n in range(0,21):
    stock[n] = deck.deal()
    stock[n].set_hidden()

print('\n',stock)

foundation = {}

for n in range(0,4):
    foundation[n] = ''

print('\n',foundation)

rank = input('Choose a card rank. 1-13 ')
suit = input('Choose its suit. ')


where = input('What column is it in and which position? Enter 0-6. ')
put = input('Where should it go. Enter 0-6. ')
card_type = cards.Card(rank,suit)

for v in tableau.values():       
    for card in v:
        if card_type.get_rank() == card.get_rank() and card_type.get_suit() == card.get_suit():
            tableau[int(put)].insert(0,card_type)

print(tableau)
            
             

