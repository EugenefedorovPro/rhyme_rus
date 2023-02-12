from rhyme_rus.utils.stressed_word import FactoryStress
from rhyme_rus.utils.intipa import FactoryIntipa
from rhyme_rus.utils.all_scope_rhymes import MetaAllScopeRhymes
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.exceptions import MultipleStresses
from rhyme_rus.utils.pattern_score import PatternScore
from rhyme_rus.utils.range_rhymes import RangeRhymes
from rhyme_rus.utils.pat_word_rhyme import AllPadWordRhyme
from rhyme_rus.seeds.ipa_dicts import IpaDicts


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
        for intipa in self.word.intipa[:2]:
            if intipa in IpaDicts().all_stressed_vowels:
                self.word.stressed_vowel = intipa

    def __get_all_scope_rhymes_dict(self) -> None:
        self.word.all_scope_rhymes_dict = MetaAllScopeRhymes(self.word.intipa).get_all_scope_rhymes_dict()

    def __get_all_scope_rhymes_intipa(self) -> None:
        self.word.all_scope_rhymes_intipa = list(self.word.all_scope_rhymes_dict.keys())

    def __get_all_scope_pads_dict(self) -> None:
        self.word.all_scope_pads_dict = AllPadWordRhyme(
            intipa=self.word.intipa,
            all_scope_rhymes_intipa=self.word.all_scope_rhymes_intipa,
            stressed_vowel=self.word.stressed_vowel
        ).get_all_pads_dict()

    def __get_all_scope_pads_list(self) -> None:
        self.word.all_scope_pads_list = [list(item) for item in self.word.all_scope_pads_dict.keys()]

    def __get_all_rhyme_patterns(self) -> None:
        self.word.all_rhymes_patterns = PatternScore(self.word.intipa, self.word.all_scope_pads_list).get_patterns()

    def __get_all_rhyme_scores(self) -> None:
        self.word.all_rhymes_scores = PatternScore(self.word.intipa, self.word.all_scope_rhymes_intipa).get_scores()

    def __get_sum_scores(self) -> None:
        self.word.sum_scores = RangeRhymes(self.word.all_rhymes_scores).get_sum_scores()

    def build(self):
        self.__get_all_stresses()
        self.__get_stressed_word()
        self.__get_intipa()
        self.__get_stressed_vowel()
        self.__get_all_scope_rhymes_dict()
        self.__get_all_scope_rhymes_intipa()
        self.__get_all_scope_pads_dict()
        self.__get_all_scope_pads_list()
        self.__get_all_rhyme_patterns()
        # self.__get_all_rhyme_scores()
        # self.__get_sum_scores()
        return self.word
