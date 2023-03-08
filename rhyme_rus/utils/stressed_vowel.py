from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.utils.exceptions import StressedVowelNotDetected
from typing import Optional

def get_stressed_vowel(intipa: list[int], stressed_word: str) -> Optional[int]:
    int_ipa: int
    stressed_vowel = None
    for int_ipa in intipa[:2]:
        if int_ipa in IpaDicts().all_stressed_vowels:
            stressed_vowel = int_ipa
    if not stressed_vowel:
        raise StressedVowelNotDetected(stressed_word, IpaDicts().number2sign, intipa)
    else:
        return stressed_vowel


