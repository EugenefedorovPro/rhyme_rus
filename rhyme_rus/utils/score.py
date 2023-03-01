from typing import Union


class Score:
    def __init__(self, index_stressed_v, all_rhymes_stressed_index, patterns):
        self.index_stressed_v = index_stressed_v
        self.rhymes_stressed_index = all_rhymes_stressed_index
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

    def __get_rhyme_score(self, pat: tuple[str], rm_stress_index) -> tuple[int]:
        pat_copy: list[str] = list(pat)
        score: list[int] = []
        for i, p in enumerate(pat_copy):
            # first - target word, second - rhyme
            # 'дом' - 'ом', add_sound (-2) in 'ом' score 1, not 5 as in other cases
            # if the stressed 'o' in rhyme 'ом' takes the initial position, that is index == 0
            # 'ом' - 'дом', no_sound (-1) in 'дом' scores 1 instead of 5
            # if stressed  'о' in target word 'ом' takes index 0
            if (p == "add_sound" and i == 0 and rm_stress_index == 0) or (
                    p == "no_sound" and i == 0 and self.index_stressed_v == 0
            ):
                score.append(1)
            else:
                score.append(self.dict_pat_score[p])
        return tuple(score)

    def get_all_rhymes_scores_dict(self) -> dict[tuple[int], list[tuple[str]]]:
        all_rhyme_scores: dict[tuple[int], list[tuple[str]]] = {}
        pat: Union[tuple[str], list[tuple[str]]]
        rm_stress_index: int
        for pat, rm_stress_index in zip(self.patterns, self.rhymes_stressed_index):
            score: tuple[int] = self.__get_rhyme_score(pat, rm_stress_index)
            if score not in all_rhyme_scores:
                all_rhyme_scores[score] = [pat]
            else:
                value = all_rhyme_scores[score]
                value.append(pat)
                all_rhyme_scores[score] = value

        return all_rhyme_scores
