#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia

import constants
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
    


def intToTime(hour, minutes, add0 = True):
    """
    Converts the two int's given to a str in the format HHhMM, where H is hours and M minutes
    Requires: hour and minutes are int's, hour < 12 and minutes < 60 
    Ensures: a str in the format HHhMM
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
    """
    if time == "weekly leave":
        totalMins = 9999 #pass?
    else:
        hours = hourToInt(time)
        minutes = minutesToInt(time)
        totalMins = minutes + (hours * 60)
    
    return totalMins

def minutesToTime(minutes, add0 = True):
    '''
    '''
    hours = minutes // 60
    minutes -
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    = hours*60
    return intToTime(hours, minutes, add0)


#print(minutesToTime())

#print(intToTime())


def getHeaderHour(fileName):
    '''
    '''

    HourLine = fileName[constants.NAME_HOUR_CHAR:-4]
    
    #hours = hourToInt(HourLine)
    #minute = minutesToInt(HourLine)

    #final = intToTime(hours,minute)
    return HourLine


#print(getHeaderHour("testSets_v2/testSets_v2/testSet1/doctors10h00.txt"))

def add30Minutes(lastHour):
    """
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