import ipapy.ipastring
from ipapy.ipastring import IPAString
import json
from rhyme_rus.seeds.mysql_connect import MySql
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from abc import ABC, abstractmethod
from typing import Optional


class AIntIpa(ABC):
    def __init__(self, stressed_word):
        self.stressed_word = stressed_word

    @abstractmethod
    def fetch_intipa(self):
        pass


class FetchIntipaFromDb(AIntIpa):

    def fetch_intipa(self) -> Optional[list[int]]:
        _query: str = f'''select intipa from  wiki_pickled where accent = "{self.stressed_word}"'''
        _mysql = MySql()
        intipa = _mysql.cur_execute(_query)
        if intipa:
            intipa = list(set(intipa))
            intipa = json.loads(intipa[0][0])
            return intipa
        else:
            return None


class FetchIntipaFromNn(AIntIpa):

    def __init__(self, stressed_word):
        super().__init__(stressed_word)
        self.ipa: ipapy.ipastring = None
        self.shortened_ipa: list[ipapy.ipastring] = []
        self.__stressed_word_to_trans_uni()
        self.__trans_uni_to_ipa()
        self.__shorten_ipa()

    def fetch_intipa(self):
        intipa: list[int] = []
        for sign in self.shortened_ipa:
            _int = IpaDicts().sign2number[sign]
            intipa.append(_int)
        return intipa

    def __stressed_word_to_trans_uni(self) -> None:
        # nn yields no stress mark for one syllable words
        # dom -> 'dom'
        from word2ipa_rus.word2ipa import word2ipa
        trans_uni: str = word2ipa(self.stressed_word)
        if "ˈ" in trans_uni:
            self.trans_uni = trans_uni
        else:
            self.trans_uni = f"ˈ{trans_uni}"
        return None

    def __trans_uni_to_ipa(self) -> None:
        self.ipa: ipapy.ipastring = IPAString(unicode_string=self.trans_uni)
        return None

    # func to shorten ipa by scheme: one consonant before stressed vowel (if available)
    # stressed vowel + the rest of characters to the end of word
    # e.g. ipa ʂɨpʲɪˈlʲævʲɪtʲ shorened to lʲævʲɪtʲ
    def __shorten_ipa(self) -> None:
        stress_index: int = self.ipa.index(IpaDicts().stress_ipa)
        index_stressed_vowel: int = 0
        i: int
        ipa: ipapy.ipachar
        for i, ipa in enumerate(self.ipa):
            if i > stress_index and ipa.is_vowel:
                index_stressed_vowel = i
                break
        if index_stressed_vowel and self.ipa[index_stressed_vowel - 1].is_consonant:
            self.shortened_ipa: list[ipapy.ipachar] = self.ipa[index_stressed_vowel - 1:]
            return None
        else:
            self.shortened_ipa = self.ipa[index_stressed_vowel:]
            return None


class FactoryIntipa:
    @classmethod
    def fetch_intipa(cls, stressed_word):
        intipa = FetchIntipaFromDb(stressed_word).fetch_intipa()
        if intipa:
            print(f"intipa {intipa} fetched from db")
            return intipa
        else:
            intipa = FetchIntipaFromNn(stressed_word).fetch_intipa()
            print(f"intipa {intipa} fetched from neural network")
            return intipa
