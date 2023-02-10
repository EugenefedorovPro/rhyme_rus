import dill
from rhyme_rus.utils.pattern_score import PatternScore

word_intipa = [6, 34, 26]  # дом
list_intipa = [[24, 34, 26], [22, 78, 47]]  # лом, лёд


def test_get_patterns():
    actual = PatternScore(word_intipa=word_intipa, list_intipa=list_intipa).get_patterns()
    path = "./test_pattern/test_pattern.pkl"
    with open(path, "rb") as f:
        expected = dill.load(f)
    assert actual == expected


def test_get_score():
    actual = PatternScore(word_intipa=word_intipa, list_intipa=list_intipa).get_scores()
    path = "./test_score/test_score.pkl"
    with open(path, "rb") as f:
        expected = dill.load(f)
    assert actual == expected
