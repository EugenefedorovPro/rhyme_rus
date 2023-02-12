import dill
from pathlib import Path
from rhyme_rus.utils.intipa import IpaDicts


class Score:
    def __init__(self, patterns):
        self.patterns: list[tuple[int]] = patterns
        self.dict_pat_score: dict[str, int] = {"same_stressed": 0,
                                               "same_v": 0,
                                               "same_cons": 0,
                                               "near_stressed": 1,
                                               "prolong": 1,
                                               "voice": 2,
                                               "voice_prolong": 2,
                                               "palat": 3,
                                               "any_cons": 4,
                                               "any_v": 4,
                                               "add_sound": 5,
                                               "no_sound": 5
                                               }

    def __get_rhyme_score(self, pat: tuple[str]) -> list[int]:
        pat_copy: list[str] = list(pat)
        score: list[int] = []
        for p in pat_copy:
            score.append(self.dict_pat_score[p])
        return score

    def get_all_rhymes_scores_dict(self) -> dict[tuple[int], tuple[str]]:
        all_rhyme_scores: dict[tuple[int], tuple[str]] = {}
        pat: tuple[str]
        for pat in self.patterns:
            score: list[int] = self.__get_rhyme_score(pat)
            all_rhyme_scores[tuple(score)] = pat
        return all_rhyme_scores
