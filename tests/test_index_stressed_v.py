import pytest
from rhyme_rus.utils.index_stressed_v import get_index_stressed_v

@pytest.mark.parametrize("intipa, stressed_vowel, expected_index", [
    ([56, 26], 56, 0),
    ([43, 34, 30], 34, 1),
]
                         )

def test_get_index_stressed_v(intipa, stressed_vowel, expected_index):
   actual_index = get_index_stressed_v(intipa, stressed_vowel)
   assert actual_index == expected_index