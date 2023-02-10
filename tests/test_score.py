import dill
from rhyme_rus.utils.score import Score


def test_get_all_rhymes_patterns():
    word_intipa = [6, 34, 26]  # дом
    list_intipa = [[24, 34, 26], [22, 78, 47]]  # лом, лёд
    all_rhymes_score = Score(word_intipa=word_intipa, list_intipa=list_intipa).get_all_rhymes_scores()

    with open("test_score/test_score.pkl", "rb") as f:
        expected = dill.load(f)

    assert expected == all_rhymes_score
