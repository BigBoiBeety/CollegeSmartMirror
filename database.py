import sqlite3
from sqlite3 import Error, connect
from typing import Type

from studentdata import *
import users
import datetime as dt

database = "database.db"

def connectToDatabase():
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    return conn

def InsertCollegeUpdate(collegeUpdateClass):
    # Validation
    if type(collegeUpdateClass) is not CollegeUpdate:
        raise TypeError("Not a collegeUpdateClass")

    sqlcode = """INSERT INTO collegeupdates(date, description) VALUES(?,?)"""
    data = (collegeUpdateClass.date, collegeUpdateClass.text)

    return InsertSQLWithData(sqlcode, data)

def InsertAssignment(assignmentClass, userID):
    # Validation
    if type(assignmentClass) is not Assignment:
        raise TypeError("Not a assignment class")
    
    sqlcode = """INSERT INTO assignments(subject, teacher, date, userID) VALUES (?,?,?,?)"""
    data = (assignmentClass.subject, assignmentClass.teacher, assignmentClass.dueDate, userID)

    return InsertSQLWithData(sqlcode, data)

def InsertPeriod(periodClass, nextID):
    # Validation
    if type(periodClass) is not Period:
        raise TypeError("Is not a period class")
    if type(nextID) is not int:
        raise TypeError("Next id isn't an int")

    sqlcode = """INSERT INTO periods(nextID, subject, teacher, classroom) VALUES (?,?,?,?)"""
    data = (nextID, periodClass.subject, periodClass.teacher, periodClass.classroom)

    return InsertSQLWithData(sqlcode, data)

def InsertMultiplePeriods(periodList):
    i = 1
    reversePeriods = []
    for period in periodList:
        reversePeriods.append(periodList[len(periodList) - i])
        i += 1

    lastID = 0
    for period in reversePeriods:
        lastID = InsertPeriod(period, lastID)
    
    return lastID

def InsertTimetable(timetableClass):
    # Validation
    if type(timetableClass) is not Timetable:
        raise TypeError("Timetable is not a timetable class")

    mondayPeriodID = InsertMultiplePeriods(timetableClass.periods[0])
    tuesdayPeriodID = InsertMultiplePeriods(timetableClass.periods[1])
    wednesdayPeriodID = InsertMultiplePeriods(timetableClass.periods[2])
    thursdayPeriodID = InsertMultiplePeriods(timetableClass.periods[3])
    fridayPeriodID = InsertMultiplePeriods(timetableClass.periods[4])

    sqlcode = """INSERT INTO timetables(mondayID, tuesdayID, wednesdayID, thursdayID, fridayID) VALUES (?,?,?,?,?)"""
    data = (mondayPeriodID, tuesdayPeriodID, wednesdayPeriodID, thursdayPeriodID, fridayPeriodID)

    return InsertSQLWithData(sqlcode, data)

def InsertStudent(studentClass):
    # Validation
    if type(studentClass) is not users.Student:
        raise TypeError("Student isn't a student class")

    sqlcode = """INSERT INTO students(firstName, lastName, facePath, yearGroup, timetableID) VALUES (?,?,?,?,?)"""

    timetableID = InsertTimetable(studentClass.timetable)

    data = (studentClass.firstName, studentClass.lastName, studentClass.facePath, studentClass.yearGroup, timetableID)
    
    return InsertSQLWithData(sqlcode, data)

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

def InsertSQLWithData(sqlcode, data):
    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(sqlcode, data)
    conn.commit()
    return cursor.lastrowid

def GetIDandFacePathFromStudents():
    sqlcode = "SELECT id, facePath FROM students"

    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(sqlcode)
    rows = cursor.fetchall()
    return rows

def MakeCollegeUpdateFromID(id):
    # Validation
    if type(id) is not int:
        raise TypeError("ID is not an int")

    sqlcode = "SELECT * FROM collegeupdates WHERE id = ?"
    data = (id,)

    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(sqlcode, data)
    rows = cursor.fetchall()[0]

    date = dt.datetime.strptime(rows[1], '%Y-%m-%d').date()
    collegeUpdate = CollegeUpdate(date, rows[2])
    return collegeUpdate

def MakeAssignmentClassFromID(assignmentID):
    # Validation
    if type(assignmentID) is not int:
        raise TypeError("ID is not an int")

    sqlcode = "SELECT * FROM assignments WHERE id = ?"
    data = (assignmentID,)

    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(sqlcode, data)
    data = cursor.fetchall()[0]

    assignment = Assignment(data[1], data[2], dt.datetime.strptime(data[3], '%Y-%m-%d').date())
    return assignment

def GetAllUserAssignments(userID):
    # Validation
    if type(userID) is not int:
        raise TypeError("ID is not an int")
    
    assignments = []

    sqlcode = "SELECT id FROM assignments WHERE userID = ?"
    data = (userID,)

    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(sqlcode, data)
    rows = cursor.fetchall()

    for id in rows:
        assignments.append(MakeAssignmentClassFromID(id[0]))

    return assignments

def MakeTimetable(id):
    if type(id) is not int:
        raise TypeError("ID isn't a integer")
    
    sqlcode = "SELECT * FROM timetables WHERE id = ?"
    data = (id,)

    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(sqlcode, data)

    timetable = cursor.fetchall()[0]

    mondayPeriods = GetAllPeriods(timetable[1])
    tuesdayPeriods = GetAllPeriods(timetable[2])
    wednesdayPeriods = GetAllPeriods(timetable[3])
    thursdayPeriods = GetAllPeriods(timetable[4])
    fridayPeriods = GetAllPeriods(timetable[5])

    return Timetable(mondayPeriods, tuesdayPeriods, wednesdayPeriods, thursdayPeriods, fridayPeriods)
    

def GetAllPeriods(periodID):
    if type(periodID) is not int:
        raise TypeError("ID is not an int")
    
    periods = []

    conn = connectToDatabase()
    cursor = conn.cursor()

    sqlcode = "SELECT * FROM periods WHERE id = ?"
    currentID = periodID
    while True:
        cursor.execute(sqlcode, (currentID,))
        period = cursor.fetchall()[0]
        periods.append(MakePeriodClass(period))
        if period[1] == 0:
            break
        currentID = period[1]
        
    conn.close()

    return periods


def MakePeriodClass(periodData):
    return Period(periodData[2], periodData[3], periodData[4])

def MakeStudent(studentID):
    if type(studentID) is not int:
        raise TypeError("ID is not an int")
    
    sqlcode = "SELECT * FROM students WHERE id = ?"
    data = (studentID,)

    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(sqlcode, data)
    student = cursor.fetchall()[0]

    timetable = MakeTimetable(student[5])
    assignments = GetAllUserAssignments(student[0])

    return users.Student(student[0], student[1], student[2], student[3], student[4], assignments, timetable)