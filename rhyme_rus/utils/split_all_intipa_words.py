from multiprocessing import cpu_count


class SplitIntipaWords:

    def __init__(
            self,
            all_stresses: list[str],
            stressed_word: str,
            intipa: list[int],
            stressed_vowel: int,
            near_stressed_v: int,
            index_stressed_v: int,
            all_intipa_words: dict[tuple[int], list[str]]
            ):
        self.all_stresses = all_stresses
        self.stressed_word = stressed_word
        self.intipa = intipa
        self.stressed_vowel = stressed_vowel
        self.near_stressed_v = near_stressed_v
        self.index_stressed_v = index_stressed_v
        self.intipa_words: dict[tuple[int], list[str]] = all_intipa_words
        self.ratio = cpu_count()

    def __get_dict_split(self) -> tuple[tuple[tuple[int], ...], ...]:
        dict_keys: tuple[tuple[int]] = tuple(self.intipa_words.keys())
        cutter: int = len(dict_keys) // self.ratio
        split_array: tuple[tuple[tuple[int], ...], ...]
        split_array = tuple(
            dict_keys[start:stop]
            for start, stop in zip(
                range(0, len(dict_keys), cutter),
                range(cutter, len(dict_keys) + cutter, cutter)
                )
            )
        return split_array

    def __array2dict(self, split_intipa_words: tuple[tuple[tuple[int], ...], ...]) -> list[tuple, ...]:
        split_array: list[tuple, ...] = []
        for item in split_intipa_words:
            new_item: dict[tuple[int], list[str]] = {}
            key: tuple[int]
            for key in item:
                value: list[str] = self.intipa_words[key]
                new_item[key] = value
            all_values: tuple[list[str] | str | list[int] | int | int | int | dict[tuple[int], list[str]]]
            all_values = tuple(
                [
                    self.all_stresses,
                    self.stressed_word,
                    self.intipa,
                    self.stressed_vowel,
                    self.near_stressed_v,
                    self.index_stressed_v,
                    new_item
                    ]
                )
            split_array.append(all_values)
        return split_array

    def split_intipa_words(self) -> list[tuple, ...]:
        split_intipa_words: tuple[tuple[tuple[int], ...], ...] = self.__get_dict_split()
        split_intipa_words: list[tuple, ...] = self.__array2dict(split_intipa_words)
        return split_intipa_words
