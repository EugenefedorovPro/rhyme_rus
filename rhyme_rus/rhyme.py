import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# from wiktionary_rus.wiktionary import find_item_from_wiki
from rhyme_rus.utils.charts import Charts
from rhyme_rus.utils.ipa_processing import IpaProcessing
from rhyme_rus.utils.patterns import Patterns
from rhyme_rus.utils.rhymeflow import RhymeFlow
from rhyme_rus.utils.score import Score
from rhyme_rus.utils.nn_usage import NnUsage
import pandas as pd
from word2ipa_rus.word2ipa import word2ipa


pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


def stress_word(word_without_stress):
    word_with_stress = NnUsage.accentuate(word_without_stress)
    return word_with_stress


def rhyme(
    word_with_stress,
    max_length_pat_of_ipa=6,
    list_score_numbers=range(0, 45, 5),
    max_number_hard_sounds_in_one_pat=1,
):
    word_as_uni = word2ipa(word_with_stress)
    word_ipa_shortened = NnUsage.get_ipa_shortened(word_as_uni)
    ipa_short_int = IpaProcessing.uni_string_to_int(str(word_ipa_shortened))

    pat_of_ipa = Patterns.take_pat_of_ipa(ipa_short_int)

    if len(pat_of_ipa) > max_length_pat_of_ipa:
        print(
            "Algorythm reduced combinations for {} down to {} "
            "sounds after stressed vowel".format(
                word_with_stress, max_length_pat_of_ipa
            )
        )

        head, tail = Patterns.shorten_pat_long_words_to_head_tail(
            pat_of_ipa, max_length_pat_of_ipa
        )

        ipa_short_int_for_long_words = Patterns.shorten_ipa_short_int_for_long_words(
            ipa_short_int, max_length_pat_of_ipa
        )

        all_rhyme_pats = Patterns.generate_all_rhyme_pats(head)

        all_rhyme_pats = Patterns.condition_all_rhyme_pats(
            all_rhyme_pats,
            ipa_short_int_for_long_words,
            max_number_hard_sounds_in_one_pat,
        )
        print(
            "Algorythm produces patterns, which include only {} "
            "CPU-consuming parameter".format(max_number_hard_sounds_in_one_pat)
        )

        all_rhyme_pats = Patterns.add_sound_to_rhyme_pats(all_rhyme_pats)

        tail_to_pattern = Patterns.convert_tail_to_pattern(tail)

        all_rhyme_pats = Patterns.add_tail_to_pats(all_rhyme_pats, tail_to_pattern)

    else:

        all_rhyme_pats = Patterns.generate_all_rhyme_pats(pat_of_ipa)

        all_rhyme_pats = Patterns.condition_all_rhyme_pats(
            all_rhyme_pats, ipa_short_int, max_number_hard_sounds_in_one_pat
        )

        all_rhyme_pats = Patterns.add_sound_to_rhyme_pats(all_rhyme_pats)

    all_rhyme_pats = Patterns.condition_add_sound_to_rhyme_pats(all_rhyme_pats)

    all_rhyme_pats = Score.reduce_all_rhyme_pats_by_score(
        all_rhyme_pats, list_score_numbers
    )

    dict_all_rhymed_intipa_pat = {}

    for pat in all_rhyme_pats:
        (
            indexes_add_sound,
            indexes_no_sound,
        ) = RhymeFlow.generate_indexes_before_add_no(pat)

        ipa_short_int_new = RhymeFlow.shorten_prolong_ipa(
            ipa_short_int, indexes_add_sound, indexes_no_sound
        )

        new_working_pat = RhymeFlow.remove_no_sound_pat(pat)

        tuple_indexes = RhymeFlow.generate_indexes_after_add_no(new_working_pat)

        rhymed_ints = RhymeFlow.rhymes_by_pat(
            ipa_short_int_new, new_working_pat, tuple_indexes
        )

        if rhymed_ints:

            dict_rhymed_intipa_pat = {ri: tuple(pat) for ri in rhymed_ints}

            dict_all_rhymed_intipa_pat.update(dict_rhymed_intipa_pat)

    dict_rhymed_items_pat = Charts.make_dict_rhymed_items_pat(
        dict_all_rhymed_intipa_pat
    )

    table_word_pat_score = Charts.chart_table_word_pat_score(dict_rhymed_items_pat)

    print(
        "Algorythm produces {} of {} possible combinations".format(
            (list(list_score_numbers)), "range(0, 105, 5)"
        )
    )

    return table_word_pat_score


def rhyme_only_words(
    word_with_stress,
    max_length_pat_of_ipa=6,
    list_score_numbers=range(0, 40, 5),
    max_number_hard_sounds_in_one_pat=1,
):

    table_word_pat_score = rhyme(
        word_with_stress,
        max_length_pat_of_ipa,
        list_score_numbers,
        max_number_hard_sounds_in_one_pat,
    )

    only_words = " ".join(list(table_word_pat_score["rhymes"]))

    only_words = only_words.split()

    length_line = 1

    only_words = [
        " ".join(only_words[i : i + length_line]) + "\n"
        for i in range(0, len(only_words), length_line)
    ]

    only_words = "".join(only_words)
    return only_words
