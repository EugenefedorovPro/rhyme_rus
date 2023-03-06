import json
import pandas as pd
from rhyme_rus.seeds.mysql_connect import MySql
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure


class WordStatistics:
    def __init__(self):
        self.all_lengths_after_stress: list[int] = []
        self.word_statistics: pd.DataFrame = pd.DataFrame(columns=["length", "number"])
        self.samples: dict[int, str] = {}
        self.seed_length_word: dict[int, str] = {}
        self.seed_length_word: dict[int, str] = {}
        self.length_word: dict[int, str] = {}

    @staticmethod
    def get_accent_intipa_by_length(length: int):
        query = f"select accent, intipa from wiki_pickled where len_after_stress = {length}"
        words_by_length = MySql().cur_execute(query)
        return words_by_length

    def get_all_lengths_after_stress(self) -> list[int]:
        query = "select distinct (len_after_stress) from wiki_pickled"
        self.all_lengths_after_stress = MySql().cur_execute(query)
        self.all_lengths_after_stress = [item[0] for item in self.all_lengths_after_stress]
        self.all_lengths_after_stress.sort()
        return self.all_lengths_after_stress

    def get_word_statistics(self) -> pd.DataFrame:
        length_number: dict[str:int, str:int] = {"length": [], "number": []}
        self.get_all_lengths_after_stress()
        for length in self.all_lengths_after_stress:
            query = f"select count(len_after_stress) as number_words " \
                    f"from wiki_pickled where len_after_stress = {length}"
            number = MySql().cur_execute(query)
            numbers = length_number["number"]
            numbers.append(number[0][0])
            length_number["number"] = numbers
            lengths = length_number["length"]
            lengths.append(length)
            length_number["length"] = lengths
        return pd.DataFrame.from_dict(length_number).sort_values(by="length")

    def factory_length_word(self, seed) -> dict[int, str]:
        select_seed: dict[bool, dict[int, str]] = {True: self.__select_length_word(seed),
                                                   False: self.__select_length_word(seed)}
        length_word = select_seed[seed]
        return length_word

    @staticmethod
    def __check_if_only_word(word):
        query_check = f"select word from wiki_pickled where word = '{word}'"
        check = MySql().cur_execute(query_check)
        return len(check) == 1

    @staticmethod
    def __check_stress_intipa(word) -> True | False:
        query = f"select intipa from wiki_pickled where word = '{word}'"
        intipa: list[tuple[str]] = MySql().cur_execute(query)
        intipa: list[int] = json.loads(intipa[0][0])
        sound_1 = intipa[0]
        sound_2 = 0
        if len(intipa) > 1:
            sound_2 = intipa[1]
        all_vowels: tuple[int] = IpaDicts().all_stressed_vowels
        return sound_1 in all_vowels or sound_2 in all_vowels

    @staticmethod
    def __get_word(length: int, seed) -> str:
        rand_select = {False: "rand()", True: "rand(3)"}
        rand_option = rand_select[seed]
        query = f"select word from wiki_pickled where len_after_stress = {length} order by {rand_option} limit 1"
        word = MySql().cur_execute(query)
        word = word[0][0]
        return word

    def __select_length_word(self, seed):
        length_word: dict[int, str] = {}
        self.get_all_lengths_after_stress()
        for length in self.all_lengths_after_stress:
            word = self.__get_word(length, seed)
            while not WordStatistics().__check_if_only_word(word):
                word = WordStatistics().__get_word(length, seed)
            while not WordStatistics().__check_stress_intipa(word):
                word = WordStatistics().__get_word(length, seed=False)
            length_word[length] = word
        return length_word

    @staticmethod
    def write_rhyme(selected_word):
        word = Word(selected_word)
        word = Procedure(word).build()
        length = len(word.intipa)
        file_name = f"{length}_{selected_word}.csv"
        word.table.to_csv(file_name)
        print(f"saved {file_name}", flush=True)

    def write_all_rhymes(self, seed=True, lengths=range(1, 17)):
        length_word = self.factory_length_word(seed)
        self.length_word = length_word
        print(self.length_word)
        for length in length_word:
            if length in lengths:
                selected_word = length_word[length]
                WordStatistics().write_rhyme(selected_word)


if __name__ == "__main__":
    # print(WordStatistics().factory_length_word(seed=True))
    print(WordStatistics().get_accent_intipa_by_length(6))
    # print(WordStatistics().seed_length_word)
    # print(WordStatistics().seed_length_word)
