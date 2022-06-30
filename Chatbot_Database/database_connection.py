import pymysql.cursors

#%%

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='qwerty',
                             database='timetable',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "select * from course"
        cursor.execute(sql)
        # cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchall()
        print(result)

#%%


