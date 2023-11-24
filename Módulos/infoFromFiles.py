#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 75001 Maria Marisa

def removeHeader(fileName):
    '''
    Removes the lines of the header of the fileName
    Requires: fileName to be a existing file in the same directory of the module
    Ensures: Removes the header lines from the file
    '''

    inFile = open(fileName, 'r')
    outFile = open(fileName, 'w')

    allLines = inFile.readlines()
    noHeaderLines = allLines[7:]

    outFile.writelines(noHeaderLines)

    outFile.close()
    inFile.close()

teste = removeHeader('doctors10h00-Copy.txt')
print(teste.read())

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



def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    
    """

    inFile = removeHeader(open(fileName, "r"))       

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList


