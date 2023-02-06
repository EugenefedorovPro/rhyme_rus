from rhyme_rus.utils.stressed_word import FactoryStress
from rhyme_rus.utils.intipa import FactoryIntipa
from rhyme_rus.utils.all_scope_rhymes import AllScopeRhymes
from rhyme_rus.utils.word import Word
from rhyme_rus.utils.exceptions import MultipleStresses


class Procedure:
    def __init__(self, word: Word):
        self.word = word

    def __get_all_stresses(self) -> None:
        self.word.all_stresses = FactoryStress().fetch_stress(self.word.unstressed_word)

    def __get_stressed_word(self) -> None:
        if len(self.word.all_stresses) == 1:
            self.word.stressed_word = self.word.all_stresses[0]
        elif self.word.stressed_word:
            pass
        else:
            raise MultipleStresses(self.word.unstressed_word, self.word.all_stresses)

    def __get_intipa(self) -> None:
        self.word.intipa = FactoryIntipa().fetch_intipa(self.word.stressed_word)

    def __get_all_scope_rhymes(self) -> None:
        self.word.all_scope_rhymes_str = AllScopeRhymes(self.word.intipa).get_all_scope_rhymes()

    def build(self):
        self.__get_all_stresses()
        self.__get_stressed_word()
        self.__get_intipa()
        self.__get_all_scope_rhymes()
        return self.word
