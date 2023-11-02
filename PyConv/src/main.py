import numpy as np
import pandas as pd
import os

files_to_read = []

def main():
    read_xlsx()
    

def read_xlsx():

    for file_name in os.listdir('./PyConv/data/'):
        if "Boundry" in file_name:
            files_to_read.append(file_name) 
    
    
    for file in files_to_read:
        
        data = pd.read_excel(f'./PyConv/data/{file}', sheet_name = 0, index_col = 0)

        print(data)

if __name__ == "__main__":
    main()