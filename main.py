from package import *
from tkinter import *
from time import sleep
from tkcalendar import Calendar
from datetime import datetime

# venv activation bash: source $HOME/.venvs/MyEnv/activate

# Initialize the main window
ws = Tk()
ws.title("Countdown Timer")
ws.geometry("850x550")
ws.minsize(850, 550)
ws.config(bg="#1B263B")

# Fonts and colors
f = ('Lexend', 20)
font_color = "white"
bg_color = "#1B263B"
theme_color = "#EDEDE9"

# Variable to stop countdown timer once user click restart button
stop_timer = False

# Function to switch to the main program
def start_program():
    welcome_frame.place_forget()
    date_picker_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def restart_program():
    # Stop the countdown timer
    stop_countdown_timer(True)
    
    # Reset calendar selections
    start_cal.selection_set(datetime.now())
    end_cal.selection_set(datetime.now())
    
    # Reset date box
    start_date_entry.delete(0, 'end')
    start_date_entry.insert(0, "mm/dd/yyyy")
    start_date_entry.config(fg='grey')
    
    end_date_entry.delete(0, 'end')
    end_date_entry.insert(0, "mm/dd/yyyy")
    end_date_entry.config(fg='grey')

    # Resetting spinbox values to 0
    hour_sb.delete(0, 'end')
    hour_sb.insert(0, '0')
    min_sb.delete(0, 'end')
    min_sb.insert(0, '0')
    sec_sb.delete(0, 'end')
    sec_sb.insert(0, '0')
    end_hour_sb.delete(0, 'end')
    end_hour_sb.insert(0, '0')
    end_min_sb.delete(0, 'end')
    end_min_sb.insert(0, '0')
    end_sec_sb.delete(0, 'end')
    end_sec_sb.insert(0, '0')
    
    # Hide result frame
    result_frame.place_forget()
    
    # Re-show date picker frame
    date_picker_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Function to stop the countdown timer when called
def stop_countdown_timer(status):
    global stop_timer
    stop_timer = status
    
# Function to handle invalid dates
def handle_invalid_date(entry, button):
    # Reset date box
    entry.delete(0, 'end')
    entry.insert(0, "mm/dd/yyyy")
    entry.config(fg='grey')
    
    # Flash the button red
    original_color = button.cget("bg")
    button.config(bg='red')
    ws.after(500, lambda: button.config(bg=original_color))

# Function to check for invalid date
def check_for_invalid_date(entry, cal, btn, start_end):
    date_str = entry.get() # Assign test inside date box to variable
    try: # Try to use the given user input
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        cal.selection_set(date_obj)
        # Check if the date is valid and after the start date
        if start_end == "end":
            if date_obj < start_date_obj:
                handle_invalid_date(entry, btn)
                return False
            else:
                cal.selection_set(date_obj)
                return True
        
    except ValueError: # If user input outputs error, call error processing function
        handle_invalid_date(entry, btn)
        return False

# Function to exit the program
def exit_program():
    stop_countdown_timer(True)
    ws.destroy()

# Function to make datetime object able to be parsed by tkcalendar
def date_str_replace(cal):
    date_str = cal.get_date()
    date_str = date_str.replace("-", "/")
    return date_str

# Function to confirm the start date and switch to end date selection
def confirm_start_date():
    global start_date_obj
    
    # Check to see if date is valid
    if check_for_invalid_date(start_date_entry, start_cal, confirm_start_btn, "start") == False:
        return
    
    # Making start_cal output parsable by datetime
    date_str = date_str_replace(start_cal)
    
    # Retrieving the value of the spinboxes
    h = hour_sb.get()
    m = min_sb.get()
    s = sec_sb.get()

    # Converting the format to be parsable
    start_date_obj = datetime.strptime(f"{date_str} {h}:{m}:{s}", "%m/%d/%Y %H:%M:%S")

    # Disable dates before start date in the end date calendar
    end_cal.config(mindate=start_date_obj.date())
    
    # Re-setting entry text color
    end_date_entry.config(fg='grey')
    
    # Removing start date selector and moving on to end date selector
    date_picker_frame.place_forget()
    end_date_picker_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Function to validate the end date and start the countdown timer
def confirm_end_date():
    global end_date_obj
    
    # Checking to see if end date is valid
    if check_for_invalid_date(end_date_entry, end_cal, confirm_end_btn, "end") == False:
        return

    # Making end_cal output parsable by datetime
    date_str = date_str_replace(end_cal)
    
    # Retrieving the value of the spinboxes
    h = end_hour_sb.get()
    m = end_min_sb.get()
    s = end_sec_sb.get()

    # Adapt the format to handle the two-digit year correctly
    end_date_obj = datetime.strptime(f"{date_str} {h}:{m}:{s}", "%m/%d/%Y %H:%M:%S")

    # Removing end date selector and moving on to result frame
    end_date_picker_frame.place_forget()
    result_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    # Start the countdown timer
    start_countdown_timer()

