import tkinter as tk
import tkinter.ttk as ttk
import database
import datetime as dt

class UserScreen:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("College Smart Mirror")
        self.tk.attributes("-fullscreen", True)

        self.greetingLabel = tk.Label(self.tk, text="Good morning!", font=("Arial", 50), borderwidth=4, relief=tk.SOLID)
        self.greetingLabel.grid(column=0, row=0, pady=(0, 50))

        # Assignments
        self.assignmentFrame = tk.Frame(self.tk)
        self.assignmentFrame.grid(column=0, row=1, rowspan=7)
        self.assignmentLabel = tk.Label(self.assignmentFrame, text="Assignments", font=("Arial", 30, "bold"))
        self.assignmentLabel.grid(column=0,row=1, pady=(0, 30))
        self.assignmentRecentLabel = tk.Label(self.assignmentFrame, text="Recently Due", font=("Arial", 20, "underline bold"))
        self.assignmentRecentLabel.grid(column=0, row=2,pady=(0, 10))
        self.assignmentRecentContent = tk.Label(self.assignmentFrame, text="Due Yesterday - Maths Vector Sheet", font=("Arial", 20), fg="red")
        self.assignmentRecentContent.grid(column=0, row=3,pady=(0, 20))
        self.assignmentSoonLabel = tk.Label(self.assignmentFrame, text="Due Soon", font=("Arial", 20, "underline bold"))
        self.assignmentSoonLabel.grid(column=0, row=4,pady=(0, 10))
        self.assignmentSoonContent = tk.Label(self.assignmentFrame, text="Due tomorrow - Computer Science Networking Test\nDue Friday - IT Unit 21 Deadline", font=("Arial", 20))
        self.assignmentSoonContent.grid(column=0, row=5,pady=(0, 20))
        self.assignmentLaterLabel = tk.Label(self.assignmentFrame, text="Due Later", font=("Arial", 20, "underline bold"))
        self.assignmentLaterLabel.grid(column=0, row=6,pady=(0, 10))
        self.assignmentLaterContent = tk.Label(self.assignmentFrame, text="Due 27/6 - IT Unit 21 Deadline", font=("Arial", 20))
        self.assignmentLaterContent.grid(column=0, row=7,pady=(0, 20))
        

        # School News
        self.newsFrame = tk.Frame(self.tk)
        self.newsFrame.grid(column=1, row=0, rowspan=2)
        self.newsLabel = tk.Label(self.newsFrame, text="School News", font=("Arial", 30, "bold"))
        self.newsLabel.grid(column=1,row=0,pady=(0, 30))
        self.newsContent = tk.Label(self.newsFrame, text="07/06 - Bookings for the University Trip are now open!\n 04/06 - Exams for PE begin tomorrow at 1:40PM\n 31/05 - Students that have completed their extended certificate.", font=("Arial", 20))
        self.newsContent.grid(column=1, row=1,pady=(0, 20))
        
        # Timetable
        self.timetableFrame = tk.Frame(self.tk)
        self.timetableFrame.grid(column=1, row=2)
        self.timetableLabel = tk.Label(self.timetableFrame, text="Timetable", font=("Arial", 30, "bold"))
        self.timetableLabel.grid(column=1,row=2, pady=(0,30))
        self.timetableMon = tk.Label(self.timetableFrame, text="Mon     Ma      Ma      Ma              CS      CS", font=("Arial", 20, "bold"))
        self.timetableMon.grid(column=1,row=4)
        self.timetableTues = tk.Label(self.timetableFrame, text="Tues       IT      IT      IT      IT      IT      IT", font=("Arial", 20, "bold"))
        self.timetableTues.grid(column=1,row=5)
        self.timetableWed = tk.Label(self.timetableFrame, text="Wed                                    Maths      Maths", font=("Arial", 20, "bold"))
        self.timetableWed.grid(column=1,row=6)
        self.timetableThurs = tk.Label(self.timetableFrame, text="Thurs     IT      IT      IT      IT      IT      IT", font=("Arial", 20, "bold"))
        self.timetableThurs.grid(column=1,row=7)
        self.timetableFri = tk.Label(self.timetableFrame, text="Fri     CS      CS      CS                      ", font=("Arial", 20, "bold"))
        self.timetableFri.grid(column=1,row=8)

        # Date and Time
        self.dateLabel = tk.Label(self.tk, text=dt.datetime.strftime(dt.datetime.now(),'%m/%d/%y %H:%M:%S'), font=("Arial", 40), borderwidth=4, relief=tk.SOLID)
        self.dateLabel.grid(column=2,row=0)

        file = open("output.txt", "r")
        self.currentUser = int(file.read())
        print(self.currentUser)

        self.studentClass = database.MakeStudent(self.currentUser)

        self.greetingLabel.config(text="Hello " + self.studentClass.firstName)

        collegeUpdates = database.GetRecentCollegeUpdates()
        collegeUpdateText = ""
        for update in collegeUpdates:
            collegeClass = database.MakeCollegeUpdateFromID(update[0])
            collegeUpdateText += "\n" + collegeClass.date.strftime("%d/%m") + " | " + collegeClass.text

        self.newsContent.config(text=collegeUpdateText)

        periods = self.studentClass.timetable.periods
        
        self.timetableMon.config(text="MON " + self.MakeTimetableText(periods[0]))
        self.timetableTues.config(text="TUE " + self.MakeTimetableText(periods[1]))
        self.timetableWed.config(text="WED " + self.MakeTimetableText(periods[2]))
        self.timetableThurs.config(text= "THU " + self.MakeTimetableText(periods[3]))
        self.timetableFri.config(text="FRI " + self.MakeTimetableText(periods[4]))

        sortedAssignments = database.SortAssignmentDueDates(self.studentClass.assignments)

        self.assignmentRecentContent.config(text=self.MakeAssignmentText(sortedAssignments[0]))
        self.assignmentSoonContent.config(text=self.MakeAssignmentText(sortedAssignments[1]))
        self.assignmentLaterContent.config(text=self.MakeAssignmentText(sortedAssignments[2]))



        # Close after xxxx milliseconds
        self.tk.after(10000, self.tk.destroy)
    def MakeTimetableText(self, periods):
        text = ""
        for period in periods:
            text += period.subject[:2] + " "
        return text
    def MakeAssignmentText(self, assignments):
        text = ""
        for assignment in assignments:
            text += "\n" + str(assignment.getTimeRemaining()) + " days | " + assignment.subject
        return text
