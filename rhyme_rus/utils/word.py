class Word:
    def __init__(self, unstressed_word):
        self.unstressed_word: str = unstressed_word
        self.all_stresses: list[str] = []
        self.stressed_word: str = ''
        self.intipa: list[int] = []
        self.all_scope_rhymes_dict: dict[tuple[int], set[str]] = {}
        self.all_scope_rhymes_intipa: list[tuple[int]] = []
        self.all_rhymes_patterns: dict[tuple[str], list[tuple[int]]] = {}
        self.all_rhymes_scores: dict[tuple[int], list[tuple[int]]] = {}
        self.sum_scores = {}
