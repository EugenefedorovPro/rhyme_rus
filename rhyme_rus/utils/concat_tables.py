import pandas as pd


def concat_tables(word_instances):
    tables: list[pd.DataFrame] = []
    for instance in word_instances:
        word = instance.table
        tables.append(word)
    united_table = pd.concat(tables)
    united_table = united_table.sort_values(by = ["score", "assonance", "rhyme"])
    united_table = united_table.reset_index(drop = True)
    return united_table
