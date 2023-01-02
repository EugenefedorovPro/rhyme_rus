from rhyme_rus.utils.ipa_types import IpaTypes
from rhyme_rus.utils.dictionary_processing import DictionaryProcessing


class RhymeFlow:
    @classmethod
    def generate_indexes_before_add_no(cls, pat):
        indexes_no_sound = []
        indexes_add_sound = []
        for i, p in enumerate(pat):
            if p == "add_sound":
                indexes_add_sound.append(i)
            elif p == "no_sound":
                indexes_no_sound.append(i)
        return indexes_add_sound, indexes_no_sound

    @classmethod
    def shorten_prolong_ipa(cls, ipa_short_int, indexes_add_sound, indexes_no_sound):
        ipa_short_int_new = ipa_short_int[:]
        if indexes_add_sound:
            for ad in indexes_add_sound:
                ipa_short_int_new.insert(ad, 0)
        if indexes_no_sound:
            indexes_no_sound.sort(reverse=True)
            for ns in indexes_no_sound:
                ipa_short_int_new.pop(ns)
        return ipa_short_int_new

    @classmethod
    def remove_no_sound_pat(cls, pat):
        new_working_pat = [p for p in pat if p != "no_sound"]
        return new_working_pat

    @classmethod
    def generate_indexes_after_add_no(cls, new_working_pat):
        indexes_near_stressed_v = []
        indexes_any_cons = []
        indexes_any_v = []
        indexes_palatal_cons = []
        indexes_voice_cons = []
        indexes_same = []
        for i, p in enumerate(new_working_pat):
            if p == "any_cons":
                indexes_any_cons.append(i)
            elif p == "any_v":
                indexes_any_v.append(i)
            elif p == "palatal_cons":
                indexes_palatal_cons.append(i)
            elif p == "voice_cons":
                indexes_voice_cons.append(i)
            elif p == "near_stressed_v":
                indexes_near_stressed_v.append(i)
            elif p == "add_sound":
                pass
            else:
                indexes_same.append(i)

        return tuple(
            [
                indexes_same,
                indexes_near_stressed_v,
                indexes_palatal_cons,
                indexes_voice_cons,
                indexes_any_cons,
                indexes_any_v,
            ]
        )

    @classmethod
    def find_indexes_same(cls, indexes_same, ipa_short_int_new, _intipa):
        if indexes_same:
            list_s = []
            for s in indexes_same:
                list_s.append(_intipa[s] == ipa_short_int_new[s])
            if not all(list_s):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def find_near_stressed_v(cls, indexes_near_stressed_v, ipa_short_int_new, _intipa):
        if indexes_near_stressed_v:
            near_stressed_v = IpaTypes.make_near_stressed_v_to_n()
            list_nsv = []
            for nsv in indexes_near_stressed_v:
                list_nsv.append(_intipa[nsv] == near_stressed_v[ipa_short_int_new[nsv]])
            if not all(list_nsv):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def find_palatal_cons(cls, indexes_palatal_cons, ipa_short_int_new, _intipa):
        if indexes_palatal_cons:
            palatal_cons = IpaTypes.make_palatal_cons_to_n()
            list_pc = []
            for pc in indexes_palatal_cons:
                list_pc.append(_intipa[pc] == palatal_cons[ipa_short_int_new[pc]])
            if not all(list_pc):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def find_voice_cons(cls, indexes_voice_cons, ipa_short_int_new, _intipa):
        if indexes_voice_cons:
            voice_cons = IpaTypes.make_voice_cons_to_n()
            list_vc = []
            for vc in indexes_voice_cons:
                list_vc.append(_intipa[vc] == voice_cons[ipa_short_int_new[vc]])
            if not all(list_vc):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def find_any_cons(cls, indexes_any_cons, ipa_short_int_new, _intipa):
        voice_cons_to_n = IpaTypes.make_voice_cons_to_n()
        palatal_cons_to_n = IpaTypes.make_palatal_cons_to_n()
        if indexes_any_cons:
            all_cons_n = IpaTypes.generate_all_cons_n()
            list_c = []
            for c in indexes_any_cons:
                current_all_cons_n = all_cons_n[:]
                current_all_cons_n.remove(ipa_short_int_new[c])
                if ipa_short_int_new[c] in voice_cons_to_n:
                    current_all_cons_n.remove(voice_cons_to_n[ipa_short_int_new[c]])
                if ipa_short_int_new[c] in palatal_cons_to_n:
                    current_all_cons_n.remove(palatal_cons_to_n[ipa_short_int_new[c]])
                list_c.append(_intipa[c] in current_all_cons_n)
            if not all(list_c):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def find_any_v(cls, indexes_any_v, ipa_short_int_new, _intipa):
        if indexes_any_v:
            all_vowels_n = IpaTypes.generate_all_vowels_n()
            list_v = []
            for v in indexes_any_v:
                current_all_vowels_n = all_vowels_n[:]
                current_all_vowels_n.remove(ipa_short_int_new[v])
                list_v.append(_intipa[v] in current_all_vowels_n)
            if not all(list_v):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def rhymes_by_pat(cls, ipa_short_int_new, new_working_pat, tuple_indexes):
        if len(ipa_short_int_new) == len(new_working_pat):
            indexes_same = tuple_indexes[0]
            indexes_near_stressed_v = tuple_indexes[1]
            indexes_palatal_cons = tuple_indexes[2]
            indexes_voice_cons = tuple_indexes[3]
            indexes_any_cons = tuple_indexes[4]
            indexes_any_v = tuple_indexes[5]

            unique_of_all_int_from_dict = (
                DictionaryProcessing.get_unique_of_all_int_from_dict()
            )

            rhymed_ints = []

            for _intipa in unique_of_all_int_from_dict:
                if _intipa and len(_intipa) == len(ipa_short_int_new):

                    if cls.find_indexes_same(indexes_same, ipa_short_int_new, _intipa):
                        continue
                    if cls.find_near_stressed_v(
                        indexes_near_stressed_v, ipa_short_int_new, _intipa
                    ):
                        continue
                    if cls.find_palatal_cons(
                        indexes_palatal_cons, ipa_short_int_new, _intipa
                    ):
                        continue
                    if cls.find_voice_cons(
                        indexes_voice_cons, ipa_short_int_new, _intipa
                    ):
                        continue
                    if cls.find_any_cons(indexes_any_cons, ipa_short_int_new, _intipa):
                        continue
                    if cls.find_any_v(indexes_any_v, ipa_short_int_new, _intipa):
                        continue
                    rhymed_ints.append(_intipa)
        else:
            raise Exception("Pat and ipa_short_int of different lengths")

        return rhymed_ints
