#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia

import constants
import dateTime



def updateHeader(fileName):
    """
    Updates the hours of last modified hour in header of file.

    Requires:
    fileName is the name of a non-empty .txt file.
    Ensures:
    Adds 30 minutes to the hours in the header of the file and returns
    it as a str 
    """
    fp = open(fileName,"r", encoding = "utf-8")
    fileList = fp.readlines()
    header = fileList[:constants.NUM_HEADER_LINES]

    lastHour = header[constants.HOUR_LINE_IDX]

    newHour = dateTime.add30Minutes(lastHour)

    header[constants.HOUR_LINE_IDX] = newHour + "\n"

    headerStr = str()
    for i in header:
        headerStr += i
    
    fp.close()
    return headerStr



def updatedName(fileName):
    """
    Updates the hours to last modified hour in name of file.

    Requires:
    fileName is the name of a .txt file with a hour in the format HHhMM.
    Ensures:
    Adds 30 minutes to the hours in the name of the file and returns
    it as a str 
    """
    fp = open(fileName,"r", encoding = "utf-8")
    linesList = fp.readlines()

    lastHour = linesList[constants.HOUR_LINE_IDX]
    
    newHour = dateTime.add30Minutes(lastHour)

    newName = fileName[:constants.NAME_HOUR_CHAR] + newHour + ".txt"

    return newName



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
    schedStr=str()
    for scheduled in sched:
        for info in scheduled:
            
            if info !=  scheduled[constants.SCHE_HOUR_IDX]:
                schedStr += ", "
            schedStr = schedStr + j
        if  scheduled != sched[-1]:
            schedStr += "\n"

    allLines = header + schedStr
    fp = open(fileName,"w", encoding = "utf-8")
    fp.writelines(allLines)

    fp.close()



def writeDoctorsFile(doctors, header, fileName):
    """
    Writes a collection of informations of doctors into a file.

    Requires:
    doctors is a list with the structure as in the output of
    planning.updateDoctors representing the doctor's updated hours;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the informations of every available doctor,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the statistics as ordered head to tail in doctors.
    """
    docStr=str()
    for doctor in doctors:
        for info in doctor:
            
            if info != doctor[constants.DOCT_NAME_IDX]:
                docStr += ", "
            docStr = docStr + j
        if doctor != doctors[-1]:
            docStr += "\n"

    allLines = header + docStr
    fp = open(fileName,"w", encoding = "utf-8")
    fp.writelines(allLines)

    fp.close()