from bokeh.io import output_file, show
from bokeh.models import FactorRange
from bokeh.plotting import figure
import numpy as np
output_file("mutiLine.html")
x = []
y = []
y2= []
for i in range(0,100):
    n = np.random.randint(1,5)
    n2 = np.random.randint(1, 5)
    x.append(i)
    y.append(i*n2)

    y2.append(i*n)
# x = np.random.randint(low = 0,high=20,size=10)
# random = np.random.randint(low = 0,high=20,size=10)
# random2 = np.random.randint(low = 0,high=20,size=10)

# cosine = np.cos(x)
#
p = figure()
p.line(x=x, y=y,line_color='black', line_width=2)
# p.circle(x=x, y=y ,size=10)

p.line(x=x, y=y2,line_color='red', line_width=2)
show(p)


