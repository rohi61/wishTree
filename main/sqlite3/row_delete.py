import sqlite3

#データベース読み込み
db = sqlite3.connect(
    "/Users/h-imada/Documents/program/python/wishTree/db.sqlite3",              #ファイル名
    isolation_level=None,
)

#レコード削除用SQL文
sql = """DELETE FROM main_groop_list WHERE id="1";"""

db.execute(sql)  #sql文を実行
db.close()      #データベースを閉じる