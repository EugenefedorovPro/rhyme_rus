import ipapy.ipastring
from ipapy.ipastring import IPAString
import json
from rhyme_rus.seeds.mysql_connect import MySql
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from abc import ABC, abstractmethod
from typing import Optional


class AIntIpaSounds(ABC):
    def __init__(self, stressed_word):
        self.stressed_word = stressed_word

    @abstractmethod
    def fetch_intipa_sounds(self):
        pass

class FactoryIntipaNumbers:
    @classmethod
    def fetch_intipa_sounds(cls, stressed_word):
        intipa, sounds = FetchIntipaSoundsDb(stressed_word).fetch_intipa_sounds()
        if intipa and sounds:
            return intipa, sounds
        else:
            intipa, sounds = FetchIntipaSoundsNn(stressed_word).fetch_intipa_sounds()
            return intipa, sounds


class FetchIntipaSoundsDb(AIntIpaSounds):
    def fetch_intipa_sounds(self) -> tuple[list[int], str] | tuple[None, None]:
        _query: str = f'''select intipa, sounds from  wiki_pickled where accent = "{self.stressed_word}"'''
        _mysql = MySql()
        intipa_sounds = _mysql.cur_execute(_query)
        if intipa_sounds:
            intipa_sounds = intipa_sounds[0]
            intipa = intipa_sounds[0]
            intipa = json.loads(intipa)
            sounds = intipa_sounds[1]
            return intipa, sounds
        else:
            return None, None


class FetchIntipaSoundsNn(AIntIpaSounds):

    def __init__(self, stressed_word):
        super().__init__(stressed_word)
        self.trans_uni: str = ''
        self.ipa: ipapy.ipastring = None
        self.shortened_ipa: list[ipapy.ipastring] = []
        self.__stressed_word_to_trans_uni()
        self.__trans_uni_to_ipa()
        self.__shorten_ipa()

    def fetch_intipa_sounds(self) -> tuple[list[int], str]:
        intipa: list[int] = []
        for sign in self.shortened_ipa:
            _int = IpaDicts().sign2number[sign]
            intipa.append(_int)
        return intipa, self.trans_uni

    def __stressed_word_to_trans_uni(self) -> None:
        # TODO add stress for sounds from db
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

    # func to shorten_rhyme ipa by scheme: one consonant before stressed vowel (if available)
    # stressed vowel + the rest of characters to the end of intipa
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


