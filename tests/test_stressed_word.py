from rhyme_rus.utils.stressed_word import get_stressed_word
from rhyme_rus.utils.exceptions import MultipleStresses
import pytest

@pytest.mark.parametrize("stressed_word, all_stresses, expected_stressed_word", [
    ("дом", ["до'м"], "до'м"),
    ("остров", ["о'стров"], "о'стров"),
    ("ель", ["е'ль"], "е'ль")
]
                         )
def test_get_stressed_word(stressed_word, all_stresses, expected_stressed_word):
   actual_stressed_word = get_stressed_word(all_stresses, stressed_word)
   assert actual_stressed_word == expected_stressed_word

def test_get_stressed_word_exception():
    all_stresses = ["за'мок", "замо'к"]
    stressed_word = "за'мок"
    with pytest.raises(MultipleStresses) as mstreses:
        get_stressed_word(all_stresses, stressed_word)
    assert mstreses.value.all_stresses == ["за'мок", "замо'к"]
    assert mstreses.value.unstressed_word == stressed_word

# f"{unstressed_word} has  stress variants for a user to choose from {all_stresses}"
