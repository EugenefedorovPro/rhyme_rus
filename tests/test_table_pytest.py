from rhyme_rus.utils.table import Table


def test_table():
    test_rhyme_scores_patterns = {'changes': {0: ('same_cons', 'same_stressed')},
                                  'all': {0: ('same_cons', 'same_stressed')},
                                  'today': {1: ('any_cons', 'same_stressed')},
                                  'even': {1: ('any_cons', 'same_stressed')}
                                  }
    actual = Table(
        rhyme_pattern_score = test_rhyme_scores_patterns
    ).make_dict_for_table()
    expected = {'score': [0, 0, 1, 1], 'pattern': [('same_cons', 'same_stressed'), ('same_cons', 'same_stressed'),
                                                   ('any_cons', 'same_stressed'), ('any_cons', 'same_stressed')],
                'rhyme': ['changes', 'all', 'today', 'even']}
    assert actual == expected
