from rhyme_rus.utils.score import *
from rhyme_rus.utils.dictionary_processing import DictionaryProcessing


class Charts:
    @classmethod
    def make_dict_rhymed_items_pat(cls, dict_all_rhymed_intipa_pat):
        dict_of_int_from_ipa = DictionaryProcessing.make_dict_of_int_from_ipa()
        dict_rhymed_items_pat = {dict_of_int_from_ipa[_intipa[0]]: _intipa[1] for _intipa
                                 in dict_all_rhymed_intipa_pat.items()}
        return dict_rhymed_items_pat

    @classmethod
    def chart_table_word_pat_score(cls, dict_rhymed_items_pat):
        col_words = []
        col_pats = []
        col_score = []
        col_pos = []
        for item in dict_rhymed_items_pat.items():
            # print(item[1])
            pat_score = Score.count_score_pat(item[1])
            pat = item[1]
            for it in item[0]:
                col_words.append(it.word)
                col_pats.append(pat)
                col_score.append(pat_score)
                col_pos.append(it.pos)
        table_word_pat_score = pd.DataFrame.from_dict(
            {"rhymes": col_words, "patterns": col_pats,
             "part_speech": col_pos, "score": col_score})\
            .sort_values("score")\
            .reset_index(drop=True)\
            .drop_duplicates()

        return table_word_pat_score

