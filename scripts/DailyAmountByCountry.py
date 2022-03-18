import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns

dataset = pd.read_excel('Files\InvoiceListReport_TP24_20220307.xlsx')
dataset = dataset[['Invoice Amount','Invoice Date', 'Country']]

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
            sns.lineplot(data=country, x=country.index, y=country['Invoice Amount'],
            ax=ax[i][j], markers=True, dashes=False).ticklabel_format(style='plain', axis='y')
        except:
            # Hide empty plots
            ax[i][j].axis('off')
plt.show()
