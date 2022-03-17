import pandas as pd
import matplotlib.pyplot as plt
import datetime
import math
import numpy as np
import seaborn as sns
import copy

dataset = pd.read_excel('Files\InvoiceListReport_TP24_20220307.xlsx')
dataset = dataset[['Invoice Amount','Invoice Date', 'Country']]

countries = ['Switzerland', 'Italy', 'Germany', 'France', 'Belgium', 'Denmark']
dataset = dataset.groupby(['Country'])
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']

for i in range(0, len(countries)):
    temp = dataset.get_group(countries[i])
    temp['Invoice Date'] = pd.to_datetime(temp['Invoice Date'])
    temp[countries[i]] = temp['Invoice Date'].dt.day_name()
    temp = temp.groupby(countries[i]).sum()
    # renditja ne baze te diteve me radhe, dhe emertimi i index per paraqitje tek vizualizimi
    orderCriteria = pd.CategoricalIndex(days, days, ordered=True, name=countries[i])
    temp = temp.reindex(orderCriteria, fill_value = 0)

    countries[i] = temp
columns = 2;
rows = math.ceil(len(countries) / columns)
fig, ax = plt.subplots(nrows = rows, ncols = columns)

for i in range(0, rows):
    for j in range(0, columns):
        try:
            country = countries[i*columns + j]
            sns.lineplot(data=country, x=country.index, y=country['Invoice Amount'], ax=ax[i][j])
            current_values = ax[i][j].get_yticks()
            ax[i][j].set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
        except:
            # Hide empty plots
            ax[i][j].axis('off')

plt.show()
