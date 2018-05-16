import csv
import sqlite3
from sqlite3 import OperationalError
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

file = open('new-level.csv', "rt")
read = csv.reader(file)
i = 1
for row in read:
    ro = 'INSERT INTO questions_level VALUES (%d,%d, %d, %d)' % (i, int(row[0]), int(row[1]), int(row[2]))
    cursor.execute(ro)
    conn.commit()
    i += 1

    # import sys
    #
    # print("\n".join(sys.argv))
    #check does it take new serial no from begning
