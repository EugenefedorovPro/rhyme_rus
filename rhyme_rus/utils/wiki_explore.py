import random
import pandas as pd
from wiktionary_rus.wiktionary import wiki_instances


class WikiExplore:
    @classmethod
    def make_df_n_vowels_after_stress(cls):
        n_sounds_after_stress = [
            len(item.ipa) for item in wiki_instances if item.ipa and item.status
        ]
        n_vowels_after_stress = [
            len(item.ipa.vowels) for item in wiki_instances if item.ipa and item.status
        ]
        df_n_vowels_after_stress = (
            pd.DataFrame.from_dict(
                {"vowels": n_vowels_after_stress, "sounds": n_sounds_after_stress}
            )
            .value_counts()
            .reset_index(name="freq")
            .sort_values(by="sounds", ascending=False)
            .reset_index(drop=True)
        )

        return df_n_vowels_after_stress

    @classmethod
    def get_items_by_n_vowels_after_stress(
        cls,
        n_vowels_after_stress,
        n_sounds_after_stress,
        n_of_words,
        random_choice=True,
    ):
        items_by_n_vowels_after_stress = [
            (item.word, item.sounds)
            for i, item in enumerate(wiki_instances)
            if item.ipa
            and item.status
            and len(item.ipa.vowels) == n_vowels_after_stress
            and len(item.ipa) == n_sounds_after_stress
        ]
        if random_choice:
            rand_n = [
                random.randint(0, len(items_by_n_vowels_after_stress))
                for i in range(n_of_words)
            ]
            items_by_n_vowels_after_stress = [
                item
                for i, item in enumerate(items_by_n_vowels_after_stress)
                if i in rand_n
            ]
        else:
            items_by_n_vowels_after_stress = [
                item
                for i, item in enumerate(items_by_n_vowels_after_stress)
                if i in range(n_of_words)
            ]

        return items_by_n_vowels_after_stress
