import dill
from rhyme_rus.rhyme import rhyme


def test_rhyme():
    with open("tests/test_rhyme/test_rhyme.pkl", "rb") as f:
        assert bool(True) == dill.load(f).equals(rhyme("ко'т", list_score_numbers=[5]))
