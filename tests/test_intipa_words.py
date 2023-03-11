import pytest
from unittest.mock import patch
from rhyme_rus.utils.intipa_words import AllIntipaWords


@pytest.mark.parametrize(
    "intipa, db_response, expected_word_intipa",
    [
        (
                [43, 34, 30],
                [
                    ('ясон', '[43,34,30]'),
                    ('аксон', '[43,34,30]'),
                    ('персона', '[43, 34, 30, 71]'),
                    ('фасона', '[43, 34, 30, 71]'),
                    ('колесо', '[43, 34]'),

                    ],
                {
                    (43, 34, 30): ['аксон', 'ясон'],
                    (43, 34, 30, 71): ['персона', 'фасона'],
                    (43, 34): ['колесо']
                    }
                )
        ]
    )
@patch("rhyme_rus.utils.intipa_words.MySql")
def test_get_intipa_words(cur, intipa, db_response, expected_word_intipa):
    range_sql = 3
    cur().cur_execute.return_value = db_response
    actual_word_intipa = AllIntipaWords(range_sql, intipa).get_all_intipa_words()
    assert actual_word_intipa == expected_word_intipa
