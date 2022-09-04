from home_screen import *
from user_screen import *
import face_detection as fd


while True:

    home = HomeScreen()
    home.tk.mainloop()

    user = UserScreen()
    user.tk.mainloop()

