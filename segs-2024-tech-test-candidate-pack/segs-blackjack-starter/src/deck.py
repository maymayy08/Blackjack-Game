class Deck:
    def __init__(self):
        # Initialize the cards with suits and face cards including Aces
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
        self.face_cards = ['Jack', 'Queen', 'King']
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # Numeric cards (between 2-10).
        self.aces = ['Ace']

        # Create full set deck of cards
        self.cards = [(value, suit) for value in self.values for suit in self.suits]  # Numeric cards.
        self.cards += [(face_card, suit) for face_card in self.face_cards for suit in self.suits]  # Face cards.
        self.cards += [(ace, suit) for ace in self.aces for suit in self.suits]  # Ace cards

    def obtain_the_deck_value(self, card):
        # Returns the value for each single card.
        value, suit = card
        (print(card))

        # This method is use to check For numeric cards (2-10).
        if value.isdigit():
            return int(value)

        # This method is use to check the Face cards (Jack, Queen, King) that is equal to 10 points.
        if value in ["Jack", "Queen", "King"]:
            return 10

        # This method is use to check if Ace is equal to 1 (or 11, adjusted in hand calculations).
        if value == "Ace":
            return 1
        
        # This method is use to return the value back without indicating any error found.
        return 0

    def count_aces(self):
        # Returns the number of Aces in the deck.
        ace_count = 0
        for card in self.cards:
            value, suit = card
            if value == "Ace":
                ace_count += 1
        return ace_count

