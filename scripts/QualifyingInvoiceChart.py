import pandas as pd
import matplotlib.pyplot as plt
import datetime

dataset = pd.read_excel('Files\Qualifying_Invoice_11_02_2022_09_28_21.xlsx')
# print(dataset.keys())
dataset = dataset[['Invoice Amount', 'Invoice Date']]

today = datetime.datetime.today()

dataset['Invoice Date'] = pd.to_datetime(dataset['Invoice Date'])

dataset['Day of Week'] = dataset['Invoice Date'].dt.day_name()
dataset = dataset.groupby(['Day of Week']).sum()
dataset = dataset.sort_values(['Invoice Amount'])

fig, ax = plt.subplots()
dataset['Invoice Amount'].plot(kind='bar', color='blue')

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()