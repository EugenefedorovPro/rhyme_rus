from typing import Union


class Score:
    def __init__(self, index_stressed_v, patterns):
        self.index_stressed_v = index_stressed_v
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

    def __get_rhyme_score(self, pat: tuple[str]) -> tuple[int]:
        pat_copy: list[str] = list(pat)
        score: list[int] = []
        for i, p in enumerate(pat_copy):
            # 'дом' - 'ом', no_sound in 'ом' score 1, not 5 as in other cases
            # if the stressed 'o' in 'дом' takes the second position, that is index == 1
            # 'ом' - 'дом', add_sound (-2) in 'дом' scores 1 instead of 5 anyway
            if (p == "add_sound" and i == 0 and self.index_stressed_v == 1) or (
                    p == "no_sound" and i == 0 and self.index_stressed_v == 1
            ):
                score.append(1)
            else:
                score.append(self.dict_pat_score[p])
        return tuple(score)

    def get_all_rhymes_scores_dict(self) -> dict[tuple[int], list[tuple[str]]]:
        all_rhyme_scores: dict[tuple[int], list[tuple[str]]] = {}
        pat: Union[tuple[str], list[tuple[str]]]
        for pat in self.patterns:
            score: tuple[int] = self.__get_rhyme_score(pat)
            if score not in all_rhyme_scores:
                all_rhyme_scores[score] = [pat]
            else:
                value = all_rhyme_scores[score]
                value.append(pat)
                all_rhyme_scores[score] = value

        return all_rhyme_scores
