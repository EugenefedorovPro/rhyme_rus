def get_all_word_numbers(all_intipa_words: dict[tuple[int], set[str]]):
    all_words_numbers: dict[str, tuple(int)] = {}
    intipa: tuple[int]
    for intipa in all_intipa_words:
        words: tuple[str] = tuple(all_intipa_words[intipa])
        for word in words:
            all_words_numbers[word] = intipa
    return all_words_numbers




