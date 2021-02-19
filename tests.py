import unittest
import card, deck
suite = unittest.TestSuite()

#Card tests
class CardInitCorrectRankAndSuit(unittest.TestCase):
  pass
suite.addTest(unittest.makeSuite(CardInitCorrectRankAndSuit))

class CardInitRaiseValueError(unittest.TestCase):
  pass
suite.addTest(unittest.makeSuite(CardInitRaiseValueError))

class CardGetSuite(unittest.TestCase):
  pass
suite.addTest(unittest.makeSuite(CardGetSuite))

class CardGetRank(unittest.TestCase):
  pass
suite.addTest(unittest.makeSuite(CardGetRank))

class CardGetValue(unittest.TestCase):
  pass
suite.addTest(unittest.makeSuite(CardGetValue))

class CardStr(unittest.TestCase):
  pass
suite.addTest(unittest.makeSuite(CardStr))

#deck tests
#you must add these tests to te suite
class DeckInit(unittest.TestCase):
  pass
class DeckCount(unittest.TestCase):
  pass
class DeckDrawValue(unittest.TestCase):
  pass
class DeckDrawException(unittest.TestCase):
  pass
class DeckShuffle(unittest.TestCase):
  pass

  