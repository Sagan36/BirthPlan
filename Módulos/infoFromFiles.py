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
    The enconding used in opening is utf-8
    Ensures: 
    Returns the lines of the file excluding the first 7 lines
    that contains the header.
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
    inFile = removeHeader(open(fileName,"r", encoding = "utf-8")) 
    
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

    inFile = removeHeader(open(fileName,"r", encoding = "utf-8"))       

    requestsList = [] 
    for line in inFile:
        if line.strip():
            requestData = line.rstrip().split(", ")
            requestsList.append(requestData)        

    return requestsList



def readScheduleFile(fileName): #tive que mudar isto pois eu so feio e tambem que eu precisava da hora do header e n sabia como o obtelo entao fiz assim
    """
    Reads a file with a list of the last schedule into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of previous schedule organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    Returns list of lists where each list corresponds to a scheduled parturition listed in
    the file fileName (with all the info pieces belonging to that parturition),
    following the order provided in the lines of the file.

    """

    inFile = removeHeader(open(fileName,"r", encoding = "utf-8"))
    HourLine = dateTime.getHeaderHour(fileName)       
    previousSched = [] 
    for line in inFile:
        if line.strip(): #Tipo isto ve se existe algum caraters na linha que esta a analisar e se existir faz o codigo abaixo se nao nao o faz, foi ao chat gpt pq a maneira que tinhas dito acho que n tava a funcionar mas tenta tu 
            scheduleData = line.rstrip().split(", ")# eu acho que este comando é inututil vai dar a mesma merda sem ele 
            previousSched.append(scheduleData)
    return previousSched

#print(readScheduleFile("testSets_v2/testSets_v2/testSet1/schedule10h00.txt"))

def sortMothers(sortedMoms): #Se calhar metemos isto a receber logo o sortedMoms?
    '''
    Sorts list of requests by service priority.

    Requires:
    FileName is the name of a non-empty .txt file of the pending requests
    organized as in the examples provided in the general specification 
    (omitted here for the sake of readability).
    Ensures:
    Returns list of requests sorted by Risk -> Urgency -> Age -> Name
    '''
    Color_Order = {"red":1, "yellow":2, "green":3}
    Risk_Order = {"high":1, "medium":2, "low":3}
    sortedMoms.sort(key=lambda mother: (Risk_Order[mother[constants.MOTH_RISK_IDX]], Color_Order[mother[constants.MOTH_COLOR_IDX]], \
                                        (-int(mother[constants.MOTH_AGE_IDX])), mother[constants.MOTH_NAME_IDX]))           
    return sortedMoms
    #-int é para fazer decresecnte



def sortDoctors(sorted_Doctors): #UPdate contrato
    '''
    Sorts list of doctors by service availability.

    Requires:
    FileName is the name of a non-empty .txt file of the available doctors
    organized as in the examples provided in the general specification 
    (omitted here for the sake of readability).
    Ensures:
    Returns list of doctors sorted by First- -> Experience -> Time-to-Break -> Name
    '''
    sorted_Doctors.sort(key=lambda doctor: (dateTime.timeToMinutes(doctor[constants.DOCT_LASTBIRTH_IDX]), (-int(doctor[constants.DOCT_EXP_IDX])), doctor[constants.DOCT_ACCUMULATOR_IDX], doctor[constants.DOCT_LASTREST_IDX], doctor[constants.DOCT_NAME_IDX]))

    return sorted_Doctors

def type_Header(fileName):
    '''
    '''

    inFile = open(fileName,"r", encoding = "utf-8")       

    allLines = inFile.readlines()

    FileType = allLines[constants.TYPE_HEADER] 
    
    FileType = FileType[:-2]
    inFile.close()

    return FileType

#print(type_Header("testSets_v2/testSets_v2/testSet1/doctors10h00.txt"))