from rhyme_rus.utils.intipa_sounds import IpaDicts
from rhyme_rus.utils.pattern import Pattern
from rhyme_rus.utils.score import Score


class PatternScore:
    def __init__(self, word_intipa, list_intipa):
        self.word_intipa: list[int] = word_intipa
        self.list_intipa: list[list[int]] = list_intipa
        self.all_vowels: tuple[int] = tuple()
        self.__get_all_vowels()

    def __get_all_vowels(self):
        self.all_vowels: tuple[int] = IpaDicts().numbers_vowels

    def get_patterns(self):
        all_rhymes_patterns = Pattern(self.word_intipa, self.list_intipa).get_all_rhymes_patterns()
        return all_rhymes_patterns

    def get_scores(self):
        all_rhymes_score = Score(self.word_intipa, self.list_intipa).get_all_rhymes_scores()
        return all_rhymes_score
