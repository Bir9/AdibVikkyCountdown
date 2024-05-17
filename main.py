from package import *
from tkinter import *
from time import sleep

s = Canvas(Tk(), width = 800, height = 600, background = "black")
s.pack()

years, days, hours, minutes, seconds = timeDifference("09:52:14, May 04, 2022", "14:20:00, Jun 27, 2022")

while seconds - 1 >= 0:
    years, days, hours, minutes, seconds = timerDecreaser()
    time = f"{years} years {days} days {hours} hours {minutes} minutes {seconds} seconds"
    
    display = s.create_text(400, 300, text = time, fill = "white", font = ("Helvetica 25 bold"))
    
    s.update()
    sleep(1)
    s.delete(display)

s.mainloop()