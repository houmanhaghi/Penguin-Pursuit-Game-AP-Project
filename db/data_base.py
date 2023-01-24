import sqlite3 as sq


class DB:
    def __init__(self, data_base_file):
        self.data_base_file = data_base_file
        self.connect = sq.connect(self.data_base_file)
        self.cursor = self.connect.cursor()


    def read(self, info: tuple):
        self.cursor.execute("SELECT * FROM ALL_MEMBERS")
        result = self.cursor.fetchall()

        for line in result:
            if line[0] == info[0]:
                return line


    def insert(self, info:tuple):
        self.cursor.executemany("INSERT INTO ALL_MEMBERS VALUES ( ? , ? , ? , ? )", info)
        self.connect.commit()


    def update(self, info):
        self.cursor.execute(f"""
                UPDATE ALL_MEMBERS
                SET scores = {info[1]}, lase_level = {info[2]}, last_result = {info[3]}
                WHERE username = {info[0]} 
        """)
        self.connect.commit()


