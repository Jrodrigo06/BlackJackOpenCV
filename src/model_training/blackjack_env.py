import gymnasium as gym
import numpy as np
from gymnasium import spaces
import random

class BlackjackEnv(gym.Env):
    def __init__(self):
        super(BlackjackEnv, self).__init__()

        # Action space: 0 = stick, 1 = hit
        self.action_space = spaces.Discrete(2)

        # Observation space: 
        # [player's current score, dealer's visible card]
        self.observation_space = spaces.Box(
            low=np.array([4, 1]), 
            high=np.array([31, 11]), 
            dtype=np.int32
        )

        # Initialize game variables
        self.player_hand = None
        self.dealer_hand = None
        self.deck = None
        self.player_turn = None
        self.current_observation = None

    def create_deck(self):
        """Create a shuffled deck of 52 cards"""
        deck = ['Ace', 'Ace', 'Ace', 'Ace', 
                'King', 'King', 'King', 'King', 
                'Queen', 'Queen', 'Queen', 'Queen', 
                'Jack', 'Jack', 'Jack', 'Jack', 
                '10', '10', '10', '10', 
                '9', '9', '9', '9', 
                '8', '8', '8', '8',
                '7', '7', '7', '7', 
                '6', '6', '6', '6', 
                '5', '5', '5', '5', 
                '4', '4', '4', '4', 
                '3', '3', '3', '3', 
                '2', '2', '2', '2']
        random.shuffle(deck)
        return deck

    def draw_card(self):
        """Draw a random card from the deck"""
        if not self.deck:
            self.deck = self.create_deck()
        return self.deck.pop()

    def score_calc(self, hand):
        """Calculate the score for a given hand"""
        score = 0
        non_aces = [card for card in hand if card != "Ace"]
        aces = [card for card in hand if card == "Ace"]

        # Score non-ace cards
        for card in non_aces:
            if card in ["King", "Queen", "Jack"]:
                score += 10
            else:
                score += int(card)

        # Handle aces
        for _ in aces:
            if score + 11 <= 21:
                score += 11
            else:
                score += 1

        return score

    def reset(self, seed=None, options=None):
        """Reset the environment to a new game state"""
        super().reset(seed=seed)
        
        # Create and shuffle deck
        self.deck = self.create_deck()

        # Deal initial hands
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card(), self.draw_card()]
        if(self.score_calc(self.dealer_hand) == 21):
            self.reset()
        self.player_turn = True

        # Calculate and store current observation
        self.current_observation = np.array(self._get_observation(), dtype=np.int32)

        return self.current_observation, {}

    def _get_observation(self):
        """Get the current observation: player score and dealer's visible card"""
        return [
            self.score_calc(self.player_hand), 
            self.score_calc([self.dealer_hand[0]])
        ]

    def step(self, action):
        """Perform a step in the environment"""
        # Ensure we have a current observation
        if self.current_observation is None:
            return self.reset()

        # Player turn
        if self.player_turn:
            if action == 0:  # Stick
                # Switch to dealer's turn
                self.player_turn = False
            elif action == 1:  # Hit
                self.player_hand.append(self.draw_card())
                
                # Check if player busts
                if self.score_calc(self.player_hand) > 21:
                    # Update observation before returning
                    self.current_observation = np.array(self._get_observation(), dtype=np.int32)
                    return (
                        self.current_observation, 
                        -1,      # Negative reward for losing
                        True,    # Episode is done
                        False,   # Not truncated
                        {}       # Additional info
                    )
            
            # Update observation
            self.current_observation = np.array(self._get_observation(), dtype=np.int32)
            
            # Continue game if not bust
            return (
                self.current_observation, 
                0,      # No reward yet
                False,  # Not done
                False,  # Not truncated
                {}      # Additional info
            )
        
        # Dealer's turn
        dealer_score = self.score_calc(self.dealer_hand)
        player_score = self.score_calc(self.player_hand)

        # Dealer hits until score is at least 17
        while dealer_score < 17:
            self.dealer_hand.append(self.draw_card())
            dealer_score = self.score_calc(self.dealer_hand)

        # Determine game outcome
        if dealer_score > 21:  # Dealer busts
            reward = 1
        elif player_score > dealer_score:  # Player wins
            reward = 1
        elif player_score == dealer_score:  # Tie
            reward = 0
        else:  # Dealer wins
            reward = -1

        # Update observation before returning
        self.current_observation = np.array(self._get_observation(), dtype=np.int32)

        return (
            self.current_observation, 
            reward, 
            True,   # Episode is done
            False,  # Not truncated
            {}      # Additional info
        )

    def render(self):
        """Optional rendering method"""
        print(f"Player's Hand: {self.player_hand}, Score: {self.score_calc(self.player_hand)}")
        print(f"Dealer's Hand: {self.dealer_hand}, Score: {self.score_calc(self.dealer_hand)}")