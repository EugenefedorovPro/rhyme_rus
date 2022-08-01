from rhyme_rus.utils.score import Score


def test_get_dict_score():
    dict_score = {'same_cons': 0,
                  'voice_cons': 1,
                  'palatal_cons': 2,
                  'any_cons': 3,
                  'no_sound': 4,
                  'same_v': 0,
                  'same_stressed_v': 0,
                  'near_stressed_v': 3,
                  'any_v': 4,
                  'add_sound': 5}
    assert dict_score == Score.get_dict_score()


def test_count_score_pat():
    pat_0 = ["same_cons", "same_stressed_v", "same_cons"]
    pat_15 = ["any_cons", "same_stressed_v", "same_cons"]
    pat_65 = ["any_cons", "any_v", "add_sound", "same_stressed_v", "palatal_cons"]
    assert 0 == Score.count_score_pat(pat_0)
    assert 15 == Score.count_score_pat(pat_15)
    assert 65 == Score.count_score_pat(pat_65)

