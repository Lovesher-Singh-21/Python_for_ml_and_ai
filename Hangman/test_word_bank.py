"""Tests for Hangman's word bank."""

import unittest
from unittest.mock import patch

from word_bank import WordBank


class WordBankTests(unittest.TestCase):
    def setUp(self):
        self.word_bank = WordBank()

    def test_categories_lists_all_word_groups(self):
        self.assertEqual(
            self.word_bank.categories,
            ("Everyday", "Food", "Nature", "Technology"),
        )

    def test_choose_returns_a_word_from_the_requested_category(self):
        with patch("word_bank.random.choice", side_effect=lambda choices: choices[0]):
            word, category = self.word_bank.choose("Food")

        self.assertEqual(category, "Food")
        self.assertIn(word, self.word_bank.WORDS["Food"])

    def test_choose_all_categories_returns_matching_word_and_category(self):
        with patch("word_bank.random.choice", side_effect=lambda choices: choices[-1]):
            word, category = self.word_bank.choose(WordBank.ALL_CATEGORIES)

        self.assertIn(category, self.word_bank.categories)
        self.assertIn(word, self.word_bank.WORDS[category])

    def test_choose_excludes_previous_word_when_alternatives_exist(self):
        previous_word = self.word_bank.WORDS["Food"][0]
        with patch("word_bank.random.choice", side_effect=lambda choices: choices[0]):
            word, category = self.word_bank.choose("Food", previous_word)

        self.assertNotEqual(word, previous_word)
        self.assertEqual(category, "Food")

    def test_choose_reuses_previous_word_when_it_is_the_only_candidate(self):
        self.word_bank.WORDS = {"Food": ("BREAD",)}

        with patch("word_bank.random.choice", return_value=("BREAD", "Food")):
            self.assertEqual(self.word_bank.choose("Food", "BREAD"), ("BREAD", "Food"))

    def test_choose_rejects_unknown_category(self):
        with self.assertRaisesRegex(ValueError, "Choose a category"):
            self.word_bank.choose("Unknown")


if __name__ == "__main__":
    unittest.main()
