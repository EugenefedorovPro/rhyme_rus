import mysql.connector

class MySql:

    def __init__(self):
        self.con = mysql.connector.connect(
            host='rhyme_db',
            user='eugene',
            password='sql_1980',
            port=3306,
            database="rhymes")
        self.cur = self.con.cursor()

    def cur_execute(self, query: str) -> list[tuple]:
        self.cur.execute(query)
        return self.cur.fetchall()

    def cur_executemany(self, query: str, values: list[tuple]) -> str:
        self.cur.executemany(query, values)
        self.con.commit()
        return f"{self.cur.rowcount} 'was inserted'"
