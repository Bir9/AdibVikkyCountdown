from package import *
from tkinter import *
from time import sleep

s = Canvas(Tk(), width = 800, height = 600, background = "black")
s.pack()

years, days, hours, minutes, seconds = timeDifference("18:40:33, May 17, 2022", "14:30:00, Jun 27, 2022") #Calling function and assigning its output to variables

while seconds - 1 >= 0: #Keep running the loop until there is are 0 seconds left
    years, days, hours, minutes, seconds = timerDecreaser() #Re-assigning the counter after we decrease it by 1 second
    
    time = f"{years} years {days} days {hours} hours {minutes} minutes {seconds} seconds"
    display = s.create_text(400, 300, text = time, fill = "white", font = ("Helvetica 25 bold"))
    
    s.update()
    sleep(1)
    s.delete(display)

s.mainloop()