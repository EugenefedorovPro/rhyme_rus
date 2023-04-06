from rhyme_rus.rhyme import rhyme_with_stresses, rhyme
import pytest
from rhyme_rus.utils.exceptions import MultipleStresses


def test_with_stresses():
    actual = rhyme_with_stresses("пушкинд")
    expected = (None, ["пушки'нд", "пу'шкинд"], None)
    assert actual == expected


def test_rhyme():
    with pytest.raises(MultipleStresses):
        rhyme("пушкинд")
