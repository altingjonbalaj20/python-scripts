import pandas as pd
import matplotlib.pyplot as plt
import datetime

dataset = pd.read_excel('Files\InvoiceListReport_TP24_20220307.xlsx')
# print(dataset.keys())
dataset = dataset[['Invoice Amount', 'Eligible Amount', 'Invoice Date']]

today = datetime.datetime.today()
lastweek = today - datetime.timedelta(days=30)
dataset['Invoice Date'] = pd.to_datetime(dataset['Invoice Date'])
dataset = dataset[(dataset['Invoice Date'] >= lastweek)]

dataset['Day of Week'] = dataset['Invoice Date'].dt.day_name()

dataset = dataset.groupby(['Day of Week']).sum()
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']

## order index by ordercriteria on days

