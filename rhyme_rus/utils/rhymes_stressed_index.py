from rhyme_rus.seeds.ipa_dicts import IpaDicts


class RhymesStressedIndex:
    def __init__(self, all_pattern_pads):
        self.all_pattern_pads = all_pattern_pads
        self.all_stressed_vowels = IpaDicts().all_stressed_vowels

    def get_all_rhymes_stressed_index(self) -> list[int]:
        all_rhymes_stressed_index: list[int] = []
        for pattern in self.all_pattern_pads:
            list_pads: list[list[int]] = self.all_pattern_pads[pattern]
            first_pad: list[int] = list_pads[0]
            for _int in first_pad:
                if _int in self.all_stressed_vowels:
                    all_rhymes_stressed_index.append(_int)
        return all_rhymes_stressed_index
