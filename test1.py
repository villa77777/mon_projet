import unittest
from Test import FizzBuzz

class TestFactorielle(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = FizzBuzz("MaClasse")

    def test_affiche_5_10(self):
        # Tester la méthode avec n1=5 et n2=10
        self.assertEqual(
            self.instance.affiche(5, 10),
            "BuzzFizz78FizzBuzz"
        )

    def test_affiche_10_16(self):
        # Tester la méthode avec n1=10 et n2=16
        self.assertEqual(
            self.instance.affiche(10, 16),
            "Buzz11Fizz1314FrisBee16"
        )

if __name__ == "__main__":
    unittest.main()
