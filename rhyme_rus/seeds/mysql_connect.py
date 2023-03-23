from pathlib import Path
import sqlite3


class MySql:
    _self = None

    def __new__(cls):
        if not cls._self:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        path = Path(__file__).parent.parent.parent / "rhyme_rus/rhyme.sqlite3"
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def cur_execute(self, query: str) -> list[tuple]:
        self.cur.execute(query)
        return self.cur.fetchall()

    def cur_executemany(self, query: str, values: list[tuple]) -> str:
        self.cur.executemany(query, values)
        self.con.commit()
        return f"{self.cur.rowcount} 'was inserted'"


my_sql = MySql()

if __name__ == "__main__":  # pragma: no cover
    result = my_sql.cur_execute("select accent from wiki_pickled where word = 'дом'")
    print(result)
