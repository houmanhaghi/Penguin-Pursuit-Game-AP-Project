import sqlite3 as sq


class DB:
    def __init__(self, data_base_file):
        self.data_base_file = data_base_file
        self.connect = sq.connect(self.data_base_file)
        self.cursor = self.connect.cursor()


    def read(self, info: tuple):
        self.cursor.execute("SELECT * FROM ALL_MEMBERS")
        print('readed')
        result = self.cursor.fetchall()

        for line in result:
            if line[0] == info[0]:
                print('founded')
                return line
        # line -> name, scores, last_level, last_result
        # name : name
        # score: ex) 34, 5, 54
        # last_level: 3
        # last_result: "win" or "loss" or "double loss"


    def insert(self, info:tuple):
        self.cursor.execute("INSERT INTO ALL_MEMBERS VALUES ( ? , ? , ? , ? )", info)
        print('inserted')
        self.connect.commit()


    def update(self, info):
        # first delete then insert :)
        # self.cursor.execute(f"""
        #                 DELETE FROM ALL_MEMBERS
        #                 WHERE username = '{info[0]}';
        #                 """)
        #
        # self.cursor.execute("INSERT INTO ALL_MEMBERS VALUES ( ? , ? , ? , ? )", info)

        self.cursor = self.connect.cursor()
        self.cursor.execute(f'''
                UPDATE ALL_MEMBERS
                SET scores = "{info[1]}", lase_level = {info[2]}, last_result = "{info[3]}"
                WHERE username = "{info[0]}" ;
        ''')

        print('updated')
        self.connect.commit()
