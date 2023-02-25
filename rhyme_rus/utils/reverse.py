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

    def reverse(self) -> dict[[str, dict[int, tuple[str]]]]:
        score_patterns_rhymes: dict[[str, dict[int, tuple[str]]]] = {}
        score: int
        for score in self.sum_scores:
            patterns: tuple[str] = self.sum_scores[score]
            pat: tuple[str]
            for pat in patterns:
                pads: list[list[int]] = self.all_rhymes_patterns_dict[pat]
                pad: list[int]
                for pad in pads:
                    rhymes_intipa: list[tuple[int]] = self.all_scope_pads_dict[tuple(pad)]
                    for rhyme_intipa in rhymes_intipa:
                        rhymes: list[str] = list(self.all_scope_rhymes_dict[rhyme_intipa])
                        for rm in rhymes:
                            if rm in score_patterns_rhymes:
                                score_pat: dict[int, tuple[str]] = score_patterns_rhymes[rm]
                                min_score_pat: dict[int, tuple[str]] = {min(score_pat): score_pat[min(score_pat)]}
                                score_patterns_rhymes[rm] = min_score_pat
                            else:
                                score_patterns_rhymes[rm] = {score: pat}

        return score_patterns_rhymes
