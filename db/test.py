import sqlite3 as sq
from data_base import *

def score_table(player):
     D = DB('members.db')
     d = D.read(player)

     name , last_level = d[0],  d[2]
     print(name, last_level)

     print(d)
     arr = d[1].split(",")



     for i in range(len(arr)):
          arr[i] = int(arr[i])

     print(max(arr))

score_table(("houmanhaghi", "0, 10, 23, 4, 76, 23", 1, "null"))
# start_menu(("hello", "23, 45, 80", 1, "win"))
