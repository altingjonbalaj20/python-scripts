import pandas as pd
import matplotlib.pyplot as plt
import datetime

dataset = pd.read_excel('Files\InvoiceListReport_TP24_20220307.xlsx')
# print(dataset.keys())
dataset = dataset[['Invoice Amount', 'Eligible Amount', 'Invoice Date']]

today = datetime.datetime.today()
lastweek = today - datetime.timedelta(days=24)
dataset['Invoice Date'] = pd.to_datetime(dataset['Invoice Date'])
dataset = dataset[(dataset['Invoice Date'] >= lastweek)]

dataset['Day of Week'] = dataset['Invoice Date'].dt.day_name()

dataset = dataset.groupby(['Day of Week']).sum()
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
#Sortimi ne baze te diteve
dataset.index = pd.CategoricalIndex(dataset.index, categories=days, ordered=True)
dataset = dataset.sort_index()

fig, ax = plt.subplots()
dataset['Invoice Amount'].plot(kind='bar', color='magenta')
dataset['Eligible Amount'].plot(kind='line', marker='.', color='black', ms=10)

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()
## order index by ordercriteria on days

