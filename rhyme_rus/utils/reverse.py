class Reverse:
    sum_scores: dict[int, tuple[str]]
    all_rhymes_patterns_dict: dict[tuple[str], list[list[int]]]
    all_scope_pads_dict: dict[tuple[int], list[tuple[int]]]
    all_scope_rhymes_dict: dict[tuple[int], set[str]]

    def __init__(self, sum_scores, all_rhymes_patterns_dict, all_scope_pads_dict, all_scope_rhymes_dict):
        self.sum_scores = sum_scores
        self.all_rhymes_patterns_dict = all_rhymes_patterns_dict
        self.all_scope_pads_dict = all_scope_pads_dict
        self.all_scope_rhymes_dict = all_scope_rhymes_dict
        self.ratio: int = 1
        self.cut_sum_scores: dict[int, list[tuple[str]]] = {}
        self.__get_cut_sum_scores()

    def __get_cut_sum_scores(self) -> None:
        cut_number = round(len(self.sum_scores) / self.ratio)
        self.cut_sum_scores: dict[int, tuple[str]] = {}
        for i, key in enumerate(self.sum_scores):
            if i <= cut_number:
                value = self.sum_scores[key]
                self.cut_sum_scores[key] = value

    def reverse(self):
        score_patterns_rhymes: dict[int, dict[tuple[str], tuple[str]]] = {}
        score: int
        for score in self.cut_sum_scores:
            patterns: list[tuple[str]] = self.cut_sum_scores[score]
            pat: tuple[str]
            for pat in patterns:
                pads: list[list[int]] = self.all_rhymes_patterns_dict[pat]
                pad: list[int]
                for pad in pads:
                    rhymes_intipa: list[tuple[int]] = self.all_scope_pads_dict[tuple(pad)]
                    for rhyme_intipa in rhymes_intipa:
                        rhymes: list[str] = list(self.all_scope_rhymes_dict[rhyme_intipa])

                        if score not in score_patterns_rhymes:
                            pattern_rhymes: dict[tuple[str], tuple[str]] = {pat: rhymes}
                            score_patterns_rhymes[score] = pattern_rhymes
                        else:
                            values_pat: dict[tuple[str], tuple[str]] = score_patterns_rhymes[score]
                            if pat not in values_pat:
                                values_pat[pat] = rhymes
                                score_patterns_rhymes[score] = values_pat
                            else:
                                values_rhymes = values_pat[pat]
                                values_rhymes.extend(rhymes)
                                values_pat[pat] = values_rhymes
                                score_patterns_rhymes[score] = values_pat

        return score_patterns_rhymes
