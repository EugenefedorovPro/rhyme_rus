from multiprocessing import cpu_count


class SplitIntipaWords:
    all_intipa_words: dict[tuple[int], list[str]]

    def __init__(self, all_intipa_words):
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

    def __array2dict(self, split_intipa_words: tuple[tuple[tuple[int], ...], ...]):
        split_array: list[dict] = []
        for item in split_intipa_words:
            new_item: dict[tuple[int], list[str]] = {}
            key: tuple[int]
            for key in item:
                value: list[str] = self.intipa_words[key]
                new_item[key] = value
            split_array.append(new_item)
        return split_array

    def split_intipa_words(self) -> list[dict[tuple[int]:list[str, ...]], ...]:
        split_intipa_words: tuple[tuple[tuple[int], ...], ...] = self.__get_dict_split()
        split_intipa_words: list[dict[tuple[int]:list[str, ...]], ...] = self.__array2dict(split_intipa_words)
        return split_intipa_words
