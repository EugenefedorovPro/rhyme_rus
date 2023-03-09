from rhyme_rus.utils.pad import Pad
from rhyme_rus.seeds.ipa_dicts import IpaDicts

intipa = [43, 34, 45, 67, 87]
all_intipa_word: dict[tuple[int, ...], set[str]] = {(78, 30): {'any_0', "any_1"}}
stressed_vowel = 34
near_stressed_v = IpaDicts().near_stressed_v_int[stressed_vowel]
index_stressed_v = 1

if __name__ == "__main__":
    all_pad_intipa = Pad(
        intipa,
        all_intipa_word,
        stressed_vowel,
        near_stressed_v,
        index_stressed_v
    ).get_all_pads_dict()

    print(all_pad_intipa)
