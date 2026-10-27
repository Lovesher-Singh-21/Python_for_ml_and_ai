"""Word selection utilities for the Hangman game."""

import random

class WordBank:
    """Choose a categorized word without repeating the previous round's word."""

    ALL_CATEGORIES = "All Categories"
    WORDS = {
        "Everyday": (
            "BASKET", "BOTTLE", "CANDLE", "CHAIR", "CLOCK",
            "CUPBOARD", "DOOR", "FAN", "FLOOR", "LAMP", 
            "MIRROR", "PILLOW", "SHELF", "TABLE", "WINDOW"
        ),
        "Food": (
            "ALMOND", "BREAD", "BUTTER", "CHEESE", "CHOCOLATE",
            "EGGPLANT", "HONEY", "LEMON", "MANGO", "POTATO",
            "SALAD", "SPAGHETTI", "TOMATO", "YOGURT", "ZUCCHINI"
        ),
        "Nature": (
            "AUTUMN", "BEACH", "CLOUD", "FLOWER", "FOREST",
            "MOUNTAIN", "OCEAN", "RAINBOW", "RIVER", "SNOW", 
            "SUNSET", "TREE", "WATERFALL", "WILDFLOWER", "WINTER"
        ),
        "Technology": (
            "BROWSER", "COMPUTER", "DRONE", "HEADPHONES", "KEYBOARD",
            "LAPTOP", "MICROPHONE", "PRINTER", "ROUTER", "SMARTPHONE", 
            "TABLET", "WEBCAM", "WIRELESS", "SOFTWARE", "HARDWARE"
        )
    }

    @property
    def categories(self) -> tuple[str, ...]:
        return tuple(self.WORDS)

    def choose(
            self, category: str, previous_word: str | None = None
    ) -> tuple[str, str]:
        """Return a word and its category; reject unknown category names"""
        if category not in self.ALL_CATEGORIES and category not in self.WORDS:
            raise ValueError("Choose a category from the word bank.")

        candidates = [
            (word, group)
            for group, words in self.WORDS.items()
            if category in (self.ALL_CATEGORIES, group)
            for word in words
        ]
        alternatives = [entry for entry in candidates if entry[0] != previous_word]
        return random.choice(alternatives or candidates)