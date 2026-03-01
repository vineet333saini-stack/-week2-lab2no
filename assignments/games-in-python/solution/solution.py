import random
from typing import List, Set


def choose_word(words: List[str]) -> str:
    return random.choice(words)


def reveal_progress(secret: str, guessed: Set[str]) -> str:
    return ' '.join([c if c in guessed else '_' for c in secret])


def update_guessed(secret: str, guessed: Set[str], letter: str) -> bool:
    letter = letter.lower()
    if letter in guessed:
        return letter in secret
    guessed.add(letter)
    return letter in secret


def is_won(secret: str, guessed: Set[str]) -> bool:
    return all(c in guessed for c in secret)


def play_hangman(words: List[str], max_incorrect: int = 6) -> None:
    secret = choose_word(words)
    guessed: Set[str] = set()
    incorrect = 0
    while True:
        print(reveal_progress(secret, guessed))
        guess = input("Guess a letter: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        hit = update_guessed(secret, guessed, guess)
        if not hit and guess not in secret:
            incorrect += 1
            print(f"Incorrect guesses: {incorrect}/{max_incorrect}")
        if is_won(secret, guessed):
            print(f"You won! The word was: {secret}")
            break
        if incorrect >= max_incorrect:
            print(f"You lost. The word was: {secret}")
            break


if __name__ == "__main__":
    WORDS = ["python", "hangman", "challenge", "programming", "computer"]
    play_hangman(WORDS)
