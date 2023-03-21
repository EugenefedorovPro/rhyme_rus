import dill
import pandas as pd

from rhyme_rus.rhyme import rhyme

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
            table = rhyme(word, "пала'ма")
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
