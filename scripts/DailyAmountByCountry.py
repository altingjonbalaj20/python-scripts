import pandas as pd
import matplotlib.pyplot as plt
import datetime
import math
import numpy as np
import seaborn as sns
import copy

dataset = pd.read_excel('Files\InvoiceListReport_TP24_20220307.xlsx')
dataset = dataset[['Invoice Amount','Invoice Date', 'Country']]

dataset = dataset.groupby(['Country'])
# renditja e shteve ne baze te Invoice Amount, dhe marrja e 8 shteteve te para
countries = dataset.sum().sort_values(['Invoice Amount'], ascending = False).head( 4 )
countries = list(countries.index)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']

for i in range(0, len(countries)):
    countryName = countries[i]
    temp = dataset.get_group(countryName)
    temp['Invoice Date'] = pd.to_datetime(temp['Invoice Date'])
    temp[countryName] = temp['Invoice Date'].dt.day_name()
    temp = temp.groupby(countryName).sum()
    # renditja ne baze te diteve me radhe, dhe emertimi i index per paraqitje tek vizualizimi
    orderCriteria = pd.CategoricalIndex(days, days, ordered=True, name=countryName)
    temp = temp.reindex(orderCriteria, fill_value = 0)
    countries[i] = temp
columns = 2;
rows = math.ceil(len(countries) / columns)
fig, ax = plt.subplots(nrows = rows, ncols = columns)

for i in range(0, rows):
    for j in range(0, columns):
        try:
            country = countries[i*columns + j]
            sns.lineplot(data=country, x=country.index, y=country['Invoice Amount'],
            ax=ax[i][j], markers=True, dashes=False).ticklabel_format(style='plain', axis='y')
        except:
            # Hide empty plots
            ax[i][j].axis('off')
plt.show()
