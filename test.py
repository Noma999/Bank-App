
import sqlite3
mydb = sqlite3.connect('test.db')
c = mydb.cursor()


def insert_user(name, DOB, phone, email, address, deposit, pick, pin):
    with mydb:
        c.execute("INSERT INTO user VALUES (?,?,?,?,?,?,?,?)",
                  (name, DOB, phone, email, address, deposit, pick, pin))
        mydb.commit()


def get_person_by_name(name):
    c.execute("SELECT FROM person WHERE name= (?)", name)
    return c.fetchall()


def remove_person(name):
    with mydb:
        c.execute("DELETE from person WHERE name =(?)", name)
