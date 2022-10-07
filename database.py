import sqlite3
from sqlite3 import Error

from studentdata import *
import users
import datetime as dt

database = "database.db"

def connectToDatabase():
    conn = None
    try:
        conn = sqlite3.connect(database)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def InsertCollegeUpdate(collegeUpdateClass):
    # Validation
    if type(collegeUpdateClass) is not CollegeUpdate:
        raise TypeError("Not a collegeUpdateClass")

    sqlcode = """INSERT INTO collegeupdates(date, description) VALUES(?,?)"""
    data = (collegeUpdateClass.date, collegeUpdateClass.text)

    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(sqlcode, data)
    conn.commit()
    return cursor.lastrowid

def SelectAllRowsFromTable(table):
    # Validation
    if type(table) is not str:
        raise TypeError("Table is not a string")

    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ?", table)
    rows = cursor.fetchall()
    return rows

rows = SelectAllRowsFromTable("collegeupdates")
for row in rows:
    print(row)
