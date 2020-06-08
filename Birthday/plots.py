from bokeh.plotting import figure, show, output_file

# we specify an HTML file where the output will go
output_file("plot.html")

# load our x and y data
x = [10, 20, 30]
y = [4, 5, 6]

# create a figure
p = figure()

# create a histogram
p.vbar(x=x, top=y, width=1)

# render (show) the plot
show(p)