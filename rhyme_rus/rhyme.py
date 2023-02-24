from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

word = Word("сорт")
word = Procedure(word).build()

print(word.table)
