from rhyme_rus.utils.pattern import Pattern
# legend - {-1: "add_sound", -2: "no_sound", -3: "no_init_cons", -4: "add_init_cons"}


word_intipa = [18, 34, 2, 39, 71]
list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(34, 36, -1, 39, 71):[(0,0,0)]}

if __name__ == "__main__":
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    print(all_rhymes_patterns)

