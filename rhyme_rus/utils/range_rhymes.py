class RangeRhymes:
    def __init__(self, all_scores: dict[tuple[int], tuple[str]]):
        self.all_scores = all_scores

    def get_sum_scores(self) -> dict[int, tuple[str]]:
        sum_scores: dict[int, tuple[str]] = {}
        for item in self.all_scores.items():
            key: tuple[int] = item[0]
            value: tuple[str] = item[1]
            sum_scores[sum(key)] = value
        sum_scores = dict(sorted(sum_scores.items()))
        return sum_scores
