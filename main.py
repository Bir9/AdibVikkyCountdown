from package import *
from tkinter import *
from time import sleep
from tkcalendar import Calendar
from datetime import datetime

# Initialize the main window
ws = Tk()
ws.title("Countdown Timer")
ws.geometry("850x550")
ws.minsize(850, 550)
ws.config(bg="#1B263B")
ws.resizable(width=1000, height=700)

# Fonts and colors
f = ('Lexend', 20)
font_color = "white"
bg_color = "#1B263B"
theme_color = "#EDEDE9"

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

# Update the calendar when the entry changes
def update_calendar_from_entry(entry, calendar):
    
    date_str = entry.get()
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        calendar.selection_set(date_obj)
    except ValueError:
        pass

# Update the entry when the calendar changes
def update_entry_from_calendar(entry, calendar):
    date_str = calendar.get_date()
    date_obj = datetime.strptime(date_str, "%m/%d/%y")
    date_obj = date_obj.strftime("%m/%d/%Y")  # Use %Y for four-digit year
    
    entry.delete(0, END)
    entry.insert(0, date_obj)
    
    start_date_entry.config(fg='black')
    end_date_entry.config(fg='black')

def focus_in_start(event):
    if start_date_entry.get() == "mm/dd/yyyy":
        start_date_entry.delete(0, 'end')
        start_date_entry.config(fg='black')

def focus_out_start(event):
    if start_date_entry.get() == "":
        start_date_entry.insert(0, "mm/dd/yyyy")
        start_date_entry.config(fg='grey')

def update_start_cal(event):
    try:
        date_str = start_date_entry.get()
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        start_cal.set_date(date_obj)
    except ValueError:
        pass  # Ignore invalid dates

def focus_in_end(event):
    if end_date_entry.get() == "mm/dd/yyyy":
        end_date_entry.delete(0, 'end')
        end_date_entry.config(fg='black')

def focus_out_end(event):
    if end_date_entry.get() == "":
        end_date_entry.insert(0, "mm/dd/yyyy")
        end_date_entry.config(fg='grey')

def update_end_cal(event):
    try:
        date_str = end_date_entry.get()
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        end_cal.set_date(date_obj)
    except ValueError:
        pass  # Ignore invalid dates

# Welcome frame
welcome_frame = Frame(ws, bg=bg_color)
welcome_msg = Label(welcome_frame, text="COUNTDOWN TIMER", font=("Lexend", 30, "bold"), bg=bg_color, fg=font_color)
welcome_msg.grid(column=0, row=0, pady=(0, 20))

start_btn = Button(welcome_frame, text="START", command=start_program, padx=28, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
start_btn.grid(column=0, row=1, pady=(10, 5))

exit_btn = Button(welcome_frame, text="EXIT", command=exit_program, padx=36, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
exit_btn.grid(column=0, row=2)

welcome_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Date picker frame for start date
date_picker_frame = Frame(ws, bg=bg_color)

# Calendar for start date
start_cal = Calendar(date_picker_frame, selectmode="day", font=("Lexend", 21), background=theme_color, foreground=bg_color, headersforeground=bg_color, selectbackground=bg_color)
start_cal.selection_set(datetime.now())
start_cal.grid(column=0, row=0, padx=130, pady=(12, 5))

# Entry for start date
start_date_entry = Entry(date_picker_frame, font=("Lexend", 21), bg=theme_color, justify=CENTER)
start_date_entry.grid(column=0, row=1, pady=(15, 5))

# Insert placeholder text
start_date_entry.insert(0, "mm/dd/yyyy")
start_date_entry.config(fg='grey')

time_units_frame = Frame(date_picker_frame, bg=bg_color)
time_units_frame.grid(column=0, row=2)

units_display = Label(time_units_frame, text="HRS                                MINS                               SECS   ", font=("Lexend", 12, "bold"), bg=bg_color, fg=font_color)
units_display.grid(column=0, row=0, pady=(10, 0))

spinbox_frame = Frame(date_picker_frame, bg=bg_color)
spinbox_frame.grid(column=0, row=3)

# Clock boxes
hour_sb = Spinbox(spinbox_frame, from_=0, to=23, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)
min_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)
sec_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)

