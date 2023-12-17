#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 160
# 62214 Luís Lima
# 62269 Dinis Garcia


# This module records the constants used in the application

# You should define here as many constants as you need to keep your 
# code clean and legible

# Value for weekly pause in the output schedule
WKL_LEAVE = "weekly leave"

# Indentifies the type of the file while using the header
TYPE_HEADER = 6

# In a file:
# Number of header's lines
NUM_HEADER_LINES = 7
# Index of line with hour of last refresh
HOUR_LINE_IDX = 3
# Number of characters correponding to the hour in a file's name + ".txt":
NAME_HOUR_CHAR = -9 #Last 9 digits


# In a doctor's list:
# Index of the element with the doctor's name
DOCT_NAME_IDX = 0
# Index of the element with the doctor's experience
DOCT_EXP_IDX = 1
# Index of the element with the doctor's last birth
DOCT_LASTBIRTH_IDX = 2
# Index of the element with the doctor's acumulated daily hours
DOCT_ACCUMULATOR_IDX = 3 
# Index of the element with the doctor's last weekly break
DOCT_LASTREST_IDX = 4

# In a mother's list:
# Index of the element with the mother's name
MOTH_NAME_IDX = 0
# Index of the element with the mother's age
MOTH_AGE_IDX = 1
# Index of the element with the mother's bracelet color
MOTH_COLOR_IDX = 2
# Index of the element with the mother's childbirth risk
MOTH_RISK_IDX = 3

# In a schedule's list:
# Index of the element with the planned hour of assistance
SCHE_HOUR_IDX = 0
# Index of the element with the name of the mother
SCHE_MOTHER_IDX = 1
# Index of the element with the name of the mother
SCHE_DOCTOR_IDX = 2