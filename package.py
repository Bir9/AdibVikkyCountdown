from time import sleep

daysInMonthDict = {
    "1": 31, "2": 28, "3": 31, "4": 30,
    "5": 31, "6": 30, "7": 31, "8": 31,
    "9": 30, "10": 31, "11": 30, "0": 31 #0 was used as the key as 12%12 = 0
}

def timeDifference(start, end):
    startDate = start[0].split('/') #Seperating the month, day and year into another list
    
    endDate = end[0].split('/') #Similar to code above but for end date
    
    global years, days, hours, minutes, seconds #making variable global so other functions can use them
    
    years = int(endDate[2]) - int(startDate[2]) #getting the difference in years between both dates
    months = int(endDate[0]) - int(startDate[0]) #getting the difference in months between both dates
    days = 0 #creating a days variable
    
    if years >= 0: #checking to see if the end date's year is after the start date's year
        if months < 0: #checking to see if the end date's month is before the start date's month
            if years > 0: #check to see if there's a year that can be carried over
                years -= 1
                months += 12
            else:
                return print("user input error")
    else:
        return print("user input error")
    
    #adds up all the days in every month between our start month and end month
    for i in range(months): #looping for however many months there are in between both dates
        j = i + int(startDate[0]) #assigning j to be our index i plus our starting month number (0 + Jan(1) => Jan(1), 1 + Jan(1) => Feb(2))
        days += daysInMonthDict[str(j%12)] #makes sure that even if j > 12 it can still be used as a key
    
    days += int(endDate[1]) - int(startDate[1]) #getting the difference in days between both dates and adding it to our pre-existing variable
    hours = int(end[1]) - int(start[1]) #getting the difference in hours between both dates
    minutes = int(end[2]) - int(start[2]) #getting the difference in minutes between both dates
    seconds = int(end[3]) - int(start[3]) #getting the difference in seconds between both dates
    
    #Similar to what we did for checking if our end date's month is before our start date's month we now do it for the days, hours, minutes, and seconds variables
    if days < 0:
        if years > 0:
            years -= 1
            days += 365
        else:
            return print("user input error")
    if hours < 0:
        if days > 0:
            days -= 1
            hours += 24
        else:
            return print("user input error")
    if minutes < 0:
        if hours > 0:
            hours -= 1
            minutes += 60
        else:
            return print("user input error")
    if seconds < 0:
        if minutes > 0:
            minutes -= 1
            seconds += 60
        else:
            return print("user input error")
    
    return years, days, hours, minutes, seconds

#keeps decreases the seconds by one if possible, otherwise we check if we can carry seconds over from minutes, hours, days and years
def timerDecreaser():
    global years, days, hours, minutes, seconds
    
    if seconds != 0:
        seconds -= 1
    else:
        if minutes != 0:
            minutes -= 1
            seconds = 59
        else:
            if hours!= 0:
                hours -= 1
                minutes = 59
                seconds = 59
            else:
                if days!= 0:
                    days -= 1
                    hours = 23
                    minutes = 59
                    seconds = 59
                else:
                    if years!= 0:
                        years -= 1
                        days = 365
                        hours = 23
                        minutes = 59
                        seconds = 59
                    else:
                        return print("user input error")
    return years, days, hours, minutes, seconds

def checkLeapYear(year):
    if year % 4 == 0: #checks if the year is divisble by 4
        if year % 400 == 0: #checks to wee if century years like 1700 or 1900 are leap years
            return True
        else:
            return False
    else:
        return False