#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa


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

    headerType_Doctors = infoFromFiles.type_Header(doctorsFileName)
    headerType_Requests =  infoFromFiles.type_Header(requestsFileName)
    headerType_Schedule = infoFromFiles.type_Header(scheduleFileName)


    if headerType_Doctors.lower() != "doctors":
      message = "File head error: scope inconsistency between name and header in file " + doctorsFileName + "."
      raise IOError(message)
    
    if headerType_Requests.lower() != "mothers":
      message = "File head error: scope inconsistency between name and header in file " + requestsFileName + "."
      raise IOError(message)
    
    if headerType_Schedule.lower() != "schedule":
      message = "File head error: scope inconsistency between name and header in file " + scheduleFileName + "."
      raise IOError(message)

         


    previousDoctors = infoFromFiles.readDoctorsFile(doctorsFileName)
    previousRequests = infoFromFiles.readRequestsFile(requestsFileName)
    previousSched = infoFromFiles.readScheduleFile(scheduleFileName)
    nextHour = dateTime.getHeaderHour(requestsFileName)
    

    previousDoctors_Sorted = infoFromFiles.sortDoctors(previousDoctors)
    previousRequests_Sorted = infoFromFiles.sortMothers(previousRequests)

    newSched, newDocs = planning.updateofFiles(previousDoctors_Sorted, previousRequests_Sorted, previousSched, nextHour)

    schedHeader = infoToFiles.updateHeader(scheduleFileName)
    schedName = infoToFiles.updatedName(scheduleFileName)

    docsHeader = infoToFiles.updateHeader(doctorsFileName)
    docsName = infoToFiles.updatedName(doctorsFileName)

    
    infoToFiles.writeScheduleFile(newSched,schedHeader, schedName)
    infoToFiles.writeDoctorsFile(newDocs,docsHeader, docsName)


# if __name__ == "__main__":
#    import sys
#    plan(sys.argv[1],sys.argv[2],sys.argv[3])     

plan("testSets_v2/testSets_v2/testSet1/doctors10h00.txt", "testSets_v2/testSets_v2/testSet1/schedule10h00.txt", "testSets_v2/testSets_v2/testSet1/requests10h30.txt")
plan("testSets_v2/testSets_v2/testSet2/doctors14h00.txt", "testSets_v2/testSets_v2/testSet2/schedule14h00.txt", "testSets_v2/testSets_v2/testSet2/requests14h30.txt")
plan("testSets_v2/testSets_v2/testSet3/doctors16h00.txt", "testSets_v2/testSets_v2/testSet3/schedule16h00.txt", "testSets_v2/testSets_v2/testSet3/requests16h30.txt")
plan("testSets_v2/testSets_v2/testSet4/doctors18h00.txt", "testSets_v2/testSets_v2/testSet4/schedule18h00.txt", "testSets_v2/testSets_v2/testSet4/requests18h30.txt")