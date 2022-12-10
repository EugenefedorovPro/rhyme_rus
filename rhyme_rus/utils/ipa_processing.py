from functools import lru_cache
from ipapy import UNICODE_TO_IPA
from ipapy.ipastring import IPAString
import dill
from pathlib import Path


class IpaProcessing:
    @classmethod
    @lru_cache
    def get_list_unique_unicodes(cls):
        path = Path(__file__).parent.parent / "data//list_unique_unicodes.pkl"
        with open(path, "rb") as f:
            list_unique_unicodes = dill.load(f)
        list_unique_unicodes.sort()
        return list_unique_unicodes

    @classmethod
    @lru_cache
    def get_sign2number(cls):
        list_unique_unicodes = cls.get_list_unique_unicodes()
        sign2number = dict(
            (UNICODE_TO_IPA[l], i) for i, l in enumerate(list_unique_unicodes, start=1)
        )
        return sign2number

    @classmethod
    @lru_cache
    def get_number2sign(cls):
        list_unique_unicodes = cls.get_list_unique_unicodes()
        number2sign = dict(
            (i, UNICODE_TO_IPA[l]) for i, l in enumerate(list_unique_unicodes, start=1)
        )
        return number2sign

    @classmethod
    @lru_cache
    def get_max_length_of_ipa(cls):
        max_length_of_ipa = 25
        return max_length_of_ipa

    @classmethod
    def uni_string_to_int(cls, uni_str):
        sign2number = IpaProcessing.get_sign2number()
        uni_str = IPAString(unicode_string=uni_str)
        uni_as_numbers = []
        for ch in uni_str:
            n = sign2number[ch]
            uni_as_numbers.append(n)
        return uni_as_numbers

    @classmethod
    def int_to_ipa_string(cls, int_numbers):
        number2sign = cls.get_number2sign()
        ipa_string = []
        for i in int_numbers:
            ipa_string.append(number2sign[i])
        ipa_string = IPAString(ipa_chars=ipa_string)
        return ipa_string

    @classmethod
    @lru_cache
    def generate_all_chars(cls):
        list_unique_unicodes = cls.get_list_unique_unicodes()
        all_chars = IPAString(unicode_string="".join(list_unique_unicodes))
        return all_chars
