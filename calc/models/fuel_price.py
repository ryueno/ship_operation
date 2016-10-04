import os
import xlrd
import matplotlib.pyplot as plt
import datetime
from numpy.random import *

def history_data(filename):
    FILE_NAME = filename
    FILE_PATH = '/Users/ueno/app/ship_operation/calc/data/oil_price.xlsx'
    DATA_PATH = '../data'
    #FILE_PATH = os.path.join(DATA_PATH, FILE_NAME)
    book = xlrd.open_workbook(FILE_PATH)
    sheet_1 = book.sheet_by_index(0)
    date = [] #date
    dataCO = [] #CrudeOil
    dataNG = [] #NaturalGas_JP
    for row in range(1, sheet_1.nrows):
        value0 = sheet_1.cell_value(row, 0)
        value0 = value0.split('M')
        value1 = sheet_1.cell_value(row, 1)
        if value1 == '':
            value1 = 0;
        value2 = sheet_1.cell_value(row, 2)
        if value2 == '':
            value2 = 0;
        value3 = sheet_1.cell_value(row, 3)
        if value3 == '':
            value3 = 0;
        value4 = sheet_1.cell_value(row, 4)
        if value4 == '':
            value4 = 0;
        value5 = sheet_1.cell_value(row, 5)
        if value5 == '':
            value5 = 0;
        value6 = sheet_1.cell_value(row, 6)
        if value6 == '':
            value6 = 0;
        date.append(value0)
        dataCO.append([value1, value2, value3])
        dataNG.append([value4, value5, value6])
    return date, dataCO, dataNG

# generate scenario by wiener process
def winner_process(myu, sigma, year, initial):
    dates = []
    values = []
    month = year*12
    #if sigma == None:
        
    myu = float(myu)
    sigma = float(sigma)
    initial = float(initial)
    for index in range(month):
        dates.append(index)
        values.append(initial)
        eps = randn()
        initial *= (myu + sigma*eps)
    return dates, values


#plt.xlabel(sheet_1.cell_value(0, 0))
#plt.ylabel(sheet_1.cell_value(0, 1))
#plt.plot(date, data)
#plt.show()
