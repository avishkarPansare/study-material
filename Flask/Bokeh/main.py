from bokeh.plotting import  figure,output_file,show , save
from bokeh.models import BoxSelectTool,PointDrawTool ,WheelZoomTool,ZoomInTool,ZoomOutTool

x= [1,2,3,4,5,6,7,8,9,10]
y= [5,12,3,4,23,6,7,8,9,10]

output_file("index.html")

p = figure(
    title = "Bokeh Ploting",
    x_axis_label = "X Axis",
    y_axis_label="Y Axis",

)
p.line(x,y,legend="Test",line_width=2)
# show(p)

# ----------------------------------------------------------------
p2 = figure(width=400, height=400,
           title=None, toolbar_location="below",tools = "pan,wheel_zoom,box_zoom,reset")
p2.add_tools(BoxSelectTool(dimensions="width"))

p2.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)
# show(p2)



# ---------------------------------------------------------------------
TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),

]
p3 = figure(
    width=400,
    height=400,
    title=None,
    toolbar_location="below",
tooltips=TOOLTIPS,
    tools = "pan,wheel_zoom,box_zoom,reset,lasso_select,xpan,ypan,tap,box_select,hover,freehand_draw",

            )

from bokeh.io import curdoc
curdoc().theme = 'dark_minimal'
# p3.add_tools(BoxSelectTool(dimensions="width"))

# configure so that no drag tools are active
# p3.toolbar.active_drag = None

# configure so that Bokeh chooses what (if any) scroll tool is active
# p3.toolbar.active_scroll = "auto"

p3.add_tools(ZoomInTool())
p3.add_tools(ZoomOutTool())
p3.circle([1, 2, 3, 4, 5,2, 5, 8, 2, 7], [2, 5, 8, 2, 7,2, 5, 8, 2, 7], size=10)
show(p3)

# ------------------------------------------------------------
# Save
# save(p)


from bokeh.io import output_file, show
from bokeh.layouts import layout
from bokeh.models import BoxAnnotation, Toggle
from bokeh.plotting import figure

output_file("styling_visible_annotation_with_interaction.html")

p = figure(width=600, height=200, tools='')
p.line([1, 2, 3], [1, 2, 1], line_color="#0072B2")
pink_line = p.line([1, 2, 3], [2, 1, 2], line_color="#CC79A7")

green_box = BoxAnnotation(left=1.5, right=2.5, fill_color='#009E73', fill_alpha=0.1)
p.add_layout(green_box)

# Use js_link to connect button active property to glyph visible property

toggle1 = Toggle(label="Green Box", button_type="success", active=True)
toggle1.js_link('active', green_box, 'visible')

toggle2 = Toggle(label="Pink Line", button_type="success", active=True)
toggle2.js_link('active', pink_line, 'visible')

# show(layout([p], [toggle1, toggle2]))