#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia

#ERROS:
#Quando lê as linhas do ficheiro, tbm lê as linhas vazias, o que resulta em ter listas do tipo [""] 
#O QUE FIZ
#dei fix no erro mas ve se concordas antes de por em todas as funções
import constants

def removeHeader(fileOpen):
    '''
    Removes the lines of the header of the fileName
    Requires: fileName to be a existing file in the same directory of the module
    Ensures: Removes the header lines from the file
    '''

    allLines = fileOpen.readlines()
    noHeaderLines = allLines[constants.NUM_HEADER_LINES:]
    
    fileOpen.close()

    return noHeaderLines


def readDoctorsFile(fileName):
    """
    Reads a file with a list of doctors into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of doctors organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a doctor listed in
    the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file.
    """
    inFile = removeHeader(open(fileName,"r")) 
    
    DoctorsList=[]
    for line in inFile:
        doctorInfo = line.rstrip().split(", ")
        DoctorsList.append(doctorInfo)
    
    return DoctorsList     
    


def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    """

    inFile = removeHeader(open(fileName,"r"))       

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList

def readScheduleFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    """

    inFile = removeHeader(open(fileName,"r"))       

    previousSched = [] 
    for line in inFile:
        if line.strip(): #Tipo isto ve se existe algum caraters na linha que esta a analisar e se existir faz o codigo abaixo se nao nao o faz, foi ao chat gpt pq a maneira que tinhas dito acho que n tava a funcionar mas tenta tu 
            scheduleData = line.rstrip().split(", ")# eu acho que este comando é inututil vai dar a mesma merda sem ele 
            previousSched.append(scheduleData)
    return previousSched

print(readDoctorsFile("./testSets_v2/testSets_v2/testSet1/doctors10h00.txt"))
