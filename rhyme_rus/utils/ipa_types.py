from functools import lru_cache
from ipapy import UNICODE_TO_IPA
from rhyme_rus.utils.ipa_processing import IpaProcessing


class IpaTypes:
    @classmethod
    @lru_cache
    def get_voice_cons(cls):
        voice_cons = {
            UNICODE_TO_IPA["b"]: UNICODE_TO_IPA["p"],
            UNICODE_TO_IPA["bʲ"]: UNICODE_TO_IPA["pʲ"],
            UNICODE_TO_IPA["bʲː"]: UNICODE_TO_IPA["pʲː"],
            UNICODE_TO_IPA["bː"]: UNICODE_TO_IPA["pː"],
            UNICODE_TO_IPA["p"]: UNICODE_TO_IPA["b"],
            UNICODE_TO_IPA["pʲ"]: UNICODE_TO_IPA["bʲ"],
            UNICODE_TO_IPA["pʲː"]: UNICODE_TO_IPA["bʲː"],
            UNICODE_TO_IPA["pː"]: UNICODE_TO_IPA["bː"],
            UNICODE_TO_IPA["d"]: UNICODE_TO_IPA["t"],
            UNICODE_TO_IPA["dʲ"]: UNICODE_TO_IPA["tʲ"],
            UNICODE_TO_IPA["dʲː"]: UNICODE_TO_IPA["tʲː"],
            UNICODE_TO_IPA["dː"]: UNICODE_TO_IPA["tː"],
            UNICODE_TO_IPA["t"]: UNICODE_TO_IPA["d"],
            UNICODE_TO_IPA["tʲ"]: UNICODE_TO_IPA["dʲ"],
            UNICODE_TO_IPA["tʲː"]: UNICODE_TO_IPA["dʲː"],
            UNICODE_TO_IPA["tː"]: UNICODE_TO_IPA["dː"],
            UNICODE_TO_IPA["d͡z"]: UNICODE_TO_IPA["t͡s"],
            UNICODE_TO_IPA["d͡zʲ"]: UNICODE_TO_IPA["t͡sʲ"],
            UNICODE_TO_IPA["d͡z"]: UNICODE_TO_IPA["t͡sː"],
            UNICODE_TO_IPA["t͡s"]: UNICODE_TO_IPA["d͡z"],
            UNICODE_TO_IPA["t͡sʲ"]: UNICODE_TO_IPA["d͡zʲ"],
            UNICODE_TO_IPA["t͡sː"]: UNICODE_TO_IPA["d͡z"],
            UNICODE_TO_IPA["f"]: UNICODE_TO_IPA["v"],
            UNICODE_TO_IPA["fʲ"]: UNICODE_TO_IPA["vʲ"],
            UNICODE_TO_IPA["f"]: UNICODE_TO_IPA["vː"],
            UNICODE_TO_IPA["v"]: UNICODE_TO_IPA["f"],
            UNICODE_TO_IPA["vʲ"]: UNICODE_TO_IPA["fʲ"],
            UNICODE_TO_IPA["vː"]: UNICODE_TO_IPA["f"],
            UNICODE_TO_IPA["vʲː"]: UNICODE_TO_IPA["vʲ"],
            UNICODE_TO_IPA["k"]: UNICODE_TO_IPA["ɡ"],
            UNICODE_TO_IPA["kʲ"]: UNICODE_TO_IPA["ɡʲ"],
            UNICODE_TO_IPA["kʲː"]: UNICODE_TO_IPA["ɡʲ"],
            UNICODE_TO_IPA["kː"]: UNICODE_TO_IPA["ɡː"],
            UNICODE_TO_IPA["ɡ"]: UNICODE_TO_IPA["k"],
            UNICODE_TO_IPA["ɡʲ"]: UNICODE_TO_IPA["kʲ"],
            UNICODE_TO_IPA["ɡʲ"]: UNICODE_TO_IPA["kʲː"],
            UNICODE_TO_IPA["ɡː"]: UNICODE_TO_IPA["kː"],
            UNICODE_TO_IPA["sʲ"]: UNICODE_TO_IPA["zʲ"],
            UNICODE_TO_IPA["s"]: UNICODE_TO_IPA["z"],
            UNICODE_TO_IPA["sʲː"]: UNICODE_TO_IPA["zʲː"],
            UNICODE_TO_IPA["sː"]: UNICODE_TO_IPA["zː"],
            UNICODE_TO_IPA["zʲ"]: UNICODE_TO_IPA["sʲ"],
            UNICODE_TO_IPA["z"]: UNICODE_TO_IPA["s"],
            UNICODE_TO_IPA["zʲː"]: UNICODE_TO_IPA["sʲː"],
            UNICODE_TO_IPA["zː"]: UNICODE_TO_IPA["sː"],
            UNICODE_TO_IPA["ɕ"]: UNICODE_TO_IPA["z"],
            UNICODE_TO_IPA["ɕː"]: UNICODE_TO_IPA["zː"],
            UNICODE_TO_IPA["z"]: UNICODE_TO_IPA["ɕ"],
            UNICODE_TO_IPA["zː"]: UNICODE_TO_IPA["ɕː"],
            UNICODE_TO_IPA["ʂ"]: UNICODE_TO_IPA["ʐ"],
            UNICODE_TO_IPA["ʂː"]: UNICODE_TO_IPA["ʐː"],
            UNICODE_TO_IPA["ʐ"]: UNICODE_TO_IPA["ʂ"],
            UNICODE_TO_IPA["ʐː"]: UNICODE_TO_IPA["ʂː"],
        }
        return voice_cons

    @classmethod
    def get_palatal_cons(cls):
        palatal_cons = {
            UNICODE_TO_IPA["b"]: UNICODE_TO_IPA["bʲ"],
            UNICODE_TO_IPA["bʲ"]: UNICODE_TO_IPA["b"],
            UNICODE_TO_IPA["bʲː"]: UNICODE_TO_IPA["bː"],
            UNICODE_TO_IPA["bː"]: UNICODE_TO_IPA["bʲː"],
            UNICODE_TO_IPA["p"]: UNICODE_TO_IPA["pʲ"],
            UNICODE_TO_IPA["pʲ"]: UNICODE_TO_IPA["p"],
            UNICODE_TO_IPA["pʲː"]: UNICODE_TO_IPA["pː"],
            UNICODE_TO_IPA["pː"]: UNICODE_TO_IPA["pʲː"],
            UNICODE_TO_IPA["d"]: UNICODE_TO_IPA["dʲ"],
            UNICODE_TO_IPA["dʲ"]: UNICODE_TO_IPA["d"],
            UNICODE_TO_IPA["dʲː"]: UNICODE_TO_IPA["dː"],
            UNICODE_TO_IPA["dː"]: UNICODE_TO_IPA["dʲː"],
            UNICODE_TO_IPA["t"]: UNICODE_TO_IPA["tʲ"],
            UNICODE_TO_IPA["tʲ"]: UNICODE_TO_IPA["t"],
            UNICODE_TO_IPA["tʲː"]: UNICODE_TO_IPA["tː"],
            UNICODE_TO_IPA["tː"]: UNICODE_TO_IPA["tʲː"],
            UNICODE_TO_IPA["d͡z"]: UNICODE_TO_IPA["d͡zʲ"],
            UNICODE_TO_IPA["d͡zʲ"]: UNICODE_TO_IPA["d͡z"],
            UNICODE_TO_IPA["t͡s"]: UNICODE_TO_IPA["t͡sʲ"],
            UNICODE_TO_IPA["t͡sʲ"]: UNICODE_TO_IPA["t͡s"],
            UNICODE_TO_IPA["f"]: UNICODE_TO_IPA["fʲ"],
            UNICODE_TO_IPA["fʲ"]: UNICODE_TO_IPA["f"],
            UNICODE_TO_IPA["v"]: UNICODE_TO_IPA["vʲ"],
            UNICODE_TO_IPA["vʲ"]: UNICODE_TO_IPA["v"],
            UNICODE_TO_IPA["vː"]: UNICODE_TO_IPA["vʲː"],
            UNICODE_TO_IPA["vʲː"]: UNICODE_TO_IPA["vː"],
            UNICODE_TO_IPA["k"]: UNICODE_TO_IPA["kʲ"],
            UNICODE_TO_IPA["kʲ"]: UNICODE_TO_IPA["k"],
            UNICODE_TO_IPA["kʲː"]: UNICODE_TO_IPA["kː"],
            UNICODE_TO_IPA["kː"]: UNICODE_TO_IPA["kʲː"],
            UNICODE_TO_IPA["ɡ"]: UNICODE_TO_IPA["ɡʲ"],
            UNICODE_TO_IPA["ɡʲ"]: UNICODE_TO_IPA["ɡ"],
            UNICODE_TO_IPA["lˠ"]: UNICODE_TO_IPA["lʲ"],
            UNICODE_TO_IPA["lʲ"]: UNICODE_TO_IPA["lˠ"],
            UNICODE_TO_IPA["lʲː"]: UNICODE_TO_IPA["lˠː"],
            UNICODE_TO_IPA["lˠː"]: UNICODE_TO_IPA["lʲː"],
            UNICODE_TO_IPA["m"]: UNICODE_TO_IPA["mʲ"],
            UNICODE_TO_IPA["mʲ"]: UNICODE_TO_IPA["m"],
            UNICODE_TO_IPA["mː"]: UNICODE_TO_IPA["mʲː"],
            UNICODE_TO_IPA["mʲː"]: UNICODE_TO_IPA["mː"],
            UNICODE_TO_IPA["n"]: UNICODE_TO_IPA["nʲ"],
            UNICODE_TO_IPA["nʲ"]: UNICODE_TO_IPA["n"],
            UNICODE_TO_IPA["nː"]: UNICODE_TO_IPA["nʲː"],
            UNICODE_TO_IPA["nʲː"]: UNICODE_TO_IPA["nː"],
            UNICODE_TO_IPA["sʲ"]: UNICODE_TO_IPA["s"],
            UNICODE_TO_IPA["s"]: UNICODE_TO_IPA["sʲ"],
            UNICODE_TO_IPA["sʲː"]: UNICODE_TO_IPA["sː"],
            UNICODE_TO_IPA["sː"]: UNICODE_TO_IPA["sʲː"],
            UNICODE_TO_IPA["zʲ"]: UNICODE_TO_IPA["z"],
            UNICODE_TO_IPA["z"]: UNICODE_TO_IPA["zʲ"],
            UNICODE_TO_IPA["zʲː"]: UNICODE_TO_IPA["zː"],
            UNICODE_TO_IPA["zː"]: UNICODE_TO_IPA["zʲː"],
            UNICODE_TO_IPA["r"]: UNICODE_TO_IPA["rʲ"],
            UNICODE_TO_IPA["rʲ"]: UNICODE_TO_IPA["r"],
            UNICODE_TO_IPA["rː"]: UNICODE_TO_IPA["rʲː"],
            UNICODE_TO_IPA["rʲː"]: UNICODE_TO_IPA["rː"],
            UNICODE_TO_IPA["x"]: UNICODE_TO_IPA["xʲ"],
            UNICODE_TO_IPA["xʲ"]: UNICODE_TO_IPA["x"],
        }
        return palatal_cons

    @classmethod
    @lru_cache
    def get_near_stressed_v(cls):
        near_stressed_v = {
            UNICODE_TO_IPA["a"]: UNICODE_TO_IPA["æ"],
            UNICODE_TO_IPA["æ"]: UNICODE_TO_IPA["a"],
            UNICODE_TO_IPA["ɛ"]: UNICODE_TO_IPA["e"],
            UNICODE_TO_IPA["e"]: UNICODE_TO_IPA["ɛ"],
            UNICODE_TO_IPA["i"]: UNICODE_TO_IPA["ɨ"],
            UNICODE_TO_IPA["ɨ"]: UNICODE_TO_IPA["i"],
            UNICODE_TO_IPA["o"]: UNICODE_TO_IPA["ɵ"],
            UNICODE_TO_IPA["ɵ"]: UNICODE_TO_IPA["o"],
            UNICODE_TO_IPA["u"]: UNICODE_TO_IPA["ʉ"],
            UNICODE_TO_IPA["ʉ"]: UNICODE_TO_IPA["u"],
        }
        return near_stressed_v

    @classmethod
    def convert_chars_to_n(cls, dict_ipa):
        sign2number = IpaProcessing.__get_sign2number()
        n_ipa = {}
        for item in dict_ipa.items():
            key = sign2number[item[0]]
            value = sign2number[item[1]]
            n_ipa[key] = value
        n_ipa = {key: n_ipa[key] for key in sorted(n_ipa)}
        return n_ipa

    @classmethod
    @lru_cache
    def make_voice_cons_to_n(cls):
        voice_cons = cls.get_voice_cons()
        voice_cons_to_n = cls.convert_chars_to_n(voice_cons)
        return voice_cons_to_n

    @classmethod
    @lru_cache
    def make_palatal_cons_to_n(cls):
        palatal_cons = cls.get_palatal_cons()
        palatal_cons_to_n = cls.convert_chars_to_n(palatal_cons)
        return palatal_cons_to_n

    @classmethod
    @lru_cache
    def make_near_stressed_v_to_n(cls):
        near_stressed_v = cls.get_near_stressed_v()
        n_near_stressed_v = cls.convert_chars_to_n(near_stressed_v)
        return n_near_stressed_v

    @classmethod
    @lru_cache
    def generate_all_cons_n(cls):
        sign2number = IpaProcessing.__get_sign2number()
        all_chars = IpaProcessing.generate_all_chars()
        all_cons_n = []
        for cons in all_chars.consonants:
            all_cons_n.append(sign2number[cons])
        return all_cons_n

    @classmethod
    @lru_cache
    def generate_all_vowels_n(cls):
        sign2number = IpaProcessing.__get_sign2number()
        all_chars = IpaProcessing.generate_all_chars()
        all_vowels_n = []
        for vowel in all_chars.vowels:
            all_vowels_n.append(sign2number[vowel])
        return all_vowels_n
