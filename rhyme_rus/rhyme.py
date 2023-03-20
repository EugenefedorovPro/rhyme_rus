from multiprocessing import Pool
from time import perf_counter
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure
from rhyme_rus.utils.split_all_intipa_words import SplitIntipaWords
from rhyme_rus.utils.concat_tables import concat_tables

target_word = "облако"
word = Word(target_word)

if __name__ == "__main__":
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
        united_table.to_csv(f"{target_word}_mult.csv")

    target_word = "облако"
    word_one = Word(target_word)
    word_one = Procedure(word_one).build()
    word_one.table.to_csv(f"{target_word}_one.csv")

    print(united_table["rhyme"].equals(word_one.table["rhyme"]))
