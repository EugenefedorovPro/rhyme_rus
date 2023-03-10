import pandas as pd
from collections import namedtuple
from typing import NamedTuple

NamedTuple('Table', [('n_sounds', int), ('score', int), ('assonance', int)])
Table = namedtuple('Table', ['n_sounds', 'score', 'assonance'])


class ReduceTable:
    table: pd.DataFrame
    word_intipa: list[int]

    def __init__(self, word_intipa, table_long):
        self.word_n_sounds: int = len(word_intipa)
        self.table = table_long
        self.reduce_table_figures: list[Table] = []
        self.__get_reduce_table_figures()

    def __get_reduce_table_figures(self):
        word_2 = Table(2, 5, 1)
        word_3 = Table(3, 5, 1)
        word_4 = Table(4, 5, 1)
        word_5 = Table(5, 8, 1)
        word_6 = Table(6, 8, 1)
        word_7 = Table(7, 9, 1)
        word_8 = Table(8, 9, 1)
        word_9 = Table(9, 10, 2)
        word_10 = Table(9, 14, 3)
        word_11 = Table(11, 15, 4)
        word_12 = Table(12, 23, 4)
        word_13 = Table(13, 22, 5)
        word_14 = Table(14, 35, 6)
        word_15 = Table(15, 35, 6)
        word_16 = Table(16, 44, 6)
        word_17 = Table(17, 42, 6)

        self.reduce_table_figures = {2: word_2, 3: word_3, 4: word_4, 5: word_5, 6: word_6, 7: word_7, 8: word_8,
                                     9: word_9, 10: word_10,
                                     11: word_11, 12: word_12, 13: word_13, 14: word_14, 15: word_15, 16: word_16,
                                     17: word_17}

    NamedTuple('Table', [('n_sounds', int), ('score', int), ('assonance', int)])

    def get_reduced_table(self):
        word_some = self.reduce_table_figures[self.word_n_sounds]
        reduced_table = self.table[
            (self.table.score <= word_some.score) | (self.table.assonance <= word_some.assonance)]
        reduced_table = reduced_table.reset_index(drop = True)
        reduced_table.index.name = 'id'

        return reduced_table
