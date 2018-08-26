
# coding: utf-8

# In[ ]:


#Defining cards
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

#Card class
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank + ' of ' + self.suit
class Deck():
    def __init__(self):
        self.deck=[] #deck starts with empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) #build card objects and append them to deck list
                
    def __str__(self):
        deck_comp='' # Define empty string to store 
        for card in self.deck:
            deck_comp +=  ' \n'  +card.__str__() #Add each card Object's to print 
        return 'The deck has ' + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.ace=0;
    def add_cards(self,card):
        self.cards.append(card)
        self.value +=values[card.rank]
        if card.rank=='ace':
            self.ace +=1
        
    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value -=10
            self.ace -=1
class Chips:
    def __init__(self):
        self.total=100
        self.bet=0
    def win_bet(self):
        self.total +=self.bet
    def lose_bet(self):
        self.taotal -=self.bet
def take_bet(chips):
    while True:
        try:
            chips.bet= int(input('How many chips would you like to bet'))
        except ValueError:
            Print('Invalid Chips provided')
        else:
            if chips.bet>chips.total:
                print("sorry your bet can't exceed",chips.total) 
            else:
                break
def hit(deck,hand):
    hand.add_cards(deck.deal())
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input("Would you like to Hit or Stand? 'h' or 's'")
        
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print('Player is standing,Dealer is playing')
            playing= False
        else:
            print('Sorry ,please play again')
            continue
        break
def show_some(player,dealer):
    print('\nDealers Hand ')
    print("<Hidden card>")
    print('',dealer.cards[1])
    print('\nPlayer Hand :', *player.cards ,sep='\n') 
def show_all(player,dealer):
    print('\n Dealers Hand :' ,*dealer.cards,sep='\n')
    print('Dealers Hand:' ,dealer.value)
    print('\n Players Hand :' ,*player.cards,sep='\n')
    print('Players Hand :', player.value)
def player_busts(player,dealer,chips):
    print("Player Busts")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("Player Wins")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print('Dealer Busts')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print('Dealer Busts')
    chips.lose_bet()
    
def tie(player,dealer):
    print("Player and Dealer Tie")
#Real Game ON
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()     
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
              
    if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

    elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

    elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

    else:
            push(player_hand,dealer_hand)  
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break


# In[ ]:



    


# In[ ]:





# In[ ]:



   