# Function to display and update the timer
def start_countdown_timer():
    global start_date_obj, end_date_obj, stop_timer
    
    # Making sure stop function is False(off)
    stop_countdown_timer(False)
    
    # Getting the difference between both dates
    years, days, hours, minutes, seconds = time_difference(start_date_obj, end_date_obj)

    while seconds != -1 and stop_timer == False:  # Keep running the loop until there are 0 seconds left and stop function is False
        if start_date_obj == end_date_obj:
            # If start and end dates are equal, keep the timer variables at 0
            years, days, hours, minutes, seconds = 0, 0, 0, 0, 0
        else:
            # Otherwise, decrement the timer variables
            years, days, hours, minutes, seconds, end_date_obj = timer_decreaser(start_date_obj, end_date_obj)  # Re-assigning the counter after decreasing it by 1 second

        # Display the timer
        time_str = f"{years} years {days} days {hours} hours {minutes} minutes {seconds} seconds"
        timer_display.config(text=time_str)
        timer_display.grid(column=0, row=0)
        
        # Displaying buttons
        restart_btn.grid(column=0, row=1)
        exit_timer_btn.grid(column=0, row=2)

        # Updating window
        ws.update()
        
        # Waiting for one second so time doesn't decrease instantaneously
        sleep(1)

# Update the time limits for the end date
def update_time_limits(*args):
    end_date_str = date_str_replace(end_cal)
    end_date_time = datetime.strptime(end_date_str, "%m/%d/%Y")
    
    if end_date_time.date() == start_date_obj.date(): # If end date and start date are the same
        end_hour_sb.config(from_=int(start_date_obj.hour), to=23) # Making end date hour minimum equal to the start date hours
        end_min_sb.config(from_=int(start_date_obj.minute), to=59) # Making end date minute minimum equal to the start date minutes
        end_sec_sb.config(from_=int(start_date_obj.second), to=59) # Making end date second minimum equal to the start date seconds
    else:
        # Resetting spinbox minimum and maximum values
        end_hour_sb.config(from_=0, to=23)
        end_min_sb.config(from_=0, to=59)
        end_sec_sb.config(from_=0, to=59)
        
        # Resetting the spinbox values to 0
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
    date_str = date_str_replace(calendar)
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    date_obj = date_obj.strftime("%m/%d/%Y")
    
    entry.delete(0, END)
    entry.insert(0, date_obj)
    
    start_date_entry.config(fg='black')
    end_date_entry.config(fg='black')

# Function called when user clicks into start date box
def focus_in_start(event):
    if start_date_entry.get() == "mm/dd/yyyy":
        start_date_entry.delete(0, 'end')
        start_date_entry.config(fg='black')

# Function called when user clicks out of start date box
def focus_out_start(event):
    if start_date_entry.get() == "":
        start_date_entry.insert(0, "mm/dd/yyyy")
        start_date_entry.config(fg='grey')

# Function called when user clicks into end date box
def focus_in_end(event):
    if end_date_entry.get() == "mm/dd/yyyy":
        end_date_entry.delete(0, 'end')
        end_date_entry.config(fg='black')

# Function called when user clicks out of end date box
def focus_out_end(event):
    if end_date_entry.get() == "":
        end_date_entry.insert(0, "mm/dd/yyyy")
        end_date_entry.config(fg='grey')
        
def combined_end_cal_handler(event):
    update_entry_from_calendar(end_date_entry, end_cal)
    update_time_limits()

# Creating welcome frame
welcome_frame = Frame(ws, bg=bg_color)

# Creating header
welcome_msg = Label(welcome_frame, text="COUNTDOWN TIMER", font=("Lexend", 30, "bold"), bg=bg_color, fg=font_color)
welcome_msg.grid(column=0, row=0, pady=(0, 20))

# Creating start button + making it call start_program function when clicked
start_btn = Button(welcome_frame, text="START", command=start_program, padx=28, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
start_btn.grid(column=0, row=1, pady=(10, 5))

# Creating end button + making it call exit_program function when clicked
exit_btn = Button(welcome_frame, text="EXIT", command=exit_program, padx=36, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
exit_btn.grid(column=0, row=2)

# Showing welcome frame on window
welcome_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Date picker frame for start date
date_picker_frame = Frame(ws, bg=bg_color)

# Calendar for start date
start_cal = Calendar(date_picker_frame, selectmode="day", font=("Lexend", 21), date_pattern="mm-dd-yyyy", background=theme_color, foreground=bg_color, headersforeground=bg_color, selectbackground=bg_color)
start_cal.selection_set(datetime.now())
start_cal.grid(column=0, row=0, padx=130, pady=(12, 5))

# Entry for start date
start_date_entry = Entry(date_picker_frame, font=("Lexend", 21), bg=theme_color, justify=CENTER)
start_date_entry.grid(column=0, row=1, pady=(15, 5))

# Inserting placeholder text
start_date_entry.insert(0, "mm/dd/yyyy")
start_date_entry.config(fg='grey')

# Time units label
units_display = Label(date_picker_frame, text="HRS                                MINS                               SECS   ", font=("Lexend", 12, "bold"), bg=bg_color, fg=font_color)
units_display.grid(column=0, row=2, pady=(10, 0))

# Frame to hold all 3 spinboxes
spinbox_frame = Frame(date_picker_frame, bg=bg_color)
spinbox_frame.grid(column=0, row=3)

# Creating start date spinboxes
hour_sb = Spinbox(spinbox_frame, from_=0, to=23, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)
min_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)
sec_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)

