import dill
from pathlib import Path
from rhyme_rus.seeds.ipa_dicts import IpaDicts


class Pattern:
    def __init__(self, word_intipa: list[int], list_intipa: dict[tuple[int], list[tuple[int]]]):
        self.word_intipa: list[int] = word_intipa
        self.list_intipa: list[tuple[int]] = list(list_intipa)
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

    # if word_preprocessed = [1,2,3], rhyme = [1,2,3,-2,-2]
    # fun will process only first three positions:
    # ["any", "any", "any"]
    # TODO vowels_but_stressed - how to simplify?
    def __get_rhyme_pattern_short(self, rhyme_intipa) -> tuple[str]:
        word_padded = self.__get_word_padded(rhyme_intipa)
        except_pats = {-1: "add_sound", -2: "no_sound", -3: "no_init_cons", -4: "add_init_cons"}
        vowels_but_stressed = {"same_stressed": "same_v", "near_stressed": "near_v"}
        rhyme_pattern: list = []
        for i, _int_word_int_rhyme in enumerate(zip(word_padded, rhyme_intipa)):
            _int_word, _int_rhyme = _int_word_int_rhyme[0], _int_word_int_rhyme[1]
            try:
                similarity: dict[int, str] = self.similarities[_int_word]
            except KeyError:
                similarity = {-4: "add_init_cons"}
            try:
                pat: str = similarity[_int_rhyme]
                if i not in (0, 1) and pat in ("same_stressed", "near_stressed"):
                    pat = vowels_but_stressed[pat]
                rhyme_pattern.append(pat)
            except KeyError:
                if _int_rhyme in except_pats:
                    rhyme_pattern.append(except_pats[_int_rhyme])
                elif _int_rhyme in self.all_vowels:
                    rhyme_pattern.append("any_v")
                elif _int_rhyme in self.all_consonants:
                    rhyme_pattern.append("any_cons")

        rhyme_pattern: tuple[str] = tuple(rhyme_pattern)
        return rhyme_pattern

    def __get_word_padded(self, rhyme_intipa):
        word_padded: list[int] = self.word_intipa.copy()
        if rhyme_intipa[0] == -4:
            word_padded.insert(0, 0)
        indexes_minus_1 = [i for i, __ in enumerate(rhyme_intipa) if __ == -1]
        for index in indexes_minus_1:
            word_padded.insert(index, 0)
        return word_padded

    def get_all_pattern_pads(self) -> dict[tuple[str], list[list[int]]]:
        all_rhymes_patterns: dict[tuple[str], list[list[int]]] = {}
        rhyme_intipa: list[int]
        for rhyme_intipa in self.list_intipa:
            rhyme_pattern: tuple[str] = self.__get_rhyme_pattern_short(rhyme_intipa)
            if rhyme_pattern not in all_rhymes_patterns:
                all_rhymes_patterns[rhyme_pattern] = [rhyme_intipa]
            else:
                list_rhyme_intipa = all_rhymes_patterns[rhyme_pattern]
                list_rhyme_intipa.append(rhyme_intipa)
                all_rhymes_patterns[rhyme_pattern] = list_rhyme_intipa
        return all_rhymes_patterns
