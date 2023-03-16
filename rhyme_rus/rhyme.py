from time import perf_counter
import pandas as pd
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure
from rhyme_rus.utils.word_statistics import WordStatistics
from rhyme_rus.utils.exceptions import MultipleStresses
import coverage

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

start = perf_counter()

target_word = "облако"
word = Word(target_word)
# word.stressed_word = "пала'ма"
word = Procedure(word).build()
print(word.table)

stop = perf_counter()
print("time = ", stop - start)
# print(word.reduce_table_figures)
# print(type(word.reduce_table_figures[2]))

# word_preprocessed.table.to_csv("long_table.csv")

# WordStatistics().write_all_rhymes(seed=False, long=False)
# WordStatistics().write_all_rhymes(depends_on:
# print(word.table)
# print(len(word.all_word_numbers))
# print(list(wa7b8b9389cfford.all_word_numbers.items())[:10])
# print(word.sounds)

# WordStatistics().write_rhyme("соотечественница")
# word = Word("дромса")
# word = Procedure(word).build()
