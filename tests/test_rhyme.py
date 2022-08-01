from rhyme_rus.rhyme import rhyme, rhyme_only_words
import dill
import json


def test_rhyme():
    with open("test_rhyme/test_rhyme.pkl", "rb") as f:
        assert bool(True) == dill.load(f).equals(rhyme("кот", list_score_numbers=[5]))


def test_rhyme_only_words():
    with open("test_rhyme/test_rhyme_only_words.json", "r") as f:
        assert json.load(f) == rhyme_only_words("кот", list_score_numbers=[0])
