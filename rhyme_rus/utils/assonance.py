class Assonance:
    score_pattern_rhyme: dict[str: list[int], str: list[tuple[str], str: list[str]]]
    all_word_numbers: dict[str, tuple[int]]
    def __init__(self, unstressed_word, score_pattern_rhyme):
        self.unstressed_word = unstressed_word
        self.rhymes = score_pattern_rhyme["rhyme"]


    def get_all_assonance(self):
        all_assonance: list[int] = []
        for rhyme in self.rhymes:
           n_same_sounds: list[str] = [_str for _str in rhyme if _str in self.unstressed_word]
           all_assonance.append(len(n_same_sounds))
        return all_assonance



