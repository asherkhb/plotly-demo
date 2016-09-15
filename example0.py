import plotly.plotly as py
from plotly.graph_objs import *

trace0 = Scatter(x=[1,2,3], y=[10,15,13])
trace1 = Scatter(x=[1,2,3], y=[7,8,14])
my_data = Data([trace0, trace1])

my_layout = Layout(title="Example 0", xaxis=dict(title="X"))

my_figure = Figure(data=my_data, layout=my_layout)

py.plot(my_figure, filename='example0')

