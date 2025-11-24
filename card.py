class Card:
  def __init__(self, s, r):
    #initialize a card to the given suit (1-4) and rank (1-13)
    #1:clubs 2:spades 3:hearts 4:diamonds
    #raise an exception for invalid argument, ValueError
    if not isinstance(s, int) or not isinstance(r, int):
      raise ValueError("Suit and rank must be integers")
    if s < 1 or s > 4:
      raise ValueError("Suit must be between 1 and 4")
    if r < 1 or r > 13:
      raise ValueError("Rank must be between 1 and 13")
    self.suit = s
    self.rank = r
    
  def getSuit(self):
    #return the suit of the card (1-4)
    return self.suit
    
  def getRank(self):
    #return the rank of the card (1-13)
    return self.rank
    
  def __str__(self):
    #return rank and suite, as AS for ace of spades, or 3H for
    #three of hearts, JC for jack of clubs.
    rank_map = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    suit_map = {1: 'C', 2: 'S', 3: 'H', 4: 'D'}
    
    rank_str = rank_map.get(self.rank, str(self.rank))
    suit_str = suit_map[self.suit]
    
    return rank_str + suit_str