import json
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.seeds.mysql_connect import my_sql


class AllIntipaWords:
    def __init__(self, range_sql, intipa):
        self.intipa: list[int] = intipa
        self.length_after_stress: int = 0
        self.stressed_vowel: int = 0
        self.near_stressed_v: int = 0
        self.range_sql = range_sql
        self.word_intipa_word_as_number: list[tuple[str, str]] = []
        self.__get_stressed_vowel()
        self.__get_length_after_stress()
        self.__get_near_stressed_v()
        self.__fetch_all_scope_rhymes()

    def __get_stressed_vowel(self) -> None:
        self.stressed_vowel = self.intipa[0] if self.intipa[0] in IpaDicts().numbers_vowels else self.intipa[1]

    def __get_near_stressed_v(self) -> None:
        dict_near_stressed = IpaDicts().near_stressed_v_int
        self.near_stressed_v = dict_near_stressed[self.stressed_vowel]

    def __get_length_after_stress(self) -> None:
        index_stressed_vowel = self.intipa.index(self.stressed_vowel)
        self.length_after_stress = len(self.intipa[index_stressed_vowel:])

    def __fetch_all_scope_rhymes(self) -> None:
        all_scope_rhymes: list[tuple[str, str]]
        query: str = f"select word, intipa from wiki_pickled where stressed_vowel in ({self.stressed_vowel}, " \
                     f"{self.near_stressed_v}) " \
                     f"and (len_after_stress between {self.length_after_stress - self.range_sql} " \
                     f"and {self.length_after_stress + self.range_sql})"
        self.word_intipa_word_as_number = my_sql.cur_execute(query)

    @staticmethod
    def turn_set_to_sorted_list(all_intipa_words) -> dict[tuple[int], list[str]]:
        all_intipa_words_list = {}
        for intipa in all_intipa_words:
            words: set[str] = all_intipa_words[intipa]
            words: list[str] = list(words)
            words.sort()
            all_intipa_words_list[intipa] = words
        return all_intipa_words_list

    def get_all_intipa_words(self) -> dict[tuple[int], set[str]] | dict[tuple[int], list[str]]:
        # TODO: add similar sound to stressed_vowel
        # TODO: make length_after_stress +- 1(2?)
        all_intipa_words: dict[tuple[int], set[str]] | dict[tuple[int], list[str]] = {}
        for item in self.word_intipa_word_as_number:
            word: str = item[0]
            intipa: tuple[int] = tuple(json.loads(item[1]))
            if intipa not in all_intipa_words:
                all_intipa_words[intipa] = {word}
            else:
                list_word = all_intipa_words[intipa]
                list_word.update([word])
                all_intipa_words[intipa] = list_word
        all_intipa_words = self.turn_set_to_sorted_list(all_intipa_words)
        return all_intipa_words
