import json
from rhyme_rus.utils.fetch_stressed_word import FactoryStress
from rhyme_rus.seeds.mysql_connect import MySql


class Word:
    def __init__(self,
                 unstressed_word: str,
                 ) -> None:
        self.unstressed_word = unstressed_word
        self.sounds: str = ''
        self.intipa: list[int] = []
        self.stressed_word: str = ''
        self.all_stresses: list[str] = []
        self.unstressed_word: str = unstressed_word
        self.set_all_stresses()

    def set_all_stresses(self) -> None:
        self.all_stresses = FactoryStress.fetch_stress(self.unstressed_word)
        if len(self.all_stresses) == 1:
            self.set_stressed_word(self.all_stresses[0])
            self.fetch_sounds_intipa()
        return None

    def set_stressed_word(self, stressed_word: str) -> None:
        self.stressed_word = stressed_word
        self.fetch_sounds_intipa()

    def fetch_sounds_intipa(self) -> None:
        if self.stressed_word:
            _sql = MySql()
            _sounds_intipa = _sql.cur_execute(
                f'''select sounds, intipa from wiki_pickled where accent = "{self.stressed_word}"''')
            self.sounds: str = _sounds_intipa[0][0]
            self.intipa: list[int] = json.loads(_sounds_intipa[0][1])
            return None
