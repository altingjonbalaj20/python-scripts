import plotly.graph_objects as go
import matplotlib.pyplot as plt

h = "25;50;75;100"
min = 0
max = 600
distance = max - min

color = "red;yellow;green;cyan"
color = color.split(sep=';')
h = ['0'].__add__(h.split(sep=';'))
ranges = list()
for i in range(len(h) - 1):
    ranges.append([int(h[i])*distance/100 + min, int(h[i+1])*distance/100 + min])

indicator = go.Indicator(
    mode = "gauge+number+delta",
    value = 420,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Speed", 'font': {'size': 24}},
    delta = {'reference': 400, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 500], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [ ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 490}})

steps = list()
for i in range(len(ranges)):
    steps.append({'range': ranges[i], 'color': color[i]})

indicator.__getitem__('gauge').__setitem__('steps', steps)

fig = go.Figure(indicator)
fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
fig.write_image('test.png')
img = plt.imread('test.png')
plt.imshow(img)
plt.show()