from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure
from rhyme_rus.utils.word_statistics import WordStatistics

target_word = "облако"
word = Word(target_word)
word = Procedure(word).build()
# word.table.to_csv(f"{target_word}_{word.range_sql}.csv")

# word_preprocessed.table.to_csv("long_table.csv")

# WordStatistics().write_all_rhymes(lengths=[1])
# WordStatistics().write_all_rhymes(depends_on:
print(list(word.all_score_patterns.items())[:3])