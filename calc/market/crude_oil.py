import os
import xlrd
import matplotlib.pyplot as plt
import datetime

BOOK_NAME = '/Users/ueno/app/ship_operation/calc/data/crude_oil_history.xlsx'
#DATA_PATH = os.path.join(os.path.join(os.path.abspath(__file__), os.pardir), 'data')
#BOOK_PATH = os.path.join(DATA_PATH, BOOK_NAME)

book = xlrd.open_workbook(BOOK_NAME)

sheet_1 = book.sheet_by_index(0)
date = []
data = []
for row in range(1, sheet_1.nrows):
    value1 = sheet_1.cell_value(row, 0)
    value1 = datetime.datetime.fromtimestamp(value1)
    value2 = sheet_1.cell_value(row, 1)
    if value2 != '':
        date.append(value1)
        data.append(value2)

plt.xlabel(sheet_1.cell_value(0, 0))
plt.ylabel(sheet_1.cell_value(0, 1))
plt.plot(date, data)
plt.show()
