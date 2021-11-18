import sqlite3

con = sqlite3.connect('/Users/h-imada/Documents/program/python/wishTree/db.sqlite3')
cur = con.cursor()
cur.execute("DROP TABLE main_groop_member_list")
con.close()
print("処理終了")