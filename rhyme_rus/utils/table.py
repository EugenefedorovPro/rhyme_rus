class Table:
    def __init__(self, score_patterns_rhymes):
        self.score_patterns_rhymes: dict[int, dict[tuple[str], tuple[str]]] = score_patterns_rhymes

    def make_table(self):
        table_dict: dict[str, list[int | tuple | str]] = {'score': [], 'pattern': [], 'rhyme': []}
        score: int
        for score in self.score_patterns_rhymes:
            patterns: dict[tuple[str], tuple[str]] = self.score_patterns_rhymes[score]
            pat: tuple[str]
            for pat in patterns:
                rhymes: tuple[str] = patterns[pat]
                for rhyme in rhymes:
                    value_score = table_dict['score']
                    value_score.append(score)
                    table_dict['score'] = value_score

                    value_pat = table_dict['pattern']
                    value_pat.append(pat)
                    table_dict['pattern'] = value_pat

                    value_rhyme = table_dict['rhyme']
                    value_rhyme.append(rhyme)
                    table_dict['rhyme'] = value_rhyme

        return table_dict
