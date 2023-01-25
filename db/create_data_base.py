"""
this file is for creating data base with sqlite3
it just run first time and does not need to run more
"""


import sqlite3 as sq


#create db or just call if exist
connect = sq.connect("members.db")

#create curseor
cursoe = connect.cursor()


# create table
# cursoe.execute("""
#         CREATE TABLE ALL_MEMBERS (
#             username TEXT,
#             scores TEXT,
#             lase_level INTEGER,
#             last_result TEXT
#                         )
#             """)


########### adding information

connect.commit()
connect.close()