import multi_process as mp
from time import perf_counter
import rhyme as r


def assess_time_oneprocessor_rhyming(word_with_stress):
    start_time = perf_counter()
    output_one = r.rhyme_to_table(word_with_stress)
    time_passed = perf_counter() - start_time
    return time_passed, output_one


word_with_stress = "ко'бра"

time_elapsed, output_mult = mp.rhyme_with_multiprocess(word_with_stress)
time_passed, output_one = assess_time_oneprocessor_rhyming(word_with_stress)

print("time_elapsed, output_multi", time_elapsed)
print("time_passed, output_one", time_passed)
