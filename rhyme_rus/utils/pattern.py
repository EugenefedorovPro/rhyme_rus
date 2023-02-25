import dill
from pathlib import Path
from rhyme_rus.seeds.ipa_dicts import IpaDicts


class Pattern:
    def __init__(self, word_intipa: list[int], list_intipa: list[list[int]]):
        self.word_intipa: list[int] = word_intipa
        self.list_intipa: list[list[int]] = list_intipa
        self.all_vowels: tuple[int] = tuple()
        self.all_consonants: tuple[int] = tuple()
        self.similarities: dict[int, dict[int, str]] = {}
        self.__get_all_vowels()
        self.__get_all_consonants()
        self.__get_similarities()

    def __get_all_vowels(self):
        self.all_vowels: tuple[int] = IpaDicts().numbers_vowels

    def __get_all_consonants(self):
        self.all_consonants: tuple[int] = IpaDicts().numbers_consonants

    def __get_similarities(self):
        # TODO similarities data is in seeds folder, not in data
        path = Path(__file__).parent.parent / "seeds/similarities_pat.pkl"
        with open(path, "rb") as f:
            self.similarities: dict[int, dict[int, str]] = dill.load(f)

    # if word = [1,2,3], rhyme = [1,2,3,-2,-2]
    # fun will process only first three positions:
    # ["any", "any", "any"]
    def __get_rhyme_pattern_short(self, rhyme_intipa) -> list[str]:
        rhyme_pattern: list = []
        for _int_word, _int_rhyme in zip(self.word_intipa, rhyme_intipa):
            similarity: dict[int, str] = self.similarities[_int_word]
            try:
                pat: str = similarity[_int_rhyme]
                rhyme_pattern.append(pat)
            except KeyError:
                if _int_rhyme == -1:
                    rhyme_pattern.append("no_sound")
                elif _int_rhyme == -2:
                    rhyme_pattern.append("add_sound")
                elif _int_rhyme in self.all_vowels:
                    rhyme_pattern.append("any_v")
                elif _int_rhyme in self.all_consonants:
                    rhyme_pattern.append("any_cons")

        rhyme_pattern: list[str] = rhyme_pattern
        return rhyme_pattern

    def __get_rhyme_pattern(self, rhyme_intipa) -> tuple[str]:
        rhyme_pattern: list[str] = self.__get_rhyme_pattern_short(rhyme_intipa)
        len_word = len(self.word_intipa)
        len_rhyme = len(rhyme_intipa)
        len_dif = abs(len_word - len_rhyme)
        if len(self.word_intipa) < len(rhyme_intipa):
            rhyme_pattern.extend(["add_sound" for _ in range(len_dif)])
        return tuple(rhyme_pattern)

    def get_all_rhymes_patterns(self) -> dict[tuple[str], list[tuple[int]]]:
        all_rhymes_patterns: dict[tuple[str], list[tuple[int]]] = {}
        rhyme_intipa: tuple[int]
        for rhyme_intipa in self.list_intipa:
            rhyme_pattern: tuple[str] = self.__get_rhyme_pattern(rhyme_intipa)
            if rhyme_pattern not in all_rhymes_patterns:
                all_rhymes_patterns[rhyme_pattern] = [rhyme_intipa]
            else:
                list_rhyme_intipa = all_rhymes_patterns[rhyme_pattern]
                list_rhyme_intipa.append(rhyme_intipa)
                all_rhymes_patterns[rhyme_pattern] = list_rhyme_intipa
        return all_rhymes_patterns

