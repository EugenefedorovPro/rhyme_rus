import multiprocessing

import pandas as pd
from multiprocessing import Pool
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure
from rhyme_rus.utils.split_all_intipa_words import SplitIntipaWords
from rhyme_rus.utils.concat_tables import concat_tables

pd.set_option("display.max_rows", 10000)
pd.set_option("display.max_columns", 10000)
pd.set_option("display.width", 10000)
pd.set_option("display.max_colwidth", None)


# multiprocessing.set_start_method('spawn')


def rhyme(target_word):
    if __name__ == "rhyme_rus.rhyme" or __name__ == "__main__":
        word = Word(target_word)
        word = Procedure(word).build_till_intipa_words()
        split_intipa_words: list[dict[tuple[int]:list[str, ...]], ...]
        split_intipa_words = SplitIntipaWords(
            word.all_stresses,
            word.stressed_word,
            word.intipa,
            word.stressed_vowel,
            word.near_stressed_v,
            word.index_stressed_v,
            word.all_intipa_words
            ).split_intipa_words()
        with Pool() as p:
            word_instances = p.starmap(Procedure(word).build_split_intipa_words, split_intipa_words)
            united_table = concat_tables(word_instances)
        return united_table
