from numba import jit
from timeit import timeit
from rhyme_rus.rhyme import rhyme_to_table

def assess_regular(word_with_stress):
    mysetup = '''
from rhyme_rus.rhyme import rhyme_to_table
word_with_stress = "{}"'''.format(word_with_stress)

    mystmt = "rhyme_to_table(word_with_stress)"
    time_passed = timeit(setup=mysetup, stmt=mystmt, number=1)
    return time_passed

def assess_numba(word_with_stress):
    mysetup = '''

from numba import jit
from rhyme_rus.rhyme import rhyme_to_table
word_with_stress = "{}"
    '''.format(word_with_stress)
    
    mystmt = '''
@jit(nopython=True)
def rhyme_under_jit():
    _ = rhyme_to_table(word_with_stress)
    '''
    time_passed = timeit(setup=mysetup, stmt=mystmt, number=1)
    return time_passed

@jit(nopython=True)
def rhyme_with_numba(word_with_stress):
    output = rhyme_to_table(word_with_stress)
    return output


