import card
import random

class Deck:
  def __init__(self):
    #create a standard 52 card deck of cards
    self.cards = []
    for suit in range(1, 5):  # 1-4: clubs, spades, hearts, diamonds
      for rank in range(1, 14):  # 1-13: ace through king
        self.cards.append(card.Card(suit, rank))
        
  def count(self):
    #return the number of cards remaining in the deck
    return len(self.cards)
    
  def draw(self):
    #return and remove the top card in the deck
    #if the deck is empty, raise a ValueError
    if len(self.cards) == 0:
      raise ValueError("Cannot draw from an empty deck")
    return self.cards.pop(0)
    
  def shuffle(self):
    #shuffle the deck using a random number generator to repeatedly swap cards
    n = len(self.cards)
    for i in range(n):
      j = random.randint(0, n - 1)
      self.cards[i], self.cards[j] = self.cards[j], self.cards[i]