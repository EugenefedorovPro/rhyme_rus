import pandas as pd
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.utils.exceptions import StressedVowelNotDetected
from rhyme_rus.utils.stressed_word import FactoryStress
from rhyme_rus.utils.intipa_sounds import FactoryIntipaNumbers
from rhyme_rus.utils.intipa_words import MetaAllIntipaWords
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.exceptions import MultipleStresses
from rhyme_rus.utils.range_rhymes import RangeRhymes
from rhyme_rus.utils.pad import Pad
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.utils.pattern import Pattern
from rhyme_rus.utils.score import Score
from rhyme_rus.utils.reverse import Reverse
from rhyme_rus.utils.assonance import Assonance
from rhyme_rus.utils.table import Table


class Procedure:
    def __init__(self, word: Word):
        self.word: Word = word

    def __get_all_stresses(self) -> None:
        self.word.all_stresses = FactoryStress().fetch_stress(self.word.unstressed_word)

    def __get_stressed_word(self) -> None:
        if len(self.word.all_stresses) == 1:
            self.word.stressed_word = self.word.all_stresses[0]
        elif self.word.stressed_word:
            pass
        else:
            raise MultipleStresses(self.word.unstressed_word, self.word.all_stresses)

    def __get_intipa(self) -> None:
        intipa, sounds = FactoryIntipaNumbers().fetch_intipa_sounds(self.word.stressed_word)
        # remove initial stresses, put by NN
        if "ˈ" in sounds:
            sounds = sounds[1:]
        self.word.intipa, self.word.sounds = intipa, sounds

    def __get_numbers(self):
        self.word.numbers = IpaDicts().unistring_to_numbers(self.word.sounds)

    def __get_stressed_vowel(self) -> None:
        for int_ipa in self.word.intipa[:2]:
            if int_ipa in IpaDicts().all_stressed_vowels:
                self.word.stressed_vowel = int_ipa
        if not self.word.stressed_vowel:
            raise StressedVowelNotDetected(self.word.stressed_word, IpaDicts().number2sign, self.word.intipa)

    def __get_index_stressed_v(self) -> None:
        self.word.index_stressed_v = self.word.intipa.index(self.word.stressed_vowel)

    def __get_near_stressed_v(self):
        dict_near_stressed = IpaDicts().near_stressed_v_int
        self.word.near_stressed_v = dict_near_stressed[self.word.stressed_vowel]

    def __get_all_intipa_words(self) -> None:
        self.word.all_intipa_words, self.word.all_word_numbers = MetaAllIntipaWords(self.word.range_sql,
                                                        self.word.intipa).get_all_intipa_words()

    def __get_all_intipa(self) -> None:
        self.word.all_intipa = list(self.word.all_intipa_words.keys())


    def __get_all_pad_intipa(self) -> None:
        self.word.all_pad_intipa = Pad(
            intipa=self.word.intipa,
            all_scope_rhymes_intipa=self.word.all_intipa,
            stressed_vowel=self.word.stressed_vowel,
            near_stressed_v=self.word.near_stressed_v,
            index_stressed_v=self.word.index_stressed_v
        ).get_all_pads_dict()

    def __get_all_pads(self) -> None:
        self.word.all_pads = [list(item) for item in self.word.all_pad_intipa.keys()]

    def __get_all_pattern_pads(self) -> None:
        self.word.all_pattern_pads = Pattern(self.word.intipa,
                                             self.word.all_pads).get_all_rhymes_patterns()

    def __get_all_patterns(self):
        self.word.all_patterns = [key for key in self.word.all_pattern_pads.keys()]

    def __get_all_score_patterns(self) -> None:
        self.word.all_score_patterns = Score(self.word.index_stressed_v,
                                             self.word.all_patterns).get_all_score_patterns()

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
        self.word.assonance = Assonance(numbers=self.word.numbers,
                                        all_word_numbers=self.word.all_word_numbers,
                                        score_pattern_rhyme=self.word.score_pattern_rhyme).get_all_assonance()

    def __get_table(self) -> None:
        self.word.score_pattern_rhyme["assonance"] = self.word.assonance
        self.word.table = pd.DataFrame.from_dict(self.word.score_pattern_rhyme)

    def build(self):
        self.__get_all_stresses()
        self.__get_stressed_word()
        self.__get_intipa()
        self.__get_numbers()
        self.__get_stressed_vowel()
        self.__get_index_stressed_v()
        self.__get_near_stressed_v()
        self.__get_all_intipa_words()
        self.__get_all_intipa()
        self.__get_all_pad_intipa()
        self.__get_all_pads()
        self.__get_all_pattern_pads()
        self.__get_all_patterns()
        self.__get_all_score_patterns()
        self.__get_sum_scores()
        self.__get_reverse()
        self.__get_score_pattern_rhyme()
        self.__get_assonance()
        self.__get_table()
        return self.word
