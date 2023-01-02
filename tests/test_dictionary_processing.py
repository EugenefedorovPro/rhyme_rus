from pathlib import Path
import dill
from rhyme_rus.utils.dictionary_processing import DictionaryProcessing


def test_get_dict_word_accent():
    dict_word_accent = DictionaryProcessing.get_dict_word_accent()
    stressed_word = ("замо'к", "за'мок")
    assert dict_word_accent["замок"] == stressed_word


def test_get_unique_of_all_int_from_dict():
    unique_of_all_int_from_dict = DictionaryProcessing.get_unique_of_all_int_from_dict()
    proper_tuple = (58, 12, 16, 48, 12)
    assert proper_tuple in unique_of_all_int_from_dict


def test_make_dict_of_int_from_ipa():
    dict_of_int_from_ipa = DictionaryProcessing.make_dict_of_int_from_ipa()
    path = (
        Path.cwd()
        / "tests/test_dictionary_processing/test_make_dict_of_int_from_ipa.pkl"
    )
    with open(path, "rb") as f:
        proper_output = dill.load(f)
    test_tuple = (58, 12, 16, 48, 12)
    function_result = dict_of_int_from_ipa[test_tuple]
    assert vars(proper_output[10]) == vars(function_result[10])
