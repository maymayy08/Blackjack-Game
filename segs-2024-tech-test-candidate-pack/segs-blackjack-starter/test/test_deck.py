import unittest
from src.deck import Deck  # Assuming the Deck class is inside the src folder

class DeckTestCase(unittest.TestCase):

    def setUp(self):  # This method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # This method will be run after each test
        pass

    def test_number_of_cards(self):  # Test that the deck has 52 cards
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52, "Failed: The deck does not contain 52 cards!")
        print("Passed: The deck has exactly 52 cards!")

    def test_cards_value(self):  # Test that each card has the correct value
        # Test number cards (2 to 10)
        for value in range(2, 11):  # This will go through 2 to 10
            for suit in self.deck.suits:
                card = (str(value), suit) #This create a turple to find the value and return then create a suit together 
                card_value = self.deck.obtain_the_deck_value(card)
                self.assertEqual(card_value, value, f"Failed for {card[0]} of {card[1]}")
                print(f"Success: {card[0]} of {card[1]} is equal to {card_value} points")

        # This method is use to test face cards (Jack, Queen, King)
        for face_card in self.deck.face_cards:
            for suit in self.deck.suits:
                card = (face_card, suit)
                card_value = self.deck.obtain_the_deck_value(card)
                self.assertEqual(card_value, 10, f"Failed for {card[0]} of {card[1]}")
                print(f"Success: {card[0]} of {card[1]} is equal to {card_value} points")
        
        # This method is use to test the Ace cards valuee
        for suit in self.deck.suits:
            card = ("Ace", suit)
            card_value = self.deck.obtain_the_deck_value(card)
            self.assertEqual(card_value, 1, f"Failed for Ace of {card[1]}")
            print(f"Success: Ace of {card[1]} is worth {card_value} points")

    def test_the_ace_count(self):  # This method is use to test whether there are 4 aces inside the deck
        ace_count = self.deck.count_aces() 
        self.assertEqual(ace_count, 4, "Oh no, the deck does not contain exactly 4 aces!")
        print("Success: The deck has 4 aces!")

if __name__ == '__main__':
    unittest.main()
