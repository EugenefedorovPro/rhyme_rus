import pandas as pd
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.all_stresses import FactoryStress
from rhyme_rus.utils.stressed_word import get_stressed_word
from rhyme_rus.utils.intipa import FactoryIntipa
from rhyme_rus.utils.stressed_vowel import get_stressed_vowel
from rhyme_rus.utils.index_stressed_v import get_index_stressed_v
from rhyme_rus.utils.near_stressed_v import get_near_stressed_v
from rhyme_rus.utils.intipa_words import AllIntipaWords
from rhyme_rus.utils.range_rhymes import RangeRhymes
from rhyme_rus.utils.pad import Pad
from rhyme_rus.utils.pattern import Pattern
from rhyme_rus.utils.score import Score
from rhyme_rus.utils.reverse import Reverse
from rhyme_rus.utils.assonance import Assonance
from rhyme_rus.utils.table import Table
from rhyme_rus.utils.reduce_table import ReduceTable


class Procedure:
    def __init__(self, word: Word):
        self.word: Word = word

    def __get_all_stresses(self) -> None:
        self.word.all_stresses = FactoryStress().fetch_stress(self.word.unstressed_word)

    def __get_stressed_word(self) -> None:
       self.word.stressed_word = get_stressed_word(self.word.all_stresses, self.word.unstressed_word)

    def __get_intipa(self) -> None:
        self.word.intipa = FactoryIntipa().fetch_intipa(self.word.stressed_word)

    def __get_stressed_vowel(self) -> None:
        self.word.stressed_vowel = get_stressed_vowel(self.word.intipa, self.word.stressed_word)

    def __get_index_stressed_v(self) -> None:
        self.word.index_stressed_v = get_index_stressed_v(self.word.intipa, self.word.stressed_vowel)

    def __get_near_stressed_v(self):
        self.word.near_stressed_v = get_near_stressed_v(self.word.stressed_vowel)

    def __get_all_intipa_words(self) -> None:
        self.word.all_intipa_words = AllIntipaWords(self.word.range_sql,
                                                        self.word.intipa).get_all_intipa_words()

    def __get_all_pad_intipa(self) -> None:
        self.word.all_pad_intipa = Pad(
            intipa=self.word.intipa,
            all_intipa_word=self.word.all_intipa_words,
            stressed_vowel=self.word.stressed_vowel,
            near_stressed_v=self.word.near_stressed_v,
            index_stressed_v=self.word.index_stressed_v
        ).get_all_pads_dict()


    def __get_all_pattern_pads(self) -> None:
        self.word.all_pattern_pads = Pattern(self.word.intipa,
                                             self.word.all_pad_intipa).get_all_pattern_pads()


    def __get_all_score_patterns(self) -> None:
        self.word.all_score_patterns = Score(self.word.index_stressed_v,
                                             self.word.all_pattern_pads).get_all_score_patterns()

    def __get_sum_scores(self) -> None:
        self.word.sum_scores = RangeRhymes(self.word.all_score_patterns).get_sum_scores()

    def __get_reverse(self) -> None:
        self.word.rhyme_scores_patterns = Reverse(
            self.word.intipa,
            self.word.sum_scores,
            self.word.all_pattern_pads,
            self.word.all_pad_intipa,
            self.word.all_intipa_words).reverse()

    def __get_score_pattern_rhyme(self):
        self.word.score_pattern_rhyme = Table(self.word.rhyme_scores_patterns).make_dict_for_table()

    def __get_assonance(self):
        self.word.assonance = Assonance(unstressed_word=self.word.unstressed_word,
                                        score_pattern_rhyme=self.word.score_pattern_rhyme).get_all_assonance()
        self.word.score_pattern_rhyme["assonance"] = self.word.assonance

    def __get_table_long(self) -> None:
        self.word.table_long = pd.DataFrame.from_dict(self.word.score_pattern_rhyme)
        self.word.table_long = self.word.table_long[['score', 'assonance', 'pattern', 'rhyme']]

    def __get_table(self) -> None:
        self.word.table = ReduceTable(word_intipa=self.word.intipa, table_long=self.word.table_long).get_reduced_table()
        self.word.table = self.word.table.reset_index(drop=True)
        self.word.table.index.name = 'id'

    def build(self):
        self.__get_all_stresses()
        self.__get_stressed_word()
        self.__get_intipa()
        self.__get_stressed_vowel()
        self.__get_index_stressed_v()
        self.__get_near_stressed_v()
        self.__get_all_intipa_words()
        self.__get_all_pad_intipa()
        self.__get_all_pattern_pads()
        self.__get_all_score_patterns()
        self.__get_sum_scores()
        self.__get_reverse()
        self.__get_score_pattern_rhyme()
        self.__get_assonance()
        self.__get_table_long()
        self.__get_table()
        return self.word
