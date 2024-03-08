import numpy as np
import random

dischargingTime = 10 # hrs

dischargeName = "Afro_1day"

startTime = 8.7840000e+004
endTime = 9.6480000e+004
startDischargeFlowRate = 0
constDischargeFlowRate = 1.31e-01
endDischargeFlowRate = 0

numberOfDays = int((endTime-startTime)/60/24)

rampTime = 1 # minutes

preDischargeRamp = np.zeros(numberOfDays)
startDischargeTime = np.zeros(numberOfDays)
dischargeHour = np.zeros(numberOfDays)
endDischargeTime = np.zeros(numberOfDays)
postDischargeRamp = np.zeros(numberOfDays)

startFlowRate = np.zeros(numberOfDays)
constFlowRate1 = np.zeros(numberOfDays)
constFlowRate2 = np.zeros(numberOfDays)
endFlowRate = np.zeros(numberOfDays)

completeDischargeList = np.zeros(numberOfDays*4)
dischargeFlowRates = np.zeros(numberOfDays*4)

# dischargeList = [1, 11, 12, 11, 13, 12,  5,  1, 12, 14,  2,  6,  8,  6, 13,  7,  8,  6,
#   4,  8,  8, 13,  5,  8,  3, 10,  8, 10,  3,  4, 12,  9,  9,  1,  1,  8,
#   7,  8, 10, 12,  8, 13,  1, 10,  2,  5,  9, 10,  8,  9, 12,  4,  7,  1,
#   3, 13,  2,  7,  8,  5,  4,  7,]
# dischargeHour = np.array(dischargeList)

for dischargeHourIndex, hour in enumerate(dischargeHour):
  
  dischargeHour[dischargeHourIndex] = random.randint(1,(24-(dischargingTime+1)))

  startDischargeTime[dischargeHourIndex] = dischargeHour[dischargeHourIndex]*60 + (startTime) + (dischargeHourIndex*(1440))
  endDischargeTime[dischargeHourIndex] = startDischargeTime[dischargeHourIndex] + (dischargingTime*60)

  preDischargeRamp[dischargeHourIndex] = startDischargeTime[dischargeHourIndex] - rampTime
  postDischargeRamp[dischargeHourIndex] = endDischargeTime[dischargeHourIndex] + rampTime

  startFlowRate[dischargeHourIndex] = startDischargeFlowRate
  constFlowRate1[dischargeHourIndex] = constDischargeFlowRate
  constFlowRate2[dischargeHourIndex] = constDischargeFlowRate
  endFlowRate[dischargeHourIndex] = endDischargeFlowRate
 
print(dischargeHour)

completeDischargeList = np.stack((preDischargeRamp, startDischargeTime, endDischargeTime, postDischargeRamp), axis=1)
dischargeFlowRates = np.stack((startFlowRate, constFlowRate1, constFlowRate2, endFlowRate), axis=1)
completeDischargeList = completeDischargeList.flatten()
dischargeFlowRates = dischargeFlowRates.flatten()

completeDischargeList = np.stack((completeDischargeList, dischargeFlowRates), axis=1)


print(f'pre discharge ramp: {preDischargeRamp} \n start discharge: {startDischargeTime} \n end discharge: {endDischargeTime} \n post discharge ramp: {postDischargeRamp}')
print("\n\n\n")
print(completeDischargeList)


np.savetxt(f"./file-conversions/out/discharges/{dischargeName}.csv", completeDischargeList)

