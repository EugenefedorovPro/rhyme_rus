import dill
import pandas as pd
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

# type hints
unstressed_word: str
range_sql: int
stressed_vowel: int
index_stressed_v: int
near_stressed_v: int
all_stresses: list[str]
stressed_word: str
intipa: list[int]
all_intipa_words: dict[tuple[int], set[str]]
all_pad_intipa: dict[tuple[int], list[tuple[int]]]
all_pattern_pads: dict[tuple[str], list[tuple[int]]]
all_score_patterns: dict[tuple[int], list[tuple[str]]]
sum_scores: dict[int, list[tuple[str]]]
rhyme_scores_patterns: dict[[str, dict[int, tuple[str]]]]
score_pattern_rhyme: dict[str: list[int], str: list[tuple[str], str: list[str]]] | dict[str: list[int],
                                                                                   str: list[int],
                                                                                   str: list[tuple[str],
                                                                                        str: list[str]]]
score_pattern_rhyme: dict[str: list[int], str: list[tuple[str], str: list[str]]]
assonance: list[int]
table_long: pd.DataFrame
table: pd.DataFrame

# rhyme processing
target_word = "беженец"
word = Word(target_word)
word = Procedure(word).build()

# assigning values of attributes
unstressed_word = word.unstressed_word
range_sql = word.range_sql
stressed_vowel = word.stressed_vowel
index_stressed_v = word.index_stressed_v
near_stressed_v = word.near_stressed_v
all_stresses = word.all_stresses
stressed_word = word.stressed_word
intipa = word.intipa
all_intipa_words = word.all_intipa_words
all_pad_intipa = word.all_pad_intipa
all_pattern_pads = word.all_pattern_pads
all_score_patterns = word.all_score_patterns
sum_scores = word.sum_scores
rhyme_scores_patterns = word.rhyme_scores_patterns
score_pattern_rhyme = word.score_pattern_rhyme
assonance = word.assonance
table_long = word.table_long
table = word.table

# assigning names of attributes
name_unstressed_word = "unstressed_word"
name_range_sql = "range_sql"
name_stressed_vowel = "stressed_vowel"
name_index_stressed_v = "index_stressed_v"
name_near_stressed_v = "near_stressed_v"
name_all_stresses = "all_stresses"
name_stressed_word = "stressed_word"
name_intipa = "intipa"
name_all_intipa_words = "all_intipa_words"
name_all_pad_intipa = "all_pad_intipa"
name_all_pattern_pads = "all_pattern_pads"
name_all_score_patterns = "all_score_patterns"
name_sum_scores = "sum_scores"
name_rhyme_scores_patterns = "rhyme_scores_patterns"
name_score_pattern_rhyme = "score_pattern_rhyme"
name_assonance = "assonance"
name_table_long = "table_long"
name_table = "table"

# setting list of attributes
attribute_names = (name_unstressed_word,
                   name_range_sql,
                   name_stressed_vowel,
                   name_index_stressed_v,
                   name_near_stressed_v,
                   name_all_stresses,
                   name_stressed_word,
                   name_intipa,
                   name_all_intipa_words,
                   name_all_pad_intipa,
                   name_all_pattern_pads,
                   name_all_score_patterns,
                   name_sum_scores,
                   name_rhyme_scores_patterns,
                   name_score_pattern_rhyme,
                   name_assonance,
                   name_table_long,
                   name_table)

# getting list of word attributes
word_attributes = (
    unstressed_word,
    range_sql,
    stressed_vowel,
    index_stressed_v,
    near_stressed_v,
    all_stresses,
    stressed_word,
    intipa,
    all_intipa_words,
    all_pad_intipa,
    all_pattern_pads,
    all_score_patterns,
    sum_scores,
    rhyme_scores_patterns,
    score_pattern_rhyme,
    assonance,
    table_long,
    table)


# making pkl-s of all attributes
def dump_word_attributes(attributes = word_attributes, names = attribute_names):
    for attribute, name in zip(attributes, names):
        with open(f"{name}.pkl", "wb") as f:
            dill.dump(attribute, f)
            print(f"{name}.pkl was written")


if __name__ == "__main__":
    dump_word_attributes(word_attributes, attribute_names)
    with open(f"score_pattern_rhyme.pkl", "rb") as f:
        expected_score_pattern_rhyme = dill.load(f)

    # print(table_long.equals(expected_table_long))
    # expected_table_long.to_csv("беженец_long.csv")
    print(score_pattern_rhyme == expected_score_pattern_rhyme)
