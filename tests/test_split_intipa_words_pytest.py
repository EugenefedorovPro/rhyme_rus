import dill
from rhyme_rus.utils.split_all_intipa_words import SplitIntipaWords

all_stresses: list[str] = ["но'жик"]
stressed_word: str = "но'жик"
intipa: list[int] = [0, 1, 2, 3, 4]
stressed_vowel: int = 1
near_stressed_v: int = 9
index_stressed_v: int = 1
all_intipa_words: dict[tuple[int], list[str]] = {
    (5, 6, 7): ["to"],
    (8, 9, 10): ["be"],
    (11, 12, 13): ["or"],
    (14, 15, 16): ["not"],
    (17, 18, 19): ["be"],
    (5, 6, 7, 8): ["to"],
    (8, 9, 10, 9): ["be"],
    (11, 12, 13, 10): ["or"],
    (14, 15, 16, 11): ["not"],
    (17, 18, 19, 12): ["be"],
    (5, 6, 7, 13): ["to"],
    (8, 9, 10, 14): ["be"],
    (11, 12, 13, 15): ["or"],
    (14, 15, 16, 16): ["not"],
    (17, 18, 19, 17): ["be"],
    (5, 6, 7, 18): ["to"],
    (8, 9, 10, 19): ["be"],
    (11, 12, 13, 20): ["or"],
    (14, 15, 16, 21): ["not"],
    (17, 18, 19, 22): ["be"]
    }


def test_split_intipa_words():
    with open("test_split_intipa_words/test_split_intipa_words.pkl", "rb") as f:
        expected = dill.load(f)

    siw = SplitIntipaWords(
        all_stresses,
        stressed_word,
        intipa,
        stressed_vowel,
        near_stressed_v,
        index_stressed_v,
        all_intipa_words
        )
    actual = siw.split_intipa_words()
    assert actual == expected
