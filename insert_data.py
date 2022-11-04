import datetime as dt
import database
import studentdata as sd

print("What would you like to insert?")
choice = input("0 - Student | 1 - College Update | 2 - Assignment | ")

if choice == "0":
    # Insert student
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
    duedate = dt.datetime.strptime(input("When is the due date? (In the form dd/mm/yy)\n"), '%Y-%m-%d').date()

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
    pass
