import json
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.seeds.mysql_connect import MySql


class MetaAllIntipaWords:
    def __init__(self, range_sql, intipa):
        self.range_sql = range_sql
        self.intipa = intipa
        self.all_intipa_words: dict[tuple[int], set[str]] = {}

    def get_all_intipa_words(self) -> dict[tuple[int], set[str]]:
        self.all_intipa_words = AllIntipaWords(self.range_sql, self.intipa).get_all_intipa_words()
        return self.all_intipa_words


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
        my_sql = MySql()
        query: str = f"select word, intipa, word_as_numbers from wiki_pickled where stressed_vowel in ({self.stressed_vowel}, {self.near_stressed_v}) " \
                     f"and (len_after_stress between {self.length_after_stress - self.range_sql} " \
                     f"and {self.length_after_stress + self.range_sql})"
        self.word_intipa_word_as_number = my_sql.cur_execute(query)

    def get_all_intipa_words(self) -> tuple[dict[tuple[int], set[str]], dict[str, tuple[int]]]:
        # TODO: add similar sound to stressed_vowel
        # TODO: make length_after_stress +- 1(2?)
        all_intipa_words: dict[tuple[int], set[str]] = {}
        all_word_numbers: dict[str, tuple[int]] = {}
        for item in self.word_intipa_word_as_number:
            word: str = item[0]
            intipa: tuple[int] = tuple(json.loads(item[1]))
            word_as_numbers: tuple[int] = tuple(json.loads(item[2]))
            if intipa not in all_intipa_words:
                all_intipa_words[intipa] = {word}
            else:
                list_word = all_intipa_words[intipa]
                list_word.update([word])
                all_intipa_words[intipa] = list_word

            all_word_numbers[word] = word_as_numbers

        return all_intipa_words, all_word_numbers
