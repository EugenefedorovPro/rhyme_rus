from rhyme_rus.utils.range_rhymes import RangeRhymes

def test_range_rhymes():
    all_score_patterns: dict[tuple[int, ...], list[tuple[str, ...]]] = {(0,1,2): [("any_v", "same_stressed")]}
    actual_sum_scores = RangeRhymes(all_score_patterns).get_sum_scores()
    expected_sum_scores = {3: [('any_v', 'same_stressed')]}
    assert actual_sum_scores == expected_sum_scores