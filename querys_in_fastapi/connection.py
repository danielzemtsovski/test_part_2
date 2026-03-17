import pymysql

config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "digital_hunter"
    }

try:
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    query = "SHOW TABLES"     #"select * from attacks"
    cur.execute(query)
    s = cur.fetchall()
    for r in s:
        print(r)

except Exception as a:
    print(f"{a}")

finally:
    conn.close()

