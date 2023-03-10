from rhyme_rus.utils.pattern import Pattern

# "same_stressed", "same_v", "same_cons", "near_stressed", "near_v", "add_init_cons", "no_init_cons", "prolong",
# "voice", "voice_prolong", "palat", "any_cons", "any_v", "add_sound", "no_sound"

# "near_v",
def test_get_all_patterns_pads_no_init():
    word_intipa = [6, 34, 26]  # дом
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(-3, 34, 26):[(0,0,0)]} # ом
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('no_init_cons', 'same_stressed', 'same_cons'): [(-3, 34, 26)]}
    assert expected == all_rhymes_patterns
def test_get_all_patterns_pads_add_init():
    word_intipa = [34, 26]  # ом
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(-4, 34, 26):[(0,0,0)]} # лом, дом
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('add_init_cons', 'same_stressed', 'same_cons'): [(-4, 34, 26)]}
    assert expected == all_rhymes_patterns
def test_get_all_patterns_pads_near_stressed_palat():
    word_intipa = [6, 34, 26]  # дом
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(7, 78, 79):[(0,0,0)]} # одёж
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('palat', 'near_stressed', 'any_cons'): [(7, 78, 79)]}
    assert expected == all_rhymes_patterns
def test_get_all_patterns_pads_prolong():
    word_intipa = [6, 34, 26]  # дом
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(9, 34, 26):[(0,0,0)]} # роддом
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('prolong', 'same_stressed', 'same_cons'): [(9, 34, 26)]}
    assert expected == all_rhymes_patterns
def test_get_all_patterns_pads_voice():
    word_intipa = [6, 34, 26]  # дом
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(47, 34, 26):[(0,0,0)]} # том
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('voice', 'same_stressed', 'same_cons'): [(47, 34, 26)]}
    assert expected == all_rhymes_patterns
def test_get_all_patterns_pads_same_v():
    word_intipa = [18, 34, 2, 39, 71]  # кобра
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(40, 78, 2, 39, 71):[(0,0,0)]} # рёбра
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('any_cons', 'near_stressed', 'same_cons', 'same_cons', 'same_v'): [(40, 78, 2, 39, 71)]}
    assert expected == all_rhymes_patterns
def test_get_all_patterns_pads_voice_prolong():
    word_intipa = [18, 34, 2, 39, 71]  # кобра
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(18, 34, 38, 71):[(0,0,0)]} # коппа
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('same_cons', 'same_stressed', 'voice_prolong', 'any_v'): [(18, 34, 38, 71)]}
    assert expected == all_rhymes_patterns
def test_get_all_patterns_pads_any_v():
    word_intipa = [18, 34, 2, 39, 71]  # кобра
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(18, 34, 2, 39, 76):[(0,0,0)]} # кобры
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('same_cons', 'same_stressed', 'same_cons', 'same_cons', 'any_v'): [(18, 34, 2, 39, 76)]}
    assert expected == all_rhymes_patterns
def test_get_all_patterns_pads_no_sound():
    word_intipa = [18, 34, 2, 39, 71]  # кобра
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(47, 34, -2, 39, 71):[(0,0,0)]} # штора
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('any_cons', 'same_stressed', 'no_sound', 'same_cons', 'same_v'): [(47, 34, -2, 39, 71)]}
    assert expected == all_rhymes_patterns
def test_get_all_patterns_pads_add_sound():
    word_intipa = [18, 34, 2, 39, 71]  # кобра
    list_intipa: dict[tuple[int, ...], list[tuple[int, ...]]] = {(34, 36, -1, 39, 71):[(0,0,0)]} # опера
    all_rhymes_patterns = Pattern(word_intipa=word_intipa, list_intipa=list_intipa).get_all_pattern_pads()
    expected = {('any_v', 'any_cons', 'add_sound', 'any_cons', 'any_v'): [(34, 36, -1, 39, 71)]}
    assert expected == all_rhymes_patterns
