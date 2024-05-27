from datetime import timedelta

# Function to calculate the difference between two dates
def time_difference(start, end):
    global years, days, hours, minutes, seconds # Making variables global so other functions can use them
    
    delta = end - start
    leap_days = count_leap_years(start.year, end.year)
    
    years = delta.days // 365
    remaining_days = delta.days % 365
    
    # Loop until the remaining days is less than the number of days in a year
    while True:
        # Check if the current year is a leap year
        if check_leap_year(start.year + years):
            # If it is a leap year, check if the remaining days is greater than or equal to 366
            if remaining_days >= 366:
                # If it is, subtract 366 from the remaining days
                remaining_days -= 366
            else:
                # If it's not, break the loop
                break
        else:
            # If it's not a leap year, check if the remaining days is greater than or equal to 365
            if remaining_days >= 365:
                # If it is, subtract 365 from the remaining days
                remaining_days -= 365
            else:
                # If it's not, break the loop
                break
        # Increment the number of years
        years += 1
    
    total_seconds = delta.seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return years, remaining_days, hours, minutes, seconds

# Decreases the seconds by one if possible, otherwise we check if we can carry seconds over from minutes, hours, days and years
def timer_decreaser(start, end):
    # Decrease the end time by one second
    end -= timedelta(seconds=1)
    
    # Calculate the new time difference
    years, days, hours, minutes, seconds = time_difference(start, end)
    
    return years, days, hours, minutes, seconds, end

def check_leap_year(year):
    if year % 4 == 0: # Checks if the year is divisble by 4
        if year % 100 == 0:
            if year % 400 == 0: # Checks to wee if century years like 1700 or 1900 are leap years
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def count_leap_years(start_year, end_year):
    leap_days = 0
    for year in range(start_year, end_year):
        if check_leap_year(year):
            leap_days += 1
    return leap_days