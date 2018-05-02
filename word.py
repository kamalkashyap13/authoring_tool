import csv
import sqlite3
from sqlite3 import OperationalError
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

file = open('words.csv', "rt")
read = csv.reader(file)
i = 1
level = 1
for row in read:
    ro = '''INSERT OR IGNORE INTO questions_levelwords VALUES (%d,'%s', %d)''' % (i, row[0],level)
    cursor.execute(ro)
    conn.commit()
    i += 1
    level = 1 + i//400

#type of errors
# comma
#unique constraint