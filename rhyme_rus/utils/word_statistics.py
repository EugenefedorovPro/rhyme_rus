import pandas as pd
from typing import Any
from time import perf_counter
from rhyme_rus.seeds.mysql_connect import my_sql
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


class WordStatistics:
    def __init__(self):
        self.all_lengths_after_stress: list[int] = []
        self.word_statistics: pd.DataFrame = pd.DataFrame(columns = ["length", "number"])
        self.all_stressed_vowels: tuple = ()
        self.samples: dict[int, str] = {}
        self.seed_length_word: dict[int, str] = {}
        self.seed_length_word: dict[int, str] = {}
        self.length_word: dict[int, str] = {}
        self.__get_all_stressed_vowels()

    def __get_all_stressed_vowels(self):
        self.all_stressed_vowels = IpaDicts().all_stressed_vowels

    @staticmethod
    def get_accent_intipa_by_length(length: int):
        query = f"select accent, intipa from wiki_pickled where len_after_stress = {length}"
        words_by_length = my_sql.cur_execute(query)
        return words_by_length

    def get_all_lengths_after_stress(self) -> list[int]:
        query = "select distinct (len_after_stress) from wiki_pickled"
        self.all_lengths_after_stress = my_sql.cur_execute(query)
        self.all_lengths_after_stress = [item[0] for item in self.all_lengths_after_stress]
        self.all_lengths_after_stress.sort()
        return self.all_lengths_after_stress

    def get_word_statistics(self) -> pd.DataFrame:
        length_number: dict[str:int, str:int] = {"length": [], "number": []}
        self.get_all_lengths_after_stress()
        for length in self.all_lengths_after_stress:
            query = f"select count(len_after_stress) as number_words " \
                    f"from wiki_pickled where len_after_stress = {length}"
            number = my_sql.cur_execute(query)
            numbers = length_number["number"]
            numbers.append(number[0][0])
            length_number["number"] = numbers
            lengths = length_number["length"]
            lengths.append(length)
            length_number["length"] = lengths
        return pd.DataFrame.from_dict(length_number).sort_values(by = "length")

    def get_word(self, length: int, seed: bool) -> str:
        if length in (14, 15, 16):
            offset = 0
        else:
            offset = 150

        if seed:
            query = f'''
            select word from wiki_pickled 
            where len_after_stress = {length} and
            word glob '[а-я]*' and
            (json_extract(intipa, '$[0]') in {self.all_stressed_vowels} or
            json_extract(intipa, '$[1]') in {self.all_stressed_vowels}) 
            group by word having count(1) = 1
            limit 1 offset {offset}
            '''
            word = my_sql.cur_execute(query)
        else:
            query = f'''
            select word from wiki_pickled 
            where len_after_stress = {length} and
            word glob '[а-я]*' and
            (json_extract(intipa, '$[0]') in {self.all_stressed_vowels} or
            json_extract(intipa, '$[1]') in {self.all_stressed_vowels}) 
            group by word having count(1) = 1
            order by random()
            limit 1 
            '''
            word = my_sql.cur_execute(query)
        word = word[0][0]
        return word

    def select_length_word(self, seed):
        length_word: dict[int, str] = {}
        self.get_all_lengths_after_stress()
        for length in self.all_lengths_after_stress:
            word = self.get_word(length, seed)
            length_word[length] = word
            print(length, word)
        return length_word

    @staticmethod
    def write_rhyme(selected_word, long):
        word = Word(selected_word)
        word = Procedure(word).build()
        length = len(word.intipa)
        file_name = f"{length}_{selected_word}.csv"
        if long:
            word.table_long.to_csv(file_name)
        else:
            word.table.to_csv(file_name)
        print(f"saved {file_name}, long is {long}", flush = True)

    def write_all_rhymes(self, seed = True, long = True, lengths = range(1, 17)):
        # length_word = self.factory_length_word(seed)
        length_word = self.select_length_word(seed)
        self.length_word = length_word
        print(self.length_word)
        for length in length_word:
            if length in lengths:
                selected_word = length_word[length]
                WordStatistics().write_rhyme(selected_word, long)

    @staticmethod
    def __measure_time_rhyme(selected_word) -> float:
        start_time = perf_counter()
        word = Word(selected_word)
        Procedure(word).build()
        end_time = perf_counter()
        time_execution = end_time - start_time
        print(f"time for {selected_word} measured")
        return time_execution

    word_length_time: dict[str:list[str], str:list[int], str:list[float]]

    @staticmethod
    def __get_time_average(time_table: pd.DataFrame) -> pd.DataFrame:
        time_average: tuple[Any] = tuple(round(sum(row) / len(row), 2) for row in time_table["time"])
        time_table["average_time"] = time_average
        return time_table

    @staticmethod
    def __get_time_table(word_length_time) -> pd.DataFrame:
        time_table = pd.DataFrame.from_dict(word_length_time)
        time_table = time_table.reset_index(drop = True)
        time_table.index.name = "id"
        time_table = WordStatistics().__get_time_average(time_table)
        time_table = time_table.sort_values(by = ["length", "average_time"])
        return time_table

    word_length_time: (dict[str:list[str], str:list[int], str:list[float]] |
                       dict[str:set[str], str:set[int], str:set[float]])

    @staticmethod
    def __get_pairs_from_split(split_array):
        length_inner_array: int = len(split_array[0])
        pairs: list[tuple] | tuple[tuple, ...] = []
        for index in range(length_inner_array):
            pair: list[float] | tuple[float] = []
            for item in split_array:
                number = item[index]
                pair.append(number)
            pairs.append(tuple(pair))
        pairs = tuple(pairs)
        return pairs

    @staticmethod
    def __get_tuple_split(current_tuple: tuple[int], ratio: int):
        cutter = len(current_tuple) // ratio
        split_array = tuple(
            current_tuple[start:stop]
            for start, stop in zip(
                range(0, len(current_tuple), cutter),
                range(cutter, len(current_tuple) + cutter, cutter)
                )
            )
        split_array = WordStatistics().__get_pairs_from_split(split_array)
        return split_array

    @staticmethod
    def __list2tuple(word_length_time: dict[str:list[str], str:list[int], str:list[float]], cycles: int):
        value_t = word_length_time["word"]
        value_t = WordStatistics().__get_tuple_split(value_t, cycles)
        word_length_time["word"] = value_t

        value_t = word_length_time["length"]
        value_t = WordStatistics().__get_tuple_split(value_t, cycles)
        word_length_time["length"] = value_t

        value_t = word_length_time["time"]
        value_t = WordStatistics().__get_tuple_split(value_t, cycles)
        word_length_time["time"] = value_t

        return word_length_time

    def measure_time_all_rhymes(self, seed = True, lengths = range(1, 17), cycles = 1) -> pd.DataFrame:
        word_length_time: dict[str:list[str], str:list[int], str:list[float]]
        word_length_time = {"word": list(), "length": list(), "time": list()}
        count = 0
        while count < cycles:
            length_word = self.select_length_word(seed)
            self.length_word = length_word
            print(self.length_word)
            for length in length_word:
                if length in lengths:
                    selected_word = length_word[length]
                    time_execution = WordStatistics().__measure_time_rhyme(selected_word)

                    value_w = word_length_time["word"]
                    value_w.append(selected_word)
                    word_length_time["word"] = value_w

                    value_l = word_length_time["length"]
                    value_l.append(length)
                    word_length_time["length"] = value_l

                    value_t = word_length_time["time"]
                    value_t.append(round(time_execution, 2))
                    word_length_time["time"] = value_t

            count += 1

        word_length_time = WordStatistics().__list2tuple(word_length_time, cycles)
        time_table = WordStatistics().__get_time_table(word_length_time)

        return time_table


if __name__ == "__main__":
    # print(WordStatistics().get_word_statistics())
    # print(WordStatistics().get_word(6, False))
    # print(WordStatistics().select_length_word(seed = True))
    # print(WordStatistics().get_accent_intipa_by_length(11))
    # print(WordStatistics().seed_length_word)
    print(WordStatistics().measure_time_all_rhymes(seed = False, cycles = 5))
