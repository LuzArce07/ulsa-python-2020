import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


rawData = pd.read_csv('StudentsPerformance.csv')

#print(rawData)

dataInfo = rawData.info

#print(dataInfo)

dataNeeded = pd.read_csv('StudentsPerformance.csv', usecols=['gender', 'math score'])

femaleFilter = dataNeeded['gender'].isin(['female'])
maleFilter = dataNeeded['gender'].isin(['male'])

femaleData = dataNeeded[femaleFilter]
maleData = dataNeeded[maleFilter]

femaleMathScoreAverage = np.average(femaleData['math score'])
maleMathScoreAverage = np.average(maleData['math score'])

#print(femaleMathScoreAverage)
#print(maleMathScoreAverage)

plt.title('Promedio de pruebas de matemáticas por genero')

plt.bar([1], [maleMathScoreAverage], label = 'Hombres', color = 'blue')
plt.bar([2], [femaleMathScoreAverage], label = 'Mujeres', color = 'pink')

plt.legend(['Hombres', 'Mujeres'])

plt.show()

