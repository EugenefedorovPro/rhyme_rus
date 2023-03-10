from rhyme_rus.utils.range_rhymes import RangeRhymes

if __name__ == "__main__":
    all_score_patterns: dict[tuple[int, ...], list[tuple[str, ...]]] = {(0,1,2): [("any_v", "same_stressed")]}
    sum_scores = RangeRhymes(all_score_patterns).get_sum_scores()
    print(sum_scores)
