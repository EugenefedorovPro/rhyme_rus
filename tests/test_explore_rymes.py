from rhyme_rus.utils.explore_rhymes import ExploreRhymes
from rhyme_rus.rhyme import rhyme
import dill


word = "ромб"
romb_table = rhyme(word)


def test_find_rhymes_by_score():
    short_table = ExploreRhymes.find_rhymes_by_score(10, romb_table)
    with open("test_explore_rhymes/test_find_rhymes_by_score.pkl", "rb") as f:
        assert dill.load(f).equals(short_table)


def test_find_rhymes_by_pos():
    short_table = ExploreRhymes.find_rhymes_by_pos("adv", romb_table)
    with open("test_explore_rhymes/test_find_rhymes_by_pos.pkl", "rb") as f:
        assert dill.load(f).equals(short_table)


def test_rhymes_by_pattern():
    pat = ('same_cons', 'same_stressed_v', 'same_cons', 'same_cons')
    short_table = ExploreRhymes.find_rhymes_by_pattern(pat, romb_table)
    with open("test_explore_rhymes/test_find_rhymes_by_pattern.pkl", "rb") as f:
        assert dill.load(f).equals(short_table)


def test_find_rhymes_by_word():
    short_table = ExploreRhymes.find_rhymes_by_word("тромб", romb_table)
    with open("test_explore_rhymes/test_find_rhymes_by_word.pkl", "rb") as f:
        dill.load(f).equals(short_table)




