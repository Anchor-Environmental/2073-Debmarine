import numpy as np
import pandas as pd
import os

files_to_read = []

def main():
    read_format()
    read_xlsx()
    
    

def read_format():
     pass

def read_xlsx():

    for file_name in os.listdir('./PyConv/data/'):
        if "Boundry" in file_name:
            files_to_read.append(file_name) 

        else:
             LookupError
    
    for file in files_to_read:  
        
        data = pd.read_excel(f'./PyConv/data/{file}', sheet_name = 0, index_col = 0)
        latitude = data.loc[:,'Latitude']
        prev_latitude = data['Latitude'].iloc[0]
        prev_longitude = data['Longitude'].iloc[0]

        for entry_number, entry in enumerate(data.loc[:,'V_p']):

            if (data['Latitude'].iloc[entry_number] != [prev_latitude] or data['Longitude'].iloc[entry_number] != prev_longitude):
                    print(f'The coordinates are: {data['Latitude'].iloc[entry_number]}, {data['Longitude'].iloc[entry_number]} and the V_p is {entry}')
            
            prev_latitude = data['Latitude'].iloc[entry_number]
            prev_longitude = data['Longitude'].iloc[entry_number]
        # print(prev_latitude, prev_longitude)

if __name__ == "__main__":
    main()