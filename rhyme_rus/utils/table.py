import pandas as pd


class Table:
    def __init__(self, rhyme_pattern_score):
        self.rhyme_pattern_score: dict[[str, dict[int, tuple[str]]]] = rhyme_pattern_score

    def __reduce_table(self, score_pattern_rhyme):
        pass

    def make_dict_for_table(self) -> dict[str: list[int], str: list[tuple[str], str: list[str]]]:
        score_pattern_rhyme: dict[str: list[int], str: list[tuple[str], str: list[str]]]
        score_pattern_rhyme = {"score": [], "pattern": [], "rhyme": []}
        for rhyme in self.rhyme_pattern_score:
            score_pattern = self.rhyme_pattern_score[rhyme]
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
