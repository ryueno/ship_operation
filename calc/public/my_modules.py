# -*- coding: utf-8 -*-
import math
import os
import sys
import csv


##############
# csv module #
##############
def write_csv(column_names, write_data, output_file_path):
    # for initial write
    write_column_flg = False if os.path.exists(output_file_path) else True
    
    # write file
    f = open(output_file_path, 'a')
    csvWriter = csv.writer(f)
    if write_column_flg:
        csvWriter.writerow(column_names)
    csvWriter.writerow(write_data)
    
    f.close()
    return

def write_array_to_csv(column_names, write_array, output_file_path):
    # write file
    f = open(output_file_path, 'a')
    csvWriter = csv.writer(f)
    csvWriter.writerow(column_names)
    
    # write array data based on given column names
    for write_row in write_array:
        write_row_data = []
        for column_name in column_names:
            write_data = write_row[column_name]
            # for numpy array
            if isinstance(write_data, np.ndarray):
                write_data = write_data[0]
            write_row_data.append(write_data)
        csvWriter.writerow(write_row_data)
    f.close()
    return

def read_csv(filepath):
    load_data = np.array([])
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            load_data = append_for_np_array(load_data, row)
    return header, load_data
