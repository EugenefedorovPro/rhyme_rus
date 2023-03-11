import dill
from pathlib import Path
from collections import OrderedDict


class Reverse:
    sum_scores: dict[int, tuple[str]]
    all_pattern_pads: dict[tuple[str], list[list[int]]]
    all_pad_intipa: dict[tuple[int], list[tuple[int]]]
    all_intipa_words: dict[tuple[int], set[str]]

    def __init__(self, word_intipa, sum_scores, all_pattern_pads, all_pad_intipa, all_intipa_words):
        self.word_intipa = word_intipa
        self.sum_scores = sum_scores
        self.all_pattern_pads = all_pattern_pads
        self.all_pad_intipa = all_pad_intipa
        self.all_intipa_words = all_intipa_words
        self.similarities: dict[int, dict] = {}
        self.__get_similarities()

    def __get_similarities(self):
        # TODO similarities data is in seeds folder, not in data
        path = Path(__file__).parent.parent / "seeds/similarities_pat.pkl"
        with open(path, "rb") as f:
            self.similarities: dict[int, dict[int, str]] = dill.load(f)

    def reverse(self) -> dict[[str, dict[int, tuple[str]]]]:
        rhyme_scores_patterns: dict[[str, dict[int, tuple[str]]]] = OrderedDict()
        score: int
        for score in self.sum_scores:
            patterns: tuple[str] = self.sum_scores[score]
            pat: tuple[str]
            for pat in patterns:
                pads: list[list[int]] = self.all_pattern_pads[pat]
                pad: list[int]
                for pad in pads:
                    rhymes_intipa: list[tuple[int]] = self.all_pad_intipa[tuple(pad)]
                    for rhyme_intipa in rhymes_intipa:
                        rhymes: list[str] = list(self.all_intipa_words[rhyme_intipa])
                        for rm in rhymes:
                            # rhyme_scores_patterns
                            if rm in rhyme_scores_patterns:
                                score_pat: dict[int, tuple[str]] = rhyme_scores_patterns[rm]
                                min_score_pat: dict[int, tuple[str]] = OrderedDict(
                                    [(min(score_pat), score_pat[min(score_pat)])]
                                    )
                                rhyme_scores_patterns[rm] = min_score_pat
                            else:
                                rhyme_scores_patterns[rm] = {score: pat}

        return rhyme_scores_patterns
