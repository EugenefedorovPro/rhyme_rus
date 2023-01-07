from functools import lru_cache
from pathlib import Path
import dill
import sqlite3
from typing import List, Tuple, AnyStr, Union
from rhyme_rus.utils.exec_query import ExecQuery


class DictionaryProcessing:
    List_None = Union[List[Tuple[AnyStr, AnyStr]], None]

    @classmethod
    def find_accent_from_wiki(cls, word_without_stress: str) -> List_None:
        path = "./rhyme_rus/data/word_accent.sqlite3"
        my_query = f"""select * from word_accent
                    where word_lowcase = '{word_without_stress}'
        """
        output: Union[list, None] = ExecQuery.exec_with_output(path, my_query)
        if output:
            return output
        else:
            print("query returned None")
            return None

    @classmethod
    @lru_cache
    def get_dict_word_accent(cls):
        path_dict_word_accent = (
            Path(__file__).parent.parent / "data//dict_word_accent.pkl"
        )
        with open(path_dict_word_accent, "rb") as f:
            dict_word_accent = dill.load(f)
        return dict_word_accent

    @classmethod
    @lru_cache
    def get_unique_of_all_int_from_dict(cls):
        path = Path(__file__).parent.parent / \
            "data//unique_of_all_int_from_dict.pkl"
        with open(path, "rb") as f:
            unique_of_all_int_from_dict = dill.load(f)
        return unique_of_all_int_from_dict

    @classmethod
    @lru_cache
    def make_dict_of_int_from_ipa(cls):
        path = Path(__file__).parent.parent / \
            "data//dict_of_int_from_ipa_short.pkl"
        with open(path, "rb") as f:
            dict_of_int_from_ipa = dill.load(f)
        return dict_of_int_from_ipa

    @classmethod
    @lru_cache
    def get_ipa_short_int_from_wiki(cls, word_with_stress):
        path = Path(__file__).parent.parent / "data//dict_accent_int.pkl"
        with open(path, "rb") as f:
            dict_accent_int = dill.load(f)
        ipa_short_int = dict_accent_int[word_with_stress]
        return ipa_short_int
