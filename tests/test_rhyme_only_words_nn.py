from rhyme_rus.rhyme import rhyme_only_words


def test_rhyme_only_words_nn(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "грибое'дов")
    with open(
        "tests/test_rhyme_only_words_nn/test_rhyme_only_words_nn.txt",
        "r",
        encoding="UTF-8",
    ) as f:
        output = f.read()
    assert output == rhyme_only_words("грибоедов")


def test_rhyme_only_words_nn_two(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "замо'к")
    with open(
        "tests/test_rhyme_only_words_nn/test_rhyme_only_words_nn_two.txt",
        "r",
        encoding="UTF-8",
    ) as f:
        output = f.read()
    assert output == rhyme_only_words("замок", list_score_numbers=[0])
