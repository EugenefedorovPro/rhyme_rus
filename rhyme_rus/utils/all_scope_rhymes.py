import json
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.seeds.mysql_connect import MySql


class MetaAllScopeRhymes:
    def __init__(self, intipa):
        self.intipa = intipa
        self.all_scope_rhymes_dict: dict[tuple[int], set[str]] = {}
        self.get_all_scope_rhymes_dict()

    def get_all_scope_rhymes_dict(self) -> dict[tuple[int], set[str]]:
        self.all_scope_rhymes_dict = AllScopeRhymes(self.intipa).get_all_scope_rhymes_dict()
        return self.all_scope_rhymes_dict

    def get_all_scope_rhymes_intipa(self) -> list[tuple[int]]:
        all_scope_rhymes_intipa = [key for key in self.all_scope_rhymes_dict]
        return all_scope_rhymes_intipa


class AllScopeRhymes:
    def __init__(self, intipa):
        self.intipa: list[int] = intipa
        self.length_after_stress: int = 0
        self.stressed_vowel: int = 0
        self.all_scope_rhymes: list[tuple[str, str]] = []
        self.__get_stressed_vowel()
        self.__get_length_after_stress()
        self.__fetch_all_scope_rhymes()

    def __get_stressed_vowel(self) -> None:
        self.stressed_vowel = self.intipa[0] if self.intipa[0] in IpaDicts().numbers_vowels else self.intipa[1]

    def __get_length_after_stress(self) -> None:
        index_stressed_vowel = self.intipa.index(self.stressed_vowel)
        self.length_after_stress = len(self.intipa[index_stressed_vowel:])

    def __fetch_all_scope_rhymes(self) -> None:
        all_scope_rhymes: list[tuple[str, str]]
        my_sql = MySql()
        query: str = f"select accent, intipa from wiki_pickled where stressed_vowel = {self.stressed_vowel} " \
                     f"and len_after_stress = {self.length_after_stress}"
        self.all_scope_rhymes = my_sql.cur_execute(query)

    # func to make intipa equal like in дом - ом
    def __pat_short_rhyme_intipa(self, rhyme_intipa):
        if len(self.intipa) > len(rhyme_intipa):
            rhyme_intipa = list(rhyme_intipa)
            rhyme_intipa.insert(0, -1)
            rhyme_intipa = tuple(rhyme_intipa)
        return rhyme_intipa

    def get_all_scope_rhymes_dict(self) -> dict[tuple[int], set[str]]:
        # TODO: add similar sound to stressed_vowel
        # TODO: make length_after_stress +- 1(2?)
        all_scope_rhymes_dict: dict[tuple[int], set[str]] = {}
        for item in self.all_scope_rhymes:
            word: str = item[0]
            intipa: tuple[int] = tuple(json.loads(item[1]))
            intipa = self.__pat_short_rhyme_intipa(intipa)
            if intipa not in all_scope_rhymes_dict:
                all_scope_rhymes_dict[intipa] = {word}
            else:
                list_word = all_scope_rhymes_dict[intipa]
                list_word.update([word])
                all_scope_rhymes_dict[intipa] = list_word
        return all_scope_rhymes_dict
