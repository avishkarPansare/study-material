from bokeh.server.server import Server
from bokeh.models import ColumnDataSource, Label
from bokeh.plotting import figure
from bokeh.layouts import column
import numpy as np
import datetime as dt
from functools import partial
import time


def f_random():
    data = np.random.rand()
    data = (dt.datetime.now(), data)
    return data


def f_sinewave():
    data = np.sin(time.time()/1.)
    data = (dt.datetime.now(), data)
    return data


def make_document(doc, functions, labels):
    def update():
        for index, func in enumerate(functions):
            data = func()
            sources[index].stream(new_data=dict(time=[data[0]], data=[data[1]]), rollover=1000)
            annotations[index].text = f'{data[1]: .3f}'

    sources = [ColumnDataSource(dict(time=[], data=[])) for _ in range(len(functions))]
    figs = []
    annotations = []
    for i in range(len(functions)):
        figs.append(figure(x_axis_type='datetime', plot_width=800, plot_height=400, y_axis_label=labels[i]))
        figs[i].line(x='time', y='data', source=sources[i])
        annotations.append(Label(x=10, y=200, text='', text_font_size='20px', text_color='black',
                                 x_units='screen', y_units='screen', background_fill_color='white'))
        figs[i].add_layout(annotations[i])

    doc.add_root(column([fig for fig in figs], sizing_mode='stretch_both'))
    doc.add_periodic_callback(callback=update, period_milliseconds=100)


if __name__ == '__main__':
    # list of functions and labels to feed into the scope
    functions = [f_random, f_sinewave]
    labels = ['random', 'sinewave']

    server = Server({'/': partial(make_document, functions=functions, labels=labels)})
    server.start()
    server.io_loop.add_callback(server.show, "/")
    try:
        server.io_loop.start()
    except KeyboardInterrupt:
        print('keyboard interruption')