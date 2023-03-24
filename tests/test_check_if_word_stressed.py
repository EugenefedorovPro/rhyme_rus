from rhyme_rus.utils.word import Word
from rhyme_rus.utils.procedure import Procedure


def test_check_if_word_stressed():
    input_word = "пу'шкинд"
    word = Word(input_word)
    Procedure(word)
    assert word.stressed_word == "пу'шкинд"
    assert word.unstressed_word == "пушкинд"
