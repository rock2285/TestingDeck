import unittest
import card
import deck

#this isn't in the master
#aaa
#bbb
#Card tests
class CardInitCorrectRankAndSuit(unittest.TestCase):
  def test_valid_card_initialization(self):
    # Test all valid suits and a few ranks
    c1 = card.Card(1, 1)  # Ace of Clubs
    self.assertEqual(c1.getSuit(), 1)
    self.assertEqual(c1.getRank(), 1)
    
    c2 = card.Card(2, 7)  # 7 of Spades
    self.assertEqual(c2.getSuit(), 2)
    self.assertEqual(c2.getRank(), 7)
    
    c3 = card.Card(3, 13)  # King of Hearts
    self.assertEqual(c3.getSuit(), 3)
    self.assertEqual(c3.getRank(), 13)
    
    c4 = card.Card(4, 11)  # Jack of Diamonds
    self.assertEqual(c4.getSuit(), 4)
    self.assertEqual(c4.getRank(), 11)

class CardInitRaiseValueError(unittest.TestCase):
  def test_invalid_suit_raises_error(self):
    with self.assertRaises(ValueError):
      card.Card(0, 5)  # suit too low
    with self.assertRaises(ValueError):
      card.Card(5, 5)  # suit too high
      
  def test_invalid_rank_raises_error(self):
    with self.assertRaises(ValueError):
      card.Card(1, 0)  # rank too low
    with self.assertRaises(ValueError):
      card.Card(1, 14)  # rank too high
      
  def test_non_integer_raises_error(self):
    with self.assertRaises(ValueError):
      card.Card("1", 5)
    with self.assertRaises(ValueError):
      card.Card(1, "5")

class CardGetSuit(unittest.TestCase):
  def test_get_suit(self):
    c1 = card.Card(1, 5)
    self.assertEqual(c1.getSuit(), 1)
    
    c2 = card.Card(4, 10)
    self.assertEqual(c2.getSuit(), 4)

class CardGetRank(unittest.TestCase):
  def test_get_rank(self):
    c1 = card.Card(2, 1)
    self.assertEqual(c1.getRank(), 1)
    
    c2 = card.Card(3, 13)
    self.assertEqual(c2.getRank(), 13)

class CardStr(unittest.TestCase):
  def test_ace_representation(self):
    self.assertEqual(str(card.Card(2, 1)), "AS")  # Ace of Spades
    self.assertEqual(str(card.Card(1, 1)), "AC")  # Ace of Clubs
    
  def test_number_cards(self):
    self.assertEqual(str(card.Card(3, 3)), "3H")  # 3 of Hearts
    self.assertEqual(str(card.Card(4, 7)), "7D")  # 7 of Diamonds
    
  def test_face_cards(self):
    self.assertEqual(str(card.Card(1, 11)), "JC")  # Jack of Clubs
    self.assertEqual(str(card.Card(2, 12)), "QS")  # Queen of Spades
    self.assertEqual(str(card.Card(3, 13)), "KH")  # King of Hearts

#deck tests
class DeckInit(unittest.TestCase):
  def test_deck_has_52_cards(self):
    d = deck.Deck()
    self.assertEqual(d.count(), 52)
    
  def test_deck_has_all_unique_cards(self):
    d = deck.Deck()
    card_strings = set()
    for _ in range(52):
      c = d.draw()
      card_str = str(c)
      self.assertNotIn(card_str, card_strings)
      card_strings.add(card_str)

class DeckCount(unittest.TestCase):
  def test_count_full_deck(self):
    d = deck.Deck()
    self.assertEqual(d.count(), 52)
    
  def test_count_after_drawing(self):
    d = deck.Deck()
    d.draw()
    self.assertEqual(d.count(), 51)
    d.draw()
    d.draw()
    self.assertEqual(d.count(), 49)
    
  def test_count_empty_deck(self):
    d = deck.Deck()
    for _ in range(52):
      d.draw()
    self.assertEqual(d.count(), 0)

class DeckDrawValue(unittest.TestCase):
  def test_draw_returns_card(self):
    d = deck.Deck()
    c = d.draw()
    self.assertIsInstance(c, card.Card)
    
  def test_draw_removes_card(self):
    d = deck.Deck()
    initial_count = d.count()
    d.draw()
    self.assertEqual(d.count(), initial_count - 1)
    
  def test_draw_order(self):
    d = deck.Deck()
    first_card = d.draw()
    # The first card should be Ace of Clubs (suit=1, rank=1)
    self.assertEqual(first_card.getSuit(), 1)
    self.assertEqual(first_card.getRank(), 1)

class DeckDrawException(unittest.TestCase):
  def test_draw_from_empty_deck_raises_error(self):
    d = deck.Deck()
    # Draw all cards
    for _ in range(52):
      d.draw()
    # Try to draw from empty deck
    with self.assertRaises(ValueError):
      d.draw()

class DeckShuffle(unittest.TestCase):
  def test_shuffle_maintains_count(self):
    d = deck.Deck()
    d.shuffle()
    self.assertEqual(d.count(), 52)
    
  def test_shuffle_changes_order(self):
    # Create two decks
    d1 = deck.Deck()
    d2 = deck.Deck()
    
    # Shuffle one deck
    d2.shuffle()
    
    # Check that at least some cards are in different positions
    # (there's a tiny chance they could be the same, but it's extremely unlikely)
    differences = 0
    for _ in range(52):
      c1 = d1.draw()
      c2 = d2.draw()
      if str(c1) != str(c2):
        differences += 1
    
    # We expect at least a few cards to be in different positions
    self.assertGreater(differences, 0)

if __name__ == '__main__':
  unittest.main()
  
