monthDict = {
    "Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4,
    "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8,
    "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12
}

daysInMonthDict = {
    "1": 31, "2": 28, "3": 31, "4": 30,
    "5": 31, "6": 30, "7": 31, "8": 31,
    "9": 30, "10": 31, "11": 30, "0": 31 #0 was used as the key as 12%12 = 0
}

def timeDifference(start, end):
    startSplit = start.split(',')
    for i in range(len(startSplit)):
        startSplit[i] = startSplit[i].strip()
    startTime = startSplit[0].split(':')
    startDate = startSplit[1].split(' ')
    
    endSplit = end.split(',')
    for i in range(len(endSplit)):
        endSplit[i] = endSplit[i].strip()
    endTime = endSplit[0].split(':')
    endDate = endSplit[1].split(' ')
    
    years = int(endSplit[2]) - int(startSplit[2])
    months = monthDict[endDate[0]] - monthDict[startDate[0]]
    days = 0
    
    if years >= 0:
        if months < 0:
            if years > 0:
                years -= 1
                months += 12
            else:
                return print("user input error")
    else:
        return print("user input error")
            
    for i in range(months):
        j = i + monthDict[startDate[0]]
        days += daysInMonthDict[str(j%12)]
    
    days += int(endDate[1]) - int(startDate[1])
    hours = int(endTime[0]) - int(startTime[0])
    minutes = int(endTime[1]) - int(startTime[1])
    seconds = int(endTime[2]) - int(startTime[2])
    
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
    
    print(f"{years} years {days} days {hours} hours {minutes} minutes {seconds} seconds left")

timeDifference( "05:50:50, Nov 1, 2024", "18:01:30, Oct 16, 2025")

def checkLeapYear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return False