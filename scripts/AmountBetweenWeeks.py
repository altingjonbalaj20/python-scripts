from matplotlib.transforms import Bbox
import pandas as pd
import matplotlib.pyplot as plt
import datetime

dataset = pd.read_excel('Files\InvoiceListReport_TP24_20220307.xlsx')
# print(dataset.keys())
dataset = dataset[['Invoice Amount','Invoice Date']]

today = datetime.datetime.today()
lastweek = today - datetime.timedelta(days=40)
twoWeeksBefore = lastweek - datetime.timedelta(days=7)
dataset['Invoice Date'] = pd.to_datetime(dataset['Invoice Date'])
lastweekData = dataset[(dataset['Invoice Date'] >= lastweek)]
twoWeeksBeforeData = dataset[(dataset['Invoice Date'] <= lastweek) & (dataset['Invoice Date'] >= twoWeeksBefore)]
del lastweek, twoWeeksBefore, dataset

lastweekData['Day of Week'] = lastweekData['Invoice Date'].dt.day_name()
twoWeeksBeforeData['Day of Week'] = twoWeeksBeforeData['Invoice Date'].dt.day_name()

lastweekData = lastweekData.groupby(['Day of Week']).sum()
twoWeeksBeforeData = twoWeeksBeforeData.groupby(['Day of Week']).sum()

lastweekData.rename(columns={'Invoice Amount':'Current Week Amount'}, inplace=True)
twoWeeksBeforeData.rename(columns={'Invoice Amount':'Last Week Amount'}, inplace=True)

fig, ax = plt.subplots(figsize=(20,10))
lastweekData['Current Week Amount'].plot(kind='line', color='lightblue', ms=20, linewidth=2)
twoWeeksBeforeData['Last Week Amount'].plot(kind='line', color='lightgreen', ms=20, linewidth=2)

plt.ticklabel_format(style='plain', axis='y')
ax.legend( bbox_to_anchor =(0.65,1.25), frameon=False)
plt.tight_layout()
plt.show()
## order index by ordercriteria on days

