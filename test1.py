import unittest
from Test import FizzBuzz

class TestFactorielle(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = FizzBuzz("MaClasse")

    def test_affiche_15(self):
        self.assertEqual(
            self.instance.affiche(15),
            "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
        )


if __name__ == "__main__":
    unittest.main()
