from typing import Union


class Score:
    def __init__(self, index_stressed_v, patterns):
        self.index_stressed_v = index_stressed_v
        self.patterns: list[tuple[int]] = patterns
        self.dict_pat_score: dict[str, int] = {"same_stressed": 0,
                                               "same_v": 0,
                                               "same_cons": 0,
                                               "near_stressed": 1,
                                               "near_v": 1,
                                               "add_init_cons": 1,
                                               "no_init_cons": 1,
                                               "prolong": 1,
                                               "voice": 2,
                                               "voice_prolong": 2,
                                               "palat": 3,
                                               "any_cons": 4,
                                               "any_v": 4,
                                               "add_sound": 5,
                                               "no_sound": 5
                                               }

    def __get_rhyme_score(self, pat: tuple[str]) -> tuple[int]:
        pat_copy: list[str] = list(pat)
        score: list[int] = []
        for p in pat_copy:
            score.append(self.dict_pat_score[p])
        return tuple(score)

    def get_all_score_patterns(self) -> dict[tuple[int], list[tuple[str]]]:
        all_rhyme_scores: dict[tuple[int], list[tuple[str]]] = {}
        pat: Union[tuple[str], list[tuple[str]]]
        rm_stress_index: int
        for pat in self.patterns:
            score: tuple[int] = self.__get_rhyme_score(pat)
            if score not in all_rhyme_scores:
                all_rhyme_scores[score] = [pat]
            else:
                value = all_rhyme_scores[score]
                value.append(pat)
                all_rhyme_scores[score] = value

        return all_rhyme_scores
