from functools import lru_cache
import pandas as pd


class Score:
    @classmethod
    @lru_cache()
    def get_dict_score(cls):
        dict_score = {
            "same_cons": 0,
            "voice_cons": 1,
            "palatal_cons": 2,
            "any_cons": 3,
            "no_sound": 4,
            "same_v": 0,
            "same_stressed_v": 0,
            "near_stressed_v": 3,
            "any_v": 4,
            "add_sound": 5,
        }
        return dict_score

    @classmethod
    def round_score(cls, score_pat):
        return score_pat - score_pat % 5

    @classmethod
    def sum_numbers(cls, number):
        summa = 0
        for n in list(range(number + 1)):
            summa = summa + n
        return summa

    @classmethod
    def count_score_pat(cls, pat):
        dict_score = cls.get_dict_score()
        max_possible_score = max(dict_score.values()) + 1
        penalties_for_position = cls.sum_numbers(len(pat))
        score_pat = 0
        for i, p in enumerate(pat):
            if p in ["any_cons", "no_sound", "any_v", "add_sound"]:
                score_pat = score_pat + dict_score[p] + i + len(pat) ** 1 / 2
            elif p in ["voice_cons", "palatal_cons", "near_stressed_v"]:
                score_pat = score_pat + dict_score[p] + i + len(pat) ** 1 / 3
            else:
                score_pat = score_pat + dict_score[p]

        score_pat = (
            score_pat / (max_possible_score * len(pat) + penalties_for_position)
        ) * 100
        score_pat = round(Score.round_score(score_pat))

        return score_pat

    @classmethod
    def make_dict_scores(cls, all_rhyme_pats):
        dict_scores = {}
        for pat in all_rhyme_pats:
            score_pat = cls.count_score_pat(pat)
            if score_pat not in dict_scores:
                dict_scores[score_pat] = [pat]
            else:
                current_val = dict_scores[score_pat]
                current_val.append(pat)
                dict_scores[score_pat] = current_val
        dict_scores = dict(sorted(dict_scores.items()))
        return dict_scores

    @classmethod
    def make_table_score_n_pats(cls, all_rhyme_pats):
        dict_scores = cls.make_dict_scores(all_rhyme_pats)
        list_keys = []
        list_n_pats = []
        for key in dict_scores:
            n_pats = 0
            n_pats = len(dict_scores[key])
            list_n_pats.append(n_pats)
            list_keys.append(key)
        table_score_n_pats = pd.DataFrame.from_dict(
            {"score": list_keys, "n_pats": list_n_pats}
        ).sort_values(by="score", ascending=False)
        return table_score_n_pats

    @classmethod
    def reduce_all_rhyme_pats_by_score(
        cls, all_rhyme_pats, list_score_numbers=range(0, 50, 5)
    ):
        for pat in all_rhyme_pats:
            for sn in list_score_numbers:
                if cls.count_score_pat(pat) == sn:
                    yield pat
