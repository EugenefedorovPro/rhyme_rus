from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.seeds.mysql_connect import MySql


class AllScopeRhymes:
    def __init__(self, intipa):
        self.intipa: list[int] = intipa
        self.length_after_stress: int = 0
        self.stressed_vowel: int = 0
        self.__get_stressed_vowel()
        self.__get_length_after_stress()

    def __get_stressed_vowel(self) -> None:
        self.stressed_vowel = self.intipa[0] if self.intipa[0] in IpaDicts().number_vowels else self.intipa[1]
        return None

    def __get_length_after_stress(self) -> None:
        index_stressed_vowel = self.intipa.index(self.stressed_vowel)
        self.length_after_stress = len(self.intipa[index_stressed_vowel:])
        return None

    def get_all_scope_rhymes(self) -> list[str]:
        # TODO: add similar sound to stressed_vowel
        # TODO: make length_after_stress +- 1(2?)
        my_sql = MySql()
        query: str = f"select accent from wiki_pickled where stressed_vowel = {self.stressed_vowel} " \
                     f"and len_after_stress = {self.length_after_stress}"
        all_scope_rhymes: list[tuple[str]] = my_sql.cur_execute(query)
        all_scope_rhymes: list[str] = [rhyme[0] for rhyme in all_scope_rhymes]
        all_scope_rhymes: list[str] = list(set(all_scope_rhymes))
        return all_scope_rhymes