# Placing spinboxes on spinbox_frame frame
hour_sb.grid(column=0, row=1, padx=3, pady=(0,5))
min_sb.grid(column=1, row=1, padx=3, pady=(0, 5))
sec_sb.grid(column=2, row=1, padx=3, pady=(0, 5))

# Creating confirm button for start date + making it call confirm_start_date function when clicked
confirm_start_btn = Button(date_picker_frame, text="CONFIRM", command=confirm_start_date, padx=0, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
confirm_start_btn.grid(column=0, row=4, pady=10)

# Calling functions based on user inputs received
start_date_entry.bind("<FocusIn>", focus_in_start)
start_date_entry.bind("<FocusOut>", focus_out_start)
start_date_entry.bind('<KeyRelease>', lambda event: update_calendar_from_entry(start_date_entry, start_cal))
start_cal.bind("<<CalendarSelected>>", lambda event: update_entry_from_calendar(start_date_entry, start_cal))

# Date picker frame for end date
end_date_picker_frame = Frame(ws, bg=bg_color)

# Calendar for end date
end_cal = Calendar(end_date_picker_frame, selectmode="day", font=("Lexend", 21), date_pattern="mm-dd-yyyy", background=theme_color, foreground=bg_color, headersforeground=bg_color, selectbackground=bg_color)
end_cal.selection_set(datetime.now())
end_cal.grid(column=0, row=0, padx=130, pady=(12, 5))

# Entry for end date
end_date_entry = Entry(end_date_picker_frame, font=("Lexend", 21), bg=theme_color, justify=CENTER)
end_date_entry.grid(column=0, row=1, pady=(15, 5))

# Inserting placeholder text
end_date_entry.insert(0, "mm/dd/yyyy")
end_date_entry.config(fg='grey')

# Time units label
units_display = Label(end_date_picker_frame, text="HRS                                MINS                               SECS   ", font=("Lexend", 12, "bold"), bg=bg_color, fg=font_color)
units_display.grid(column=0, row=2, pady=(10, 0))

# Frame to hold all 3 spinboxes
spinbox_frame = Frame(end_date_picker_frame, bg=bg_color)
spinbox_frame.grid(column=0, row=3)

# Creating end date spinboxes
end_hour_sb = Spinbox(spinbox_frame, from_=0, to=23, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)
end_min_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)
end_sec_sb = Spinbox(spinbox_frame, from_=0, to=59, wrap=True, font=f, width=9, justify=CENTER, bg=theme_color)

# Placing spinboxes on spinbox_frame frame
end_hour_sb.grid(column=0, row=1, padx=3, pady=(0, 5))
end_min_sb.grid(column=1, row=1, padx=3, pady=(0, 5))
end_sec_sb.grid(column=2, row=1, padx=3, pady=(0, 5))

# Calling function when date on tkcalendar is changed
end_hour_sb.bind('<Configure>', update_time_limits)
end_min_sb.bind('<Configure>', update_time_limits)
end_sec_sb.bind('<Configure>', update_time_limits)
end_cal.bind("<<CalendarSelected>>", combined_end_cal_handler)

# Creating confirm button for end date + making it call confirm_end_date function when clicked
confirm_end_btn = Button(end_date_picker_frame, text="CONFIRM", command=confirm_end_date, padx=0, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
confirm_end_btn.grid(column=0, row=4, pady=10)

# Bind the end entry and calendar to synchronize
end_date_entry.bind("<FocusIn>", focus_in_end)
end_date_entry.bind("<FocusOut>", focus_out_end)
end_date_entry.bind('<KeyRelease>', lambda event: update_calendar_from_entry(end_date_entry, end_cal))

# Creating result frame
result_frame = Frame(ws, bg=bg_color)
timer_display = Label(result_frame, text="", font=("Lexend", 25, "bold"), bg=bg_color, fg=font_color)
timer_display.grid(column=0, row=0, pady=(0, 20))

# Creating restart button + making it call restart_program function when clicked
restart_btn = Button(result_frame, text="RESTART", command=restart_program, padx=20, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
restart_btn.grid(column=0, row=0, pady=(10, 5))

# Creating exit button + making it call exit_program function when clicked
exit_timer_btn = Button(result_frame, text="EXIT", command=exit_program, padx=40, pady=0, font=("Lexend", 12, "bold"), bg=theme_color, fg="black")
exit_timer_btn.grid(column=0, row=0)

# Start the Tkinter event loop
ws.mainloop()