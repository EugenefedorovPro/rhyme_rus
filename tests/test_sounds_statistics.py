import dill
import pandas as pd
from rhyme_rus.utils.sounds_statistics import SoundsStatistics


def test_make_df_n_vowels_after_stress():
    output = pd.read_excel(
        "tests/test_sounds_statistics/make_df_n_vowels_after_stress.xlsx"
    )
    assert all(output) == all(SoundsStatistics.make_df_n_vowels_after_stress())


def test_get_items_by_n_vowels_after_stress():
    with open(
        "tests/test_sounds_statistics/get_items_by_n_vowels_after_stress.pkl", "rb"
    ) as f:
        output_list = dill.load(f)
    assert output_list == SoundsStatistics.get_items_by_n_vowels_after_stress(
        4, 10, 5, False
    )
