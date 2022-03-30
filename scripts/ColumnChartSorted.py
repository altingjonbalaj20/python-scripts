import pandas as pd
import matplotlib.pyplot as plt
import datetime

dataset = pd.read_excel('Files\Qualifying_Invoice_11_02_2022_09_28_21.xlsx')
# print(dataset.keys())
dataset = dataset[['Invoice Amount', 'Invoice Date']]

today = datetime.datetime.today()
lastweek = today - datetime.timedelta(days=40)
dataset['Invoice Date'] = pd.to_datetime(dataset['Invoice Date'])

dataset['Day of Week'] = dataset['Invoice Date'].dt.day_name()

dataset = dataset.groupby(['Day of Week']).sum()
print(dataset.index)
days = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday']
#Sortimi ne baze te diteve
orderCriteria = pd.CategoricalIndex(days, categories=days, ordered=True)
dataset = dataset.reindex(orderCriteria, fill_value = 0)

dataset = dataset.sort_values(['Invoice Amount'], ascending=False)

fig, ax = plt.subplots()
dataset['Invoice Amount'].plot(kind='bar', color='')

plt.ticklabel_format(style='plain', axis='y')
ax.legend(loc = 'upper left', bbox_to_anchor =(0.65, 1.25), frameon=False)
plt.tight_layout()
plt.show()
## order index by ordercriteria on days

