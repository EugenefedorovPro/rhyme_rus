from rhyme_rus.utils.stressed_word import FactoryStress
from rhyme_rus.utils.intipa import FactoryIntipa
from rhyme_rus.utils.all_scope_rhymes import MetaAllScopeRhymes
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.exceptions import MultipleStresses
from rhyme_rus.utils.range_rhymes import RangeRhymes
from rhyme_rus.utils.pat_word_rhyme import AllPadWordRhyme
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.utils.pattern import Pattern
from rhyme_rus.utils.score import Score
from rhyme_rus.utils.reverse import Reverse


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
        self.word.intipa = FactoryIntipa().fetch_intipa(self.word.stressed_word)

    def __get_stressed_vowel(self) -> None:
        for int_ipa in self.word.intipa[:2]:
            if int_ipa in IpaDicts().all_stressed_vowels:
                self.word.stressed_vowel = int_ipa

    def __get_index_stressed_v(self) -> None:
        self.word.index_stressed_v = self.word.intipa.index(self.word.stressed_vowel)

    def __get_near_stressed_v(self):
        dict_near_stressed = IpaDicts().near_stressed_v_int
        self.word.near_stressed_v = dict_near_stressed[self.word.stressed_vowel]

    def __get_all_scope_rhymes_dict(self) -> None:
        self.word.all_scope_rhymes_dict = MetaAllScopeRhymes(self.word.intipa).get_all_scope_rhymes_dict()

    def __get_all_scope_rhymes_intipa(self) -> None:
        self.word.all_scope_rhymes_intipa = list(self.word.all_scope_rhymes_dict.keys())

    def __get_all_scope_pads_dict(self) -> None:
        self.word.all_scope_pads_dict = AllPadWordRhyme(
            intipa=self.word.intipa,
            all_scope_rhymes_intipa=self.word.all_scope_rhymes_intipa,
            stressed_vowel=self.word.stressed_vowel,
            near_stressed_v=self.word.near_stressed_v,
            index_stressed_v=self.word.index_stressed_v
        ).get_all_pads_dict()

    def __get_all_scope_pads_list(self) -> None:
        self.word.all_scope_pads_list = [list(item) for item in self.word.all_scope_pads_dict.keys()]

    def __get_all_rhyme_patterns_dict(self) -> None:
        self.word.all_rhymes_patterns_dict = Pattern(self.word.intipa,
                                                     self.word.all_scope_pads_list).get_all_rhymes_patterns()

    def __get_all_rhyme_patterns_list(self):
        self.word.all_rhymes_patterns_list = [key for key in self.word.all_rhymes_patterns_dict.keys()]

    def __get_all_rhyme_scores_dict(self) -> None:
        self.word.all_rhymes_scores_dict = Score(self.word.all_rhymes_patterns_list).get_all_rhymes_scores_dict()

    def __get_sum_scores(self) -> None:
        self.word.sum_scores = RangeRhymes(self.word.all_rhymes_scores_dict).get_sum_scores()

    def __get_reverse(self) -> None:
        self.word.score_rhymes = Reverse(
            self.word.sum_scores,
            self.word.all_rhymes_patterns_dict,
            self.word.all_scope_pads_dict,
            self.word.all_scope_rhymes_dict).reverse()

    def build(self):
        self.__get_all_stresses()
        self.__get_stressed_word()
        self.__get_intipa()
        self.__get_stressed_vowel()
        self.__get_index_stressed_v()
        self.__get_near_stressed_v()
        self.__get_all_scope_rhymes_dict()
        self.__get_all_scope_rhymes_intipa()
        self.__get_all_scope_pads_dict()
        self.__get_all_scope_pads_list()
        self.__get_all_rhyme_patterns_dict()
        self.__get_all_rhyme_patterns_list()
        self.__get_all_rhyme_scores_dict()
        self.__get_sum_scores()
        # self.__get_reverse()
        return self.word
