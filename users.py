import studentdata as sd
import os

class User():
    def __init__(self, id, firstName, lastName, facePath):
        # Validation
        if type(id) is not int:
            raise TypeError("ID is not a integer")
        if type(firstName) is not str or type(lastName) is not str or type(facePath) is not str:
            raise TypeError("First Name, Last Name or the Face Path is not a string.")
        if None in (id, firstName, lastName, facePath) or "" in (firstName, lastName, facePath):
            raise ValueError("One variable is None")
        if not os.path.exists(facePath):
            raise FileNotFoundError("The face file doesn't exist")
        

        # Initialisation
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.facePath = facePath

    def getFullName(self):
        return self.firstName + " " + self.lastName


class Student(User):
    def __init__(self, id, firstName, lastName, facePath, yearGroup, assignments, timetable):
        super().__init__(id,firstName,lastName,facePath) # Initialises it like the User class
        if type(yearGroup) is not str:
            raise TypeError("yearGroup is not valid type.")
        if type(timetable) is not sd.Timetable:
            raise TypeError("Timetable is not a timetable type")
        if type(assignments) is not list:
            raise TypeError("Assignments is not a list")
        if None in (yearGroup, timetable):
            raise ValueError("None in yearGroup or timetable")
        self.yearGroup = yearGroup
        self.assignments = assignments
        self.timetable = timetable

class Admin(User):
    def __init__(self, id, firstName, lastName, facePath):
        super().__init__(id, firstName, lastName, facePath)

    # Check whether the input password is the same as the one on the database
    def checkPassword(self, password):
        return True