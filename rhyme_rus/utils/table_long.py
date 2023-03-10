import pandas as pd


def get_table_long(score_pattern_rhyme):
    table_long = pd.DataFrame.from_dict(score_pattern_rhyme)
    table_long = table_long[['score', 'assonance', 'pattern', 'rhyme']]
    return table_long
