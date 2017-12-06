import pymysql

conn = pymysql.Connect(host="127.0.0.1"
                       ,port=3306
                       ,user="root"
                       ,passwd="password"
                       ,db="apple"
                       ,charset="utf8")
cursor = conn.cursor()
def get():
    sql = "select * from city limit 10"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)

def update():
    sql = " "

print(conn)
print(cursor)

cursor.close()
conn.close()