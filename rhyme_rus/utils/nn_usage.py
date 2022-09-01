from ipapy.ipastring import IPAString
from ipapy import UNICODE_TO_IPA
from put_stress_rus.put_stress import put_stress
from wiktionary_rus.wiktionary import find_item_from_wiki_unstressed


class NnUsage:
    @classmethod
    def select(cls, word_without_stress):
        list_items = find_item_from_wiki_unstressed(word_without_stress)
        if list_items == []:
            return list_items  # []
        else:
            if len(list_items) > 1:
                uniques = set()
                for item in list_items:
                    uniques.add(item.accent)
                if len(list(uniques)) > 1:
                    word_with_stress = input(
                        """Wiktionary has {} omographs: {}.
                                            Print the stressed word you
                                            choose - """.format(
                            len(list(uniques)), ", ".join(list(uniques))
                        )
                    )
                    if word_with_stress:
                        return word_with_stress  # user selected word
                    else:
                        return list(uniques)[0]  # the first word from list
                else:
                    return list(uniques)[0]  # word with same accents from list_items
            else:
                return list_items[0].accent  # the only available word

    @classmethod
    def accentuate(cls, word_without_stress):
        word_with_stress = put_stress(word_without_stress)

        text_0 = "Neural Netword stressed {} as {}.".format(
            word_without_stress, word_with_stress
        )
        text_1 = "Print 'Y' if the stress is put correctly, or print word with a proper accent - "
        user_check = input(text_0 + " " + text_1)
        if user_check == "" or user_check == "Y":
            return word_with_stress
        else:
            return user_check

    @classmethod
    # func to shorten ipa by scheme: one consonant before stressed vowel (if available)
    # stressed vowel + the rest of characters to the end of word
    # e.g. ipa ʂɨpʲɪˈlʲævʲɪtʲ shorened to lʲævʲɪtʲ
    def get_ipa_shortened(cls, trans_uni):
        stress_as_uni = "ˈ"
        stress_as_ipa = UNICODE_TO_IPA[stress_as_uni]
        palat_uni = "ʲ"
        palat_ipa = UNICODE_TO_IPA[palat_uni]

        trans_ipa = IPAString(unicode_string=trans_uni)

        def shorten_word_without_stress(trans_ipa):
            # first vowel or first single consonant
            if "vowel" in trans_ipa[0].name or (
                "consonant" in trans_ipa[0].name and "vowel" in trans_ipa[1].name
            ):
                ipa_short = trans_ipa
            # more than one initial consonants
            else:
                first_vowel = trans_ipa.vowels[0]
                index_of_first_vowel = trans_ipa.index(first_vowel)
                ipa_short = trans_ipa[index_of_first_vowel - 1 :]

                if ipa_short[0] == palat_ipa:
                    ipa_short = trans_ipa[index_of_first_vowel - 2 :]
            return ipa_short

        def shorten_all_variants(trans_ipa):
            # no stress
            if stress_as_ipa not in trans_ipa:
                ipa_short = shorten_word_without_stress(trans_ipa)
            # with stress
            else:
                index_of_last_stress = trans_ipa[::-1].index(stress_as_ipa)
                ipa_after_last_stress = trans_ipa[-index_of_last_stress:]
                ipa_after_last_stress = IPAString(ipa_chars=ipa_after_last_stress)
                ipa_short = shorten_word_without_stress(ipa_after_last_stress)

            return ipa_short

        # exception for single consonant words
        try:
            ipa_short = shorten_all_variants(trans_ipa)

            # convert list type to IPA
            if isinstance(ipa_short, list):
                ipa_short = IPAString(ipa_chars=ipa_short)

            return ipa_short

        except IndexError:
            ipa_short = None
