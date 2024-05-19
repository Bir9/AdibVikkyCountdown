from package import *
from tkinter import *
from time import sleep
from tkcalendar import Calendar
from datetime import datetime

# Initialize the main window
ws = Tk()
ws.title("Countdown Timer")
ws.geometry("800x500")
ws.config(bg="black")

# Fonts and colors
f = ('Times', 20)
font_color = "white"
bg_color = "black"

# Variables for storing date and time
start_date = []
end_date = []

# Function to switch to the main program
def start_program():
    welcome_frame.pack_forget()
    date_picker_frame.pack()

# Function to exit the program
def exit_program():
    ws.destroy()

# Function to confirm the start date and switch to end date selection
def confirm_start_date():
    global start_date_obj
    date_str = start_cal.get_date()
    h = hour_sb.get()
    m = min_sb.get()
    s = sec_sb.get()

    # Adapt the format to handle the two-digit year correctly
    start_date_obj = datetime.strptime(f"{date_str} {h}:{m}:{s}", "%m/%d/%y %H:%M:%S")

    # Convert to four-digit year format for storing
    start_date.clear()  # Clear any previous data
    start_date.extend([start_date_obj.strftime("%m/%d/%Y"), h, m, s])

    start_date_only = start_date_obj.date()

    # Disable dates before start date in the end date calendar
    end_cal.config(mindate=start_date_only)
    date_picker_frame.pack_forget()
    end_date_picker_frame.pack()

# Function to confirm the end date and start the countdown timer
def confirm_end_date():
    global end_date

    date_str = end_cal.get_date()
    h = end_hour_sb.get()
    m = end_min_sb.get()
    s = end_sec_sb.get()

    # Adapt the format to handle the two-digit year correctly
    end_date_obj = datetime.strptime(f"{date_str} {h}:{m}:{s}", "%m/%d/%y %H:%M:%S")

    # Convert to four-digit year format for storing
    end_date.clear()  # Clear any previous data
    end_date.extend([end_date_obj.strftime("%m/%d/%Y"), h, m, s])

    end_date_picker_frame.pack_forget()
    result_frame.pack()
    start_countdown_timer()

def start_countdown_timer():
    global start_date, end_date

    if start_date == end_date:
        years, days, hours, minutes, seconds = 0, 0, 0, 0, 0
    else:
        print(start_date, end_date)
        years, days, hours, minutes, seconds = timeDifference(start_date, end_date)

    while seconds != -1:  # Keep running the loop until there are 0 seconds left
        if start_date == end_date:
            # If start and end dates are equal, keep the timer variables at 0
            years, days, hours, minutes, seconds = 0, 0, 0, 0, 0
        else:
            # Otherwise, decrement the timer variables
            years, days, hours, minutes, seconds = timerDecreaser()  # Re-assigning the counter after decreasing it by 1 second

        time_str = f"{years} years {days} days {hours} hours {minutes} minutes {seconds} seconds"
        timer_display.config(text=time_str)
        timer_display.pack()

        ws.update()
        sleep(1)

# Update the time limits for the end date
def update_time_limits(*args):
    end_date_str = end_cal.get_date()
    end_date_time = datetime.strptime(end_date_str, "%m/%d/%y")
    if end_date_time.date() == start_date_obj.date():
        end_hour_sb.config(from_=int(start_date[1]), to=23)
        if int(end_hour_sb.get()) == int(start_date[1]):
            end_min_sb.config(from_=int(start_date[2]), to=59)
            if int(end_min_sb.get()) == int(start_date[2]):
                end_sec_sb.config(from_=int(start_date[3]), to=59)
            else:
                end_sec_sb.config(from_=0, to=59)
        else:
            end_min_sb.config(from_=0, to=59)
            end_sec_sb.config(from_=0, to=59)
    else:
        end_hour_sb.config(from_=0, to=23)
        end_min_sb.config(from_=0, to=59)
        end_sec_sb.config(from_=0, to=59)

# Welcome frame
welcome_frame = Frame(ws, bg=bg_color)
welcome_msg = Label(welcome_frame, text="Welcome", font=("Times", 30), bg=bg_color, fg=font_color)
welcome_msg.pack(pady=20)

start_btn = Button(welcome_frame, text="Start Program", command=start_program, padx=20, pady=10, bg="white", fg="black")
start_btn.pack(pady=10)

exit_btn = Button(welcome_frame, text="Exit Program", command=exit_program, padx=20, pady=10, bg="white", fg="black")
exit_btn.pack(pady=10)

welcome_frame.pack()

# Date picker frame for start date
date_picker_frame = Frame(ws, bg=bg_color)
start_cal = Calendar(date_picker_frame, selectmode="day", year=2024, month=5, day=1, background='white', foreground='black')
start_cal.pack(pady=20)

hour_sb = Spinbox(date_picker_frame, from_=0, to=23, wrap=True, font=f, width=2, justify=CENTER)
min_sb = Spinbox(date_picker_frame, from_=0, to=59, wrap=True, font=f, width=2, justify=CENTER)
sec_sb = Spinbox(date_picker_frame, from_=0, to=59, wrap=True, font=f, width=2, justify=CENTER)

hour_sb.pack(side=LEFT, fill=X, expand=True, padx=5)
min_sb.pack(side=LEFT, fill=X, expand=True, padx=5)
sec_sb.pack(side=LEFT, fill=X, expand=True, padx=5)

confirm_start_btn = Button(date_picker_frame, text="Confirm Start Date", command=confirm_start_date, padx=10, pady=10, bg="white", fg="black")
confirm_start_btn.pack(pady=20)

# Date picker frame for end date
end_date_picker_frame = Frame(ws, bg=bg_color)
end_cal = Calendar(end_date_picker_frame, selectmode="day", year=2024, month=5, day=1, background='white', foreground='black')
end_cal.pack(pady=20)

end_hour_sb = Spinbox(end_date_picker_frame, from_=0, to=23, wrap=True, font=f, width=2, justify=CENTER)
end_min_sb = Spinbox(end_date_picker_frame, from_=0, to=59, wrap=True, font=f, width=2, justify=CENTER)
end_sec_sb = Spinbox(end_date_picker_frame, from_=0, to=59, wrap=True, font=f, width=2, justify=CENTER)

end_hour_sb.pack(side=LEFT, fill=X, expand=True, padx=5)
end_min_sb.pack(side=LEFT, fill=X, expand=True, padx=5)
end_sec_sb.pack(side=LEFT, fill=X, expand=True, padx=5)

end_hour_sb.bind('<Configure>', update_time_limits)
end_min_sb.bind('<Configure>', update_time_limits)
end_sec_sb.bind('<Configure>', update_time_limits)
end_cal.bind("<<CalendarSelected>>", update_time_limits)

confirm_end_btn = Button(end_date_picker_frame, text="Confirm End Date", command=confirm_end_date, padx=10, pady=10, bg="white", fg="black")
confirm_end_btn.pack(pady=20)

# Result frame
result_frame = Frame(ws, bg=bg_color)
timer_display = Label(result_frame, text="", font=("Times", 15), bg=bg_color, fg=font_color)
timer_display.pack(pady=20)

# Start the Tkinter event loop
ws.mainloop()
