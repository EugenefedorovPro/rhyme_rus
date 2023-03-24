import sys

sys.tracebacklimit = 0


class MultipleStresses(Exception):

    def __init__(self, unstressed_word, all_stresses):
        self.unstressed_word = unstressed_word
        self.all_stresses = all_stresses

    def __str__(self):
        return f'''
        {self.unstressed_word} has  stress variants for a user to choose from\r
        {self.all_stresses}\r
        write input word with proper stressed_vowel like\r
        rhyme("за'мок")
        '''


class WithNoInitialConsonant(Exception):
    def __str__(self):
        return "something's wrong with(out) initial consonant in intipa_rhyme"


class StressedVowelNotDetected(Exception):
    def __init__(self, stressed_word, number2sign, intipa):
        self.stressed_word = stressed_word
        self.number2sign = number2sign
        self.intipa = intipa

    def __str__(self):
        stressed_vowel_0 = str(self.number2sign[self.intipa[0]])
        stressed_vowel_1 = str(self.number2sign[self.intipa[1]])
        return f'''stressed_vowel_0 is {self.intipa[0]} - {stressed_vowel_0}, 
                stressed_vowel_1 is {self.intipa[1]} {stressed_vowel_1}'''
