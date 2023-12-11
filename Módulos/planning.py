#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia
import infoFromFiles
import constants
import dateTime
import copy
doctors = infoFromFiles.sortDoctors("testSets_v2/testSets_v2/testSet1/doctors10h00.txt")
requests = infoFromFiles.sortMothers("testSets_v2/testSets_v2/testSet1/requests10h30.txt")
previousSched = infoFromFiles.readScheduleFile("testSets_v2/testSets_v2/testSet1/schedule10h00.txt")
HeaderHour = dateTime.getHeaderHour("testSets_v2/testSets_v2/testSet1/schedule10h00.txt")
def updateSchedule(doctors, requests, previousSched, nextSched):
		"""
		Update birth assistance schedule assigning the given birth assistance requested
		to the given doctors, taking into account a previous schedule.
		
		Requires:
		doctors is a list of lists with the structure as in the output of
		infoFromFiles.readDoctorsFile concerning the time of the previous schedule;
		requests is a list of lists with the structure as in the output of 
		infoFromFile.readRequestsFile concerning the current update time;
		previousSched is a list of lists with the structure as in the output of
		infoFromFiles.readScheduleFile concerning the previous update time;
		Ensures:
		a list of birth assistances, representing the schedule updated at
		the current update time (= previous update time + 30 minutes),
		assigned according to the conditions indicated in the general specification 
		of the project (omitted here for the sake of readability).
		"""
		nextSched = []

		Total_Minutes = dateTime.timeToMinutes(HeaderHour)
		
		copy_PreviouShed = copy.deepcopy(previousSched)
		copy_Doctors = copy.deepcopy(doctors)
		copy_Requests = copy.deepcopy(requests)


		for line in previousSched:               							           					#-------------------
			if dateTime.timeToMinutes(line[constants.SCHE_HOUR_IDX]) <= Total_Minutes: 		 			#This analyzes the  |
				copy_PreviouShed.remove(line)								    					 	#the list and takes |
		if copy_PreviouShed != []:																		#the the birth that |
			nextSched.append(copy_PreviouShed)															# will still happen |
		#return nextSched #ainda está a dar tripla lista												#-------------------
		exemplo = []
		for item in requests:
			for item2 in doctors:
				if item[constants.MOTH_RISK_IDX] == "high" and int(item2[constants.DOCT_EXP_IDX]) >= 2:
					exemplo.append(item)
					exemplo.append(item2)
		return exemplo
					
					

		
		
		
		
		#for line in :
    		#if line[constants.MOTH_RISK_IDX] == "high":
       			#for line2 in sorted_Doctors:
            	#if int(line2[constants.DOCT_EXP_IDX]) >= 2:
                	#Mother_Doctor = line[constants.MOTH_NAME_IDX], line2[constants.DOCT_NAME_IDX]
                	#season_finale1.append(Mother_Doctor)
		
	

print(updateSchedule(doctors, requests, previousSched, "vski"))	
        
        
	
	
	
	
	
	
	#for line in requests:
       # if line[constants.MOTH_RISK_IDX] == "high":
            #for line2 in doctors:
                #if line2[constants.DOCT_EXP_IDX]:
                    #both = line[constants.MOTH_NAME_IDX], line2[constants.DOCT_NAME_IDX]
                    #nextSched.append(both)
	
	
    
	
	
	
	
	#return nextSched





                	













