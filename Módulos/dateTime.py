#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 75001 Maria Marisa

def hourToInt(time):
    """
    Converts the hours in time to an int
    Requires: time to be a str in the format HHhMM, where H is hours and M minutes
    Ensures: returns the HH as a int
    """
    t = time.split("h")
    return int(t[0])



def minutesToInt(time):
    """
    Converts the minutes in time to an int
    Requires: time to be a str in the format HHhMM, where H is hours and M minutes
    Ensures: returns the MM as a int
    """
    t = time.split("h")
    return int(t[1])
    


def intToTime(hour, minutes):
    """
    Converts the two int's given to a str in the format HHhMM, where H is hours and M minutes
    Requires: hour and minutes are int's, hour < 12 and minutes < 60 
    Ensures: a str in the format HHhMM
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + "h" + m


def timeToMinutes(time):
    """
    """
    hours = hourToInt(time)
    minutes = minutesToInt(time)

    totalMins = minutes + (hours * 60)

    return totalMins







