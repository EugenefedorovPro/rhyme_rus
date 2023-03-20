from multiprocessing import Pool
from time import perf_counter
import pandas as pd
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure
from rhyme_rus.utils.word_statistics import WordStatistics
from rhyme_rus.utils.exceptions import MultipleStresses
from rhyme_rus.utils.split_all_intipa_words import SplitIntipaWords
from rhyme_rus.utils.concat_tables import concat_tables

if __name__ == "__main__":
    target_word = "облако"
    word = Word(target_word)
    word = Procedure(word).build_till_intipa_words()

    split_intipa_words: list[dict[tuple[int]:list[str, ...]], ...]
    split_intipa_words = SplitIntipaWords(
        word.intipa,
        word.sum_scores,
        word.all_pattern_pads,
        word.all_pad_intipa,
        word.all_intipa_words,
        word.all_intipa_words
        ).split_intipa_words()

    with Pool() as p:
        word_instances = p.map(Procedure(word).build_till_end, split_intipa_words)
        united_table = concat_tables(word_instances)
        united_table.to_csv(f"{target_word}_mult.csv")

    target_word = "облако"
    word_one = Word(target_word)
    word_one = Procedure(word_one).build()
    word_one.table.to_csv(f"{target_word}_one.csv")

    print(united_table["rhyme"].equals(word_one.table["rhyme"]))
