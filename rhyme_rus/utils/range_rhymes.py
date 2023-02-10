class RangeRhymes:
    def __init__(self, all_rhymes_scores):
        self.all_rhyme_scores = all_rhymes_scores

    def get_sum_scores(self) -> dict[int, list[tuple[int]]]:
        sum_scores = {}
        for item in self.all_rhyme_scores.items():
            key: list[int] = list(item[0])
            value: list[tuple[int]] = item[1]
            sum_scores[sum(key)] = value
        sum_scores = dict(sorted(sum_scores.items()))
        return sum_scores
