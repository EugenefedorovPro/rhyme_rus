class Assonance:
    score_pattern_rhyme: dict[str: list[int], str: list[tuple[str], str: list[str]]]
    all_word_numbers: dict[str, tuple[int]]

    def __init__(self, unstressed_word, score_pattern_rhyme):
        self.unstressed_word = unstressed_word
        self.rhymes = score_pattern_rhyme["rhyme"]
        self.score = score_pattern_rhyme["score"]

    # TODO correct type hints
    def get_all_assonance(self):
        all_assonance: list[int] = []
        for rhyme, score in zip(self.rhymes, self.score):
            n_same_sounds: int = len([_str for _str in rhyme if _str in self.unstressed_word])
            len_rhyme = len(rhyme)
            dif_lengths = abs(len(self.unstressed_word) - len_rhyme)
            ratio_n_same_sounds_len = round(
                score / (round(round(n_same_sounds / (len_rhyme + dif_lengths), 1) * 10) + 1))
            all_assonance.append(ratio_n_same_sounds_len)
        return all_assonance
