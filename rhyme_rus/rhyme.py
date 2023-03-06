from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure
from rhyme_rus.utils.word_statistics import WordStatistics
from rhyme_rus.utils.exceptions import MultipleStresses

target_word = "облако"
word = Word(target_word)
word = Procedure(word).build()
word.table.to_csv(f"{target_word}_{word.range_sql}_.csv")
# print(word.reduce_table_figures)
# print(type(word.reduce_table_figures[2]))

# word_preprocessed.table.to_csv("long_table.csv")

# WordStatistics().write_all_rhymes(seed=False)
# WordStatistics().write_all_rhymes(depends_on:
# print(word.table)
# print(len(word.all_word_numbers))
# print(list(word.all_word_numbers.items())[:10])
# print(word.sounds)

# WordStatistics().write_rhyme("соотечественница")


# word = Word("дром")
# word.stressed_word = "дро'м"
# word = Procedure(word).build()