import dill
from rhyme_rus.utils.pattern import Pattern


def test_get_all_rhymes_patterns():
    word_intipa = [6, 34, 26]  # дом
    list_intipa = [[24, 34, 26], [22, 78, 47]]  # лом, лёд
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_rhymes_patterns()

    with open("test_pattern/test_pattern.pkl", "rb") as f:
        expected = dill.load(f)

    assert expected == all_rhymes_patterns
