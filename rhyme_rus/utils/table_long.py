import pandas as pd


def get_table_long(score_pattern_rhyme):
    table_long = pd.DataFrame.from_dict(score_pattern_rhyme)
    table_long = table_long[['score', 'assonance', 'pattern', 'rhyme']]
    table_long = table_long.reset_index(drop = True)
    table_long.index.name = 'id'
    table_long = table_long.sort_values(by = ["score", "rhyme"])
    return table_long
