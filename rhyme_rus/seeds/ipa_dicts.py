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
        self.numbers_vowels: tuple[int]
        self.stress_ipa = UNICODE_TO_IPA["ˈ"]
        self.trans_uni: str = ''
        self.__get_unique_unicodes()
        self.__get_sign2number()
        self.__get_number2sign()
        self.__get_number_vowels()

    # func does not work with stress mark
    def int_to_ipa_string(self, numbers: list[int]) -> ipapy.ipastring:
        ipa_str: ipapy.ipastring = []
        for i in numbers:
            ipa_str.append(self.number2sign[i])
        ipa_str = IPAString(ipa_chars=ipa_str)
        return ipa_str

    def __get_unique_unicodes(self) -> None:
        path: Union[pathlib.Path, str] = Path(__file__).parent.parent / "data//list_unique_unicodes.pkl"
        with open(path, "rb") as f:
            self.unique_unicodes: list[str] = dill.load(f)
            self.unique_unicodes.sort()
            self.unique_unicodes = tuple(self.unique_unicodes)
            return None

    def __get_sign2number(self) -> None:
        self.sign2number: dict[ipapy.ipachar, int] = dict(
            (UNICODE_TO_IPA[l], i) for i, l in enumerate(self.unique_unicodes, start=1)
        )
        return None

    def __get_number2sign(self) -> None:
        self.number2sign: dict[int, ipapy.ipachar] = dict(
            (i, UNICODE_TO_IPA[l]) for i, l in enumerate(self.unique_unicodes, start=1)
        )
        return None

    def __get_number_vowels(self) -> None:
        self.number_vowels = [self.sign2number[sign] for sign in self.sign2number if sign.is_vowel]
        return None