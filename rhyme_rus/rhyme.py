from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

word = Word("дом")
word = Procedure(word).build()

print("word.unstressed_word", word.unstressed_word)
print("word.all_stresses", word.all_stresses)
print("word.stressed_word", word.stressed_word)
print("word.intipa", word.intipa)
print("all_scope_rhymes_dict", word.all_scope_rhymes_dict)

print("all_scope_rhymes_dict values", sum((len(item) for item in word.all_scope_rhymes_dict.values())))

print("all_scope_rhymes_dict", len(word.all_scope_rhymes_dict))
print("all_scope_rhymes_intipa", word.all_scope_rhymes_intipa)
print("all_scope_rhymes_intipa len", len(word.all_scope_rhymes_intipa))
print("patterns len", len(word.all_rhymes_patterns))
print("patterns", word.all_rhymes_patterns)
print("scores len", len(word.all_rhymes_scores))
print("scores", word.all_rhymes_scores)

print("word.sum_scores", word.sum_scores)
print("word.sum_scores keys", word.sum_scores.keys())

lens_values = []
for key in word.sum_scores:
    value = word.sum_scores[key]
    lens_values.append(len(value))
print(sum(lens_values))
