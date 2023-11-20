import numpy as np
import pandas as pd
import os
import math

#--------------------------------------Global Vars-----------------------------------------------

files_to_read = []
chunk_length = int(30*4) # size of 

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

g = 9.81

prevValue=0
for value in raw_data_depth_array:
  raw_data_layer_thickness.append(value-prevValue)
  prevValue = value


delft_chunk_size = 10

#------------------------------------------------------------------------------------------------

def main():

  for file_name in os.listdir('./file-conversions/data/test_convert/'):
    if "FULL" in file_name:
      files_to_read.append(file_name) 

    else:
      FileNotFoundError

  for file in files_to_read:
    output_xlsx = read_xlsx(file)
    output_scaling = apply_scaling(output_xlsx)
    output_depth_bin = bin_depths(output_scaling)
    output_bin_velocity = bin_velocity(output_depth_bin[0], output_depth_bin[1])
    output_average_velocity = average_velocity(output_bin_velocity)

    # print(output_bin_velocity['depthBins'])

    outTest = testFunc(output_depth_bin, output_average_velocity)
    
    print(outTest)

    # print(outTest)

    # print(f"velocity bins: {output_bin_velocity['velocityBins']},\n\n\nThickness bins{output_bin_velocity['thicknessBins']}")
#----------------------------------------Read xlsx-----------------------------------------------

def read_xlsx(file):
    
  read_xlsx_output_dict = {
    "chunkDepth": [],
    "vp": [],
    "delftDepth": [],
    "percentLayerThickness": [],
    "weightedVp": []
  }

  print(f'Current File: {file}')
  print(f"Chunk size: {chunk_length}")
  
  pd_data = pd.read_excel(f'./file-conversions/data/test_convert/{file}', sheet_name = 0, index_col = 0)

  for current_chunk in range(int(len(pd_data)/chunk_length)):
    
    pd_bin_data = pd_data.iloc[(current_chunk * chunk_length):(current_chunk * chunk_length + chunk_length)]
    pd_bin_data = pd_bin_data.drop(["Latitude", "Longitude", "Hour"], axis=1)
    np_bin_data = pd_bin_data.to_numpy()
    nan_index = np.argwhere(np.isnan(np_bin_data[0]))[0][0]
          
    max_chunk_depth = raw_data_depth_array[nan_index - 1] 
    delft_depth_array = np.linspace(max_chunk_depth/delft_chunk_size, max_chunk_depth, delft_chunk_size)
    current_chunk_layer_thickness = [(x/max_chunk_depth * 100) for x in (raw_data_layer_thickness[0:nan_index])]
    chunkDepth = raw_data_depth_array[0:(nan_index)]

    read_xlsx_output_dict['chunkDepth'].append(chunkDepth)
    read_xlsx_output_dict['vp'].append(np_bin_data)
    read_xlsx_output_dict['delftDepth'].append(delft_depth_array)
    read_xlsx_output_dict['percentLayerThickness'].append(current_chunk_layer_thickness)
         
  return(read_xlsx_output_dict)
#------------------------------------------------------------------------------------------------

#--------------------------------------Apply Scaling---------------------------------------------

def apply_scaling(exctracted_dict):

  for chunkNumber,chunk in enumerate(exctracted_dict['vp']):
    weighted_vp = []
    for vp_list in chunk:
        vp_list = [no_nan for no_nan in vp_list if not math.isnan(no_nan)]
        weighted_vp.append([vp*exctracted_dict['percentLayerThickness'][chunkNumber][vp_count] for  vp_count, vp in enumerate(vp_list)])
        
        # print(f"The vp array is: {vp} The is : {scaling_input['percentLayerThickness'][chunkNumber]}")
    exctracted_dict['weightedVp'].append(weighted_vp)

  return(exctracted_dict)
    
#------------------------------------------------------------------------------------------------

#----------------------------------------Bin Depths----------------------------------------------
def bin_depths(bin_depths_input):
  bins = {
    "depthBins":[],
    "velocityBins":[],
    "thicknessBins": []
  }
  for chunkNumber, delft_depth_list in enumerate(bin_depths_input['delftDepth']):
    

    prevValue = 0
    depth_bins = []
    for depth in delft_depth_list:
      
      selectednum = [num for num in bin_depths_input['chunkDepth'][chunkNumber] if prevValue < num <= depth]
      depth_bins.append(selectednum)
      prevValue=depth
    
    bins["depthBins"].append(depth_bins)

  return([bins, bin_depths_input])
#------------------------------------------------------------------------------------------------

#---------------------------------------Bin Velocity---------------------------------------------

def bin_velocity(bin_velocity_depth_input, bin_velocity_input):
  
  for binned_count, binnedDepth in enumerate(bin_velocity_depth_input['depthBins']):

    # print("\n\n\n",bin_velocity_input['percentLayerThickness'][binned_count],"\n\n\n")

    for weightedVp_count, flatList in enumerate(bin_velocity_input['weightedVp'][binned_count]):
      # print(flatList)
      index = 0
      
      for bin in binnedDepth:
        newSublistVelocity = []
        newSublistThickness = []
        for element in bin:
          if index < len(flatList):
            newSublistVelocity.append(flatList[index])
            newSublistThickness.append(bin_velocity_input['percentLayerThickness'][binned_count][index])
            index += 1
        bin_velocity_depth_input['velocityBins'].append(newSublistVelocity)
        bin_velocity_depth_input['thicknessBins'].append(newSublistThickness)

  return (bin_velocity_depth_input)
#------------------------------------------------------------------------------------------------

def average_velocity(average_velocity_input):

  averaged_velocity=[]

  for val_counter,val in enumerate(average_velocity_input['velocityBins']):

    np_velocity = np.array(val).sum()
    np_thickness = np.array(average_velocity_input['thicknessBins'][val_counter]).sum()
    if np_thickness == 0:
      avgsum = np.nan
    else: 
      avgsum = np_velocity/np_thickness
    
    averaged_velocity.append(avgsum)

  return averaged_velocity

def testFunc(testFuncInputDepth,testFuncInputVel):

  # print(testFuncInputDepth[1]['delftDepth'])
  # print("\n\n")
  chunkedAvergagedVelocity = np.reshape(testFuncInputVel, (len(testFuncInputDepth[1]['delftDepth']),chunk_length,delft_chunk_size))
  # print("\n\n")

  for chunk_number, chunk in enumerate(chunkedAvergagedVelocity):
    
    for list_count, list in enumerate(chunk):
      for element_count, element in enumerate(list):
        if element>=0:
          chunkedAvergagedVelocity[chunk_number][list_count][element_count] = element +  (2*(np.sqrt(g*testFuncInputDepth[1]['delftDepth'][chunk_number][element_count])))
        else:
          chunkedAvergagedVelocity[chunk_number][list_count][element_count] = element - (2*(np.sqrt(g*testFuncInputDepth[1]['delftDepth'][chunk_number][element_count])))

  return chunkedAvergagedVelocity

if __name__ == "__main__":
    main()