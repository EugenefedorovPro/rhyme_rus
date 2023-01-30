from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

word = Word("конь")
word = Procedure().get_all_stresses(word)
word = Procedure().get_stressed_word(word)
word = Procedure().get_intipa(word)
word = Procedure().get_all_scope_rhymes(word)

print("___________________________")
print("word.unstressed_word", word.unstressed_word)
print("word.all_stresses", word.all_stresses)
print("word.stressed_word", word.stressed_word)
print("word.intipa", word.intipa)
print("all_scope_rhymes", word.all_scope_rhymes[:50])
print("all_scope_rhymes", len(word.all_scope_rhymes))
