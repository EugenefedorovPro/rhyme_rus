class Pattern:




with open("similarities_pat.pkl", "rb") as f:
    similarities_pat = dill.load(f)

def get_rhyme_pattern(intipa_word, intipa_rhyme) -> tuple[str]:
    word_pattern: list = []
    for _int_word, _int_rhyme in zip(intipa_word, intipa_rhyme):
        similarity: dict[int, str] = similarities_pat[_int_word]
        # print("similarity", similarity)
        # print("_int_rhyme", _int_rhyme)
        try:
            pat: str = similarity[_int_rhyme]
            # print("pat", pat)
            word_pattern.append(pat)
        except KeyError:
            if _int_rhyme in IpaDicts().numbers_vowels:
                word_pattern.append("any_v")
            else:
                word_pattern.append("any_cons")
            # print("exception _int_rhyme", _int_rhyme)
    word_pattern = tuple(word_pattern)
    return word_pattern
