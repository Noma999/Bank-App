
import sqlite3
from profile import Profile
from accnumber import AccNumber


mydb = sqlite3.connect('bank.db')
c = mydb.cursor()
c.execute(""" create table user(
  name text ,
  DOB integer,
  phone integer,
  email text,
  address text,
  deposit integer

)""")
c.execute(""" create table accc(
  name text,
  pick integer,
  pin integer
)""")


"""def get_person_by_name(name):
  c.execute("SELECT FROM person WHERE name=:name",{'name':name}) 
  return c.fetchall()  



def remove_person(person):
  with mydb:
    c.execute("DELETE from person WHERE name=:name",{'name':person.name}) """


name = input("Enter your name:\n")
DOB = int(input("Enter DOB:\n"))
phone = int(input("Enter phone number:\n"))
email = input("Enter email:\n")
address = input("Enter address:\n")
deposit = int(input("Enter an amount to open account:\n"))


user = Profile(name, DOB, phone, email, address, deposit)
print(user.show())


accc = AccNumber()
print(accc.pick())
print(accc.pin())
pick = accc.pick()
pin = accc.pin()


def insert_user(name, DOB, phone, email, address, deposit):
    with mydb:
        c.execute("INSERT INTO user VALUES (?,?,?,?,?,?)",
                  (name, DOB, phone, email, address, deposit))
        mydb.commit()


def insert_acc(name, pick, pin):
    with mydb:
        c.execute("INSERT INTO accc VALUES (?,?,?)",
                  (name, pick, pin))
        mydb.commit()


def join_table():
    with mydb:
        c.execute('''SELECT *
        FROM user 
        LEFT JOIN accc
        ON user.name=accc.name ''');
        mydb.commit()


insert_user(name, DOB, phone, email, address, deposit)
insert_acc(name, pick, pin)


join_table()
print("successful")


c.fetchall()
mydb.commit()
mydb.close()
