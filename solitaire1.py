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


for n in range(deck.cards_left()):
    stock[n] = deck.deal()
    stock[n].set_hidden()

print('\n',stock)

foundation = {}

for n in range(0,4):
    foundation[n] = ''

print('\n',foundation)


while True:
    rank = input('Choose a card rank. A-K ')
    suit = input('Choose its suit. ')
    where = input('What column is it in? Enter 0-6. ')
    put = input('Where should it go. Enter 0-6. ')
    
    
    if rank == 'J' or rank == 'Q' or rank == 'K' or rank == 'A':
        card_type = cards.Card(rank,suit)
        rank = int(card_type.get_rank())
    else:
        rank = int(rank)
        card_type = cards.Card(rank,suit)
        rank = int(card_type.get_rank())
    print(rank)
    
    while True:
        if card_type.has_same_color(tableau[int(put)][0]) == False \
        and int(tableau[int(put)][0].get_rank()) - rank == 1:
            break
        else:
            print('Illegal move')
            rank = input('Choose a card rank. A-K ')
            suit = input('Choose its suit. ')
            where = input('What column is it in? Enter 0-6. ')
            put = input('Where should it go. Enter 0-6. ')
    
    still_working = True
    for column in tableau.values():
        if still_working == True:
            for card in column:    
                if rank == int(card.get_rank()) and suit == card.get_suit():
                    tableau[int(put)].insert(0,card)
                    tableau[int(where)].remove(card)
                    still_working = False
                    break
        else:
            break
    
    for v in tableau.values():
        if len(v) == 2 or len(v) == 1:
            tableau[int(where)][0].show_card()
        print(v)            
    
    choice = input('Choose another? Y/N ') 
    if choice in 'Y':      
        continue
    else:
        break

            
             

