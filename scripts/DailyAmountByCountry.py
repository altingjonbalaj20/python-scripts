from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
import datetime

dataset = pd.read_excel('Files\InvoiceListReport_TP24_20220324.xlsx')
dataset = dataset[['Invoice Amount','Invoice Date', 'Country']]

today = datetime.datetime.today()
lastweek = today - datetime.timedelta(days=40)
dataset['Invoice Date'] = pd.to_datetime(dataset['Invoice Date'])
dataset = dataset[(dataset['Invoice Date'] >= lastweek)]

dataset = dataset.groupby(['Country'])
# renditja e shteve ne baze te Invoice Amount, dhe marrja e 8 shteteve te para
countries = dataset.sum().sort_values(['Invoice Amount'], ascending = False).head( 4 )
countries = list(countries.index)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']

for i in range(0, len(countries)):
    countryName = countries[i]
    country = dataset.get_group(countryName)
    country['Invoice Date'] = pd.to_datetime(country['Invoice Date'])
    country[countryName] = country['Invoice Date'].dt.day_name()
    country = country.groupby(countryName).sum()
    # renditja ne baze te diteve me radhe, dhe emertimi i index per paraqitje tek vizualizimi
    orderCriteria = pd.CategoricalIndex(days, days, ordered=True, name=countryName)
    country = country.reindex(orderCriteria, fill_value = 0)
    countries[i] = country
columns = 2;
rows = math.ceil(len(countries) / columns)
fig, ax = plt.subplots(nrows = rows, ncols = columns)

for i in range(0, rows):
    for j in range(0, columns):
        try:
            country = countries[i*columns + j]
            g2 = sns.lineplot(data=country, x=country.index, y=country['Invoice Amount'],
            ax=ax[i][j], markers=True, dashes=False)
            g2.set(xticklabels=[])
            g2.set(title=country.index.name)
            g2.set(xlabel=None)
            g2.ticklabel_format(style='plain', axis='y')
        except:
            # Hide empty plots
            ax[i][j].set_axis_off()
plt.tight_layout()
plt.show()
