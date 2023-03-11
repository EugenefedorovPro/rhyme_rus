from collections import OrderedDict


class RangeRhymes:
    def __init__(self, all_scores: dict[tuple[int], list[tuple[str]]]):
        self.all_scores = all_scores

    def get_sum_scores(self) -> dict[int, list[tuple[str]]]:
        sum_scores: dict[int, list[tuple[str]]] = OrderedDict()
        for item in self.all_scores.items():
            key: tuple[int] = item[0]
            value: list[tuple[str]] = item[1]
            summa = sum(key)
            if summa not in sum_scores:
                sum_scores[summa] = value
            else:
                old_value = sum_scores[summa]
                old_value.extend(value)
                sum_scores[summa] = old_value
        sum_scores = dict(sorted(sum_scores.items()))
        return sum_scores
