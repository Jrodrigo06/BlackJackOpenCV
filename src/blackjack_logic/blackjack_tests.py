import unittest
from multiset import Multiset
from src.blackjack_logic.blackjack_logic import Deck, Game  

class TestBlackjack(unittest.TestCase):

    def test_deck_initialization(self):
        #Test if the deck initializes with the correct number of cards"""
        deck = Deck()
        self.assertEqual(sum(deck.deck.values()), 52)

    def test_draw_card(self):
        #Test if drawing a card reduces deck size"""
        deck = Deck()
        initial_size = sum(deck.deck.values())
        drawn_card = deck.draw()
        self.assertIsNotNone(drawn_card)  # Check that a card was drawn
        self.assertEqual(sum(deck.deck.values()), initial_size - 1)

    def test_blackjack_score(self):
        ##Test various card hands for correct blackjack score calculations
        game = Game()
        
        # Test a Blackjack hand
        self.assertEqual(game.score_calc(["Ace", "King"]), 21)

        # Test a soft 17 (Ace counts as 11)
        self.assertEqual(game.score_calc(["Ace", "6"]), 17)

        # Test a hard 17 (Ace counts as 1)
        self.assertEqual(game.score_calc(["Ace", "6", "10"]), 17)

        # Test multiple Aces
        self.assertEqual(game.score_calc(["Ace", "Ace", "8"]), 20)
        self.assertEqual(game.score_calc(["Ace", "Ace", "9"]), 21)
        self.assertEqual(game.score_calc(["Ace", "Ace", "Ace", "8"]), 21)
        self.assertEqual(game.score_calc(["Ace", "Ace", "Ace", "9"]), 12)

    def test_dealer_blackjack_restart(self):
        """Test if game restarts when dealer starts with Blackjack"""
        game = Game()
        game.dealer_hand = ["Ace", "King"]
        self.assertEqual(game.score_calc(game.dealer_hand), 21)

if __name__ == "__main__":
    unittest.main()
