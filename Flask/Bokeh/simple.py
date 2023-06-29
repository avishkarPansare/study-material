import numpy as np
from bokeh.plotting import figure , show ,ColumnDataSource
import pandas as pd
#
# x = [1, 2, 3, 4, 5]
# random = np.random.standard_normal(5)
# cosine = np.cos(x)
#
# p = figure()
# p.circle(x=x, y=random,size=20)
# p.line(x=x, y=random)




data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

source = ColumnDataSource(data=data)
p = figure()
p.circle(x='x_values', y='y_values', source=source,size=10)
p.line(x='x_values', y='y_values', source=source)

# show(p)

# ---------------------------------------------------------------------------------------
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin

n = 50000
x = np.random.standard_normal(n)
y = np.random.standard_normal(n)

bins = hexbin(x, y, 0.010)

p = figure( match_aspect=True, background_fill_color='#440154')
p.grid.visible = False

p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
           fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

# show(p)

# -----------------------------------------------------------------------------------
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap, factor_mark

from bokeh.sampledata.iris import flowers  # This for source of data
print(flowers)

SPECIES = ['setosa', 'versicolor', 'virginica']
MARKERS = ['hex', 'circle_x', 'triangle']

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Sepal Width'

p.scatter("petal_length", "sepal_width", source=flowers, legend_field="species", fill_alpha=0.4, size=12,
          marker=factor_mark('species', MARKERS, SPECIES),
          color=factor_cmap('species', 'Category10_3', SPECIES))

# show(p)
# -------------------------------------------------------------------------------
# IndexFilter
from bokeh.layouts import gridplot
from bokeh.models import CDSView, ColumnDataSource, IndexFilter
from bokeh.plotting import figure, show

source = ColumnDataSource(data=dict(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]))
view = CDSView(source=source, filters=[IndexFilter([0, 2, 4])])

tools = ["box_select", "hover", "reset"]
p = figure(height=300, width=300, tools=tools)
p.circle(x="x", y="y", size=10, hover_color="red", source=source)

p_filtered = figure(height=300, width=300, tools=tools)
p_filtered.circle(x="x", y="y", size=10, hover_color="red", source=source, view=view)

# show(gridplot([[p, p_filtered]]))
# -------------------------------------------------------------
# BooleanFilter
from bokeh.layouts import gridplot
from bokeh.models import BooleanFilter, CDSView, ColumnDataSource
from bokeh.plotting import figure, show

source = ColumnDataSource(data=dict(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]))
booleans = [True if y_val > 2 else False for y_val in source.data['y']]
view = CDSView(source=source, filters=[BooleanFilter(booleans)])

tools = ["box_select", "hover", "reset"]
p = figure(height=300, width=300, tools=tools)
p.circle(x="x", y="y", size=10, hover_color="red", source=source)

p_filtered = figure(height=300, width=300, tools=tools,
                    x_range=p.x_range, y_range=p.y_range)
p_filtered.circle(x="x", y="y", size=10, hover_color="red", source=source, view=view)

# show(gridplot([[p, p_filtered]]))
# -----------------------------------------------------------
# GroupFilter
from bokeh.layouts import gridplot
from bokeh.models import CDSView, ColumnDataSource, GroupFilter
from bokeh.plotting import figure, show
from bokeh.sampledata.iris import flowers

source = ColumnDataSource(flowers)
view1 = CDSView(source=source, filters=[GroupFilter(column_name='species', group='versicolor')])

plot_size_and_tools = {'height': 300, 'width': 300,
                        'tools':['box_select', 'reset', 'help']}

p1 = figure(title="Full data set", **plot_size_and_tools)
p1.circle(x='petal_length', y='petal_width', source=source, color='black')

p2 = figure(title="Setosa only", x_range=p1.x_range, y_range=p1.y_range, **plot_size_and_tools)
p2.circle(x='petal_length', y='petal_width', source=source, view=view1, color='red')

# show(gridplot([[p1, p2]]))
# --------------------------------------------------------
# AjaxDataSource
from bokeh.models.sources import AjaxDataSource
# setup AjaxDataSource with URL and polling interval
p = figure()
source = AjaxDataSource(data_url='http://some.api.com/data',
                        polling_interval=100)

# use the AjaxDataSource just like a ColumnDataSource
p.circle('x', 'y', source=source)
# show(p)
# ------------------------------------------
# Linked selection
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

output_file("brushing.html")

x = list(range(-20, 21))
y0 = [abs(xx) for xx in x]
y1 = [xx**2 for xx in x]

# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

TOOLS = "box_select,lasso_select,help"

# create a new plot and add a renderer
left = figure(tools=TOOLS, width=300, height=300, title=None)
left.circle('x', 'y0', source=source)

# create another new plot and add a renderer
right = figure(tools=TOOLS, width=300, height=300, title=None)
right.circle('x', 'y1', source=source)

p = gridplot([[left, right]])

# show(p)
# -----------------------------------------------------------------------
# Linked selection with filtered data
from bokeh.layouts import gridplot
from bokeh.models import BooleanFilter, CDSView, ColumnDataSource
from bokeh.plotting import figure, output_file, show

output_file("linked_selection_subsets.html")

x = list(range(-20, 21))
y0 = [abs(xx) for xx in x]
y1 = [xx**2 for xx in x]

# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

# create a view of the source for one plot to use
view = CDSView(source=source, filters=[BooleanFilter([True if y > 250 or y < 100 else False for y in y1])])

TOOLS = "box_select,lasso_select,hover,help"

# create a new plot and add a renderer
left = figure(tools=TOOLS, width=300, height=300, title=None)
left.circle('x', 'y0', size=10, hover_color="firebrick", source=source)

# create another new plot, add a renderer that uses the view of the data source
right = figure(tools=TOOLS, width=300, height=300, title=None)
right.circle('x', 'y1', size=10, hover_color="firebrick", source=source, view=view)

p = gridplot([[left, right]])

show(p)