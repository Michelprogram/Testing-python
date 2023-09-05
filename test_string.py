import string
import unittest

class TestString(unittest.TestCase):

    # Check if string.ascii_letters returns all ASCII letters
    def test_ascii_letters(self):
        self.assertEqual(string.ascii_letters, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Check if string.ascii_lowercase returns all lowercase ASCII letters
    def test_ascii_lowercase(self):
        self.assertEqual(string.ascii_lowercase, 'abcdefghijklmnopqrstuvwxyz')
    
    # Check if string.ascii_uppercase returns all uppercase ASCII letters
    def test_ascii_uppercase(self):
        self.assertEqual(string.ascii_uppercase, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Check if string.digits returns all ASCII digits
    def test_digits(self):
        self.assertEqual(string.digits, '0123456789')
    
    # Check if a lowercase string is correctly converted to uppercase
    def test_to_uppercase(self):
        word = "dorian".upper()
        self.assertEqual(word, "DORIAN")

    # Check if a lowercase string with spaces is correctly converted to uppercase
    def test_to_uppercase_with_space(self):
        word = "dor ian".upper()
        self.assertEqual(word, "DOR IAN")

    # Check if a sentence is correctly split into an array of words
    # The length of the array should be greater than 1
    def test_split(self):
        sentence = "Hello i'm software engineer at Google"
        splited = sentence.split(" ")
        self.assertGreater(len(splited),1)
        self.assertEqual(len(splited), 6)

    # Check if an array of words is correctly joined into a sentence
    # The length of the sentence should be greater than the length of the array
    def test_join(self):
        splited = ['Hello', "i'm", 'software', 'engineer']
        sentence = " ".join(splited)
        self.assertLess(len(splited), len(sentence))