import pandas as pd
import random
from rhyme_rus.data.wiki_class import Dictionary


class SoundsStatistics():
    @classmethod
    def make_df_n_vowels_after_stress(cls):
        n_sounds_after_stress = [len(item.ipa) for item in Dictionary.instances if item.ipa]
        n_vowels_after_stress = [len(item.ipa.vowels) for item in Dictionary.instances if item.ipa]
        df_n_vowels_after_stress = (pd.DataFrame.from_dict
                                    ({"vowels": n_vowels_after_stress,
                                      "sounds": n_sounds_after_stress})
                                    .value_counts()
                                    .reset_index(name="freq")
                                    .sort_values(by="sounds", ascending=False)
                                    .reset_index(drop=True)
                                    )

        return df_n_vowels_after_stress

    @classmethod
    def get_items_by_n_vowels_after_stress(cls, n_vowels_after_stress,
                                           n_sounds_after_stress,
                                           n_of_words=10,
                                           random_choice=True
                                           ):
        items_by_n_vowels_after_stress = [(item.word, item.sounds)
                                          for i, item in enumerate(Dictionary.instances)
                                          if item.ipa
                                          and len(item.ipa.vowels) == n_vowels_after_stress
                                          and len(item.ipa) == n_sounds_after_stress
                                          ]
        if random_choice:
            rand_n = [random.randint(0, len(items_by_n_vowels_after_stress))
                      for i in range(n_of_words)
                      ]
            items_by_n_vowels_after_stress = [item for i, item
                                              in enumerate(items_by_n_vowels_after_stress)
                                              if i in rand_n
                                              ]
        else:
            items_by_n_vowels_after_stress = [item for i, item in
                                              enumerate(items_by_n_vowels_after_stress)
                                              if i in range(n_of_words)
                                              ]

        return items_by_n_vowels_after_stress


