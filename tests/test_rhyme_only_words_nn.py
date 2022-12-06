from rhyme_rus.rhyme import rhyme_only_words


def test_rhyme_only_words_nn():
    with open(
        "tests/test_rhyme_only_words_nn/test_rhyme_only_words_nn.txt",
        "r",
        encoding="UTF-8",
    ) as f:
        output = f.read()
    assert output == rhyme_only_words("грибое'дов")


def test_rhyme_only_words_nn_two():
    with open(
        "tests/test_rhyme_only_words_nn/test_rhyme_only_words_nn_two.txt",
        "r",
        encoding="UTF-8",
    ) as f:
        output = f.read()
    assert output == rhyme_only_words("замо'к", list_score_numbers=[0])
