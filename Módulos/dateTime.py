#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia


import constants



def hourToInt(time):
    """
    Converts the hours in time to an int.

    Requires: 
    Time to be a str in the format HHhMM, where H is hours and M minutes.
    Ensures: 
    Returns the HH as a int.
    """
    t = time.split("h")

    return int(t[0])



def minutesToInt(time):
    """
    Converts the minutes in time to an int.

    Requires: 
    Time to be a str in the format HHhMM, where H is hours and M minutes.
    Ensures: 
    Returns the MM as a int.
    """
    t = time.split("h")

    return int(t[1])
    


def intToTime(hour, minutes, add0 = True):
    """
    Converts the two int's given to a str in the format HHhMM, where H is hours and M minutes;
    If add0 = false there won't be added an extra 0 when HH < 10.

    Requires: 
    Hour and minutes are int's, hour =< 24 and minutes =< 60.
    Ensures: 
    Returns str in the format HHhMM.
    """
    h = str(hour)
    m = str(minutes)

    if add0:
        if hour < 10:
            h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + "h" + m



def timeToMinutes(time):
    """
    Converts the time to an int with the total minutes.

    Requires: 
    Time to be a str in the format HHhMM, where H is hours and M minutes.
    Ensures: 
    Returns the total minutes in time.
    """
    if time == "weekly leave":
        totalMins = 9999 

    else:
        hours = hourToInt(time)
        minutes = minutesToInt(time)
        totalMins = minutes + (hours * 60)
    
    return totalMins



def minutesToTime(minutes, add0 = True):
    '''
    Converts the int of total minutes to a time str in the format HHhMM;
    If add0 = false there won't be added an extra 0 when HH < 10.

    Requires: 
    Minutes to be the total minutes on desired HHhMM time.
    Ensures: 
    Time in the format HHhMM where HH are the hours and MM the minutes.
    '''
    hours = minutes // 60
    minutes -= hours*60

    return intToTime(hours, minutes, add0)



def getHeaderHour(fileName):
    '''
    Gets the hour on fileName header.

    Requires:
    fileName is str with the name of a .txt file.
    Ensures:
    Returns str with hour in header of fileName.
    '''
    hourLine = fileName[constants.NAME_HOUR_CHAR:-4]

    return hourLine




def add30Minutes(lastHour):
    """
    Add 30 minutes to given hour in the format HHhMM.

    Requires:
    lastHour to be a str in the format HHhMM, where H is hours and M minutes.
    Ensures:
    Returns lastHour with an increment of 30 minutes.
    """
    minutes = minutesToInt(lastHour)
    hours = hourToInt(lastHour)

    if minutes == 30:
        hours += 1
        minutes = 0
        newHour = intToTime(hours,minutes)
    else:
        minutes += 30
        newHour = intToTime(hours,minutes)
        
    return newHour