from src.utils.exception import customException
from src.utils.logger import logging
import random

class Deck:
    def  __init__(self):
        #Initializes the deck of cards, as a multiset for 52 cards

        self.deck = ['Ace', 'Ace', 'Ace', 'Ace', 'King', 'King', 'King', 'King', 
                     'Queen', 'Queen', 'Queen', 'Queen', 'Jack', 'Jack', 'Jack', 'Jack', 
                     '10', '10', '10', '10', '9', '9', '9', '9', '8', '8', '8', '8',
                     '7', '7', '7', '7', '6', '6', '6', '6', '5', '5', '5', '5', 
                     '4', '4', '4', '4', '3', '3', '3', '3', '2', '2', '2', '2']
        
    def draw(self):
        #Pops a random item from the multiset and returns it
        return self.deck.pop()
    
    def shuffle(self):
        #Shuffles the deck using random.shuffle
        random.shuffle(self.deck)
        return self.deck
    

    

class Game:
    def __init__(self):
    #Initializes the game stat

        self.player_turn = True
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer_hand = [self.deck.draw(), self.deck.draw()]
        self.player_hand = [self.deck.draw(), self.deck.draw()]
        self.player_win = None

        self.check_initial_winner()  # Check for initial winner
    

    def check_initial_winner(self):
        # Check if either the player or dealer has a score of 21 at the start
        dealer_score = self.score_calc(self.dealer_hand)
        player_score = self.score_calc(self.player_hand)

        if dealer_score == 21:
            print(f"Dealer wins with a Blackjack! Dealer's hand: {self.dealer_hand} Player's hand: {self.player_hand}")
            self.player_win = False
            self.game_over()
        elif player_score == 21:
            print(f"You win with a Blackjack! Dealer's hand: {self.dealer_hand} Player's hand: {self.player_hand}")
            self.player_win = True
            self.game_over()
        else:
            logging.info("No initial winner. Proceeding with the game.")
            self.player()

    def score_calc(self, card_hand):
        curr_score = 0
        non_aces = []
        ace_count = 0

        for card in card_hand:
            if(card == "Ace"):
                ace_count += 1
            else:
                non_aces.append(card)
        
        for card in non_aces:
            if(card in ["King", "Jack", "Queen"]):
                curr_score += 10
            else:
                curr_score += int(card)
        
        for a in range(ace_count):
            if(curr_score + 11 <= 21 and a == ace_count - 1):
                curr_score += 11  # Ace = 11 if safe
            else:
                curr_score += 1

        return curr_score  # Final score

    def player(self):
        #Player's turn to play

        while True:          
            if self.score_calc(self.player_hand) > 21:
                self.player_win = False
                self.game_over()
                break

            choice = input(f"Do you want to draw a card? \nDealer hand: {self.dealer_hand} \nYour hand: {self.player_hand} \n(y/n): ").lower()
            if choice == 'y':
                self.player_hand.append(self.deck.draw())  # Draw a card and add it to player's hand
            elif choice == 'n':
                print("You chose to stay.")
                self.dealer() ## End the player's turn
                break  
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def dealer(self):
        #Dealer's turn to play
        dealer_score = self.score_calc(self.dealer_hand)

        while dealer_score < 17:
            self.dealer_hand.append(self.deck.draw())
            dealer_score = self.score_calc(self.dealer_hand)


        if dealer_score > 21:
            self.player_win = True
        elif dealer_score == self.score_calc(self.player_hand):
            self.player_win = None
        elif dealer_score > self.score_calc(self.player_hand):
            self.player_win = False
        else:
            self.player_win = True

        self.game_over()

    def game_over(self):
        if(self.player_win == True):
            print(f"You win! Dealers hand: {self.dealer_hand} Dealers score: {self.score_calc(self.dealer_hand)} \nPlayer's hand: {self.player_hand} Player's score: {self.score_calc(self.player_hand)}")
        elif(self.player_win == False):
            print(f"Dealer wins! Dealer's hand: {self.dealer_hand} Dealers score: {self.score_calc(self.dealer_hand)} \nPlayer's hand: {self.player_hand} Player's score: {self.score_calc(self.player_hand)}")
        else:
            print(f"It's a tie! both hands are: {self.dealer_hand}")
    
    
    
game = Game()
    