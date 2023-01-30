class Word:
    def __init__(self, unstressed_word):
        self.unstressed_word: str = unstressed_word
        self.all_stresses: list[str] = []
        self.stressed_word: str = ''
        self.intipa: list[int] = []
        self.all_scope_rhymes: list[str] = []
