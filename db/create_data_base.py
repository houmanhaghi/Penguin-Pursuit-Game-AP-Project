"""
this file is for creating data base with sqlite3
it just run first time and does not need to run more
"""


import sqlite3 as sq


#create db or just call if exist
connect = sq.connect("members.db")

#create curseor
cursor = connect.cursor()


# create table
# cursor.execute("""
#         CREATE TABLE ALL_MEMBERS (
#             username TEXT,
#             scores TEXT,
#             lase_level INTEGER,
#             last_result TEXT
#                         )
#             """)


<<<<<<< HEAD
############## adding information ##############
info = (
        'houman', '10, 40, 97, 876', 1, 'win'
)


cursor.execute("select * from ALL_MEMBERS")
ii = cursor.fetchall()
for i in ii:
    print(i)


# cursor.execute("INSERT INTO ALL_MEMBERS VALUES ( ? , ? , ? , ? )", info)


# cursor.execute(f'''
#                 UPDATE ALL_MEMBERS
#                 SET scores = "{info[1]}", lase_level = {info[2]}, last_result = "{info[3]}"
#                 WHERE username = "{info[0]}" ;
#         ''')
#




# cursor.execute(f"""
#         DELETE FROM ALL_MEMBERS
#         WHERE username = "houman";
#         """)


#########################################
=======
>>>>>>> ecae7e08a6ac292dd8a377519522385b9c75fe7d

########### adding information
info = ("houman", "0, 10, 23, 4, 76, 23", 1, "null")
cursoe.execute("INSERT INTO ALL_MEMBERS VALUES ( ? , ? , ? , ? )", info)
connect.commit()
connect.close()