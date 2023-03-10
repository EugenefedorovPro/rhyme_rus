import dill
from rhyme_rus.utils.reduce_table import ReduceTable


def test_reduce_table():
    with open("test_table_long/test_table_long.pkl", "rb") as f:
        table_long = dill.load(f)
    intipa = [0, 0, 0]
    actual = ReduceTable(word_intipa = intipa,
                         table_long = table_long).get_reduced_table()
    with open("test_reduce_table/test_reduce_table.pkl", "rb") as f:
        expected = dill.load(f)

    assert actual.equals(expected)
