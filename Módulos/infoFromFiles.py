#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia

#ERROS:
#meter ", encoding = "utf-8"  nos opens
#O QUE FIZ
#dei fix no erro mas ve se concordas antes de por em todas as funções
import constants
import dateTime

def removeHeader(fileOpen):
    '''
    Removes the lines of the header of the fileName
    
    Requires: 
    fileOpen to be a file pointer of an existing .txt file.
    Ensures: 
    Removes the header lines from the file, which corresponds to the first NUM_HEADER_LINES.
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
        if line.strip():
            doctorInfo = line.rstrip().split(", ")
            DoctorsList.append(doctorInfo)
    
    return DoctorsList     
    


def readRequestsFile(fileName):
    """
    Reads a file with a list of requests into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of pending requests organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a request listed in
    the file fileName (with all the info pieces belonging to that resquest),
    following the order provided in the lines of the file.
    """

    inFile = removeHeader(open(fileName,"r"))       

    requestsList = [] 
    for line in inFile:
        if line.strip():
            requestData = line.rstrip().split(", ")
            requestsList.append(requestData)        

    return requestsList



def readScheduleFile(fileName):
    """
    Reads a file with a list of the last schedule into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of previous schedule organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a scheduled parturition listed in
    the file fileName (with all the info pieces belonging to that parturition),
    following the order provided in the lines of the file.

    """

    inFile = removeHeader(open(fileName,"r"))       

    previousSched = [] 
    for line in inFile:
        if line.strip(): #Tipo isto ve se existe algum caraters na linha que esta a analisar e se existir faz o codigo abaixo se nao nao o faz, foi ao chat gpt pq a maneira que tinhas dito acho que n tava a funcionar mas tenta tu 
            scheduleData = line.rstrip().split(", ")# eu acho que este comando é inututil vai dar a mesma merda sem ele 
            previousSched.append(scheduleData)
    return previousSched



def sortMothers(fileName):
    '''
    Sorts Moms 
    '''
    sortedMoms = readRequestsFile(fileName)
    Color_Order = {"red":1, "yellow":2, "green":3}
    Risk_Order = {"high":1, "medium":2, "low":3}
    sortedMoms.sort(key=lambda mother: (Risk_Order[mother[constants.MOTH_RISK_IDX]], Color_Order[mother[constants.MOTH_COLOR_IDX]], (-int(mother[constants.MOTH_AGE_IDX])), mother[constants.MOTH_NAME_IDX]))           
    return sortedMoms
    #-int é para fazer decresecnte

def sortDoctors(fileName):
    '''
    Sorts Doctors 
    '''
    #num estado muito rudimentar ainda 
    sortedDoctors = readDoctorsFile(fileName)
    
    sortedDoctors.sort(key= lambda doctor: doctor[constants.DOCT_EXP_IDX])

    return sortedDoctors


#TESTES:
print(readDoctorsFile("./testSets_v2/testSets_v2/testSet1/doctors10h30.txt"))
print()

print(readRequestsFile("./testSets_v2/testSets_v2/testSet1/requests10h30.txt"))
print()

print(readScheduleFile("./testSets_v2/testSets_v2/testSet1/schedule10h00.txt"))
print("\nSorted:")
print(sortDoctors("./testSets_v2/testSets_v2/testSet1/doctors10h30.txt"))
print()

print(sortMothers("./testSets_v2/testSets_v2/testSet1/requests10h30.txt"))
