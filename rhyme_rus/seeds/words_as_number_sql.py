import json
from rhyme_rus.seeds.mysql_connect import MySql
from rhyme_rus.seeds.ipa_dicts import IpaDicts
import ipapy.ipachar
from ipapy.ipastring import IPAString

class WordsNumbers:
    def __init__(self):
        self.sign2number = IpaDicts().full_sign2number
        self.all_sounds: list[str] = []
        self.all_id: list[int] = []
        self.all_ipa: list[IPAString] = []
        self.all_numbers: list[list[int]] = []
        self.exceptions: set[ipapy.ipachar] = set()
        self.numbers_id: list[tuple[str, int]] = []
        self.__get_all_sounds()
        self.__get_all_ipa()
        self.__get_all_numbers()
        self.__get_numbers_id()

    def __get_all_sounds(self):
        query = "select id, sounds from wiki_pickled"
        id_sounds: list[tuple[int, str]] = MySql().cur_execute(query)
        for i_s in id_sounds:
            _id: int = i_s[0]
            sounds = i_s[1]
            self.all_sounds.append(sounds)
            self.all_id.append(_id)

    def __get_all_ipa(self):
        for sounds in self.all_sounds:
            self.all_ipa.append(IPAString(unicode_string=sounds))

    def __get_all_numbers(self):
        for ipa in self.all_ipa:
            numbers: list[int] = []
            for i in ipa:
                num = self.sign2number[i]
                numbers.append(num)
            self.all_numbers.append(numbers)

    def __get_numbers_id(self):
        _id: int
        _num: list[int]
        for _num, _id in zip(self.all_numbers, self.all_id):
            self.numbers_id.append((json.dumps(_num), _id))


    def update_word_as_numbers(self):
        query_column = "alter table wiki_pickled add word_as_numbers json"
        query_update = "update wiki_pickled set word_as_numbers = %s where id = %s"
        MySql().cur_execute(query_column)
        n_rows_processed = MySql().cur_executemany(query_update,self.numbers_id)
        return n_rows_processed

if __name__ == "__main__":
    numbers_id = WordsNumbers().numbers_id
    print("_______________________")
    print(len(numbers_id))
    # n_rows_processed = WordsNumbers().update_word_as_numbers()
    # print(n_rows_processed)