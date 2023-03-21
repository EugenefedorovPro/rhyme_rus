import dill
import pandas as pd
from rhyme_rus.utils.concat_tables import concat_tables
from rhyme_rus.utils.word import Word

rus_words = ("дом", "клоп", "сталкер")
w_0 = Word(rus_words[0])
w_1 = Word(rus_words[1])
w_2 = Word(rus_words[2])

w_0.table = pd.DataFrame.from_dict(
    {"score": tuple(range(5)), "assonance": tuple(range(5, 10)), "rhyme": tuple(
        range(5, 10)
        )}
    )
w_1.table = pd.DataFrame.from_dict(
    {"score": tuple(range(10, 15)), "assonance": tuple(range(15, 20)), "rhyme": tuple(
        range(5, 10)
        )}
    )
w_2.table = pd.DataFrame.from_dict(
    {"score": tuple(range(25, 30)), "assonance": tuple(range(30, 35)), "rhyme": tuple(
        range(5, 10)
        )}
    )

word_instances = (w_0, w_1, w_2)


def test_concat_table():
    actual = concat_tables(word_instances)
    with open("test_concat_tables/test_concat_table.pkl", "rb") as f:
        expected = dill.load(f)
    assert actual.equals(expected)
