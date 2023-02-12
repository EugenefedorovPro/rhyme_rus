import ipapy.ipastring
from ipapy import UNICODE_TO_IPA
from ipapy.ipastring import IPAString
import dill
from pathlib import Path
from typing import Union


class IpaDicts:
    def __init__(self):
        self.unique_unicodes: tuple[str] = []
        self.sign2number: dict[ipapy.ipachar, int] = {}
        self.number2sign: dict[int, ipapy.ipachar] = {}
        self.max_length_ipa = 25
        self.numbers_vowels: tuple[int] = tuple()
        self.numbers_consonants: tuple[int] = tuple()
        self.all_ipa: list[ipapy.ipachar] = []
        self.all_stressed_vowels: tuple[int] = tuple()
        self.all_ipa_vowels: list[ipapy.ipachar] = []
        self.all_ipa_consonants: list[ipapy.ipachar] = []
        self.stress_ipa = UNICODE_TO_IPA["ˈ"]
        self.trans_uni: str = ''
        self.__get_unique_unicodes()
        self.__get_sign2number()
        self.__get_number2sign()
        self.__get_numbers_vowels()
        self.__get_numbers_consonants()
        self.__get_all_ipa()
        self.__get_all_ipa_vowels()
        self.__get_all_ipa_consonants()
        self.__get_all_stressed_vowels()

    # func does not work with stress mark
    def int_to_ipa_string(self, numbers: list[int]) -> ipapy.ipastring:
        ipa_str: ipapy.ipastring = []
        for i in numbers:
            ipa_str.append(self.number2sign[i])
        ipa_str = IPAString(ipa_chars=ipa_str)
        return ipa_str

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
