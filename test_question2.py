import unittest
from question2 import crypt  # Importer la fonction crypt du fichier question2.py

class TestCrypt(unittest.TestCase):

    def test_crypt_simple(self):
        self.assertEqual(crypt("abc"), "bcd")

    def test_crypt_with_space(self):
        self.assertEqual(crypt("hello world"), "ifmmp!xpsme")  # Remarque: " " sera remplacé par "!"

    def test_crypt_special_characters(self):
        self.assertEqual(crypt("!@#"), '"$%')

if __name__ == "__main__":
    unittest.main()
