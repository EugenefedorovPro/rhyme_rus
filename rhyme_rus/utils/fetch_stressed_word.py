from abc import ABC, abstractmethod
from rhyme_rus.seeds.mysql_connect import MySql

class IFetchStress(ABC):
    @abstractmethod
    def fetch_stress(self):
        pass

class FetchStressFromDb(IFetchStress):
    def __init__(self, unstressed_word):
        self.unstressed_word = unstressed_word

    def fetch_stress(self):
        _query = f"select accent from wiki_pickled where word = '{self.unstressed_word}'"
        _msql = MySql()
        stressed_word = _msql.cur_execute(_query)
        return stressed_word


class FetchStressFromNn(IFetchStress):
    def __init__(self, unstressed_word: str):
        self.unstressed_word = unstressed_word

    def fetch_stress(self) -> str:
        from put_stress_rus.put_stress import put_stress
        return put_stress(self.unstressed_word)


def produce_all_stresses(unstressed_word: str) -> list[tuple]:
    vowels: list = ["а", "и", "е", "ё", "о", "у", "ы", "э", "ю", "я"]
    all_stresses: list[tuple] = [tuple((f"{unstressed_word[:i+1]}'{unstressed_word[i+1:]}",)) for i, char in enumerate(unstressed_word) if char in vowels]
    return all_stresses

def put_nn_word_first(nn_word: str, all_stressed: list[tuple]) -> list[tuple]:
    nn_word_tuple: tuple = tuple((nn_word,))
    all_stressed.remove(nn_word_tuple)
    all_stressed.insert(0, nn_word_tuple)
    return all_stressed

def fetch_stress(unstressed_word: str):
    db = FetchStressFromDb(unstressed_word)
    stressed_words = db.fetch_stress()
    if stressed_words:
        print("database returned stressed_word")
        return stressed_words
    else:
        nn = FetchStressFromNn(unstressed_word)
        stressed_word: str = nn.fetch_stress()
        print(f"neural network returned {stressed_word}")
        all_stresses = produce_all_stresses(unstressed_word)
        all_stresses = put_nn_word_first(stressed_word, all_stresses)
        return all_stresses




