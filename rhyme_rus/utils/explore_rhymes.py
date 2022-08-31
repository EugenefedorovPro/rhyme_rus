from wiktionary_rus.wiktionary import find_item_from_wiki_unstressed


class ExploreRhymes:
    @classmethod
    def find_rhymes_by_score(cls, score_number, table_word_pat_score):
        rhymes_by_score = table_word_pat_score[
            table_word_pat_score["score"] == score_number
        ]
        return rhymes_by_score

    @classmethod
    def find_rhymes_by_pos(cls, pat_speech, table_word_pat_score):
        rhymes_by_pos = table_word_pat_score[
            table_word_pat_score["part_speech"] == pat_speech
        ]
        return rhymes_by_pos

    @classmethod
    def find_rhymes_by_pattern(cls, pattern, table_word_pat_score):
        rhymes_by_pattern = table_word_pat_score[
            table_word_pat_score["patterns"].apply(lambda x: tuple(x)) == tuple(pattern)
        ]
        return rhymes_by_pattern

    @classmethod
    def find_rhymes_by_word(cls, word, table_word_pat_score):
        rhymes_by_word = table_word_pat_score[table_word_pat_score["rhymes"] == word]
        try:
            str(find_item_from_wiki_unstressed(word)[0].ipa)
        except IndexError:
            return "word {} is unavailable in Wiki".format(word)
        return rhymes_by_word
