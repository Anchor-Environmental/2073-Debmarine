import numpy as np
import pandas as pd
import os

#--------------------------------------Global Vars-----------------------------------------------

files_to_read = []
chunk_length = int(1*4)
endA = np.zeros(chunk_length)
endB = np.zeros(chunk_length)
output_time = np.linspace(0.0, 60*6*3, num=4)
raw_data_depth_array = [0.4940249, 
               1.541375,
               2.645669,
               3.819495,
               5.0782242,
               6.4406142,
               7.9295602,
               9.5729971,
               11.405,
               13.46714,
               15.81007,
               18.49556,
               21.59882,
               25.211411,
               29.444731,
               34.434151,
               40.344051,
               47.373692,
               55.76429,
               65.807266,
               77.853851,
               92.326073,
               109.7293,
               130.666,
               155.85069,
               186.1256]

delft_chunk_size = 10

read_xlsx_output_dict = {
  "Vp": [],
  "delftDepth": []
}
#------------------------------------------------------------------------------------------------

def main():

  for file_name in os.listdir('./file-conversions/data/test_convert/'):
    if "Boundry" in file_name:
      files_to_read.append(file_name) 

    else:
      FileNotFoundError

  for file in files_to_read:
    output = read_xlsx(file)
    bin_velocity(output)
  

#----------------------------------------Read xlsx-----------------------------------------------

def read_xlsx(file):
    
    read_xlsx_output_dict = {
      "Vp": [],
      "delftDepth": []
    }

    print(f'Current File: {file}')
    print(f"Chunk size: {chunk_length}")
    
    pd_data = pd.read_excel(f'./file-conversions/data/test_convert/{file}', sheet_name = 0, index_col = 0)

    for current_chunk in range(int(len(pd_data)/chunk_length)):
      
      pd_bin_data = pd_data.iloc[(current_chunk * 4):(current_chunk * 4 + chunk_length)]
      pd_bin_data = pd_bin_data.drop(["Latitude", "Longitude", "Hour"], axis=1)
      np_bin_data = pd_bin_data.to_numpy()
      nan_index = np.argwhere(np.isnan(np_bin_data[0]))[0][0]
      # np_bin_data = np_bin_data[~np.isnan(np_bin_data)]
      
      # bin_data = pd_data
      # print(f"Data: {np_bin_data}, nan index: {nan_index}, depth at nan: {depth_array[nan_index]},\n__________________END OF CHUNK_________________\n")
      
      max_chunk_depth = raw_data_depth_array[nan_index - 1] 
      delft_depth_array = np.linspace(max_chunk_depth/delft_chunk_size, max_chunk_depth, delft_chunk_size)

       
      read_xlsx_output_dict['Vp'].append(np_bin_data)
      read_xlsx_output_dict['delftDepth'].append(delft_depth_array)
    
    return(read_xlsx_output_dict)
#------------------------------------------------------------------------------------------------


#--------------------------------------Bin velocity----------------------------------------------

def bin_velocity(output):
  print(output)
  pass
  
    
#------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()