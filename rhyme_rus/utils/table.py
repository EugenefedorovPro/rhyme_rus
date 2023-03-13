class Table:
    def __init__(self, rhyme_scores_patterns):
        self.rhyme_scores_patterns: dict[[str, dict[int, tuple[str]]]] = rhyme_scores_patterns

    def make_dict_for_table(self) -> dict[str: list[int], str: list[tuple[str], str: list[str]]]:
        score_pattern_rhyme: dict[str: list[int], str: list[tuple[str], str: list[str]]]
        score_pattern_rhyme = {"score": [], "pattern": [], "rhyme": []}
        for rhyme in self.rhyme_scores_patterns:
            score_pattern = self.rhyme_scores_patterns[rhyme]
            for score in score_pattern:
                pattern = score_pattern[score]

                scores = score_pattern_rhyme["score"]
                scores.append(score)
                score_pattern_rhyme["score"] = scores

                patterns = score_pattern_rhyme["pattern"]
                patterns.append(pattern)
                score_pattern_rhyme["pattern"] = patterns

                rhymes = score_pattern_rhyme["rhyme"]
                rhymes.append(rhyme)
                score_pattern_rhyme["rhyme"] = rhymes
        return score_pattern_rhyme
