import datetime
from home_screen import *
from user_screen import *
import face_detection as fd
from users import *
from studentdata import *


while True:

    home = HomeScreen()
    home.tk.mainloop()

    user = UserScreen()
    user.tk.mainloop()

