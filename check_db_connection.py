import pymysql

dbconfig = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "db": "test",
    "charset": "utf8"
}

connection = pymysql.connect(**dbconfig , cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SELECT group_id, group_name, group_header, group_footer FROM group_list;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
finally:
    connection.close()