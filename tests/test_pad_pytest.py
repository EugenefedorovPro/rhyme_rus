import pytest
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.utils.pad import Pad


def test_pads_dict_rhyme_equal() -> None:
    intipa = [43, 34, 30]
    all_intipa_words: dict[tuple[int, ...], set[str]] = {(43, 34, 26):{'any'}}
    stressed_vowel = 34
    near_stressed_v = IpaDicts().near_stressed_v_int[stressed_vowel]
    index_stressed_v = 1
    expected_pads_dict = {
        (43, 34, 26):[(43, 34, 26)]
    }
    actual_pads_dict = Pad(intipa, all_intipa_words, stressed_vowel,
                           near_stressed_v, index_stressed_v).get_all_pads_dict()
    assert expected_pads_dict == actual_pads_dict
def test_pads_dict_rhyme_shorter() -> None:
    intipa = [43, 34, 30, 34, 30]
    all_intipa_words: dict[tuple[int, ...], set[str]] = {(43, 34, 30): {'any_0', "any_1"}}
    stressed_vowel = 34
    near_stressed_v = IpaDicts().near_stressed_v_int[stressed_vowel]
    index_stressed_v = 1
    expected_pads_dict = {
        (43, 34, -2, -2, 30): [(43, 34, 30)],
        (43, 34, -2, 30, -2): [(43, 34, 30)],
        (43, 34, 30, -2, -2): [(43, 34, 30)]
    }
    actual_pads_dict = Pad(intipa, all_intipa_words, stressed_vowel,
                           near_stressed_v, index_stressed_v).get_all_pads_dict()
    assert expected_pads_dict == actual_pads_dict

def test_pads_dict_rhyme_longer() -> None:
    intipa = [43, 34, 30]
    all_intipa_words: dict[tuple[int, ...], set[str]] = {(43, 34, 30, 34, 45): {'any_0', "any_1"}}
    stressed_vowel = 34
    near_stressed_v = IpaDicts().near_stressed_v_int[stressed_vowel]
    index_stressed_v = 1
    expected_pads_dict = {
        (43, 34, -1, -1, 45): [(43, 34, 30, 34, 45)],
        (43, 34, -1, 34, -1): [(43, 34, 30, 34, 45)],
        (43, 34, 30, -1, -1): [(43, 34, 30, 34, 45)]
    }
    actual_pads_dict = Pad(intipa, all_intipa_words, stressed_vowel,
                           near_stressed_v, index_stressed_v).get_all_pads_dict()
    assert expected_pads_dict == actual_pads_dict
def test_pads_dict_rhyme_no_init() -> None:
    intipa = [43, 34, 30]
    all_intipa_words: dict[tuple[int, ...], set[str]] = {(34, 30):{'any'}}
    stressed_vowel = 34
    near_stressed_v = IpaDicts().near_stressed_v_int[stressed_vowel]
    index_stressed_v = 1
    expected_pads_dict = {
        (-3, 34, 30): [(34, 30)]
    }
    actual_pads_dict = Pad(intipa, all_intipa_words, stressed_vowel,
                           near_stressed_v, index_stressed_v).get_all_pads_dict()
    assert expected_pads_dict == actual_pads_dict
def test_pads_dict_rhyme_no_init_rhyme_longer() -> None:
    intipa = [43, 34, 30]
    all_intipa_words: dict[tuple[int, ...], set[str]] = {(34, 30, 32): {'any_0', "any_1"}}
    stressed_vowel = 34
    near_stressed_v = IpaDicts().near_stressed_v_int[stressed_vowel]
    index_stressed_v = 1
    expected_pads_dict = {
        (-3, 34, -1, 32): [(34, 30, 32)], (-3, 34, 30, -1): [(34, 30, 32)]
    }
    actual_pads_dict = Pad(intipa, all_intipa_words, stressed_vowel,
                           near_stressed_v, index_stressed_v).get_all_pads_dict()
    assert expected_pads_dict == actual_pads_dict
def test_pads_dict_word_no_init_rhyme_longer() -> None:
    intipa = [34, 30, 41]
    all_intipa_words: dict[tuple[int, ...], set[str]] = {(43, 34, 30, 32): {'any_0', "any_1"}}
    stressed_vowel = 34
    near_stressed_v = IpaDicts().near_stressed_v_int[stressed_vowel]
    index_stressed_v = 0
    expected_pads_dict = {
        (-4, 34, 30, 32): [(43, 34, 30, 32)]
    }
    actual_pads_dict = Pad(intipa, all_intipa_words, stressed_vowel,
                           near_stressed_v, index_stressed_v).get_all_pads_dict()
    assert expected_pads_dict == actual_pads_dict


@pytest.mark.parametrize("intipa, all_intipa_words, stressed_vowel, near_stressed_v, index_stressed_v, expected_pads_dict", [
    (
        [43, 34, 45],
        {(43, 78, 30): {'any_0', "any_1"}},
        34,
        IpaDicts().near_stressed_v_int[34],
        1,
        {(43, 78, 30): [(43, 78, 30)]}
    ),
    (
            [43, 34, 45],
            {(43, 78, 30, 67): {'any_0', "any_1"}},
            34,
            IpaDicts().near_stressed_v_int[34],
            1,
            {(43, 78, -1, 67): [(43, 78, 30, 67)], (43, 78, 30, -1): [(43, 78, 30, 67)]}
    ),
    (
            [43, 34, 45, 67],
            {(43, 78, 30): {'any_0', "any_1"}},
            34,
            IpaDicts().near_stressed_v_int[34],
            1,
            {(43, 78, -2, 30): [(43, 78, 30)], (43, 78, 30, -2): [(43, 78, 30)]}
    ),
    (
            [34, 45, 67],
            {(43, 78, 30): {'any_0', "any_1"}},
            34,
            IpaDicts().near_stressed_v_int[34],
            0,
            {(-4, 78, -2, 30): [(43, 78, 30)], (-4, 78, 30, -2): [(43, 78, 30)]}
    ),
    (
            [43, 34, 45, 67],
            {(78, 30): {'any_0', "any_1"}},
            34,
            IpaDicts().near_stressed_v_int[34],
            1,
            {(-3, 78, -2, 30): [(78, 30)], (-3, 78, 30, -2): [(78, 30)]}
    )
]
                         )

def test_pads_dict_near_stressed(intipa, all_intipa_words, stressed_vowel, near_stressed_v, index_stressed_v, expected_pads_dict):
    actual_pads_dict = Pad(intipa, all_intipa_words, stressed_vowel,
                           near_stressed_v, index_stressed_v).get_all_pads_dict()
    assert expected_pads_dict == actual_pads_dict
