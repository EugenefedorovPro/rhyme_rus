import pytest
from unittest.mock import patch

from rhyme_rus.utils.word import Word


@pytest.mark.parametrize(
    "unstressed_word, db_response, expected_all_stresses, expected_stressed_word, expected_sounds, expected_intipa", [
        ("конь", [("ко'нь",)], ["ко'нь"], "ко'нь", "konʲ", [18, 34, 31]),
        ("замок", [("за'мок",), ("замо'к",)], ["за'мок", "замо'к"], '', '', []),
        ("цветаева", [("цвета'ева",), ("цве'таева",), ("цветае'ва",), ("цветаева'",)],
         ["цвета'ева", "цве'таева", "цветае'ва", "цветаева'"], '', '', []),
        ["бор", [("бо'р",), ("бо'р",), ("бо'р",), ("бо'р",), ("бо'р",), ("бо'р",)], ["бо'р"], "бо'р", 'bor',
         [2, 34, 39]]
    ]
)
@patch("rhyme_rus.utils.fetch_stressed_word.MySql")
def test_word(mock_mysql: patch, unstressed_word: str, db_response: list[tuple[str]], expected_all_stresses: list[str],
              expected_stressed_word: str, expected_sounds: str, expected_intipa: list[int]):
    mock_mysql.cur_execute.return_value = db_response
    word = Word(unstressed_word)
    all_stresses = word.all_stresses
    stressed_word = word.stressed_word
    sounds = word.sounds
    intipa = word.intipa
    assert (all_stresses, stressed_word, sounds, intipa) == (
        expected_all_stresses, expected_stressed_word, expected_sounds, expected_intipa)
