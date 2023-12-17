#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia


import infoFromFiles
import constants
import dateTime
import copy



def add20Minutes(doctor, doctorsList, docsOnBreak):
	"""
	Increments 20 minutes on all the times of the doctor.

	Requires:
	doctor is a list containing all the infos of the doctor;
	doctorsList is a list of list of all the infos of the doctors;
	docsOnBreak is a list of all the doctors on weekly leave.
	Ensures:
	Add 20 minutes to all the times of the doctor and returns
	the updated docsOnBreak list. 
	"""
	lastAssis = doctor[constants.DOCT_LASTBIRTH_IDX ]
	dayBreak = int(doctor[constants.DOCT_ACCUMULATOR_IDX])
	weekBreak = doctor[4]
	

	#Add 20 minutes to the hours of the last birth plus 1 hour in case of rest
	minutes = dateTime.timeToMinutes(lastAssis)
	minutes += 20
	dayBreak += 20
	if dayBreak >= 240 and dayBreak < 260:
		minutes += 60
	doctor[constants.DOCT_ACCUMULATOR_IDX] = str(dayBreak)
	doctor[constants.DOCT_LASTBIRTH_IDX] = dateTime.minutesToTime(minutes)


	#Add 20 minutes to the hours of the last break.
	minutes = dateTime.timeToMinutes(weekBreak)
	minutes += 20
	if minutes >= 2400:
		doctor[constants.DOCT_LASTBIRTH_IDX] = constants.WKL_LEAVE
		docsOnBreak.append(doctorsList.pop(doctorsList.index(doctor)))
	
	doctor[constants.DOCT_LASTREST_IDX] = dateTime.minutesToTime(minutes, False)

	return docsOnBreak



def updateofFiles(doctors, requests, previousSched, nextTime):
	"""
	Update all files assigning the given birth assistance requested
    to the given doctors in the nextShedule,taking into account a previous schedule,
	and updates the doctors file.
	
	Requires:
	doctors is a list of lists with the structure as in the output of
	infoFromFiles.readDoctorsFile concerning the time of previous schedule;
	requests is a list of lists with the structure as in the output of 
	infoFromFile.readRequestsFile concerning the current update time;
	previousSched is a list of lists with the structure as in the output of
	infoFromFiles.readScheduleFile concerning the previous update time;
	nextTime is a string in the format HHhMM with the time of the next schedule
	Ensures:
	A list of birth assistances, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	of the project (omitted here for the sake of readability) and a list of the
	updated doctors according to the consitions indicated in the general 
	specification of the project(omitted here for the sake of readability).
	"""
	sched = []
	docsOnBreak = []

	Total_Minutes = dateTime.timeToMinutes(nextTime)
	
	copy_PreviouShed = copy.deepcopy(previousSched)

	#This analyzes the the list and takes that already happened.
	for line in previousSched:               							           					
		if dateTime.timeToMinutes(line[constants.SCHE_HOUR_IDX]) <= Total_Minutes: 		        	
			copy_PreviouShed.remove(line)								    					 	
	nextSched = copy_PreviouShed														            
                                                                                                    
																								
	for doctor in doctors:
		if dateTime.timeToMinutes(doctor[constants.DOCT_LASTBIRTH_IDX]) < dateTime.timeToMinutes(nextTime):
			doctor[constants.DOCT_LASTBIRTH_IDX] = nextTime
	#Assigns a doctor to a mother 
	while len(requests) != 0:
		needsAssis = True
		next_mother = requests[0]
		for doctor in doctors:
			if needsAssis:
				#High risk mothers
				if next_mother[constants.MOTH_RISK_IDX] == "high":
					if doctor[constants.DOCT_EXP_IDX] == "3" or \
						doctor[constants.DOCT_EXP_IDX] == "2":
						sched.append([doctor[constants.DOCT_LASTBIRTH_IDX],\
						next_mother[constants.MOTH_NAME_IDX],doctor[constants.DOCT_NAME_IDX]])
						chosen_doctor = doctor
						needsAssis = False
				else:
					sched.append([doctor[constants.DOCT_LASTBIRTH_IDX],next_mother[constants.MOTH_NAME_IDX],doctor[constants.DOCT_NAME_IDX]])
					chosen_doctor = doctor
					needsAssis = False		
		#if there isnt any doctors to attend the mother
		if len(doctors) == 0:
			temp = [nextTime,next_mother[constants.MOTH_NAME_IDX],"redirected to other network"]
			sched.append(temp)
		else:
			#Add 20 minutes to the chosen_doctor's last appointment time
			#and reorganize the list of doctors
			docsOnBreak = add20Minutes(chosen_doctor, doctors, docsOnBreak)
			infoFromFiles.sortDoctors(doctors)

		requests.remove(next_mother)
		

	#Returns the updated doctors and the updated shedule. 
	nextSched = nextSched + sched
	nextSched.sort(key=lambda x: dateTime.timeToMinutes(x[constants.SCHE_HOUR_IDX]))

	nextDoctors = doctors + docsOnBreak
	nextDoctors.sort(key=lambda x: x[constants.DOCT_NAME_IDX])
	
	return nextSched, nextDoctors
