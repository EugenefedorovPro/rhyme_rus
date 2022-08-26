from rhyme_rus.utils.dictionary_processing import DictionaryProcessing


def test_get_unique_of_all_int_from_dict():
    with open("tests/test_dictionary_processing/get_unique_of_all_int_from_dict.txt", "r") as f:
        unique_of_all_int_from_dict = f.read()
    assert unique_of_all_int_from_dict == str(DictionaryProcessing.get_unique_of_all_int_from_dict())


def test_make_dict_of_int_from_ipa():
    with open("tests/test_dictionary_processing/make_dict_of_int_from_ipa.txt", "r") as f:
        dict_of_int_from_ipa = f.read()
    assert dict_of_int_from_ipa == str(list(DictionaryProcessing.make_dict_of_int_from_ipa()))

