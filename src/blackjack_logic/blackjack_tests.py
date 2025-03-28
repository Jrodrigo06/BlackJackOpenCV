import unittest
from src.blackjack_logic.blackjack_logic import Deck, Game

class TestBlackjack(unittest.TestCase):

    def test_deck_initialization(self):
        # Test if the deck initializes with the correct number of cards
        deck = Deck()
        self.assertEqual(len(deck.deck), 52)

    def test_draw_card(self):
        # Test if drawing a card reduces deck size
        deck = Deck()
        initial_size = len(deck.deck)
        drawn_card = deck.draw()
        self.assertIsNotNone(drawn_card)  # Check that a card was drawn
        self.assertEqual(len(deck.deck), initial_size - 1)

    def test_blackjack_score(self):
        # Test various card hands for correct blackjack score calculations
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
        # Test if game restarts when dealer starts with Blackjack
        game = Game()
        game.dealer_hand = ["Ace", "King"]
        self.assertEqual(game.score_calc(game.dealer_hand), 21)
        # Test game reset if dealer hits 21
        self.assertEqual(game.player_win, None)

    def test_player_bust(self):
        # Test if the player busts
        game = Game()
        game.player_hand = ["10", "8", "7"]  # A total of 25, busts
        game.player()
        self.assertEqual(game.player_win, False)

    def test_dealer_bust(self):
        # Test if the dealer busts
        game = Game()
        game.dealer_hand = ["10", "8", "7"]  # A total of 25, busts
        game.dealer()
        self.assertEqual(game.player_win, True)

    def test_game_tie(self):
        # Test if the game results in a tie (same score)
        game = Game()
        game.dealer_hand = ["10", "8"]
        game.player_hand = ["9", "9"]
        game.dealer()  # Dealer's turn
        self.assertEqual(game.player_win, None)  # Tie scenario

if __name__ == "__main__":
    unittest.main()
