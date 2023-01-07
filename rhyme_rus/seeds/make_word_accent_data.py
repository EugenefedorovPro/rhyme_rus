from wiktionary_rus.wiktionary import wiki_instances
from typing import List, Tuple, AnyStr, Union
from pathlib import Path
from rhyme_rus.utils.exec_query import ExecQuery


class MakeWordAccentData:
    list_tuples = List[Tuple[AnyStr, AnyStr]]

    @classmethod
    def make_word_accent_data(cls, wiki_instances: list) -> list_tuples:
        input_dict = {
            item.accent: item.word_lowcase
            for item in wiki_instances
            if item.accent and item.word_lowcase
        }
        word_accent_data = [(v, k) for k, v in input_dict.items()]
        return word_accent_data

    @classmethod
    def create_db_word_accent_table(
        cls, path: str, wiki_instances: list
    ) -> Union[List, None]:
        if Path(path).exists() == False:
            query_creat_table = """create table if not exists word_accent(
                            word_lowcase varchar(100) not null,
                            accent varchar(100) not null
                      );"""

            query_insert_data = "insert into word_accent values(?, ?)"
            query_check = """select * from word_accent 
                             where word_lowcase = 'замок'
            """

            data = cls.make_word_accent_data(wiki_instances)
            ExecQuery.exec_no_output(path, query_creat_table)
            ExecQuery.exec_multi(path, query_insert_data, data)
            check_output = ExecQuery.exec_with_output(path, query_check)
            if check_output:
                return check_output
            else:
                print("query returned None")
                return None
        else:
            print("db already exists")
            return None


if __name__ == "__main__":
    path = "./rhyme_rus/data/word_accent.sqlite3"
    check_output = MakeWordAccentData.create_db_word_accent_table(
        path, wiki_instances)
    print("check_output: ", check_output)
