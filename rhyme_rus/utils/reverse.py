class Reverse:
    sum_scores: dict[int, tuple[str]]
    all_rhymes_patterns_dict: dict[tuple[str], list[list[int]]]
    all_scope_pads_dict: dict[tuple[int], tuple[int]]
    all_scope_rhymes_dict: dict[tuple[int], set[str]]

    def __init__(self, sum_scores, all_rhymes_patterns_dict, all_scope_pads_dict, all_scope_rhymes_dict):
        self.sum_scores = sum_scores
        self.all_rhymes_patterns_dict = all_rhymes_patterns_dict
        self.all_scope_pads_dict = all_scope_pads_dict
        self.all_scope_rhymes_dict = all_scope_rhymes_dict
        self.ratio: int = 1
        self.cut_sum_scores: dict[int, tuple[str]] = {}
        self.__get_cut_sum_scores()

    def __get_cut_sum_scores(self) -> None:
        cut_number = round(len(self.sum_scores) / self.ratio)
        self.cut_sum_scores = {}
        for i, key in enumerate(self.sum_scores):
            if i <= cut_number:
                value = self.sum_scores[key]
                self.cut_sum_scores[key] = value

    def reverse(self):
        score_rhymes: dict[int, set[str]] = {}
        score: int
        for score in self.cut_sum_scores:
            pattern: tuple[str] = self.cut_sum_scores[score]
            pads: list[list[int]] = self.all_rhymes_patterns_dict[pattern]
            pad: list[int]
            for pad in pads:
                rhymes_intipa: tuple[int] = self.all_scope_pads_dict[tuple(pad)]
                rhymes: set[str] = self.all_scope_rhymes_dict[rhymes_intipa]
                if score not in score_rhymes:
                    score_rhymes[score] = rhymes
                else:
                    values: set[str] = score_rhymes[score]
                    values.update(rhymes)
                    score_rhymes[score] = values
        return score_rhymes
