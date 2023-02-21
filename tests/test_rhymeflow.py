from rhyme_rus.utils.rhymeflow import RhymeFlow


def test_generate_indexes_before_add_no():
    ipa_short_int = [6, 34, 26, 71, 56]
    pat = ["same_cons", "same_stressed_v", "add_sound", "same_cons", "no_sound", "palatal_cons"]
    assert [2], [4] == RhymeFlow.generate_indexes_before_add_no(pat)


def test_shorten_prolong_ipa():
    ipa_short_int = [6, 34, 26, 71, 56]
    indexes_add_sound = [2]
    indexes_no_sound = [4]
    assert [6, 34, 0, 26, 56] == RhymeFlow.shorten_prolong_ipa(ipa_short_int,
                                                               indexes_add_sound,
                                                               indexes_no_sound)


def test_remove_no_sound_pat():
    pat = ["same_cons", "same_stressed_v", "add_sound", "same_cons", "no_sound", "palatal_cons"]
    assert ["same_cons", "same_stressed_v", "add_sound", "same_cons", "palatal_cons"] \
           == RhymeFlow.remove_no_sound_pat(pat)


def test_generate_indexes_after_add_no():
    new_working_pat = ["any_cons", "same_stressed_v", "add_cons",
                       "near_stressed_v", "palatal_cons", "any_v",
                       "voice_cons"]
    assert ([1, 2], [3], [4], [6], [0], [5]) == RhymeFlow.generate_indexes_after_add_no(new_working_pat)


def test_find_indexes_same():
    indexes_same = [0, 2]
    indexes_same_empty = []
    ipa_short_int_new = [21, 22, 23, 24]
    _intipa_true = [20, 10, 23, 11]
    _intipa_false = [21, 10, 23, 11]
    assert bool(False) == RhymeFlow.find_indexes_same(indexes_same_empty, ipa_short_int_new, _intipa_true)
    assert bool(True) == RhymeFlow.find_indexes_same(indexes_same, ipa_short_int_new, _intipa_true)
    assert bool(False) == RhymeFlow.find_indexes_same(indexes_same, ipa_short_int_new, _intipa_false)


def test_find_near_stressed_v():
    indexes_near_stressed_v = [0, 2]
    indexes_near_stressed_v_empty = []
    ipa_short_int_new = [1, 22, 12, 24]
    _intipa_true = [20, 10, 23, 11]
    _intipa_false = [67, 10, 72, 11]

    assert bool(False) == RhymeFlow.find_near_stressed_v(indexes_near_stressed_v_empty,
                                                         ipa_short_int_new, _intipa_false)

    assert bool(True) == RhymeFlow.find_near_stressed_v(indexes_near_stressed_v,
                                                        ipa_short_int_new, _intipa_true)

    assert bool(False) == RhymeFlow.find_near_stressed_v(indexes_near_stressed_v,
                                                         ipa_short_int_new, _intipa_false)


def test_find_palatal_cons():
    indexes_palatal_cons = [0, 2]
    indexes_palatal_cons_empty = []
    ipa_short_int_new = [33, 22, 38, 24]
    _intipa_true = [20, 10, 23, 11]
    _intipa_false = [32, 10, 37, 11]

    assert bool(False) == RhymeFlow.find_palatal_cons(indexes_palatal_cons,
                                                      ipa_short_int_new, _intipa_false)
    assert bool(True) == RhymeFlow.find_palatal_cons(indexes_palatal_cons,
                                                     ipa_short_int_new, _intipa_true)
    assert bool(False) == RhymeFlow.find_palatal_cons(indexes_palatal_cons_empty,
                                                      ipa_short_int_new, _intipa_true)


def test_find_voice_cons():
    indexes_voice_cons = [0, 2]
    indexes_voice_cons_empty = []
    ipa_short_int_new = [14, 22, 20, 24]
    _intipa_true = [20, 10, 23, 11]
    _intipa_false = [58, 10, 74, 11]

    assert bool(False) == RhymeFlow.find_voice_cons(indexes_voice_cons,
                                                    ipa_short_int_new, _intipa_false)
    assert bool(True) == RhymeFlow.find_voice_cons(indexes_voice_cons,
                                                   ipa_short_int_new, _intipa_true)
    assert bool(False) == RhymeFlow.find_voice_cons(indexes_voice_cons_empty,
                                                    ipa_short_int_new, _intipa_true)


def test_find_any_cons():
    indexes_any_cons = [0, 2]
    indexes_any_cons_empty = []
    ipa_short_int_new = [2, 22, 4, 24]
    ipa_short_int_new_2 = [16, 22, 9, 24]
    _intipa_true = [2, 10, 23, 11]
    _intipa_false = [58, 10, 74, 11]
    _intipa_true_2 = [16, 10, 9, 11]

    assert bool(False) == RhymeFlow.find_any_cons(indexes_any_cons,
                                                  ipa_short_int_new, _intipa_false)
    assert bool(True) == RhymeFlow.find_any_cons(indexes_any_cons,
                                                 ipa_short_int_new, _intipa_true)
    assert bool(False) == RhymeFlow.find_any_cons(indexes_any_cons_empty,
                                                  ipa_short_int_new, _intipa_true)

    assert bool(True) == RhymeFlow.find_any_cons(indexes_any_cons,
                                                 ipa_short_int_new_2, _intipa_true_2)


def test_find_any_v():
    indexes_any_v = [0, 2]
    indexes_any_v_empty = []
    ipa_short_int_new = [1, 22, 12, 24]
    _intipa_true = [2, 10, 12, 11]
    _intipa_false = [71, 10, 83, 11]

    assert bool(False) == RhymeFlow.find_any_v(indexes_any_v,
                                               ipa_short_int_new, _intipa_false)
    assert bool(True) == RhymeFlow.find_any_v(indexes_any_v,
                                              ipa_short_int_new, _intipa_true)
    assert bool(False) == RhymeFlow.find_any_v(indexes_any_v_empty,
                                               ipa_short_int_new, _intipa_true)


def test_rhymes_by_pat():
    ipa_short_int_new = [24, 34, 47]
    tuple_indexes = ([1, 2], [], [], [], [0], [])
    new_working_pat = ["any_cons", "same_stressed_v", "same"]
    assert [(6, 34, 47), (46, 34, 47), (13, 34, 47), (47, 34, 47), (39, 34, 47),
            (18, 34, 47), (79, 34, 47), (43, 34, 47), (57, 34, 47), (84, 34, 47),
            (63, 34, 47), (85, 34, 47), (61, 34, 47), (26, 34, 47), (30, 34, 47),
            (35, 34, 47), (60, 34, 47), (2, 34, 47), (73, 34, 47)] \
           == RhymeFlow.rhymes_by_pat(ipa_short_int_new, new_working_pat, tuple_indexes)
