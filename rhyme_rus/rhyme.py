from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

word = Word("дом")
word = Procedure(word).build()

print("intipa.unstressed_word", word.unstressed_word)
print("intipa.all_stresses", word.all_stresses)
print("intipa.stressed_word", word.stressed_word)
print("intipa.stressed_vowel", word.stressed_vowel)
print("intipa.intipa", word.intipa)
print("all_scope_rhymes_dict", list(word.all_scope_rhymes_dict.items())[:10])
print("all_scope_rhymes_dict values", sum((len(item) for item in word.all_scope_rhymes_dict.values())))

# print("all_scope_rhymes_dict", len(intipa.all_scope_rhymes_dict))
print("all_scope_rhymes_intipa", word.all_scope_rhymes_intipa[:10])
print("all_scope_pads_dict", len(word.all_scope_pads_dict))
for i, item in enumerate(word.all_scope_pads_dict.items()):
    if i in [0, 100, 200]:
        print("pads", item)
# print("all_scope_rhymes_intipa len", len(intipa.all_scope_rhymes_intipa))
# print("patterns len", len(word.all_rhymes_patterns))
print("word.all_scope_pads_list", word.all_scope_pads_list[:10])
for i, item in enumerate(word.all_rhymes_patterns.items()):
    if i in [0, 10, 70]:
        print(item)

print("patterns", len(word.all_rhymes_patterns))
for i, item in enumerate(word.all_rhymes_patterns.items()):
    if i in [0, 10, 20]:
        print(item)

# print("scores len", len(intipa.all_rhymes_scores))
# print("scores", intipa.all_rhymes_scores)
#
# print("intipa.sum_scores", intipa.sum_scores)
# print("intipa.sum_scores keys", intipa.sum_scores.keys())
#
# lens_values = []
# for key in intipa.sum_scores:
#     value = intipa.sum_scores[key]
#     lens_values.append(len(value))
# print(sum(lens_values))
