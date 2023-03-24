import dill
from pathlib import Path
from rhyme_rus.utils.reduce_table import ReduceTable

if __name__ == "__main__":
    path = Path(__file__).parent.parent / "test_table_long/test_table_long.pkl"
    with open(path, "rb") as f:
        table_long = dill.load(f)
    print(table_long)
    intipa = [0, 0, 0]
    table_reduced = ReduceTable(
        word_intipa = intipa,
        table_long = table_long
        ).get_reduced_table()
    with open("test_reduce_table.pkl", "wb") as f:
        dill.dump(table_reduced, f)

    print(table_reduced)
