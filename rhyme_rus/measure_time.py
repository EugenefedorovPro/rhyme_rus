import pandas as pd
from multiprocessing import Pool
from time import perf_counter
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure
from rhyme_rus.utils.word_statistics import WordStatistics
from rhyme_rus.utils.split_all_intipa_words import SplitIntipaWords
from rhyme_rus.utils.concat_tables import concat_tables

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

cycles = 5

word_length: dict[str, int] = WordStatistics().select_word_length(seed = True)
target_words: list[str] = list(word_length)

length_word_time_mult: dict[str:list[int], str:list[str], str:list[float], str:list[float]]
length_word_time_mult = {"length": [], "word": [], "time_mult": [], "time_one": []}

for i in range(cycles):
    for target_word in target_words:
        word = Word(target_word)

        if __name__ == "__main__":
            # rhyme with multiprocessing
            start_time_mult = perf_counter()

            word = Procedure(word).build_till_intipa_words()

            split_intipa_words: list[dict[tuple[int]:list[str, ...]], ...]
            split_intipa_words = SplitIntipaWords(
                word.all_stresses,
                word.stressed_word,
                word.intipa,
                word.stressed_vowel,
                word.near_stressed_v,
                word.index_stressed_v,
                word.all_intipa_words
                ).split_intipa_words()

            with Pool() as p:
                word_instances = p.starmap(Procedure(word).build_split_intipa_words, split_intipa_words)
                united_table = concat_tables(word_instances)

            end_time_mult = perf_counter()
            time_mult = round(end_time_mult - start_time_mult, 2)

            value_l = length_word_time_mult["length"]
            value_l.append(word_length[target_word])
            length_word_time_mult["length"] = value_l

            value_w = length_word_time_mult["word"]
            value_w.append(target_word)
            length_word_time_mult["word"] = value_w

            value_t = length_word_time_mult["time_mult"]
            value_t.append(time_mult)
            length_word_time_mult["time_mult"] = value_t

            # rhyme with one CPU
            start_time_one = perf_counter()

            word_one = Word(target_word)
            word_one = Procedure(word_one).build()

            end_time_one = perf_counter()
            time_one = round(end_time_one - start_time_one, 2)

            value = length_word_time_mult["time_one"]
            value.append(time_one)
            length_word_time_mult["time_one"] = value

length_word_time_mult = WordStatistics().list2tuple(length_word_time_mult, cycles)
time_table = WordStatistics().get_time_table(length_word_time_mult)
print(length_word_time_mult)
print(time_table)
time_table.to_csv("mult_one_processor_32.csv")
