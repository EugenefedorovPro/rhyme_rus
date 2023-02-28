import pandas as pd


class Word:
    def __init__(self, unstressed_word):
        self.unstressed_word: str = unstressed_word
        self.stressed_vowel: int = 0
        self.index_stressed_v: int = 0
        self.near_stressed_v: int = 0
        self.all_stresses: list[str] = []
        self.stressed_word: str = ''
        self.intipa: list[int] = []
        self.all_scope_rhymes_dict: dict[tuple[int], set[str]] = {}
        self.all_scope_rhymes_intipa: list[tuple[int]] = []
        self.all_scope_pads_dict: dict[tuple[int], list[tuple[int]]] = {}
        self.all_scope_pads_list: list[list[int]] = []
        self.all_rhymes_patterns_dict: dict[tuple[str], list[tuple[int]]] = {}
        self.all_rhymes_patterns_list: list[tuple[int]] = []
        self.all_rhymes_scores_dict: dict[tuple[int], list[tuple[str]]] = {}
        self.sum_scores: dict[int, list[tuple[str]]] = {}
        self.rhyme_pattern_score: dict[[str, dict[int, tuple[str]]]] = {}
        self.table: pd.DataFrame = pd.DataFrame()
