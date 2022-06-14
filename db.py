import sqlite3


conn = sqlite3.connect('database_name.db')

c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS user
          ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS pin
          ([user_id] INTEGER PRIMARY KEY, [pin] INTEGER)
          ''')


c.execute('''
          INSERT INTO user (user_id, user_name)

                VALUES
                (1,'Nosa'),
                (2,'Iredia'),
                (3,'Enoma'),
                (4,'Imade'),
                (5,'Peace')
          ''')

c.execute('''
          INSERT INTO pin (user_id, pin)

                VALUES
                (1,8002),
                (2,2002),
                (3,3002),
                (4,4502),
                (5,1502)
          ''')


c.execute('''
          SELECT
          a.user_name,
          b.pin
          FROM user a
          LEFT JOIN pin b ON a.user_id = b.user_id
          ''')

df = c.fetchall()
print(df)
conn.commit()
