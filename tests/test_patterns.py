import pytest
from wiktionary_rus.wiktionary import find_item_from_wiki
from rhyme_rus.utils.patterns import Patterns


def test_ipa_short_int():
    assert [6, 34, 26] == find_item_from_wiki("до'м")[0].intipa


def test_take_pat_of_ipa():
    pat = ["cons", "stress_v", "cons"]
    assert pat == Patterns.take_pat_of_ipa([6, 34, 26])


def test_shorten_pat_long_words_to_head_tail():
    word = "отта'лкивающий"
    ipa_short_int = find_item_from_wiki(word)[0].intipa
    pat_of_ipa = Patterns.take_pat_of_ipa(ipa_short_int)
    head, tail = Patterns.shorten_pat_long_words_to_head_tail(
        pat_of_ipa, max_length_pat_of_ipa=8
    )
    assert [
        "cons",
        "stress_v",
        "cons",
        "cons",
        "vowel",
        "cons",
        "vowel",
        "cons",
    ] == head
    assert ["vowel", "cons", "vowel", "cons"] == tail


def test_convert_tail_to_pattern():
    tail = ["vowel", "cons", "vowel", "cons"]
    assert [
        "same_v",
        "same_cons",
        "same_v",
        "same_cons",
    ] == Patterns.convert_tail_to_pattern(tail)


def test_add_tail_to_pats():
    all_rhyme_pats = [["add_sound", "same_stressed_v"]]
    tail_to_pattern = ["same_cons", "same_v"]
    assert [["add_sound", "same_stressed_v", "same_cons", "same_v"]] == list(
        Patterns.add_tail_to_pats(all_rhyme_pats, tail_to_pattern)
    )


def test_check_if_voice_palatal():
    pat_true = ["voice_cons", "same_stressed_v", "palatal_cons"]
    pat_false = ["voice_cons", "same_stressed_v", "voice_cons"]
    ipa_short_int = find_item_from_wiki("до'м")[0].intipa
    assert bool(True) == Patterns.check_if_voice_palatal(ipa_short_int, pat_true)
    assert bool(False) == Patterns.check_if_voice_palatal(ipa_short_int, pat_false)

    ipa_short_int = find_item_from_wiki("ра'б")[0].intipa
    pat_false = ["voice_cons", "same_stressed_v", "palatal_cons"]
    assert bool(False) == Patterns.check_if_voice_palatal(ipa_short_int, pat_false)

    with pytest.raises(Exception) as exc:
        ipa_short_int = find_item_from_wiki("до'м")[0].intipa
        pat_exception = ["voice_cons", "same_stressed_v"]
        Patterns.check_if_voice_palatal(ipa_short_int, pat_exception)
        assert "Pat and ipa_short_int of different lengths" == str(exc.value)


def test_check_n_mutations():
    pat_true_1 = ["no_sound", "no_sound"]
    pat_true_2 = ["voice_cons"]
    pat_false_1 = ["any_cons", "any_cons"]
    pat_false_2 = ["palatal_cons", "palatal_cons", "palatal_cons"]
    pat_false_3 = ["any_v", "any_v"]
    assert bool(True) == Patterns.check_n_mutations(
        pat_true_1, max_number_hard_sounds_in_one_pat=2
    )
    assert bool(True) == Patterns.check_n_mutations(pat_true_2)
    assert bool(False) == Patterns.check_n_mutations(pat_false_1)
    assert bool(False) == Patterns.check_n_mutations(pat_false_2)
    assert bool(False) == Patterns.check_n_mutations(pat_false_3)


def test_condition_all_rhyme_pats():
    ipa_short_int = find_item_from_wiki("до'м")[0].intipa
    all_rhyme_pats_1 = [
        ["no_sound", "no_sound", "any_cons"],
        ["voice_cons", "same_stressed_v", "palatal_cons"],
    ]
    all_rhyme_pats_2 = [
        ["no_sound", "no_sound", "any_cons"],
        ["voice_cons", "same_stressed_v", "voice_cons"],
    ]
    assert [["voice_cons", "same_stressed_v", "palatal_cons"]] == [
        item
        for item in Patterns.condition_all_rhyme_pats(all_rhyme_pats_1, ipa_short_int)
    ]
    assert [["no_sound", "no_sound", "any_cons"]] == [
        item
        for item in Patterns.condition_all_rhyme_pats(
            all_rhyme_pats_2, ipa_short_int, max_number_hard_sounds_in_one_pat=2
        )
    ]


def test_add_sound_to_rhyme_pats():
    with open(
        "tests/test_patterns/add_sound_to_rhyme_pats.txt", "r", encoding="UTF-8"
    ) as f:
        pats = f.read()
    all_rhyme_pats_1 = [["same_cons", "same_stressed_v"]]
    assert pats == str(
        [item for item in Patterns.add_sound_to_rhyme_pats(all_rhyme_pats_1)]
    )


def test_check_add_no_sequences():
    pat_false_1 = ["add_sound", "same_stressed_v", "no_sound", "add_sound"]
    pat_false_2 = ["add_sound", "same_stressed_v", "add_sound", "no_sound"]
    pat_true_1 = ["add_sound", "same_stressed_v", "no_sound"]
    assert bool(False) == Patterns.check_add_no_sequences(pat_false_1)
    assert bool(False) == Patterns.check_add_no_sequences(pat_false_2)
    assert bool(True) == Patterns.check_add_no_sequences(pat_true_1)


def test_check_no_any_add():
    pat_false = ["any_cons", "no_sound", "any_cons", "add_sound", "same_stressed_v"]
    assert bool(False) == Patterns.check_no_any_add(pat_false)

    pat_true = ["no_sound", "any_v", "any_cons", "add_sound", "same_stressed_v"]
    assert bool(True) == Patterns.check_no_any_add(pat_true)


def test_check_first_double_cons():
    pat_false_1 = ["add_sound", "add_sound", "same_stressed_v"]
    pat_false_2 = ["any_cons", "same_cons", "near_stressed_v"]
    pat_true_1 = ["add_sound", "same_stressed_v", "no_sound"]
    assert bool(False) == Patterns.check_first_double_cons(pat_false_1)
    assert bool(False) == Patterns.check_first_double_cons(pat_false_2)
    assert bool(True) == Patterns.check_first_double_cons(pat_true_1)


def test_condition_add_sound_to_rhyme_pats():
    all_rhyme_pats = [
        ["add_sound", "no_sound", "same_stressed_v"],
        ["palatal_cons", "voice_cons", "near_stressed_v"],
        ["add_sound", "same_stressed_v", "palatal_cons"],
    ]
    assert [["add_sound", "same_stressed_v", "palatal_cons"]] == [
        pat for pat in Patterns.condition_add_sound_to_rhyme_pats(all_rhyme_pats)
    ]
