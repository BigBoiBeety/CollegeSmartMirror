import tkinter as tk

class HomeScreen:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("College Smart Mirror")
        self.tk.attributes("-fullscreen", True)

        self.newslabel = tk.Label(self.tk, text="News placeholder", font=("Arial", 30)).place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        self.timelabel = tk.Label(self.tk, text="00:00", font=("Arial", 120, "bold")).place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.datelabel = tk.Label(self.tk, text="Monday 1 January", font=("Arial", 40, "bold")).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.smilelabel = tk.Label(self.tk, text="Smile at the camera to login", font=("Arial", 50, "bold")).place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.locationlabel = tk.Label(self.tk, text="You are in placeholder", font=("Arial", 60)).place(relx=0.5, rely=0.9, anchor=tk.CENTER)

w = HomeScreen()
w.tk.mainloop()
    