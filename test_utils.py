import unittest
from utils import find_word_in_sentence_with_regex, find_word_in_sentence
import re

class TestFindWordInSentence(unittest.TestCase):

    # Check if a word is correctly found in a sentence
    def test_find_word_sentence(self):
        sentence = "Hello i'm software engineer at Google"
        word = "software"
        self.assertTrue(find_word_in_sentence(word, sentence))

    # Check if a word is correctly found in a sentence, even if it's uppercase
    def test_find_word_sentence_case_sensible(self):
        sentence = "Hello i'm software engineer at Google"
        word = "SOFTWARE"
        self.assertTrue(find_word_in_sentence(word, sentence))

    # Check if a word is correctly found in a sentence, even if it's randomly uppercase and lowercase
    def test_find_word_sentence_case_sensible_2(self):
        sentence = "HELLo i'M soFtwaRe EnGinEer AT Google"
        word = "SofTWaRe"
        self.assertTrue(find_word_in_sentence(word, sentence))

class TestFindWordInSentenceWithRegex(unittest.TestCase):

    # Check if a word is correctly found in a sentence
    def test_word_found(self):
        sentence = "Look mom i can fly now i'm software engineer"
        word = "mom"
        self.assertTrue(find_word_in_sentence_with_regex(word, sentence))
    
    # Check if a word not exist in a sentence
    def test_word_not_found(self):
        sentence = "Look mom i can fly now i'm software engineer"
        word = "cat"
        self.assertFalse(find_word_in_sentence_with_regex(word, sentence))
    
    # Check if a word is found event if is uppercase
    def test_word_found_case_insensitive(self):
        sentence = "Look mom i can fly now i'm software engineer"
        word = "FLy"
        self.assertTrue(find_word_in_sentence_with_regex(word, sentence))
    
    # Check find word with punctuation
    def test_word_found_with_punctuation(self):
        sentence = "Look mom i can fly now, i'm software engineer"
        word = "NOW"
        self.assertTrue(find_word_in_sentence_with_regex(word, sentence))

    # Check if regex provide in find_word_in_sentence_with_regex work
    def test_regex(self):
        word = "NOW"
        pattern = re.compile(r'\b{}\b'.format(word), flags=re.IGNORECASE)
        sentence = "Look mom i can fly now, i'm software engineer"

        self.assertRegex(sentence, pattern)

    