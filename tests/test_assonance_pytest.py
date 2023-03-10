from rhyme_rus.utils.assonance import Assonance


def test_assonance():
    test_unstressed_word = "дом"
    test_score_pattern_rhyme: dict[str: list[int], str: list[tuple[str], str: list[str]]]
    test_score_pattern_rhyme = {
        "score": [0, 3, 5],
        "pattern": [(0, 0, 0), (0, 0, 0)],
        "rhyme": ["управдом", "кот", "слоту"]
    }
    actual = Assonance(unstressed_word = test_unstressed_word,
                       score_pattern_rhyme = test_score_pattern_rhyme).get_all_assonance()
    expected = [0, 1, 2]
    assert actual == expected
