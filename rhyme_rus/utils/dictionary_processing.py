from functools import lru_cache
from pathlib import Path
import dill


class DictionaryProcessing:
    @classmethod
    @lru_cache
    def get_dict_word_accent(cls):
        path_dict_word_accent = (
            Path(__file__).parent.parent / "data//wiki_short_class.pkl"
        )
        with open(path_dict_word_accent, "rb") as f:
            dict_word_accent = dill.load(f)
        return dict_word_accent

    @classmethod
    @lru_cache
    def get_unique_of_all_int_from_dict(cls):
        path = Path(__file__).parent.parent / "data//unique_of_all_int_from_dict.pkl"
        with open(path, "rb") as f:
            unique_of_all_int_from_dict = dill.load(f)
        return unique_of_all_int_from_dict

    @classmethod
    @lru_cache
    def make_dict_of_int_from_ipa(cls):
        path = Path(__file__).parent.parent / "data//dict_of_int_from_ipa_short.pkl"
        with open(path, "rb") as f:
            dict_of_int_from_ipa = dill.load(f)
        return dict_of_int_from_ipa
