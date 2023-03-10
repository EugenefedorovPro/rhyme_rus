from rhyme_rus.utils.reverse import Reverse

intipa: list[int] = []
sum_scores: dict[int, list[tuple[str, ...]]] = {}
all_pattern_pads: dict[tuple[str, ...], list[tuple[int, ...]]] = {}
all_pad_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
all_intipa_words: dict[tuple[int, ...], set[str, ...]] = {}


def test_reverse():
    test_intipa = [1,2,3]
    test_sum_scores = {0: [("same_cons", "same_stressed")]}
    test_all_pattern_pads = {("same_cons", "same_stressed"): [(3,4,5)]}
    test_all_pad_intipa = {(3,4,5): [(1,2,3)]}
    test_all_intipa_words = {(1,2,3): {"all","changes"}}

    actual = Reverse(
        word_intipa = test_intipa,
        sum_scores = test_sum_scores,
        all_pattern_pads = test_all_pattern_pads,
        all_pad_intipa = test_all_pad_intipa,
        all_intipa_words = test_all_intipa_words).reverse()

    expected = {'all': {0: ('same_cons', 'same_stressed')}, 'changes': {0: ('same_cons', 'same_stressed')}}
    assert actual == expected