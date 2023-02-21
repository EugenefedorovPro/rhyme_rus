from itertools import combinations
from rhyme_rus.utils.exceptions import WithNoInitialConsonant
from typing import Iterable


# -1 add_sound
# -2 no_sound
class AllPadWordRhyme:
    def __init__(self, intipa: list[int], all_scope_rhymes_intipa: list[tuple[int]], stressed_vowel: int):
        self.all_scope_rhymes_intipa = all_scope_rhymes_intipa
        self.word = intipa
        self.stressed_vowel = stressed_vowel

    def get_all_pads_dict(self) -> dict[tuple[int], list[tuple[int]]]:
        all_scope_pads: dict[tuple[int], list[tuple[int]]] = {}
        rm: list[int]
        for rm in self.all_scope_rhymes_intipa:
            factory = FactoryPadWordRhyme(self.word, rm, self.stressed_vowel)
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


class FactoryPadWordRhyme:
    def __init__(self, intipa: list[int], intipa_rhyme: list[int], stressed_vowel: int):
        self.word = intipa
        self.rhyme = intipa_rhyme
        self.stressed_vowel = stressed_vowel
        self.word_len = len(intipa)
        self.rhyme_len = len(intipa_rhyme)
        self.target_len = min(len(intipa), len(intipa_rhyme))

    def shorten(self) -> dict[tuple[int], tuple[int]]:
        pwr = PatWordRhyme(self.word, self.rhyme, self.stressed_vowel)
        if self.rhyme_len < self.word_len:
            shorts = pwr.prolong_rhyme()
        elif self.rhyme_len > self.word_len:
            shorts = pwr.shorten_rhyme()
        else:
            shorts = [list(self.rhyme)]

        dict_rhyme_shorts = {tuple(key): self.rhyme for key in shorts}
        return dict_rhyme_shorts


class PatWordRhyme(FactoryPadWordRhyme):
    def __init__(self, intipa: list[int], intipa_rhyme: list[int], stressed_vowel: int):
        super().__init__(intipa, intipa_rhyme, stressed_vowel)
        self.word = intipa
        self.rhyme = intipa_rhyme
        self.stressed_vowel = stressed_vowel
        self.word_len = len(intipa)
        self.rhyme_len = len(intipa_rhyme)
        self.target_len = abs(len(intipa) - len(intipa_rhyme))

    def shorten_rhyme(self) -> list[list[int]]:
        shorts: list[list[int]] = []
        indexes_to_replace: Iterable[tuple] = combinations(range(self.rhyme_len), self.target_len)
        for indexes in indexes_to_replace:
            rhyme_copy = list(self.rhyme).copy()
            for index in indexes:
                rhyme_copy[index] = -1
            # condition to retain stressed_vowel in any combination
            if self.stressed_vowel in rhyme_copy:
                shorts.append(rhyme_copy)
        return shorts

    # intipa_rhyme has a consonant in an initial position,
    # before the stressed vowel
    def __prolong_rhyme_with_cons(self) -> list[list[int]]:
        shorts: list[list[int]] = []
        prolonged_rhyme = list(self.rhyme).copy()
        list_to_extend = [-2 for _ in range(self.target_len)]
        prolonged_rhyme.extend(list_to_extend)
        shorts.append(prolonged_rhyme)
        return shorts

    # intipa_rhyme starts with the stressed vowel
    def __prolong_rhyme_no_consonant(self) -> list[list[int]]:
        shorts: list[list[int]] = []
        prolonged_rhyme = list(self.rhyme).copy()
        shorts.append(self.__prolong_rhyme_with_cons()[0])
        prolonged_rhyme.insert(0, -2)
        list_to_extend = [-2 for _ in range(self.target_len - 1)]
        prolonged_rhyme.extend(list_to_extend)
        shorts.append(prolonged_rhyme)
        return shorts

    def prolong_rhyme(self):
        index_stressed_vowel = self.rhyme.index(self.stressed_vowel)
        if index_stressed_vowel == 1:
            prolonged_rhyme = self.__prolong_rhyme_with_cons()
        elif index_stressed_vowel == 0:
            prolonged_rhyme = self.__prolong_rhyme_no_consonant()
        else:
            raise WithNoInitialConsonant
        return prolonged_rhyme

# if __name__ == "__main__":
#     word = [4, 2, 8]
#     rhyme = [2, 1]
#     stressed_vowel = 2
#     patted_rhyme = FactoryPadWordRhyme(word, rhyme, stressed_vowel).shorten()
#     print(patted_rhyme)
