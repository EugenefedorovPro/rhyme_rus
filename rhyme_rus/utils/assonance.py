class Assonance:
    score_pattern_rhyme: dict[str: list[int], str: list[tuple[str], str: list[str]]]
    all_word_numbers: dict[str, tuple[int]]
    def __init__(self, numbers, all_word_numbers, score_pattern_rhyme):
        self.numbers: set[int] = set(numbers)
        self.all_word_numbers = all_word_numbers
        self.rhymes = score_pattern_rhyme["rhyme"]


    def get_all_assonance(self):
        all_assonance: list[int] = []
        for rhyme in self.rhymes:
           rhyme_intipa: tuple[int] | set[int] = set(self.all_word_numbers[rhyme])
           n_same_sounds: list[int] = [_int for _int in rhyme_intipa if _int in self.numbers]
           all_assonance.append(len(n_same_sounds))
        return all_assonance



