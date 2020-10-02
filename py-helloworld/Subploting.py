import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


rawData = pd.read_csv('StudentsPerformance.csv')

#print(rawData)

dataInfo = rawData.info

#print(dataInfo)

#dataNeeded = pd.read_csv('StudentsPerformance.csv', usecols=['gender', 'math score'])
dataNeeded = rawData.drop(['reading score', 'writing score'], axis = 1)

femaleFilter = dataNeeded['gender'].isin(['female'])
maleFilter = dataNeeded['gender'].isin(['male'])

femaleData = dataNeeded[femaleFilter]
maleData = dataNeeded[maleFilter]

femaleMathScoreAverage = np.average(femaleData['math score'])
maleMathScoreAverage = np.average(maleData['math score'])

#print(femaleMathScoreAverage)
#print(maleMathScoreAverage)

plt.figure()

#Grafica promedio en pruebas de matemáticas  por genero
plt.subplot(2, 2, 1)

plt.title('Promedio de pruebas de matemáticas por genero')

plt.bar([1], [maleMathScoreAverage], label = 'Hombres', color = 'blue')
plt.bar([2], [femaleMathScoreAverage], label = 'Mujeres', color = 'pink')

plt.legend(['Hombres', 'Mujeres'])

plt.xlabel('Genero')
plt.ylabel('Puntaje')

#------------------------------------------------------------#

#Analsiis por etnia
gAFilter = dataNeeded['race/ethnicity'].isin(['group A'])
gBFilter = dataNeeded['race/ethnicity'].isin(['group B'])
gCFilter = dataNeeded['race/ethnicity'].isin(['group C'])
gDFilter = dataNeeded['race/ethnicity'].isin(['group D'])
gEFilter = dataNeeded['race/ethnicity'].isin(['group E'])

gAData = dataNeeded[gAFilter]
gBData = dataNeeded[gBFilter]
gCData = dataNeeded[gCFilter]
gDData = dataNeeded[gDFilter]
gEData = dataNeeded[gEFilter]

gAMathScore = gAData['math score']
gBMathScore = gBData['math score']
gCMathScore = gCData['math score']
gDMathScore = gDData['math score']
gEMathScore = gEData['math score']

gAScoreAverage = np.average(gAMathScore)
gBScoreAverage = np.average(gBMathScore)
gCScoreAverage = np.average(gCMathScore)
gDScoreAverage = np.average(gDMathScore)
gEScoreAverage = np.average(gEMathScore)

#Grafica promedio en pruebas de matemáticas por etnia
plt.subplot(2, 2, 2)

plt.title('Promedio de pruebas de matemáticas por etnia')

plt.bar(1, gAScoreAverage, color = 'r')
plt.bar(2, gBScoreAverage, color = 'g')
plt.bar(3, gCScoreAverage, color = 'b')
plt.bar(4, gDScoreAverage, color = 'yellow')
plt.bar(5, gEScoreAverage, color = 'cyan')

plt.legend(['grupo A', 'grupo B', 'grupo C', 'grupo D', 'grupo E'])

plt.xlabel('Grupo')
plt.ylabel('Puntaje')

#------------------------------------------------------------#

#Analisis por nivel educativo de los padres
BDFilter = dataNeeded['parental level of education'].isin(["bachelor's degree"])
SCFilter = dataNeeded['parental level of education'].isin(['some college'])
MDFilter = dataNeeded['parental level of education'].isin(["master's degree"])
ADFilter = dataNeeded['parental level of education'].isin(["associate's degree"])
HSFilter = dataNeeded['parental level of education'].isin(['high school'])

BDData = dataNeeded[BDFilter]
SCData = dataNeeded[SCFilter]
MDData = dataNeeded[MDFilter]
ADData = dataNeeded[ADFilter]
HSData = dataNeeded[HSFilter]

BDMathScore = BDData['math score']
SCMathScore = SCData['math score']
MDMathScore = MDData['math score']
ADMathScore = ADData['math score']
HSMathScore = HSData['math score']

BDScoreAverage = np.average(BDMathScore)
SCScoreAverage = np.average(SCMathScore)
MDScoreAverage = np.average(MDMathScore)
ADScoreAverage = np.average(ADMathScore)
HSScoreAverage = np.average(HSMathScore)

#Gráfica Promedio en Pruebas de Matemátcias por Nivel educativo de los padres
plt.subplot(2, 2, 3)
plt.title('Promedio de pruebas de matemáticas por Nivel educativo de los padres')

plt.bar(1, SCScoreAverage, color = 'g')
plt.bar(2, HSScoreAverage, color = 'cyan')
plt.bar(3, ADScoreAverage, color = 'yellow')
plt.bar(4, BDScoreAverage, color = 'r')
plt.bar(5, MDScoreAverage, color = 'b')


plt.legend(["bachelor's degree", 'some college', "master's degree", "associate's degree", 'high school'])

plt.xlabel('Nivel Educativo')
plt.ylabel('Puntaje')

#------------------------------------------------------------#

plt.show()