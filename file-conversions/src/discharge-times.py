import numpy as np
import random

maxTime = 10 # hrs

startTime = 4.3200000e+004
endTime = 1.3248000e+005

numberOfDays = int((endTime-startTime)/60/24)

rampTime = 1 # minutes

preDischargeRamp = np.zeros(numberOfDays)
startDischargeTime = np.zeros(numberOfDays)
dischargeHour = np.zeros(numberOfDays)
endDischargeTime = np.zeros(numberOfDays)
postDischargeRamp = np.zeros(numberOfDays)

for dischargeHourIndex, hour in enumerate(dischargeHour):
  
  dischargeHour[dischargeHourIndex] = random.randint(1,(24-(maxTime+1)))

  startDischargeTime[dischargeHourIndex] = dischargeHour[dischargeHourIndex]*60 + (startTime) + (dischargeHourIndex*(1440))
  endDischargeTime[dischargeHourIndex] = startDischargeTime[dischargeHourIndex] + (maxTime*60)

  preDischargeRamp[dischargeHourIndex] = startDischargeTime[dischargeHourIndex] - rampTime
  postDischargeRamp[dischargeHourIndex] = endDischargeTime[dischargeHourIndex] + rampTime

print(dischargeHour)

print(f'pre discharge ramp: {preDischargeRamp} \n start discharge: {startDischargeTime} \n end discharge: {endDischargeTime} \n post discharge ramp: {postDischargeRamp}')


# np.savetxt("./test.csv", startDischargeTime)

