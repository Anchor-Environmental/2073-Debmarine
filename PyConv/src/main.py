import numpy as np
import pandas as pd
import os

#--------------------------------------Global Vars-----------------------------------------------

files_to_read = []
chunk_length = 30*4
endA = np.zeros(chunk_length)
endB = np.zeros(chunk_length)
output_time = np.linspace(0.0, 60*6*119, num=120)

#------------------------------------------------------------------------------------------------

def main():

    read_format()
    read_xlsx()

#--------------------------------------Read format-----------------------------------------------

def read_format():
    """" Reads a format file and stores the string as a global var """
    
    for file_name in os.listdir('./PyConv/data/'):
        if "Boundry" in file_name:
            files_to_read.append(file_name) 

        else:
            FileNotFoundError
    
    with open(r'./PyConv/data/format.txt',mode='r') as format_file:
        
        global output_format 
        output_format = format_file.readlines()
        output_format = ''.join(output_format)
    
    format_file.close()

#------------------------------------------------------------------------------------------------

#----------------------------------------Read xlsx-----------------------------------------------

def read_xlsx():
    """ Reads xlsx file and writes data to .txt file """

    with open('./Pyconv/out/output.txt', 'w') as output_file:

        boundary_section_count = 0

        for file in files_to_read:  

            data = pd.read_excel(f'./PyConv/data/{file}', sheet_name = 0, index_col = 0)
            print(f'Current File: {file}')
            print(f"Chunk size {chunk_length}\n")
            num_rows = len(data.loc[:,'V_p'])
            chunk_count = 0

            for entry_number in range(num_rows-chunk_length):
                # There are only (number of rows)/(size of chunk)-1 chunks since we
                # are using one set of V_p values twice
                
                endA[entry_number%chunk_length] = data['V_p'].iloc[entry_number]
                endB[entry_number%chunk_length] = data['V_p'].iloc[entry_number+chunk_length]

                if (entry_number%chunk_length == (chunk_length-1)):

                    boundary_section_count+=1
                    chunk_count+=1
                    write_output(output_file,
                                  endA, 
                                  endB, 
                                  output_format, 
                                  boundary_section_count, 
                                  file, 
                                  chunk_count)
                    # this write_output function can be simplified later on
        
    output_file.close()

#------------------------------------------------------------------------------------------------


#----------------------------------------Write to output-----------------------------------------

def write_output(output_file, 
                 endA, 
                 endB, 
                 file_format, 
                 boundary_section_count, 
                 file_name, chunk_count):
    """ Writes the data to a .txt file according to an input format """

    place = file_name[0: 8]
    chunk_place = f'{place}{chunk_count}'
    output_chunk = np.column_stack((output_time, endA, endB))
    output_chunk.reshape(chunk_length, 3)
    namespace = {'boundary_number': f'{boundary_section_count}',
                 'location_chunk':'{:<20}'.format(chunk_place), 
                 'chunk_count': f'{chunk_length}'}
    file_format = file_format.format(**namespace)
    output_file.write(file_format)

    np.savetxt(output_file, output_chunk, fmt='% .7e')
    
#------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()