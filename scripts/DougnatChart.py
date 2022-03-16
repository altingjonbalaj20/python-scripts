import pandas as pd
import matplotlib.pyplot as plt
import datetime

dataset = pd.read_excel('Files\Qualifying_Invoice_11_02_2022_09_28_21.xlsx')

dataset = dataset[['Eligible']]

dataset = dataset.groupby(['Eligible'], as_index=False)['Eligible'].count()
print(dataset.index)
dataset.rename(index={1:'Eligible', 0:'Not Eligible'}, inplace=True)

plt.pie(dataset['Eligible'], colors=['#515A5A', '#5DADE2'], autopct='%1.2f%%', pctdistance=1.2)
# add a circle at the center to transform it in a donut chart
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(dataset.index, frameon=False)
plt.show()


print(dataset)