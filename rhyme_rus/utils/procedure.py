from rhyme_rus.utils.stressed_word import FactoryStress
from rhyme_rus.utils.intipa import FactoryIntipa
from rhyme_rus.utils.all_scope_rhymes import AllScopeRhymes
from rhyme_rus.utils.word import Word


class Procedure:
    @staticmethod
    def get_all_stresses(word) -> Word:
        word.all_stresses = FactoryStress().fetch_stress(word.unstressed_word)
        return word

    @staticmethod
    def get_stressed_word(word):
        if len(word.all_stresses) == 1:
            word.stressed_word = word.all_stresses[0]
            return word
        elif word.stressed_word:
            return word
        else:
            raise Exception(f"Client should choose stressed_word from list {word.all_stresses}")

    @staticmethod
    def get_intipa(word) -> Word:
        word.intipa = FactoryIntipa().fetch_intipa(word.stressed_word)
        print(f"intipa - {word.intipa}")
        return word

    @staticmethod
    def get_all_scope_rhymes(word) -> Word:
        word.all_scope_rhymes = AllScopeRhymes(word.intipa).get_all_scope_rhymes()
        return word

