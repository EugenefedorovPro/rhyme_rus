from pathlib import Path
import dill
from rhyme_rus.rhyme.rhyme import rhyme_till_dict, rhyme_to_table


def test_rhyme_till_dict():
    path = Path.cwd() / "tests/test_rhyme/test_rhyme_till_dict.pkl"
    with open(path, "rb") as f:
        expected_result = dill.load(f)
        expected_result = vars(list(expected_result.items())[10][0][0])
    word = "ко'нь"
    func_result = vars(list(rhyme_till_dict(word).items())[10][0][0])
    assert expected_result == func_result


def test_rhyme_to_table():
    path = Path.cwd() / "tests/test_rhyme/test_rhyme_to_table.pkl"
    with open(path, "rb") as f:
        expected_result = dill.load(f)
    word = "ко'нь"
    func_result = rhyme_to_table(word)
    assert all(expected_result) == all(func_result)
