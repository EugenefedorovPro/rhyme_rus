from rhyme_rus.utils.table import Table

if __name__ == "__main__":
    test_rhyme_scores_patterns  = {'changes': {0: ('same_cons', 'same_stressed')},
                'all': {0: ('same_cons', 'same_stressed')},
                'today': {1: ('any_cons', 'same_stressed')},
                'even': {1: ('any_cons', 'same_stressed')}
                }
    score_pattern_rhyme = Table(
    rhyme_pattern_score  = test_rhyme_scores_patterns
                                ).make_dict_for_table()
    print(score_pattern_rhyme)