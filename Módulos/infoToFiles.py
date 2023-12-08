#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia

import constants
import dateTime
import infoFromFiles as iF #PARA TESTAR, RETIRAR DPS!!



def updateHeader(fileName):
    """
    Updates the hours of last modified hour in header of file.

    Requires:
    fileName is the name of a  non-empty .txt file.
    Ensures:
    Adds 30 minutes to the hours in the header of the file and returns
    it in a str 
    Returns the calculated new hour in str.
    """
    fp = open(fileName,"r")
    fileList = fp.readlines()
    header = fileList[:constants.NUM_HEADER_LINES]

    lastHour = header[constants.HOUR_LINE_IDX]
    minutes = dateTime.minutesToInt(lastHour)
    hours = dateTime.hourToInt(lastHour)

    if minutes == 30:
        hours += 1
        minutes = 0
        newHour = dateTime.intToTime(hours,minutes)
    else:
        minutes += 30
        newHour = dateTime.intToTime(hours,minutes)

    header[constants.HOUR_LINE_IDX] = newHour + "\n"

    headerStr = str()
    for i in header:
        headerStr += i
    
    fp.close()
    return headerStr, newHour



def updatedName(fileName):
    """
    """
    newHour = updateHeader(fileName)[1]


# print(iF.readDoctorsFile("./testSets_v2/testSets_v2/testSet3/doctors16h00.txt"))
# print(iF.readRequestsFile("./testSets_v2/testSets_v2/testSet2/requests14h30.txt"))
# print(iF.readScheduleFile("./testSets_v2/testSets_v2/testSet2/schedule14h30.txt"))


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
    for i in sched:
        for j in i:
            
            if j != i[0]:
                schedStr += ", "
            schedStr = schedStr + j
            
        schedStr += "\n"

    allLines = header + schedStr
    fp = open(fileName,"w")
    fp.writelines(allLines)

    fp.close()



def writeDoctorsFile(doctors, header, fileName):
    """
    Writes a collection of informations of doctors into a file.
    #Escrever o resto com o planning feito
    """
    docStr=str()
    for i in doctors:
        for j in i:
            
            if j != i[0]:
                docStr += ", "
            docStr = docStr + j
            
        docStr += "\n"

    allLines = header + docStr
    fp = open(fileName,"w")
    fp.writelines(allLines)

    fp.close()


#Testes
# print(updateHourHeader(open("./testSets_v2/testSets_v2/testSet1/doctors10h00.txt","r")))
# fp = open("teste.txt","w")
# fp.writelines(updateHourHeader(open("./testSets_v2/testSets_v2/testSet1/doctors10h00.txt","r")))
# fp.close()

x = updateHeader("./testSets_v2/testSets_v2/testSet2/schedule14h00.txt")
writeScheduleFile([['14h30', 'GraÃ§a GonÃ§alves', 'HorÃ¡cio Horta'], ['14h30', 'HortÃªnsia Holmes', 'JosÃ© Justo'],\
                ['14h30', 'Irene IlÃ\xaddio', 'Guilherme Gaspar'], ['14h30', 'Joana Joanes', 'Ildefonso InÃ¡cio']],x,"teste.txt")

x = updateHeader("./testSets_v2/testSets_v2/testSet2/doctors14h00.txt")
writeScheduleFile([['Manuel Machado', '3', '16h30', '120', '39h40'], ['Orlando Oliveira', '3', '16h40', '80', '39h20']],x,"teste.txt")
    