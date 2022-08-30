from functools import lru_cache
import itertools
from rhyme_rus.utils.ipa_types import IpaTypes


class Patterns:
    @classmethod
    @lru_cache
    def make_dict_combinations(cls):
        combinations = {
            "cons": ["same_cons", "voice_cons", "palatal_cons", "any_cons", "no_sound"],
            "stress_v": ["same_stressed_v", "near_stressed_v"],
            "vowel": ["same_v", "any_v", "no_sound"],
        }
        return combinations

    @classmethod
    @lru_cache
    def make_dict_combinations_long_words(cls):
        combinations = {
            "cons": "same_cons",
            "stress_v": "same_stressed_v",
            "vowel": "same_v",
        }
        return combinations

    @classmethod
    def shorten_pat_long_words_to_head_tail(cls, pat_of_ipa, max_length_pat_of_ipa=8):
        head = pat_of_ipa[:max_length_pat_of_ipa]
        tail = pat_of_ipa[max_length_pat_of_ipa:]
        return head, tail

    @classmethod
    def shorten_ipa_short_int_for_long_words(
        cls, ipa_short_int, max_length_pat_of_ipa=8
    ):
        if len(ipa_short_int) > max_length_pat_of_ipa:
            ipa_short_int_for_long_words = ipa_short_int[:max_length_pat_of_ipa]
            return ipa_short_int_for_long_words
        else:
            return ipa_short_int

    @classmethod
    def convert_tail_to_pattern(cls, tail):
        combinations_long_words = cls.make_dict_combinations_long_words()
        tail_to_pattern = [combinations_long_words[char] for char in tail]
        return tail_to_pattern

    @classmethod
    def add_tail_to_pats(cls, all_rhyme_pats, tail_to_pattern):
        for pat in all_rhyme_pats:
            pat = list(pat)
            pat.extend(tail_to_pattern)
            yield pat

    @classmethod
    def take_pat_of_ipa(cls, ipa_short_int):
        all_cons_n = IpaTypes.generate_all_cons_n()
        all_vowels_n = IpaTypes.generate_all_vowels_n()
        pat_of_ipa = []
        for ip in ipa_short_int:
            if ip in all_cons_n:
                pat_of_ipa.append("cons")
            elif ip in all_vowels_n:
                pat_of_ipa.append("vowel")
        pat_of_ipa[pat_of_ipa.index("vowel")] = "stress_v"
        return pat_of_ipa

    @classmethod
    def add_sound_to_rhyme_pats(cls, all_rhyme_pats):
        for pat in all_rhyme_pats:
            for i in range(len(list(pat)) + 1):
                new_pat = list(pat).copy()
                new_pat.insert(i, "add_sound")
                yield new_pat
            yield pat

    @classmethod
    def generate_all_rhyme_pats(cls, pat_of_ipa):
        combinations = cls.make_dict_combinations()
        list_of_p = []
        for p in pat_of_ipa:
            list_of_p.append(combinations[p])
        return itertools.product(*list_of_p)

    @classmethod
    def check_if_voice_palatal(cls, ipa_short_int, pat):
        voice_cons_to_n = IpaTypes.make_voice_cons_to_n()
        palatal_cons_to_n = IpaTypes.make_palatal_cons_to_n()
        near_stressed_v_to_n = IpaTypes.make_near_stressed_v_to_n()
        if len(ipa_short_int) == len(pat):
            voice_palatal_check = True
            for ip, p in zip(ipa_short_int, pat):

                if p == "voice_cons":
                    if ip in voice_cons_to_n:
                        voice_palatal_check = True
                    else:
                        return False

                if p == "palatal_cons":
                    if ip in palatal_cons_to_n:
                        voice_palatal_check = True
                    else:
                        return False

                if p == "near_stressed_v":
                    if ip in near_stressed_v_to_n:
                        voice_palatal_check = True
                    else:
                        return False
        else:
            raise Exception("Pat and ipa_short_int of different lengths")
        return voice_palatal_check

    @classmethod
    def check_n_mutations(cls, pat, max_number_hard_sounds_in_one_pat=1):
        max_any_cons = (
            max_no_sound
        ) = (
            max_palatal_cons
        ) = max_voice_cons = max_any_v = max_number_hard_sounds_in_one_pat
        if (
            len([p for p in pat if p == "any_cons"]) <= max_any_cons
            and len([p for p in pat if p == "no_sound"]) <= max_no_sound
            and len([p for p in pat if p == "palatal_cons"]) <= max_palatal_cons
            and len([p for p in pat if p == "voice_cons"]) <= max_voice_cons
            and len([p for p in pat if p == "any_v"]) <= max_any_v
        ):

            return True
        else:
            return False

    @classmethod
    def condition_all_rhyme_pats(
        cls, all_rhyme_pats, ipa_short_int, max_number_hard_sounds_in_one_pat=1
    ):
        for pat in all_rhyme_pats:
            if cls.check_n_mutations(
                pat, max_number_hard_sounds_in_one_pat
            ) and cls.check_if_voice_palatal(ipa_short_int, pat):
                yield pat

    # to avoid bad sequences like 'add_sound' + 'no_sound'
    # pat_added = ['any_v', 'add_sound', 'no_sound', 'add_sound', "any_v"]
    @classmethod
    def check_add_no_sequences(cls, pat):
        pat_added_copy = list(pat).copy()
        if pat_added_copy[0] == "add_sound" and pat_added_copy[1] == "no_sound":
            return False
        elif pat_added_copy[0] == "no_sound" and pat_added_copy[1] == "add_sound":
            return False
        if len(pat_added_copy) == 2:
            return True
        pat_added_copy = pat_added_copy[1:]
        return cls.check_add_no_sequences(pat_added_copy)

    @classmethod
    def check_first_double_cons(cls, pat):
        if pat[0] in (
            "any_cons",
            "same_cons",
            "palatal_cons",
            "voice_cons",
            "add_sound",
        ) and pat[1] in (
            "any_cons",
            "same_cons",
            "palatal_cons",
            "voice_cons",
            "add_sound",
        ):
            return False
        else:
            return True

    @classmethod
    def check_no_any_add(cls, pat):
        if len(pat) >= 3:
            pat_added_copy = list(pat).copy()
            if (
                pat_added_copy[0] == "add_sound"
                and pat_added_copy[1] == "any_cons"
                and pat_added_copy[2] == "no_sound"
            ):
                return False

            elif (
                pat_added_copy[0] == "no_sound"
                and pat_added_copy[1] == "any_cons"
                and pat_added_copy[2] == "add_sound"
            ):
                return False

            if len(pat_added_copy) == 3:
                return True
            pat_added_copy = pat_added_copy[1:]
        else:
            return True
        return cls.check_no_any_add(pat_added_copy)

    @classmethod
    def condition_add_sound_to_rhyme_pats(cls, all_rhyme_pats):
        for pat in all_rhyme_pats:
            if (
                cls.check_add_no_sequences(pat)
                and cls.check_first_double_cons(pat)
                and cls.check_no_any_add(pat)
            ):
                yield list(pat)
