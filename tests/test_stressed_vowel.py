from rhyme_rus.utils.stressed_vowel import get_stressed_vowel
from rhyme_rus.utils.exceptions import StressedVowelNotDetected
import pytest

@pytest.mark.parametrize("intipa, stressed_word, stressed_vowel_expected", [
    ([18, 34, 47], "ко'т", 34),
    ([34, 30], "о'н", 34),
    ([56, 22, 77, 16], "у'лей", 56)
]
                         )
def test_get_stressed_vowel(intipa, stressed_word, stressed_vowel_expected):
    stressed_vowel_processed = get_stressed_vowel(intipa, stressed_word)
    assert stressed_vowel_expected == stressed_vowel_processed


# class StressedVowelNotDetected(Exception):
# return f"in the word {self.stressed_word} stressed vowel {stressed_vowel_0} or {stressed_vowel_1} not detected"


def test_get_stressed_vowel_exception():
    intipa = [18, 47]
    stressed_word = 'кт'
    with pytest.raises(StressedVowelNotDetected) as notdetected:
        get_stressed_vowel(intipa, stressed_word)
    assert notdetected.value.stressed_word == stressed_word
    assert notdetected.value.intipa == intipa
