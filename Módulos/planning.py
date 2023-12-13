#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia
import infoFromFiles
import constants
import dateTime
import copy

# print(doctors, requests, previousSched, HeaderHour)

doctors = print(infoFromFiles.readDoctorsFile("testSets_v2/testSets_v2/testSet3/doctors16h00.txt"))
requests = print(infoFromFiles.readRequestsFile("testSets_v2/testSets_v2/testSet1/requests10h30.txt"))
previousSched = print(infoFromFiles.readScheduleFile("testSets_v2/testSets_v2/testSet1/schedule10h00.txt"))

def add20Minutes(doctor, doctorsList):
    lastAssis = doctor[2]
    dayBreak = int(doctor[3])
    weekBreak = doctor[4]
    docsOnBreak = []
    
	#Adicionar 20 minutos ás horas do último parto mais 1 hora em caso de descanso
    minutes = dateTime.timeToMinutes(lastAssis)
    minutes += 20
    dayBreak += 20
    if dayBreak >= 240:
        minutes += 60
        dayBreak = 0
    doctor[3] = str(dayBreak)
    doctor[2] = dateTime.minutesToTime(minutes)


    #Adicionar 20 minutos ás horas do último descanso
    minutes = dateTime.timeToMinutes(weekBreak)
    minutes += 20
    if minutes >= 2400:
        doctor[4] = constants.WKL_LEAVE
        docsOnBreak = doctorsList.pop(doctorsList.index(doctor))
    else:
        doctor[4] = dateTime.minutesToTime(minutes)

    return doctor #doctors



def updateSchedule(doctors, requests, previousSched, nextTime):
	"""
	Update birth assistance schedule assigning the given birth assistance requested
    to the given doctors, taking into account a previous schedule.
	
	Requires:
	doctors is a list of lists with the structure as in the output of
	infoFromFiles.readDoctorsFile concerning the time of previous schedule;
	requests is a list of lists with the structure as in the output of 
	infoFromFile.readRequestsFile concerning the current update time;
	previousSched is a list of lists with the structure as in the output of
	infoFromFiles.readScheduleFile concerning the previous update time;
	nextTime is a string in the format HHhMM with the time of the next schedule
	Ensures:
	a list of birth assistances, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	of the project (omitted here for the sake of readability).
	"""
	sched = []

	Total_Minutes = dateTime.timeToMinutes(nextTime)
	
	copy_PreviouShed = copy.deepcopy(previousSched)
	copy_Doctors = copy.deepcopy(doctors)
	copy_Requests = copy.deepcopy(requests)

	for line in previousSched:               							           					#-----------------------
		if dateTime.timeToMinutes(line[constants.SCHE_HOUR_IDX]) <= Total_Minutes: 		        	#This analyzes the     |
			copy_PreviouShed.remove(line)								    					 	#the list and takes    |
	nextSched = copy_PreviouShed														            #that already happened |
                                                                                                    #-----------------------

	
	
	#Os doutores esperam até aos pedidos das mães
	for doctor in doctors:
		if dateTime.timeToMinutes(doctor[2]) < dateTime.timeToMinutes(nextTime):
			doctor[2] = nextTime
				
	
	#Enquanto há mães à espera
	while len(requests) != 0:
		#Determina se a mãe ainda precisa de assistência
		needsAssis = True
		next_mother = requests[0]
		#Procurar doutores para next_mother
		for doctor in doctors:
			if needsAssis:
				#Partos de risco
				if next_mother[3] == "high":
					if doctor[1] == "3" or doctor[1] == "2":
						sched.append([doctor[2],next_mother[0],doctor[0]])
						#Doutor que ficou de assistir a mãe
						chosen_doctor = doctor
						#Já não é preciso assistência para esta mãe
						needsAssis = False
				else:
					sched.append([doctor[2],next_mother[0],doctor[0]])
					#Doutor que ficou de assistir a mãe
					chosen_doctor = doctor
					#Já não é preciso assistência para esta mãe
					needsAssis = False		
		#Se não houver doutores
		if len(doctors) == 0:
			#as mães têm de ser mandadas para outra rede de hospitais
			temp = [nextTime,next_mother[0],"redirected to other network"]
			sched.append(temp)
		else:
			#Adicionar 20 minutos ao tempo da ultima consulta do chosen_doctor e reorganizar a lista dos doutores
			add20Minutes(chosen_doctor, doctors)
			infoFromFiles.sortDoctors(doctors)

		#Remover o pedido pendente da mãe
		requests.remove(next_mother)
		

	#Retornar o schedule com o antigo + novo, organizado por tempo de atendimento
	nextSched = nextSched + sched
	nextSched.sort(key=lambda x: dateTime.timeToMinutes(x[0]))
	return nextSched



def UpdateDoctors(doctors, nextSched):
	'''
	'''
	while nextSched == len(nextSched):
		for scheduled in nextSched:
			for doctor in doctors:
				if scheduled[2] == doctor[constants.DOCT_NAME_IDX]:
					nextSched.remove(scheduled)
					plus_20_doctors = add20Minutes(doctor)
	return doctors				

	
	
	
#print(UpdateDoctors(doctors, updateSchedule(doctors, requests, previousSched,[])))
	
	#for line in requests:
       # if line[constants.MOTH_RISK_IDX] == "high":
            #for line2 in doctors:
                #if line2[constants.DOCT_EXP_IDX]:
                    #both = line[constants.MOTH_NAME_IDX], line2[constants.DOCT_NAME_IDX]
                    #nextSched.append(both)de
	
	
    
	
	
	
	
	#return nextSched





                	













