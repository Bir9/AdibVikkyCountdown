monthDict = {
    "Jan" : 1,
    "Feb" : 2,
    "Mar" : 3,
    "Apr" : 4,
    "May" : 5,
    "Jun" : 6,
    "Jul" : 7,
    "Aug" : 8,
    "Sep" : 9,
    "Oct" : 10,
    "Nov" : 11,
    "Dec" : 12
}

def timeDifference(start, end):
    timeDiff = []
    
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
    
    print(startSplit, startTime, startDate)
    print(endSplit, endTime, endDate)

timeDifference("09:52:14, Apr 04, 2022", "12:32:59, Jan 20, 2025")

def checkLeapYear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return False