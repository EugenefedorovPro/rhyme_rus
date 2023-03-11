import pandas as pd


class Word:
    def __init__(self, unstressed_word):
        self.unstressed_word: str = unstressed_word
        self.range_sql = 3
        self.stressed_vowel: int = 0
        self.index_stressed_v: int = 0
        self.near_stressed_v: int = 0
        self.all_stresses: list[str] = []
        self.stressed_word: str = ''
        self.intipa: list[int] = []
        self.all_intipa_words: dict[tuple[int], set[str]] = {}
        self.all_pad_intipa: dict[tuple[int], list[tuple[int]]] = {}
        self.all_pattern_pads: dict[tuple[str], list[tuple[int]]] = {}
        self.all_score_patterns: dict[tuple[int], list[tuple[str]]] = {}
        self.sum_scores: dict[int, list[tuple[str]]] = {}
        self.rhyme_scores_patterns: dict[[str, dict[int, tuple[str]]]] = {}
        self.score_pattern_rhyme: dict[str: list[int], str: list[tuple[str], str: list[str]]] | dict[str: list[int],
                                                                                                str: list[int],
                                                                                                str: list[tuple[str],
                                                                                                     str: list[
                                                                                                         str]]] = {}
        self.assonance: list[int] = []
        self.table_long: pd.DataFrame = pd.DataFrame()
        self.table: pd.DataFrame = pd.DataFrame()
