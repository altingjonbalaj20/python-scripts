from ctypes import alignment
from matplotlib import style
import pandas as pd

#html_content=""" <h3>Process for File: {FileName} has been completed <br>Date: {today}</h3> """.format(**locals()),
dataset = pd.read_excel('Files/Test.xlsx')
html = dataset.to_html(index=False, justify='left', col_space='200px')

# write html to file
text_file = open("Files/index.html", "w")
text_file.write(html)
text_file.close()