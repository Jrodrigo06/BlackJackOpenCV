from multiset import *
from src.exception import customException
from src.logger import logging
import unittest


class Deck:
    def  __init__(self):
        #Initializes the deck of cards, as a multiset for 52 cards

        self.deck = Multiset({'Ace': 4, 'King' : 4, 'Queen' : 4, 'Jack' : 4, 
                 '10' : 4, '9' : 4, '8' : 4, '7' : 4, '6' : 4, 
                 '5' : 4, '4' : 4, '3' : 4, '2' : 4})
        
    def draw(self):
        #Pops a random item from the multiset and returns it
        return self.deck.popitem()
    

    

class Game:
    def __init__(self):
    #Initializes the game stat

        self.player_turn = True
        deck = Deck()
        dealer_hand = [deck.draw(), deck.draw()]
        ##Restarts the game if the dealer wins from the get go!
        if(self.score_calc(dealer_hand) == 21):
            self.__init__()
    

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
                card += 10
            else:
                card += int(card)
        
        for _ in range(ace_count):
            if cur_score + 11 > 21:
                cur_score += 1  # Ace = 1 if 11 would cause bust
            else:
                cur_score += 11  # Ace = 11 if safe

        return cur_score  # Final score

            



    
    
    

    