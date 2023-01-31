from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

word = Word("пушкинд")
word.stressed_word = "пу'шкинд"
word = Procedure(word).build()

print("word.unstressed_word", word.unstressed_word)
print("word.all_stresses", word.all_stresses)
print("word.stressed_word", word.stressed_word)
print("word.intipa", word.intipa)
print("all_scope_rhymes", word.all_scope_rhymes[:50])
print("all_scope_rhymes", len(word.all_scope_rhymes))
