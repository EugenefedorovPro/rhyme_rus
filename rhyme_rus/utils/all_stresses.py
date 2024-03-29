from abc import ABC, abstractmethod
from rhyme_rus.seeds.mysql_connect import my_sql


class AFetchStress(ABC):
    def __init__(self, unstressed_word: str):
        self.unstressed_word = unstressed_word

    @abstractmethod
    def fetch_stress(self):  # pragma: no cover
        pass


class FetchStressFromDb(AFetchStress):
    def fetch_stress(self) -> list[str]:
        query = f"select accent from wiki_pickled where word = '{self.unstressed_word}'"
        stressed_words = my_sql.cur_execute(query)
        stressed_words = list(set(stressed_words))
        stressed_words = [word[0] for word in stressed_words]
        return stressed_words


class FetchStressFromNn(AFetchStress):

    # produces a list of all possible variants of stressed and inserts
    # the intipa stressed by neural network on the first place
    @staticmethod
    def __produce_all_stresses(unstressed_word: str, stressed_word: list[str]) -> list[str]:
        vowels: list = ["а", "и", "е", "ё", "о", "у", "ы", "э", "ю", "я"]
        stressed_word: str = stressed_word[0]
        all_stresses: list = []
        for i, char in enumerate(unstressed_word):
            if char in vowels:
                _stressed_word = f"{unstressed_word[:i + 1]}'{unstressed_word[i + 1:]}"
                all_stresses.append(_stressed_word)
        all_stresses.remove(stressed_word)
        all_stresses.insert(0, stressed_word)  # insert the variant produced by nn on the first place
        return all_stresses

    def fetch_stress(self) -> list[str]:
        # supress tf info, warnings, errors
        import os
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        from put_stress_rus.put_stress import put_stress

        stressed_word = put_stress(self.unstressed_word)
        stressed_word = list((stressed_word,))
        all_stresses = FetchStressFromNn.__produce_all_stresses(self.unstressed_word, stressed_word)
        return all_stresses


class FactoryStress:
    @classmethod
    def fetch_stress(cls, unstressed_word: str) -> list[str]:
        db = FetchStressFromDb(unstressed_word)
        all_stresses = db.fetch_stress()
        if all_stresses:
            return all_stresses
        else:
            nn = FetchStressFromNn(unstressed_word)
            all_stresses: list[str] = nn.fetch_stress()
            return all_stresses
