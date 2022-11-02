import tkinter as tk
import face_detection as fd
import datetime as dt
import database
import sys

sys.setrecursionlimit = 10000

class HomeScreen:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("College Smart Mirror")
        self.tk.attributes("-fullscreen", True)
        self.tk.after(200, self.faceDetected)

        collegeUpdate = database.MakeCollegeUpdateFromID(database.GetRecentCollegeUpdates()[0][0])

        self.newslabel = tk.Label(self.tk, text=collegeUpdate.text, font=("Arial", 30))
        self.newslabel.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        self.timelabel = tk.Label(self.tk, text="00:00", font=("Arial", 120, "bold"))
        self.timelabel.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.datelabel = tk.Label(self.tk, text="Monday 1 January", font=("Arial", 40, "bold"))
        self.datelabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.smilelabel = tk.Label(self.tk, text="Smile at the camera to login", font=("Arial", 50, "bold"))
        self.smilelabel.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.locationlabel = tk.Label(self.tk, text="You are in the SOC", font=("Arial", 60))
        self.locationlabel.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.tk.after(1, self.updateScreen)
    def faceDetected(self):
        if fd.getFirstIdentifiedPerson():
            self.tk.destroy()
    def updateScreen(self):
        timeString = dt.datetime.strftime(dt.datetime.now(), "%H:%M")
        dateString = dt.datetime.strftime(dt.datetime.now(), "%d %B %Y")

        self.timelabel.config(text=timeString)
        self.datelabel.config(text=dateString)

        self.tk.update()

        self.tk.after(1000, self.updateScreen())
    