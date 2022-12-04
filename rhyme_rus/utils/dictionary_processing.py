from functools import lru_cache

# from wiktionary_rus.wiktionary import wiki_instances
import dill


class DictionaryProcessing:
    @classmethod
    @lru_cache
    def get_unique_of_all_int_from_dict(cls):
        path = "rhyme_rus//data//unique_of_all_int_from_dict.pkl"
        with open(path, "rb") as f:
            unique_of_all_int_from_dict = dill.load(f)
        return unique_of_all_int_from_dict

    @classmethod
    @lru_cache
    def make_dict_of_int_from_ipa(cls):
        path = "rhyme_rus//data//dict_of_int_from_ipa.pkl"
        with open(path, "rb") as f:
            dict_of_int_from_ipa = dill.load(f)
        return dict_of_int_from_ipa
