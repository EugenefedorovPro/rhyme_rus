import dill
from rhyme_rus.utils.table_long import get_table_long


def test_table_long():
    score_pattern_rhyme: dict[str: list[int], str: list[int], str: list[tuple[str], str: list[str]]]
    score_pattern_rhyme = {"score": [0, 3, 4],
                           "assonance": [0, 1, 2],
                           "pattern": [("any", "any", "any"), ("any", "any", "any"), ("any", "any", "any")],
                           "rhyme": ["time", "to", "go"]
                           }
    actual = get_table_long(score_pattern_rhyme)
    with open("test_table_long/test_table_long.pkl", "rb") as f:
        expected = dill.load(f)
    assert actual.equals(expected)
