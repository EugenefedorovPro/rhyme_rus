import cProfile
import pstats
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure

profiler = cProfile.Profile()
profiler.enable()

target_word = "облако"
word = Word(target_word)
word = Procedure(word).build()
#
path = "rhyme_profile_2.stats"
profiler.disable()
profiler.dump_stats(path)

stats = pstats.Stats(path)
stats.sort_stats("cumtime").print_stats(30)
# stats.print_callees("pattern.py:35")
