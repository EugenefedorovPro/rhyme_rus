from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure
from rhyme_rus.utils.word_statistics import WordStatistics

word = Word("ом")
word = Procedure(word).build()
print(word.table)
word.table.to_csv("ом.csv")

# word.table.to_csv("long_table.csv")

# WordStatistics().write_all_rhymes(lengths=[1])
# WordStatistics().write_all_rhymes()
