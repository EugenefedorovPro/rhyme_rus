import ipapy.ipastring
import ipapy.ipachar
from ipapy import UNICODE_TO_IPA
from ipapy.ipastring import IPAString
import dill
import pathlib
from pathlib import Path
from typing import Union


class IpaDicts:
    def __init__(self):
        self.unique_unicodes: list[str] = []
        self.sign2number: dict[ipapy.ipachar, int] = {}
        self.number2sign: dict[int, ipapy.ipachar] = {}
        self.max_length_ipa = 25
        self.additional_uni: list[str] = ["fʲː", "ʑː", "ˈ"]
        self.additional_ipa: list[ipapy.ipachar] = []
        self.additional_ipa2number: dict[ipapy.ipachar, int] = {}
        self.full_sign2number: dict[ipapy.ipachar, int] = {}
        self.full_number2sign: dict[int, ipapy.ipachar] = {}
        self.numbers_vowels: tuple[int] = tuple()
        self.numbers_consonants: tuple[int] = tuple()
        self.all_ipa: list[ipapy.ipachar] = []
        self.all_stressed_vowels: tuple[int] = tuple()
        self.all_ipa_vowels: list[ipapy.ipachar] = []
        self.all_ipa_consonants: list[ipapy.ipachar] = []
        self.stress_ipa = UNICODE_TO_IPA["ˈ"]
        self.trans_uni: str = ''
        self.near_stressed_v_ipa: dict[ipapy.ipachar, ipapy.ipachar] = {}
        self.near_stressed_v_int: dict[int, int] = {}
        self.__get_unique_unicodes()
        self.__get_sign2number()
        self.__get_number2sign()
        self.__get_additional_ipa()
        self.__get_additional_ipa2number()
        self.__get_full_sign2number()
        self.__get_full_number2sign()
        self.__get_numbers_vowels()
        self.__get_numbers_consonants()
        self.__get_all_ipa()
        self.__get_all_ipa_vowels()
        self.__get_all_ipa_consonants()
        self.__get_all_stressed_vowels()
        self.__get_near_stressed_v_ipa()
        self.__get_near_stressed_v_int()


    def unistring_to_numbers(self, uni_string: str):
        numbers: list[int] = []
        ipa_string = IPAString(unicode_string=uni_string)
        for sign in ipa_string:
            numbers.append(self.full_sign2number[sign])
        return numbers


    # func does not work with stress mark
    def int_to_ipa_string(self, numbers: list[int]) -> ipapy.ipastring:
        ipa_str: ipapy.ipastring = []
        for i in numbers:
            ipa_str.append(self.number2sign[i])
        ipa_str = IPAString(ipa_chars=ipa_str)
        return ipa_str


    def __get_near_stressed_v_ipa(self) -> None:
        self.near_stressed_v_ipa = {
            UNICODE_TO_IPA["a"]: UNICODE_TO_IPA["æ"],
            UNICODE_TO_IPA["æ"]: UNICODE_TO_IPA["a"],
            UNICODE_TO_IPA["ɛ"]: UNICODE_TO_IPA["e"],
            UNICODE_TO_IPA["e"]: UNICODE_TO_IPA["ɛ"],
            UNICODE_TO_IPA["i"]: UNICODE_TO_IPA["ɨ"],
            UNICODE_TO_IPA["ɨ"]: UNICODE_TO_IPA["i"],
            UNICODE_TO_IPA["o"]: UNICODE_TO_IPA["ɵ"],
            UNICODE_TO_IPA["ɵ"]: UNICODE_TO_IPA["o"],
            UNICODE_TO_IPA["u"]: UNICODE_TO_IPA["ʉ"],
            UNICODE_TO_IPA["ʉ"]: UNICODE_TO_IPA["u"],
        }

    def __get_near_stressed_v_int(self) -> None:
        for key in self.near_stressed_v_ipa:
            key_int = self.sign2number[key]
            value = self.near_stressed_v_ipa[key]
            value_int = self.sign2number[value]
            self.near_stressed_v_int[key_int] = value_int

    def __get_all_stressed_vowels(self) -> None:

        all_stressed_uni: list[ipapy.ipachar] = [
            UNICODE_TO_IPA["a"], UNICODE_TO_IPA["æ"],
            UNICODE_TO_IPA["ɛ"], UNICODE_TO_IPA["e"],
            UNICODE_TO_IPA["i"], UNICODE_TO_IPA["ɨ"],
            UNICODE_TO_IPA["o"], UNICODE_TO_IPA["ɵ"],
            UNICODE_TO_IPA["u"], UNICODE_TO_IPA["ʉ"],
        ]
        all_stressed_vowels: list[int] = []
        uni: ipapy.ipachar
        for uni in all_stressed_uni:
            all_stressed_vowels.append(self.sign2number[uni])
        self.all_stressed_vowels = tuple(all_stressed_vowels)

    def __get_unique_unicodes(self) -> None:
        path: Union[pathlib.Path, str] = Path(__file__).parent.parent / "data//list_unique_unicodes.pkl"
        with open(path, "rb") as f:
            self.unique_unicodes: list[str] = dill.load(f)
            self.unique_unicodes.sort()
            self.unique_unicodes = tuple(self.unique_unicodes)

    def __get_sign2number(self) -> None:
        self.sign2number: dict[ipapy.ipachar, int] = dict(
            (UNICODE_TO_IPA[l], i) for i, l in enumerate(self.unique_unicodes, start=1)
        )

    def __get_number2sign(self) -> None:
        self.number2sign: dict[int, ipapy.ipachar] = dict(
            (i, UNICODE_TO_IPA[l]) for i, l in enumerate(self.unique_unicodes, start=1)
        )

    def __get_additional_ipa(self) -> None:
        for uni in self.additional_uni:
            self.additional_ipa.append(UNICODE_TO_IPA[uni])

    def __get_additional_ipa2number(self):
        max_number = max(self.number2sign)
        for ipa in self.additional_ipa:
            max_number += 1
            self.additional_ipa2number[ipa] = max_number

    def __get_full_sign2number(self):
        self.full_sign2number = {**self.sign2number, **self.additional_ipa2number}


    def __get_full_number2sign(self):
        self.full_number2sign = {self.full_sign2number[sign]:sign for sign in self.full_sign2number}

    def __get_numbers_vowels(self) -> None:
        self.numbers_vowels = [self.sign2number[sign] for sign in self.sign2number if sign.is_vowel]

    def __get_numbers_consonants(self) -> None:
        self.numbers_consonants = [self.sign2number[sign] for sign in self.sign2number if sign.is_consonant]

    # TODO: make test for __IpaDict().all_ipa
    def __get_all_ipa(self) -> None:
        self.all_ipa = [sign for sign in self.sign2number]

    # TODO: make test for __IpaDict().all_ipa_vowels
    def __get_all_ipa_vowels(self) -> None:
        self.all_ipa_vowels = [sign for sign in self.sign2number if sign.is_vowel]

    # TODO: make test for __IpaDict().all_ipa_consonants
    def __get_all_ipa_consonants(self) -> None:
        self.all_ipa_consonants = [sign for sign in self.sign2number if sign.is_consonant]


if __name__ == "__main__":
    uni_string = "ɐˈprʲelʲ"
    expected_numbers = IpaDicts().unistring_to_numbers(uni_string)
    print(expected_numbers)
    # for sign in IpaDicts().full_sign2number:
    #     print(sign, sign.name)

