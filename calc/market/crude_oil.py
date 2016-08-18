import os
import xlrd
import matplotlib.pyplot as plt
import datetime
from numpy.random import *

def history_data(filename):
    FILE_NAME = filename
    BOOK_NAME = '/Users/ueno/app/ship_operation/calc/data/crude_oil_monthly_history.xlsx'
    #DATA_PATH = os.path.join(os.path.join(os.path.abspath(__file__), os.pardir), 'data')
    #BOOK_PATH = os.path.join(DATA_PATH, BOOK_NAME)
    book = xlrd.open_workbook(BOOK_NAME)
    sheet_1 = book.sheet_by_index(0)
    date = [] #historical date
    data = [] #historical data
    for row in range(1, sheet_1.nrows):
        value1 = sheet_1.cell_value(row, 0)
        value1 = datetime.datetime.fromtimestamp(value1)
        value2 = sheet_1.cell_value(row, 1)
        if value2 != '':
            date.append(value1)
            data.append(value2)
    return date, data

def winner_process(myu, sigma, year, initial):
    dates = []
    values = []
    month = year*12
    #if sigma == None:
        
    myu = float(myu)
    sigma = float(sigma)
    for index in range(month):
        dates.append(index)
        values.append(initial)
        eps = randn()
        initial += myu + sigma*eps
    return dates, values

#plt.xlabel(sheet_1.cell_value(0, 0))
#plt.ylabel(sheet_1.cell_value(0, 1))
#plt.plot(date, data)
#plt.show()
