from rhyme_rus.utils.fetch_stressed_word import FactoryStress

class Word:
    def __init__(self,
                 unstressed_word: str,
    ) -> None:
        self.stressed_word: str = ''
        self.all_stresses: list[str] = []
        self.unstressed_word: str = unstressed_word
        self.set_all_stresses()

    def set_all_stresses(self) -> None:
            self.all_stresses = FactoryStress.fetch_stress(self.unstressed_word)
            if len(self.all_stresses) == 1:
                self.set_stressed_word(self.all_stresses[0])
            return None

    def set_stressed_word(self, stressed_word: str) -> None:
        print(f"stressed word - {stressed_word}")
        self.stressed_word = stressed_word

