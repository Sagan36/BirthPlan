#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa


# if __name__ == "__main__":
#   import sys
#   plan(sys.argv[1],sys.argv[2],...)
#[refresh.py, arg1, arg2, etc...]

import constants
import dateTime
import infoFromFiles
import planning
import infoToFiles

def plan(doctorsFileName, scheduleFileName, requestsFileName):
    """
    Runs the birthPlan application.

    Requires:
    doctorsFileName is a str with the name of a .txt file containing a list
    of doctors at date d and time t, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of birth assistances assigned to doctors at date d and time t, as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested at date d and time t+30mins;
    Ensures:
    writing of two .txt files containing the updated list of doctors assigned
    to mothers and the updated list of birth assistances, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, doctorsXXhYY.txt and
    scheduleXXhYY.txt, where XXhYY represents the time 30 minutes
    after the time t indicated in the files doctorsFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """
    HeaderType_Doctors = infoFromFiles.type_Header(doctorsFileName)
    HeaderType_Requests =  infoFromFiles.type_Header(requestsFileName)
    HeaderType_Schedule = infoFromFiles.type_Header(scheduleFileName)

    if HeaderType_Doctors == doctorsFileName[0:6]:
       raise File_head_error("scope inconsistency between name and header in file doctorsFileName.")
    if HeaderType_Requests == requestsFileName[0:6]:
       raise File_head_error("scope inconsistency between name and header in file requestsFileName.")
    if HeaderType_Schedule == scheduleFileName[0:6]:
       raise File_head_error("scope inconsistency between name and header in file requestsFileName.")

         


    previousDoctors = infoFromFiles.readDoctorsFile(doctorsFileName)
    previousRequests = infoFromFiles.readRequestsFile(requestsFileName)
    previousSched = infoFromFiles.readScheduleFile(scheduleFileName)
    nextHour = dateTime.getHeaderHour(requestsFileName)
    

    previousDoctors_Sorted = infoFromFiles.sortDoctors(previousDoctors)
    previousRequests_Sorted = infoFromFiles.sortMothers(previousRequests)

    newSched = planning.updateSchedule(previousDoctors_Sorted, previousRequests_Sorted, previousSched, nextHour)
    #newDoctors = planning.updateDoctors()

    SchedHeader = infoToFiles.updateHeader(scheduleFileName)
    SchedName = infoToFiles.updatedName(scheduleFileName)

    infoToFiles.writeScheduleFile(newSched,SchedHeader, "testSets_v2/testSets_v2/testSet3/schedule16h00.txt")


plan("testSets_v2/testSets_v2/testSet3/doctors16h00.txt", "testSets_v2/testSets_v2/testSet3/schedule16h00.txt", "testSets_v2/testSets_v2/testSet3/requests16h30.txt")

if __name__ == "__main__":
  import sys
  plan(sys.argv[1],sys.argv[2],sys.argv[3])     

