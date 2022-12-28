from rhyme_rus.utils.sounds_statistics import SoundsStatistics
from rhyme_rus.utils.nn_usage import NnUsage
from timeit import default_timer as timer
from pathlib import Path
import json
import dill
from slugify import slugify
from rhyme_rus.rhyme import rhyme, rhyme_with_stressed_word
import matplotlib.pyplot as plt 
import rhyme_rus

class RhymingTime(SoundsStatistics):
    pass

df_n_vowels_after_stress = RhymingTime.make_df_n_vowels_after_stress()
print(df_n_vowels_after_stress)
