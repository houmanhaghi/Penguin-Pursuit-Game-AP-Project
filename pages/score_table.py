import sqlite3 as sq
from db.data_base import *

def score_table(player):
     d = DB.read(player)
     name = d[0], last_level = d[2]
     for s in d[1]:
          score = max(s)

