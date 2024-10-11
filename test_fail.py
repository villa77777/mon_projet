import unittest
from Test import FizzBuzz

    

class TestFactorielle(unittest.TestCase):

    def setUp(self) -> None:
          self.instance = FizzBuzz("MaClasse")

    def test_factorielle_de_5(self):
            self.assertEqual(factorielle(5), 120)
