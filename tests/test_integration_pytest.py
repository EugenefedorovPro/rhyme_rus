import dill
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

target_words = ['ом', 'дом', 'кома', 'палама']
words_names = ['om', 'dom', 'koma', 'palama']


def load_tables(words, names):
    tables_loaded = []
    for w, name in zip(words, names):
        with open(f"test_integration/{name}.pkl", "rb") as f:
            table = dill.load(f)
            tables_loaded.append(table)
            print(f"{name}.pkl was loaded")
    return tables_loaded


def get_actual_tables(words, names):
    actual = []
    for w, name in zip(words, names):
        word = Word(w)
        if w == 'палама':
            word.stressed_word = "пала'ма"
        word = Procedure(word).build()
        actual.append(word.table)
    return actual


expected_tables = load_tables(target_words, words_names)
actual_tables = get_actual_tables(target_words, words_names)


def test_integration():
    expected_actual_dict = {}
    for expected, actual, name in zip(expected_tables, actual_tables, words_names):
        expected_actual_dict[name] = expected.equals(actual)
    print(expected_actual_dict)
    expected_actual_bool = list(expected_actual_dict.values())
    assert expected_actual_bool.count(False) == 0
