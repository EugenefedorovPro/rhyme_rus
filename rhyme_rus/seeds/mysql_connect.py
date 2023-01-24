import mysql.connector


# singleton to quick access mysql db
class MySql:
    _instance = None
    con = None
    cur = None
    def __new__(cls):
        if cls._instance:
            return cls._instance
        else:
            cls._instance = super().__new__(cls)
            cls.con = mysql.connector.connect(
                host='db',
                user='eugene',
                password='sql_1980',
                port=3306,
                database="rhymes")
            cls.cur = cls.con.cursor()
    def cur_execute(self, query: str) -> list[tuple]:
        self.cur.execute(query)
        return self.cur.fetchall()

    def cur_executemany(self, query: str, values: list[tuple]) -> str:
        self.cur.executemany(query, values)
        self.con.commit()
        return f"{self.cur.rowcount} 'was inserted'"
