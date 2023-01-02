from rhyme_rus.rhyme import rhyme_to_table, rhyme_to_table_with_jit
from time import perf_counter

def reg(word_with_stress):
    time_start = perf_counter()
    output = rhyme_to_table(word_with_stress)
    time_passed = perf_counter() - time_start
    return time_passed, output

def jitt(word_with_stress):
    time_start = perf_counter()
    output = rhyme_to_table_with_jit(word_with_stress)
    time_passed = perf_counter() - time_start
    return time_passed, output

word_with_stress = "о'блако"
reg_time_passed, reg_output = reg(word_with_stress)
jitt_time_passed, jitt_output = jitt(word_with_stress)

print(reg_time_passed)
print(jitt_time_passed)
print(reg_time_passed/ jitt_time_passed)
print(jitt_output["rhymes"])
