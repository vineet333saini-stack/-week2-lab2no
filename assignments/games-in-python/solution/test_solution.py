import pytest

from solution.solution import reveal_progress, update_guessed, is_won


def test_reveal_progress_empty():
    assert reveal_progress("hangman", set()) == "_ _ _ _ _ _ _"


def test_reveal_progress_some_guessed():
    assert reveal_progress("hangman", {"a", "n"}) == "_ a n _ _ a n"


def test_update_guessed_and_win():
    guessed = set()
    # correct guess
    assert update_guessed("hi", guessed, "h") is True
    # incorrect guess
    assert update_guessed("hi", guessed, "x") is False
    # win condition
    assert is_won("hi", {"h", "i"}) is True
