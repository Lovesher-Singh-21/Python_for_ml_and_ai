# Hangman word bank

This folder contains the word-selection component for the Hangman game.

## Usage

From this folder, import and use the `WordBank` class:

```python
from word_bank import WordBank

bank = WordBank()
print(bank.categories)
word, category = bank.choose("Food")
print(f"{word} ({category})")
```

Pass `WordBank.ALL_CATEGORIES` to choose from any category. The optional
`previous_word` argument prevents the same word from being chosen again when
other candidates are available. An unknown category raises `ValueError`.

## Tests

The project uses only the Python standard library. Run its tests from this
folder with:

```text
python -m unittest -v
```
