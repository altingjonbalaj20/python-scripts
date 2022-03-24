import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pathlib

dataset = pd.read_excel('Files\InvoiceListReport_TP24_20220324.xlsx')
# print(dataset.keys())
dataset = dataset[['Invoice Amount', 'Eligible Amount', 'Invoice Date']]

today = datetime.datetime.today()
lastweek = today - datetime.timedelta(days=7)
dataset['Invoice Date'] = pd.to_datetime(dataset['Invoice Date'])
dataset = dataset[(dataset['Invoice Date'] >= lastweek)]

dataset['Day of Week'] = dataset['Invoice Date'].dt.day_name()

dataset = dataset.groupby(['Day of Week']).sum()
days = ['Sunday','Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
#Sortimi ne baze te diteve
orderCriteria = pd.CategoricalIndex(days, categories=days, ordered=True)
dataset = dataset.reindex(orderCriteria, fill_value = 0)

fig, ax = plt.subplots()
dataset['Invoice Amount'].plot(kind='bar', color='blue')
dataset['Eligible Amount'].plot(kind='line', color='lightgreen', ms=10)

plt.ticklabel_format(style='plain', axis='y')
ax.legend(loc='upper left', frameon=False)
plt.tight_layout()
plt.show()
## order index by ordercriteria on days

