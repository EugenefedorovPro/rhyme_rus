from functools import lru_cache
from wiktionary_rus.wiktionary import wiki_instances


class DictionaryProcessing:
    @classmethod
    @lru_cache
    def get_unique_of_all_int_from_dict(cls):
        tuple_of_all_int_from_dict = tuple(
            [tuple(item.intipa) for item in wiki_instances if item.intipa]
        )
        unique_of_all_int_from_dict = set(tuple_of_all_int_from_dict)
        return unique_of_all_int_from_dict

    @classmethod
    @lru_cache
    def make_dict_of_int_from_ipa(cls):
        dict_of_int_from_ipa = dict()
        for item in wiki_instances:
            if item.intipa:
                key = tuple(item.intipa)
                if key not in dict_of_int_from_ipa:
                    dict_of_int_from_ipa[key] = tuple(list([item]))
                else:
                    value = list(dict_of_int_from_ipa[key])
                    value.append(item)
                    dict_of_int_from_ipa[key] = tuple(value)
        return dict_of_int_from_ipa
