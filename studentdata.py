import datetime as dt

class Assignment():
    def __init__(self, subject, teacher, dueDate):
        # Validation
        if type(subject) is not str or type(teacher) is not str:
            raise TypeError("Subject or Teacher isn't a string")
        if type(dueDate) is not dt.date:
            raise TypeError("Due date is not a datetime")
        if None in (subject, teacher, dueDate):
            raise ValueError("A input is a None type")

        self.subject = subject
        self.teacher = teacher
        self.dueDate = dueDate
    def getTimeRemaining(self):
        currentDate = dt.datetime.now().date()
        timeDifference = self.dueDate - currentDate
        return timeDifference.days

class Period():
    def __init__(self, subject, teacher, classroom):
        # Validation
        if type(subject) is not str or type(teacher) is not str or type(classroom) is not str:
            raise TypeError("Subject, Teacher or Classroom isn't a string")
        if None in (subject, teacher, classroom):
            raise ValueError("One variable is None")

        self.subject = subject
        self.teacher = teacher
        self.classroom = classroom

class Timetable():
    def __init__(self, mondayPeriods, tuesdayPeriods, wednesdayPeriods, thursdayPeriods, fridayPeriods):
        # Validation
        if type(mondayPeriods) is not list or type(tuesdayPeriods) is not list or type(wednesdayPeriods) is not list or type(thursdayPeriods) is not list or type(fridayPeriods) is not list:
            raise TypeError("A input is not a list")
        if None in (mondayPeriods, tuesdayPeriods, wednesdayPeriods, thursdayPeriods, fridayPeriods):
            raise ValueError("One variable is None")

        self.periods = [mondayPeriods, tuesdayPeriods, wednesdayPeriods, thursdayPeriods, fridayPeriods]

class CollegeUpdate():
    def __init__(self, date, text):
        # Validation
        if type(date) is not dt.date:
            raise TypeError("Date is not a date object")
        if type(text) is not str:
            raise TypeError("Text is not a string")
        if None in (date, text):
            raise ValueError("Date or text is a None type")
        self.date = date
        self.text = text
