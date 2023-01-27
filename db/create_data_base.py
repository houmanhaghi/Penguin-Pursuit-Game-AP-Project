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


############## adding information ##############

info = ('houmanhaghi', '0, 50, 31, 69, 59, 64, 28, 41, 56, 84, 83, 102', 9, 'win')


# cursor.execute("INSERT INTO ALL_MEMBERS VALUES ( ? , ? , ? , ? )", info)


# cursor.execute(f'''
#                 UPDATE ALL_MEMBERS
#                 SET scores = "{info[1]}", lase_level = {info[2]}, last_result = "{info[3]}"
#                 WHERE username = "{info[0]}" ;
#         ''')
#




# cursor.execute(f"""
#         DELETE FROM ALL_MEMBERS
#         WHERE username = "houmanhaghi";
#         """)



cursor.execute("select * from ALL_MEMBERS")
ii = cursor.fetchall()
for i in ii:
    print(i)



#########################################
connect.commit()
connect.close()

