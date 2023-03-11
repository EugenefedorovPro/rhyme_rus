from unittest.mock import patch
import pytest

from rhyme_rus.utils.all_stresses import (
    FetchStressFromNn,
    FactoryStress
    )


@pytest.mark.parametrize(
    "unstressed_word, stressed_word", [('быль', ["бы'ль"]),
                                       ('киев', ["кие'в", "ки'ев"])
                                       ]
    )
def test_fetch_stress_from_nn(unstressed_word: str, stressed_word: list[tuple]):
    nn = FetchStressFromNn(unstressed_word)
    one_stressed_word = nn.fetch_stress()
    assert stressed_word == one_stressed_word


# noinspection PyRedundantParentheses
@pytest.mark.parametrize(
    "unstressed_word, word_from_db, expected_stressed_word", [
        ("дом", [("до'м",)], ["до'м"]),
        ("баргузин", [], (["баргузи'н", "ба'ргузин", "баргу'зин"])),
        ("округа", [("окру'га",), ("о'круга",), ("округа'",)], ["окру'га", "о'круга", "округа'"]),
        ("зинзивер", [], ["зинзи'вер", "зи'нзивер", "зинзиве'р"]),
        ("моль", [("мо'ль",)], ["мо'ль"])
        ]
    )
@patch("rhyme_rus.utils.all_stresses.MySql")
def test_factory_stress(cur, unstressed_word, word_from_db, expected_stressed_word):
    cur().cur_execute.return_value = word_from_db
    actual_stressed_word = FactoryStress.fetch_stress(unstressed_word)
    assert set(actual_stressed_word) == set(expected_stressed_word)
