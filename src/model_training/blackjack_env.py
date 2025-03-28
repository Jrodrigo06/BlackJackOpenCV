import sys
import os
import gymnasium as gym
from gymnasium import spaces
import random


class BlackjackEnv(gym.Env):
    def __init__(self):
        try:
            super(BlackjackEnv, self).__init__()

            self.action_space = spaces.Discrete(2)  # 0: 'n', 1: 'y'

            # Observation space: 
            # (player's hand value, dealer's showing card)

            self.observation_space = spaces.Tuple((spaces.Discrete(32), spaces.Discrete(11)))

            # Initialize deck and game state
            self.deck = self.create_deck()
            self.reset()
        except Exception as e:
            print(e,sys)


    def create_deck(self):
        try:
            """Create a deck of 52 cards (multiset)"""
            deck = ['Ace', 'Ace', 'Ace', 'Ace', 'King', 'King', 'King', 'King', 
                    'Queen', 'Queen', 'Queen', 'Queen', 'Jack', 'Jack', 'Jack', 'Jack', 
                    '10', '10', '10', '10', '9', '9', '9', '9', '8', '8', '8', '8',
                    '7', '7', '7', '7', '6', '6', '6', '6', '5', '5', '5', '5', 
                    '4', '4', '4', '4', '3', '3', '3', '3', '2', '2', '2', '2']
            random.shuffle(deck)
            return deck
        except Exception as e:
            print(e,sys)
    
    def draw_card(self):
        """Draw a random card from the deck"""
        return self.deck.pop()
    
    def score_calc(self, hand):
        try:
            """Calculate the score for a given hand"""
            score = 0
            non_aces = []
            ace_count = 0

            for card in hand:
                if card == "Ace":
                    ace_count += 1
                else:
                    non_aces.append(card)

            for card in non_aces:
                if card in ["King", "Jack", "Queen"]:
                    score += 10
                else:
                    score += int(card)

            for _ in range(ace_count):
                if score + 11 <= 21:
                    score += 11  # Ace = 11 if it doesn't bust
                else:
                    score += 1  # Otherwise, Ace = 1

            return score
        except Exception as e:
            print(e,sys)

            
    def reset(self):
            try:
                """Reset the environment to a new game state."""
                self.player_hand = [self.draw_card(), self.draw_card()]
                self.dealer_hand = [self.draw_card(), self.draw_card()]
                self.player_turn = True  # True if it's the player's turn, False if it's the dealer's turn
                
                return self._get_observation()
            except Exception as e:
                print(e,sys)
    
    def _get_observation(self):
        try:
            """Get the current observation: player score and dealer's visible card"""
            return (self.player_hand,self.score_calc(self.player_hand), self.dealer_hand[0])
        except Exception as e:
            print(e,sys)
    
    def step(self, action):
        try:
        ##Perform a step in the environment (hit or stick)"""
        # Player's turn
            if self.player_turn:
                if action == 0:  # Stick (stay)
                    self.player_turn = False  # End player's turn, start dealer's turn
                
                elif action == 1:  # Hit (draw a card)
                    self.player_hand.append(self.draw_card())  # Add card to player's hand
                    player_score = self.score_calc(self.player_hand)
                    
                    # If player busts, end game
                    if player_score > 21:
                        return self._get_observation(), -1.25, True, {}  # Player loses (bust)

                    # Otherwise, game continues (player can still hit or stay)
                    return self._get_observation(), 0, False, {}  # No win/loss yet, player's turn continues
            
            # Dealer's turn (only if player has finished their turn)
            else:
                dealer_score = self.score_calc(self.dealer_hand)
                
                # Dealer hits if their score is less than 17
                while dealer_score < 17:
                    self.dealer_hand.append(self.draw_card())
                    dealer_score = self.score_calc(self.dealer_hand)
                
                # Check win conditions
                player_score = self.score_calc(self.player_hand)
                if dealer_score > 21:  # Dealer busts
                    return self._get_observation(), 1, True, {}  # Player wins
                elif player_score > dealer_score:  # Player wins
                    return self._get_observation(), 1, True, {}
                elif player_score == dealer_score:  # Tie
                    return self._get_observation(), 0, True, {}
                else:  # Dealer wins
                    return self._get_observation(), -1, True, {}
                
        except Exception as e:
            print(e,sys)

    def render(self):
        try:
            """Render the current game state"""
            print(f"Player's Hand: {self.player_hand}, Score: {self.score_calc(self.player_hand)}")
            print(f"Dealer's Hand: {self.dealer_hand}, Score: {self.score_calc(self.dealer_hand)}")
        except Exception as e:
            print(e,sys)