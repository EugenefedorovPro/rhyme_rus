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
actual_unstressed_word = word.unstressed_word
actual_range_sql = word.range_sql
actual_stressed_vowel = word.stressed_vowel
actual_index_stressed_v = word.index_stressed_v
actual_near_stressed_v = word.near_stressed_v
actual_all_stresses = word.all_stresses
actual_stressed_word = word.stressed_word
actual_intipa = word.intipa
actual_all_intipa_words = word.all_intipa_words
actual_all_pad_intipa = word.all_pad_intipa
actual_all_pattern_pads = word.all_pattern_pads
actual_all_score_patterns = word.all_score_patterns
actual_sum_scores = word.sum_scores
actual_rhyme_scores_patterns = word.rhyme_scores_patterns
actual_score_pattern_rhyme = word.score_pattern_rhyme
actual_assonance = word.assonance
actual_table_long = word.table_long
actual_table = word.table

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
actual_attributes = (
    actual_unstressed_word,
    actual_range_sql,
    actual_stressed_vowel,
    actual_index_stressed_v,
    actual_near_stressed_v,
    actual_all_stresses,
    actual_stressed_word,
    actual_intipa,
    actual_all_intipa_words,
    actual_all_pad_intipa,
    actual_all_pattern_pads,
    actual_all_score_patterns,
    actual_sum_scores,
    actual_rhyme_scores_patterns,
    actual_score_pattern_rhyme,
    actual_assonance,
    actual_table_long,
    actual_table)


# making pkl-s of all attributes
def load_expected_attributes(names):
    expected = []
    for name in names:
        with open(f"test_word/{name}.pkl", "rb") as f:
            expected.append(dill.load(f))
    return expected


expected_attributes = load_expected_attributes(attribute_names)


def test_word():
    expected_actual_dict = {}
    for expected, actual, name in zip(expected_attributes, actual_attributes, attribute_names):
        if isinstance(expected, pd.core.frame.DataFrame) and isinstance(actual, pd.core.frame.DataFrame):
            expected_actual_dict[name] = expected.equals(actual)
        else:
            expected_actual_dict[name] = expected == actual
    print(expected_actual_dict)
    expected_actual_bools = list(expected_actual_dict.values())
    assert 0 == expected_actual_bools.count(False)
