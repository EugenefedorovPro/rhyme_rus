import json
from pathlib import Path
from rhyme_rus.utils.intipa import IpaProcessing


def test_get_list_unique_unicodes():
    path = Path(__file__).parent / "test_ipa_processing" / "get_list_unique_unicodes.json"
    with open(path, 'r') as f:
        list_unique_unicodes = json.load(f)
    assert list_unique_unicodes == IpaProcessing.get_list_unique_unicodes()


def test_get_sign2number():
    path = Path(__file__).parent / "test_ipa_processing" / "__get_sign2number.json"
    with open(path, "r") as f:
        sign2number = json.load(f)
    assert sign2number == str(IpaProcessing.__get_sign2number())


def test_get_number2sign():
    path = Path(__file__).parent / "test_ipa_processing" / "__get_number2sign.json"
    with open(path, "r") as f:
        number2sign = json.load(f)
    assert number2sign == str(IpaProcessing.__get_number2sign())


def test_get_max_length_of_ipa():
    assert 25 == IpaProcessing.get_max_length_of_ipa()


def test_uni_string_to_int():
    assert [6, 34, 26] == IpaProcessing.uni_string_to_int('dom')


def test_int_to_ipa_string():
    assert 'dom' == str(IpaProcessing.int_to_ipa_string([6, 34, 26]))


def test_generate_all_chars():
    assert 85 == len(IpaProcessing.generate_all_chars())
