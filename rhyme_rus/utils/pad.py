from itertools import combinations
from typing import Iterable


# -1 add_sound
# -2 no_sound
class Pad:
    def __init__(self, intipa: list[int], all_scope_rhymes_intipa: list[tuple[int]], stressed_vowel: int,
                 near_stressed_v: int, index_stressed_v: int):
        self.all_intipa = all_scope_rhymes_intipa
        self.word = intipa
        self.stressed_vowel = stressed_vowel
        self.near_stressed_v: int = near_stressed_v
        self.index_stressed_v = index_stressed_v

    def get_all_pads_dict(self) -> dict[tuple[int], list[tuple[int]]]:
        all_scope_pads: dict[tuple[int], list[tuple[int]]] = {}
        rm: tuple[int]
        for rm in self.all_intipa:
            factory = FactoryPad(
                intipa=self.word,
                intipa_rhyme=rm,
                stressed_vowel=self.stressed_vowel,
                near_stressed_v=self.near_stressed_v,
                index_stressed_v=self.index_stressed_v
            )
            shorts = factory.shorten()
            for key in shorts:
                if key not in all_scope_pads:
                    value = [shorts[key]]
                    all_scope_pads[key] = value
                else:
                    key: tuple[int]
                    value_short: tuple[int] = shorts[key]
                    value_pad: list[tuple[int]] = all_scope_pads[key]
                    value_pad.append(value_short)
                    new_value: list[tuple[int]] = value_pad
                    all_scope_pads[key] = new_value
        return all_scope_pads


class FactoryPad:
    def __init__(self, intipa: list[int], intipa_rhyme: list[int], stressed_vowel: int, near_stressed_v: int,
                 index_stressed_v: int):
        self.word = intipa
        self.rhyme = intipa_rhyme
        self.rhyme_preprocessed: tuple[int] = tuple()
        self.word_preprocessed: list[int] = []
        self.stressed_vowel: int = stressed_vowel
        self.near_stressed_v: int = near_stressed_v
        self.index_stressed_vowel_word: int = index_stressed_v
        self.index_stressed_vowel_rhyme: int = 0
        self.word_len: int = len(intipa)
        self.rhyme_len: int = len(intipa_rhyme)
        self.index_farthest_stressed_v: int = 0
        self.__fit_stressed_vowel()
        self.__get_index_stressed_vowel_rhyme()
        self.__get_rhyme_preprocessed()
        self.__get_word_preprocessed()
        self.__get_index_farthest_stressed_v()

    def __fit_stressed_vowel(self):
        if self.rhyme[0] != self.stressed_vowel and self.rhyme[1] != self.stressed_vowel:
            self.stressed_vowel = self.near_stressed_v

    def __get_index_stressed_vowel_rhyme(self) -> None:
        self.index_stressed_vowel_rhyme = self.rhyme.index(self.stressed_vowel)

    # TODO correct logics
    # process initial consonants
    # when word_preprocessed and rhyme are of the same length, and either of them has initial consonant
    # 0 is a stressed vowels
    # 1) word_preprocessed = (1, 0, 2, 3), rhyme = (0, 3, 4, 5) -> _rhyme = (-3, 0, 3, 4, 5)
    # 2) word_preprocessed = (0, 1, 2, 3), rhyme = (1, 0, 2, 3) -> _rhyme = (-4, 0, 2, 3)
    def __get_rhyme_preprocessed(self) -> None:
        if self.index_stressed_vowel_word != self.index_stressed_vowel_rhyme:
            self.rhyme_preprocessed: list[int] | tuple[int] = list(self.rhyme).copy()
            if self.index_stressed_vowel_word == 1:
                self.rhyme_preprocessed.insert(0, -3)
            else:
                self.rhyme_preprocessed.pop(0)
                self.rhyme_preprocessed.insert(0, -4)
            self.rhyme_preprocessed = tuple(self.rhyme_preprocessed)
        else:
            self.rhyme_preprocessed = self.rhyme

    def __get_word_preprocessed(self) -> None:
        self.word_preprocessed = self.word.copy()
        if self.index_stressed_vowel_word < self.index_stressed_vowel_rhyme:
            self.word_preprocessed.insert(0, 0)

    def __get_index_farthest_stressed_v(self):
        self.index_farthest_stressed_v = max(self.index_farthest_stressed_v, self.index_stressed_vowel_rhyme)

    def shorten(self) -> dict[tuple[int], tuple[int]]:
        pwr = PadWordRhyme(self.word_preprocessed, self.rhyme_preprocessed, self.stressed_vowel, self.near_stressed_v,
                           self.index_stressed_vowel_word, self.index_farthest_stressed_v)
        len_rhyme_preprocessed = len(self.rhyme_preprocessed)
        len_word_preprocessed = len(self.word_preprocessed)
        if len_rhyme_preprocessed < len_word_preprocessed:
            shorts = pwr.prolong_rhyme()
        elif len_rhyme_preprocessed > len_word_preprocessed:
            shorts = pwr.shorten_rhyme()
        else:
            shorts = [list(self.rhyme_preprocessed)]

        dict_rhyme_shorts = {tuple(key): self.rhyme for key in shorts}
        return dict_rhyme_shorts


class PadWordRhyme:
    def __init__(self, intipa: list[int], intipa_rhyme: tuple[int], stressed_vowel: int, near_stressed_v: int,
                 index_stressed_vowel_word: int, index_farthest_stressed_v: int):
        self.word_preprocessed = intipa
        self.rhyme = intipa_rhyme
        self.stressed_vowel = stressed_vowel
        self.near_stressed_v = near_stressed_v
        self.index_stressed_vowel_word = index_stressed_vowel_word
        self.word_len = len(intipa)
        self.rhyme_len = len(intipa_rhyme)
        self.target_len = abs(len(intipa) - len(intipa_rhyme))
        self.index_farthest_stressed_v = index_farthest_stressed_v

    def shorten_rhyme(self) -> list[list[int]]:
        shorts: list[list[int]] = []
        indexes_to_replace: Iterable[tuple] = combinations(range(self.index_farthest_stressed_v + 1, self.rhyme_len),
                                                           self.target_len)
        indexes_to_replace = list(indexes_to_replace)
        for indexes in indexes_to_replace:
            rhyme_copy = list(self.rhyme).copy()
            for index in indexes:
                rhyme_copy[index] = -1
            # condition to retain stressed_vowel in any combination
            if self.stressed_vowel == rhyme_copy[self.index_stressed_vowel_word]:
                shorts.append(rhyme_copy)
        return shorts

    def prolong_rhyme(self) -> list[list[int]]:
        shorts: list[list[int]] = []
        prolonged_rhyme = list(self.rhyme).copy()
        list_to_extend = [-2 for _ in range(self.target_len)]
        prolonged_rhyme.extend(list_to_extend)
        shorts.append(prolonged_rhyme)
        return shorts

# if __name__ == "__main__":
#     word_preprocessed = [4, 2, 8]
#     rhyme = [2, 1]
#     stressed_vowel = 2
#     patted_rhyme = FactoryPad(word_preprocessed, rhyme, stressed_vowel).shorten()
#     print(patted_rhyme)