hour_sb.grid(column=0, row=1, padx=3, pady=(0,5))
min_sb.grid(column=1, row=1, padx=3, pady=(0, 5))
sec_sb.grid(column=2, row=1, padx=3, pady=(0, 5))

confirm_start_btn = Button(date_picker_frame, text="CONFIRM", command=confirm_start_date, padx=0, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
confirm_start_btn.grid(column=0, row=4, pady=10)

# Calling functions based on inputs received
start_date_entry.bind("<FocusIn>", focus_in_start)
start_date_entry.bind("<FocusOut>", focus_out_start or update_start_cal)
start_date_entry.bind('<KeyRelease>', lambda event: update_calendar_from_entry(start_date_entry, start_cal))
start_cal.bind("<<CalendarSelected>>", lambda event: update_entry_from_calendar(start_date_entry, start_cal))

# Date picker frame for end date
end_date_picker_frame = Frame(ws, bg=bg_color)

# Calendar for end date
end_cal = Calendar(end_date_picker_frame, selectmode="day", font=("Lexend", 21), background=theme_color, foreground=bg_color, headersforeground=bg_color, selectbackground=bg_color)
end_cal.selection_set(datetime.now())
end_cal.grid(column=0, row=0, padx=130, pady=(12, 5))

# Entry for end date
end_date_entry = Entry(end_date_picker_frame, font=("Lexend", 21), bg=theme_color, justify=CENTER)
end_date_entry.grid(column=0, row=1, pady=(15, 5))

# Insert placeholder text
end_date_entry.insert(0, "mm/dd/yyyy")
end_date_entry.config(fg='grey')

time_units_frame = Frame(end_date_picker_frame, bg=bg_color)
time_units_frame.grid(column=0, row=2)

units_display = Label(time_units_frame, text="HRS                                MINS                               SECS   ", font=("Lexend", 12, "bold"), bg=bg_color, fg=font_color)
units_display.grid(column=0, row=0, pady=(10, 0))

spinbox_frame = Frame(end_date_picker_frame, bg=bg_color)
spinbox_frame.grid(column=0, row=3)

# Clock boxes
end_hour_sb = Spinbox(spinbox_frame, from_=0, to=23, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)
end_min_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)
end_sec_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)

end_hour_sb.grid(column=0, row=1, padx=3, pady=(0, 5))
end_min_sb.grid(column=1, row=1, padx=3, pady=(0, 5))
end_sec_sb.grid(column=2, row=1, padx=3, pady=(0, 5))

# Calling function when date on tkcalendar is changed
end_hour_sb.bind('<Configure>', update_time_limits)
end_min_sb.bind('<Configure>', update_time_limits)
end_sec_sb.bind('<Configure>', update_time_limits)
end_cal.bind("<<CalendarSelected>>", update_time_limits)

confirm_end_btn = Button(end_date_picker_frame, text="CONFIRM", command=confirm_end_date, padx=0, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
confirm_end_btn.grid(column=0, row=4, pady=10)

# Bind the end entry and calendar to synchronize
end_date_entry.bind("<FocusIn>", focus_in_end)
end_date_entry.bind("<FocusOut>", focus_out_end or update_end_cal)
end_date_entry.bind('<KeyRelease>', lambda event: update_calendar_from_entry(end_date_entry, end_cal))
end_cal.bind("<<CalendarSelected>>", lambda event: update_entry_from_calendar(end_date_entry, end_cal))

# Result frame
result_frame = Frame(ws, bg=bg_color)
timer_display = Label(result_frame, text="", font=("Lexend", 25, "bold"), bg=bg_color, fg=font_color)
timer_display.grid(column=0, row=0, pady=(0, 20))

# Restart button in the result frame
restart_btn = Button(result_frame, text="RESTART", command=restart_program, padx=20, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
restart_btn.grid(column=0, row=0, pady=(10, 5))

# Exit button in the result frame
exit_timer_btn = Button(result_frame, text="EXIT", command=exit_program, padx=40, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
exit_timer_btn.grid(column=0, row=0)

# Start the Tkinter event loop
ws.mainloop()