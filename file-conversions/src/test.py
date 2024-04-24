import numpy as np

start_dredge_time = 36000
dredge_days = 7
dredge_zone = 1
mins_in_day = 1440
end_dredge_time = dredge_days * mins_in_day + start_dredge_time
loops = end_dredge_time - start_dredge_time
discharge_interval = 48

def main():

  for i in range(dredge_days):

    if i%2 == 0:

      start_time_1 = start_dredge_time + discharge_interval*(dredge_zone-1) + mins_in_day*i
      stop_time_1 = start_dredge_time + discharge_interval*dredge_zone + mins_in_day*i

      print(f'start time : {start_time_1}; stop time : {stop_time_1}')

    else:
      
      start_time_2 = start_dredge_time - discharge_interval*(dredge_zone) + mins_in_day*(i+1)
      stop_time_2 = start_dredge_time + mins_in_day*(i+1)

      print(f'start time : {start_time_2}; stop time: {stop_time_2}')



if __name__ == "__main__":
  main()