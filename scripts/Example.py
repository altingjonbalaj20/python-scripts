import pandas as pd
import matplotlib.pyplot as plt
import datetime

dataset = pd.read_excel('Files\InvoiceListReport_TP24_20220307.xlsx')
# print(dataset.keys())
dataset = dataset[['Invoice Amount', 'Eligible Amount', 'Invoice Date']]

today = datetime.datetime.today().date()
lastweek = today - datetime.timedelta(days=7)
print(lastweek)

dataset['Invoice Date'] = pd.to_datetime(dataset['Invoice Date'])
dataset['Day of Week'] = dataset['Invoice Date'].dt.day_name()
