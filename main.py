from package import *
from tkinter import *
from time import sleep
from tkcalendar import Calendar
from datetime import datetime

# Initialize the main window
ws = Tk()
ws.title("Countdown Timer")
ws.geometry("800x500")
ws.config(bg="#1B263B")

# Fonts and colors
f = ('Lexend', 20)
font_color = "white"
bg_color = "#1B263B"

# Variables for storing date and time
start_date = []
end_date = []

# Function to switch to the main program
def start_program():
    welcome_frame.place_forget()
    date_picker_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def restart_program():
    result_frame.place_forget()
    date_picker_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

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
    date_picker_frame.place_forget()
    end_date_picker_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

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

    end_date_picker_frame.place_forget()
    result_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    start_countdown_timer()

def start_countdown_timer():
    global start_date, end_date
    
    if start_date == end_date:
        years, days, hours, minutes, seconds = 0, 0, 0, 0, 0
    else:
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
        timer_display.grid(column=0, row=0)
        
        restart_btn.grid(column=0, row=1)
        exit_timer_btn.grid(column=0, row=2)

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
        end_hour_sb.config(from_=0, to=23)
        end_min_sb.config(from_=0, to=59)
        end_sec_sb.config(from_=0, to=59)
        
        # Reset the spinbox values to 0
        end_hour_sb.delete(0, 'end')
        end_hour_sb.insert(0, '0')
        end_min_sb.delete(0, 'end')
        end_min_sb.insert(0, '0')
        end_sec_sb.delete(0, 'end')
        end_sec_sb.insert(0, '0')

# Welcome frame
welcome_frame = Frame(ws, bg=bg_color)
welcome_msg = Label(welcome_frame, text="COUNTDOWN TIMER", font=("Lexend", 30, "bold"), bg=bg_color, fg=font_color)
welcome_msg.grid(column=0, row=0, pady=(0, 20))

start_btn = Button(welcome_frame, text="START", command=start_program, padx=28, pady=0, font=("Lexend", 12, "bold"), bg="#EDEDE9", fg="black")
start_btn.grid(column=0, row=1, pady=(10, 5))

exit_btn = Button(welcome_frame, text="EXIT", command=exit_program, padx=36, pady=0, font=("Lexend", 12, "bold"), bg="#EDEDE9", fg="black")
exit_btn.grid(column=0, row=2)

welcome_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Date picker frame for start date
date_picker_frame = Frame(ws, bg=bg_color)
start_cal = Calendar(date_picker_frame, selectmode="day", year=2024, month=5, day=1, font=("Lexend", 21), background='#EDEDE9', foreground='black')
start_cal.grid(column=0, row=0, padx=130, pady=(40, 0))

time_units_frame = Frame(date_picker_frame, bg=bg_color)
time_units_frame.grid(column=0, row=1)

units_display = Label(time_units_frame, text="HRS                                MINS                               SECS   ", font=("Lexend", 12, "bold"), bg=bg_color, fg=font_color)
units_display.grid(column=0, row=0, pady=(10, 0))

spinbox_frame = Frame(date_picker_frame, bg=bg_color)
spinbox_frame.grid(column=0, row=2)

# Clock boxes
hour_sb = Spinbox(spinbox_frame, from_=0, to=23, wrap=True, font=f, width=9, justify=CENTER, bg="#EDEDE9")
min_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg="#EDEDE9")
sec_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg="#EDEDE9")

hour_sb.grid(column=0, row=1, padx=3, pady=(0,5))
min_sb.grid(column=1, row=1, padx=3, pady=(0, 5))
sec_sb.grid(column=2, row=1, padx=3, pady=(0, 5))

confirm_start_btn = Button(date_picker_frame, text="CONFIRM", command=confirm_start_date, padx=0, pady=0, font=("Lexend", 12, "bold"), bg="#EDEDE9", fg="black")
confirm_start_btn.grid(column=0, row=3, pady=10)

# Date picker frame for end date
end_date_picker_frame = Frame(ws, bg=bg_color)
end_cal = Calendar(end_date_picker_frame, selectmode="day", year=2024, month=5, day=1, font=("Lexend", 21), background='#EDEDE9', foreground='black')
end_cal.grid(column=0, row=0, padx=130, pady=(40, 0))

time_units_frame = Frame(end_date_picker_frame, bg=bg_color)
time_units_frame.grid(column=0, row=1)

units_display = Label(time_units_frame, text="HRS                                MINS                               SECS   ", font=("Lexend", 12, "bold"), bg=bg_color, fg=font_color)
units_display.grid(column=0, row=0, pady=(10, 0))

spinbox_frame = Frame(end_date_picker_frame, bg=bg_color)
spinbox_frame.grid(column=0, row=2)

# Clock boxes
end_hour_sb = Spinbox(spinbox_frame, from_=0, to=23, wrap=True, font=f, width=9, justify=CENTER, bg="#EDEDE9")
end_min_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg="#EDEDE9")
end_sec_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg="#EDEDE9")

end_hour_sb.grid(column=0, row=1, padx=3, pady=(0, 5))
end_min_sb.grid(column=1, row=1, padx=3, pady=(0, 5))
end_sec_sb.grid(column=2, row=1, padx=3, pady=(0, 5))

# Calling function when date on tkcalendar is changed
end_hour_sb.bind('<Configure>', update_time_limits)
end_min_sb.bind('<Configure>', update_time_limits)
end_sec_sb.bind('<Configure>', update_time_limits)
end_cal.bind("<<CalendarSelected>>", update_time_limits)

confirm_end_btn = Button(end_date_picker_frame, text="CONFIRM", command=confirm_end_date, padx=0, pady=0, font=("Lexend", 12, "bold"), bg="#EDEDE9", fg="black")
confirm_end_btn.grid(column=0, row=3, pady=10)

# Result frame
result_frame = Frame(ws, bg=bg_color)
timer_display = Label(result_frame, text="", font=("Lexend", 25, "bold"), bg=bg_color, fg=font_color)
timer_display.grid(column=0, row=0, pady=(0, 20))

# Restart button in the result frame
restart_btn = Button(result_frame, text="RESTART", command=restart_program, padx=20, pady=0, font=("Lexend", 12, "bold"), bg="#EDEDE9", fg="black")
restart_btn.grid(column=0, row=0, pady=(10, 5))

# Exit button in the result frame
exit_timer_btn = Button(result_frame, text="EXIT", command=exit_program, padx=40, pady=0, font=("Lexend", 12, "bold"), bg="#EDEDE9", fg="black")
exit_timer_btn.grid(column=0, row=0)

# Start the Tkinter event loop
ws.mainloop()
