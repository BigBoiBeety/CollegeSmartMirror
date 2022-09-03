import tkinter as tk
from tkinter.tix import COLUMN
import tkinter.ttk as ttk

class UserScreen:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("College Smart Mirror")
        self.tk.attributes("-fullscreen", True)

        self.greetingLabel = tk.Label(self.tk, text="Good morning Lewis!", font=("Arial", 50), borderwidth=4, relief=tk.SOLID).grid(column=0, row=0, pady=(0, 50))

        # Assignments
        self.assignmentFrame = tk.Frame(self.tk).grid(column=0, row=1, rowspan=7)
        self.assignmentLabel = tk.Label(self.assignmentFrame, text="Assignments", font=("Arial", 30, "bold")).grid(column=0,row=1, pady=(0, 30))
        self.assignmentRecentLabel = tk.Label(self.assignmentFrame, text="Recently Due", font=("Arial", 20, "underline bold")).grid(column=0, row=2,pady=(0, 10))
        self.assignmentRecentContent = tk.Label(self.assignmentFrame, text="Due Yesterday - Maths Vector Sheet", font=("Arial", 20), fg="red").grid(column=0, row=3,pady=(0, 20))
        self.assignmentSoonLabel = tk.Label(self.assignmentFrame, text="Due Soon", font=("Arial", 20, "underline bold")).grid(column=0, row=4,pady=(0, 10))
        self.assignmentSoonContent = tk.Label(self.assignmentFrame, text="Due tomorrow - Computer Science Networking Test\nDue Friday - IT Unit 21 Deadline", font=("Arial", 20)).grid(column=0, row=5,pady=(0, 20))
        self.assignmentLaterLabel = tk.Label(self.assignmentFrame, text="Due Later", font=("Arial", 20, "underline bold")).grid(column=0, row=6,pady=(0, 10))
        self.assignmentLaterContent = tk.Label(self.assignmentFrame, text="Due 27/6 - IT Unit 21 Deadline", font=("Arial", 20)).grid(column=0, row=7,pady=(0, 20))
        

        # School News
        self.newsFrame = tk.Frame(self.tk).grid(column=1, row=0, rowspan=2)
        self.newsLabel = tk.Label(self.newsFrame, text="School News", font=("Arial", 30, "bold")).grid(column=1,row=0,pady=(0, 30))
        self.newsContent = tk.Label(self.newsFrame, text="07/06 - Bookings for the University Trip are now open!\n 04/06 - Exams for PE begin tomorrow at 1:40PM\n 31/05 - Students that have completed their extended certificate.", font=("Arial", 20)).grid(column=1, row=1,pady=(0, 20))
        
        # Timetable
        self.timetableFrame = tk.Frame(self.tk).grid(column=1, row=2)
        self.timetableLabel = tk.Label(self.timetableFrame, text="Timetable", font=("Arial", 30, "bold")).grid(column=1,row=2, pady=(0,30))
        self.timetableMon = tk.Label(self.timetableFrame, text="Mon     Ma      Ma      Ma              CS      CS", font=("Arial", 20, "bold")).grid(column=1,row=4)
        self.timetableTues = tk.Label(self.timetableFrame, text="Tues       IT      IT      IT      IT      IT      IT", font=("Arial", 20, "bold")).grid(column=1,row=5)
        self.timetableWed = tk.Label(self.timetableFrame, text="Wed                                    Maths      Maths", font=("Arial", 20, "bold")).grid(column=1,row=6)
        self.timetableThurs = tk.Label(self.timetableFrame, text="Thurs     IT      IT      IT      IT      IT      IT", font=("Arial", 20, "bold")).grid(column=1,row=7)
        self.timetableFri = tk.Label(self.timetableFrame, text="Fri     CS      CS      CS                      ", font=("Arial", 20, "bold")).grid(column=1,row=8)

        # Date and Time
        self.dateLabel = tk.Label(self.tk, text="08/06/22 12:05 PM", font=("Arial", 40), borderwidth=4, relief=tk.SOLID).grid(column=2,row=0)


w = UserScreen()
w.tk.mainloop()