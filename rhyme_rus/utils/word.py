class Word:
    def __init__(self, unstressed_word):
        self.unstressed_word: str = unstressed_word
        self.stressed_vowel: int = 0
        self.all_stresses: list[str] = []
        self.stressed_word: str = ''
        self.intipa: list[int] = []
        self.all_scope_rhymes_dict: dict[tuple[int], set[str]] = {}
        self.all_scope_rhymes_intipa: list[tuple[int]] = []
        self.all_scope_pads_dict: dict[tuple[int], list[int]] = {}
        self.all_scope_pads_list: list[list[int]] = []
        self.all_rhymes_patterns_dict: dict[tuple[str], list[tuple[int]]] = {}
        self.all_rhymes_patterns_list: list[tuple[int]] = []
        self.all_rhymes_scores_dict: dict[tuple[int], tuple[str]] = {}
        self.sum_scores: dict[int, tuple[str]] = {}
        self.score_rhymes: dict[int, set[str]] = {}
