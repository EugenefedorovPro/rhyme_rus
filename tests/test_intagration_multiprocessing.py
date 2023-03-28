import dill
import pandas as pd

from rhyme_rus.rhyme import rhyme, rhyme_with_stresses

target_words = ['ом', 'дом', 'кома', 'палама', 'сыл']
words_names = ['om', 'dom', 'koma', 'palama', 'syl']


def load_tables() -> list[pd.DataFrame]:
    tables: list[pd.DataFrame] = []
    for name in words_names:
        with open(f"test_integrated_multiprocessing/{name}.pkl", "rb") as f:
            expected = dill.load(f)
            tables.append(expected)
    return tables


expected_tables = load_tables()


def get_actual_tables():
    tables = []
    for word in target_words:
        if word == 'палама':
            table = rhyme("пала'ма")
        else:
            table = rhyme(word)
        tables.append(table)
    return tables


actual_tables = get_actual_tables()


def test_integration_multiprocessing():
    for expected, actual in zip(expected_tables, actual_tables):
        assert expected["rhyme"].equals(actual["rhyme"])
        assert expected["score"].equals(actual["score"])
        assert expected["assonance"].equals(actual["assonance"])


words_names_stresses = ['om_stresses', 'dom_stresses', 'koma_stresses', 'palama_stresses', 'syl_stresses']


def load_tuples_stresses() -> list[tuple[pd.DataFrame, tuple[str], str], ...]:
    tuples_stresses: list[pd.DataFrame] = []
    for name in words_names_stresses:
        with open(f"test_integrated_multiprocessing/{name}.pkl", "rb") as f:
            expected = dill.load(f)
            tuples_stresses.append(expected)
    return tuples_stresses


expected_tuples_stresses = load_tuples_stresses()


def get_actual_tuples_stresses():
    tuples_stresses = []
    for word in target_words:
        if word == 'палама':
            tuple_stresses = rhyme_with_stresses("пала'ма")
        else:
            tuple_stresses = rhyme_with_stresses(word)
        tuples_stresses.append(tuple_stresses)
    return tuples_stresses


actual_tuples_stresses = get_actual_tuples_stresses()


def test_integration_multiprocessing_stresses():
    for expected, actual in zip(expected_tuples_stresses, actual_tuples_stresses):
        # table_expected = expected[0]
        # table_actual = actual[0]
        assert expected[0]["rhyme"].equals(actual[0]["rhyme"])
        assert expected[0]["score"].equals(actual[0]["score"])
        assert expected[0]["assonance"].equals(actual[0]["assonance"])
        assert expected[1] == actual[1]
        assert expected[2] == actual[2]

# united_table, word.all_stresses, word.stressed_word
