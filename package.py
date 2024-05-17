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

def timeSplit(time):
    fullSplit = time.split(',')
    chronoSplit = fullSplit[0].split(':')
    dateSplit = fullSplit[1].split(' ')

def checkLeapYear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return False