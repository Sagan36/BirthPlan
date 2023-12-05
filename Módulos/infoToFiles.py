#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia

import constants
import dateTime

def writeScheduleFile(sched, header, fileName):
    """
    Writes a collection of scheduled birth assistances into a file.

    Requires:
    sched is a list with the structure as in the output of
    planning.updateSchedule representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the birth assistances in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the assistances as ordered head to tail in sched.
    """



def writeDoctorsFile(doctors, header, fileName):
    """
    """


def updateHourHeader(fileOpen):
    """
    Updates the hours of last modified hour in header of file.

    Requires:
    fileOpen is a file pointer to a non-empty .txt file.
    Ensures:
    Adds 30 minutes to the hours in header of the file and returns the
    list of lines of header.
    """
    allLines = fileOpen.readlines()
    lastHour = allLines[constants.HOUR_LINE_IDX]
    minutes = dateTime.minutesToInt(lastHour)
    hours = dateTime.hourToInt(lastHour)

    if minutes == 30:
        hours += 1
        minutes = 0
        newHour = dateTime.intToTime(hours,minutes)
    else:
        minutes += 30
        newHour = dateTime.intToTime(hours,minutes)

    allLines[constants.HOUR_LINE_IDX] = newHour + "\n"
    
    fileOpen.close() 
    return allLines

#Testes
print(updateHourHeader(open("./testSets_v2/testSets_v2/testSet1/doctors10h00.txt","r")))
fp = open("teste.txt","w")
fp.writelines(updateHourHeader(open("./testSets_v2/testSets_v2/testSet1/doctors10h00.txt","r")))
fp.close()


    