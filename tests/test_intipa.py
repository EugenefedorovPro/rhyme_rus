import pytest
from unittest.mock import patch
from rhyme_rus.utils.intipa import FactoryIntipa
from collections import namedtuple
from typing import NamedTuple

NamedTuple('Words', [('accent', str), ('uni', str), ('intipa', list[tuple[str]])])

Words = namedtuple('Words', ['accent', 'intipa', 'intipa_processed'])
son = Words("со'н", [43, 34, 30], [('[43, 34, 30]',)])
kochka = Words("ко'чка", [18, 34, 54, 18, 71], [('[18, 34, 54, 18, 71]',)])
suvo = Words("суво'", [48, 83], [('[48,83]',)])


@pytest.mark.parametrize(
    "stressed_word, intipa_expected, intipa_processed", [
        (son.accent, son.intipa, son.intipa_processed),
        (kochka.accent, kochka.intipa, kochka.intipa_processed),
        (suvo.accent, suvo.intipa, suvo.intipa_processed)
        ]
    )
@patch("rhyme_rus.utils.intipa.my_sql")
def test_intipa(my_sql, stressed_word, intipa_expected, intipa_processed):
    my_sql.cur_execute.return_value = intipa_processed
    intipa_result: list[int] = FactoryIntipa().fetch_intipa(stressed_word)
    assert intipa_result == intipa_expected
