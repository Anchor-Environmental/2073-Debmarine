import numpy as np
import pandas as pd
import os
import math

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

raw_data_layer_thickness = []

prevValue=0
for value in raw_data_depth_array:
  raw_data_layer_thickness.append(value-prevValue)
  prevValue = value


delft_chunk_size = 10

#------------------------------------------------------------------------------------------------

def main():

  for file_name in os.listdir('./file-conversions/data/test_convert/'):
    if "South" in file_name:
      files_to_read.append(file_name) 

    else:
      FileNotFoundError

  for file in files_to_read:
    output_xlsx = read_xlsx(file)
    output_scaling = apply_scaling(output_xlsx)
    bin_velocity(output_scaling)

#----------------------------------------Read xlsx-----------------------------------------------

def read_xlsx(file):
    
    read_xlsx_output_dict = {
      "vp": [],
      "delftDepth": [],
      "percentLayerThickness": [],
      "weightedVp": []
    }

    print(f'Current File: {file}')
    print(f"Chunk size: {chunk_length}")
    
    pd_data = pd.read_excel(f'./file-conversions/data/test_convert/{file}', sheet_name = 0, index_col = 0)

    for current_chunk in range(int(len(pd_data)/chunk_length)):
      
      pd_bin_data = pd_data.iloc[(current_chunk * 4):(current_chunk * 4 + chunk_length)]
      pd_bin_data = pd_bin_data.drop(["Latitude", "Longitude", "Hour"], axis=1)
      np_bin_data = pd_bin_data.to_numpy()
      nan_index = np.argwhere(np.isnan(np_bin_data[0]))[0][0]
           
      max_chunk_depth = raw_data_depth_array[nan_index - 1] 
      delft_depth_array = np.linspace(max_chunk_depth/delft_chunk_size, max_chunk_depth, delft_chunk_size)
      current_chunk_layer_thickness = [(x/max_chunk_depth * 100) for x in (raw_data_layer_thickness[0:nan_index])]
      
      read_xlsx_output_dict['vp'].append(np_bin_data)
      read_xlsx_output_dict['delftDepth'].append(delft_depth_array)
      read_xlsx_output_dict['percentLayerThickness'].append(current_chunk_layer_thickness)
         
    return(read_xlsx_output_dict)
#------------------------------------------------------------------------------------------------


#--------------------------------------Apply Scaling---------------------------------------------

def apply_scaling(scaling_input):

  for chunkNumber,chunk in enumerate(scaling_input['vp']):
    weighted_vp = []
    for vp_list in chunk:
        vp_list = [no_nan for no_nan in vp_list if not math.isnan(no_nan)]
        weighted_vp.append([vp*scaling_input['percentLayerThickness'][chunkNumber][vp_count] for  vp_count, vp in enumerate(vp_list)])
        
        # print(f"The vp array is: {vp} The is : {scaling_input['percentLayerThickness'][chunkNumber]}")
    scaling_input['weightedVp'].append(weighted_vp)

  return(scaling_input)
  
  
    
#------------------------------------------------------------------------------------------------

#--------------------------------------Apply Scaling---------------------------------------------

def bin_velocity(bin_velocity_input):
  print(bin_velocity_input['weightedVp'])

  
    
#------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()