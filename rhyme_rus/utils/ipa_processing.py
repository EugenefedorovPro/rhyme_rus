from ipapy import UNICODE_TO_IPA
from ipapy.ipastring import IPAString
import dill
from pathlib import Path
from typing import Union


class IpaProcessing:
    def __init__(self):
        self.unique_unicodes: list[str] = []
        self.sign2number: dict[ipapy.ipachar, int] = {}
        self.number2sign: dict[int, ipapy.ipachar] = {}
        self.max_length_ipa = 25
        self.__get_unique_unicodes()
        self.__get_sign2number()
        self.__get_number2sign()

    def __get_unique_unicodes(self) -> None:
        path: Union[pathlib.Path, str] = Path(__file__).parent.parent / "data//list_unique_unicodes.pkl"
        with open(path, "rb") as f:
            self.unique_unicodes: list[str] = dill.load(f)
            self.unique_unicodes.sort()
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

    # Note! func does not accent stress mark
    def uni_string_to_int(self, uni_str: str) -> list[int]:
        ipa_str: ipapy.ipachar = IPAString(unicode_string=uni_str)
        uni_as_numbers: list[int] = []
        ch: ipapy.ipachar
        for ch in ipa_str:
            n: int = self.sign2number[ch]
            uni_as_numbers.append(n)
        return uni_as_numbers

    def int_to_ipa_string(self, numbers: list[int]):
        ipa_str = []
        for i in numbers:
            ipa_str.append(self.number2sign[i])
        ipa_str = IPAString(ipa_chars=ipa_str)
        return ipa_str

    # @classmethod
    # @lru_cache
    # def generate_all_chars(cls):
    #     list_unique_unicodes = cls.get_list_unique_unicodes()
    #     all_chars = IPAString(unicode_string="".join(list_unique_unicodes))
    #     return all_chars
