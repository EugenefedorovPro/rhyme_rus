from rhyme_rus.seeds.ipa_dicts import IpaDicts

def get_near_stressed_v(stressed_vowel):
    return IpaDicts().near_stressed_v_int[stressed_vowel]
