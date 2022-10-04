from home_screen import *
from user_screen import *

while True:

    home = HomeScreen()
    home.tk.mainloop()

    user = UserScreen()
    user.tk.mainloop()