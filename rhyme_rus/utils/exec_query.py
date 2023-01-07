import sqlite3
from typing import List, Union, Tuple, AnyStr

class ExecQuery:
    @classmethod
    def get_connected(cls, path: str) -> sqlite3.Connection:
        connection = sqlite3.connect(path)
        return connection

    @classmethod
    def exec_with_output(cls, path: str, my_query: str) -> Union[list, None]:
        connection = cls.get_connected(path)
        cur = connection.cursor()
        cur.execute(my_query)
        query_output = cur.fetchall()
        connection.close()
        if query_output:
            return query_output
        else:
            connection.close()
            print("query_output is empty")
            return None

    @classmethod
    def exec_no_output(cls, path: str, my_query: str) -> None:
        connection = cls.get_connected(path)
        cur = connection.cursor()
        cur.execute(my_query)
        connection.commit()
        connection.close()
        return None

    List_Tuples = List[Tuple[AnyStr, AnyStr]]

    @classmethod
    def exec_multi(cls, path: str, my_query: str, values: List_Tuples) -> None:
        connection = cls.get_connected(path)
        cur = connection.cursor()
        cur.executemany(my_query, values)
        connection.commit()
        connection.close()
        return None





