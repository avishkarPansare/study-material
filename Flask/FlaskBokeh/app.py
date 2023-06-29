from flask import Flask
from flask import render_template
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.layouts import gridplot ,layout
from bokeh.models import BoxSelectTool,PointDrawTool ,WheelZoomTool,ZoomInTool,ZoomOutTool,HoverTool
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/dashboard/')
def show_dashboard():
    plots = []
    plots.append(make_plot())

    return render_template('dashboard.html', plots=plots)

def make_plot():
    from bokeh.io import curdoc
    curdoc().theme = 'dark_minimal'
    plot = figure(plot_height=200, sizing_mode='scale_width')
    plot2 = figure(plot_height=200, sizing_mode='scale_width')

    x = []
    y = []
    y2 = []
    for i in range(0, 100):
        n = np.random.randint(1, 5)
        n2 = np.random.randint(1, 5)
        x.append(i)
        y.append(i * n2)

        y2.append(i * n)
    # x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # y = [2**v for v in x]
    # y2 = [3**v for v in x]

    plot2.line(x, y, line_width=4,line_color="red")
    plot2.line(x, y2, line_width=4,line_color="blue")
    plot.line(x, y, line_width=4, line_color="red")
    plot.line(x, y2, line_width=4, line_color="blue")

    plot.add_tools(ZoomInTool())
    plot.add_tools(ZoomOutTool())
    plot.add_tools(HoverTool())
    grid = layout([
        [plot2],
        [plot,plot2],
    ])
    # grid = gridplot([[plot, plot2], [None, plot]], width=250, height=250)
    script, div = components(grid)
    return script, div

if __name__ == '__main__':
    # socketio.run(app,DEBUG=True)
    app.run(host='0.0.0.0', port=8001,debug=True)
