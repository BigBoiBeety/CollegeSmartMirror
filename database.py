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


def InsertAssignment(assignmentClass, userID):
    # Validation
    if type(assignmentClass) is not Assignment:
        raise TypeError("Not a assignment class")
    
    sqlcode = """INSERT INTO assignments(subject, teacher, date, userID) VALUES (?,?,?,?)"""
    data = (assignmentClass.subject, assignmentClass.teacher, assignmentClass.dueDate, userID)

    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(sqlcode, data)
    conn.commit()
    return cursor.lastrowid

def InsertPeriod(periodClass, nextID):
    # Validation
    if type(periodClass) is not Period:
        raise TypeError("Is not a period class")
    if type(nextID) is not int:
        raise TypeError("Next id isn't an int")

    sqlcode = """INSERT INTO periods(nextID, subject, teacher, classroom) VALUES (?,?,?,?)"""
    data = (nextID, periodClass.subject, periodClass.teacher, periodClass.classroom)

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
    cursor.execute("SELECT * FROM " + table)
    rows = cursor.fetchall()
    return rows

def SelectAllAssignmentsFromUser(userID):
    # Validation
    if type(userID) is not int:
        raise TypeError("User id is not an int")
    
    conn = connectToDatabase()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM assignments WHERE userID=?", (userID,))
    
    rows = cursor.fetchall()
    return rows

period = Period("Maths", "Joe", "LB1")
print(InsertPeriod(period, 0))