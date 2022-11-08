import datetime as dt
import database
import studentdata as sd
import users

def MakeTimetableClass():
    periods = [[],[],[],[],[]]

    day = 0 # Day will go from 0-4 (mon-fri)
    while True:
        willExit = input("Stop entering periods for this day? (y/n) ")
        # Will go to the next day's periods
        if willExit == "y":
            day += 1
            if day > 4:
                break

        subject = input("What subject is it for? ")
        teacher = input("What teacher is it? ")
        classroom = input("What classroom is it? ")

        periods[day].append(sd.Period(subject, teacher, classroom))
    
    timetable = sd.Timetable(periods[0], periods[1], periods[2], periods[3], periods[4])
    return timetable

print("What would you like to do?")
choice = input("0 - Insert | 1 - Read | 2 - Delete | ")

if choice == "0":
    # Insert
    print("What would you like to insert?")
    choice = input("0 - Student | 1 - College Update | 2 - Assignment | ")

    if choice == "0":
        # Insert student
        firstName = input("What is their first name? ")
        lastName = input("What is their last name? ")
        facePath = input("Where is the location of their face image? ")
        yearGroup = input("What year group are they in? ")

        timetable = MakeTimetableClass()

        student = users.Student(0, firstName, lastName, facePath, yearGroup, [], timetable)

        database.InsertStudent(student)

        pass
    elif choice == "1":
        # Insert college update
        description = input("What will the college update say?\n")
        collegeupdate = sd.CollegeUpdate(dt.datetime.now().date(), description)
        database.InsertCollegeUpdate(collegeupdate)
        pass
    elif choice == "2":
        # Insert Assignment
        subject = input("What subject is the assignment for? e.g. IT Unit 14\n")
        teacher = input("Which teacher made the assignment?\n")
        duedate = dt.datetime.strptime(input("When is the due date? (In the form yyyy-mm-dd)\n"), '%Y-%m-%d').date()

        assignment = sd.Assignment(subject, teacher, duedate)   

        print("Enter student IDs the assignment will be assigned for (type 0 to stop)")
        studentIDs = []
        while True:
            studentID = int(input("Enter student ID: "))
            if studentID == 0:
                break
            else:
                studentIDs.append(studentID)

        for id in studentIDs:
            database.InsertAssignment(assignment, id)
elif choice == "1":
    # Read
    print("What table would you like to read?")
    choice = input("0 - Assignments | 1 - College Updates | 2 - Periods | 3 - Students | 4 - Timetables | ")

    rows = []
    if choice == "0":
        # Show assignments
        print(("id", "subject", "teacher", "date", "userID"))
        rows = database.SelectAllRowsFromTable("assignments")
    elif choice == "1":
        print(("id", "date", "description"))
        rows = database.SelectAllRowsFromTable("collegeupdates")
    elif choice == "2":
        print(("id", "nextID", "subject", "teacher", "classroom"))
        rows = database.SelectAllRowsFromTable("periods")
    elif choice == "3":
        print(("id", "firstName", "lastName", "facePath", "yearGroup", "timetableID"))
        rows = database.SelectAllRowsFromTable("students")
    elif choice == "4":
        print(("id", "mondayID", "tuesdayID", "wednesdayID", "thursdayID", "fridayID"))
        rows = database.SelectAllRowsFromTable("timetables")
    
    for row in rows:
        print(row)
elif choice == "2":
    print("What table do you want to delete from? ")
    choice = input("0 - Assignments | 1 - College Updates | 2 - Periods | 3 - Students | 4 - Timetables | ")
    idToDelete = int(input("What id do you want to delete? "))

    if choice == "0":
        # Show assignments
        database.DeleteRowFromTable("assignments", idToDelete)
    elif choice == "1":
        database.DeleteRowFromTable("collegeupdates", idToDelete)
    elif choice == "2":
        database.DeleteRowFromTable("periods", idToDelete)
    elif choice == "3":
        database.DeleteRowFromTable("students", idToDelete)
    elif choice == "4":
        database.DeleteRowFromTable("timetables", idToDelete)
    
input()


