import numpy as np

start_dredge_time = 36000
dredge_days = 7
dredge_zone = 30
mins_in_day = 1440
num_dredge_cells = 30
end_dredge_time = dredge_days * mins_in_day + start_dredge_time
loops = end_dredge_time - start_dredge_time
discharge_interval = 48
start_flow_rate = 0.073
stop_flow_rate = 0

start_flow = np.zeros(dredge_days)
stop_flow = np.zeros(dredge_days)
start_time = np.zeros(dredge_days)
stop_time = np.zeros(dredge_days)
complete_discharge_list = np.zeros(dredge_days*2)
discharge_flow_rates = np.zeros(dredge_days*2)

def main():

  for i in range(dredge_days):

    if i%2 == 0:

      start_time[i] = start_dredge_time +  discharge_interval*(dredge_zone-1) + (discharge_interval * num_dredge_cells * i)
      stop_time[i] = start_dredge_time + discharge_interval*(dredge_zone) + (discharge_interval * num_dredge_cells * i)

      start_flow[i] = start_flow_rate
      stop_flow[i] = stop_flow_rate

      # print(f'day : {i+1}; start time : {start_time[i]}; stop time : {stop_time[i]}')

    else:
      
      start_time[i] = start_dredge_time +  discharge_interval*(num_dredge_cells-dredge_zone) + (discharge_interval * num_dredge_cells * i)
      stop_time[i] = start_dredge_time + discharge_interval*(num_dredge_cells-(dredge_zone - 1)) + (discharge_interval * num_dredge_cells * i)

      start_flow[i] = start_flow_rate
      stop_flow[i] = stop_flow_rate

      # print(f'day : {i+1}; start time : {start_time[i]}; stop time: {stop_time[i]}')


  complete_discharge_list = np.stack((start_time, stop_time), axis=1)
  discharge_flow_rates = np.stack((start_flow, stop_flow), axis=1)

  complete_discharge_list = complete_discharge_list.flatten()
  # discharge_flow_rates = discharge_flow_rates.flatten()

  # complete_discharge_list = np.stack((complete_discharge_list, discharge_flow_rates), axis=1)

  print(complete_discharge_list)

  np.savetxt(f"./file-conversions/out/discharges/dredgezones/DredgeZone.csv", complete_discharge_list)  


if __name__ == "__main__":
  main()