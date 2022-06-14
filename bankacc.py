import sqlite3
from profile import Profile
from accnumber import AccNumber
from test import insert_user

mydb = sqlite3.connect('test.db')
c = mydb.cursor()
c.execute(""" CREATE table user (
    name text ,
    DOB integer,
    phone integer,
    email text,
    address text,
    deposit integer,
    pick integer,
    pin
    )""")


print("create new account select 1 ")

option = int(input("Selection:\n"))

while option == 1:
    print("Only text allowed NO NUMBERS OR SYMBOLS OR SPACE")
    name = input("Enter your name:\n")

    print("Only numbers allowed NO LETTERS OR SYMBOLS OR SPACE")
    DOB = int(input("Enter DOB:\n"))

    print("Only numbers allowed NO LETTERS OR SYMBOLS OR SPACE")
    phone = int(input("Enter phone number:\n"))

    print("Only text allowed NO NUMBERS OR SYMBOLS OR SPACE")
    email = input("Enter email:\n")

    print("Only text allowed NO NUMBERS OR SYMBOLS OR SPACE")
    address = input("Enter address:\n")

    print("Only numbers allowed NO LETTERS OR SYMBOLS OR SPACE")
    deposit = int(input("Enter an amount to open account:\n"))

    user = Profile(name, DOB, phone, email, address, deposit)
    print(user.show())

    accc = AccNumber()
    print(accc.pick())
    print(accc.pin())
    pick = int(accc.pick())
    pin = int(accc.pin())

    insert_user(name, DOB, phone, email, address, deposit, pick, pin)

    print("successful")

    c.fetchall()
    mydb.commit()
    mydb.close()
    break

else:
    print("Already Exist!!!!")

'''if person == person.show():
        print("account already exist")
else:
    person1 = Profile(name, DOB, phone, email, address)
    print(person1.show())
    profile1 = AccNumber()
    print(profile1.pick())
    print(profile1.pin())'''
