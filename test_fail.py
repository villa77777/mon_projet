import unittest

    

class TestFactorielle(unittest.TestCase):
        def test_factorielle_de_5(self):
            self.assertEqual(factorielle(5), 120)
