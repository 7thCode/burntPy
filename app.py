from flask import Flask, request, jsonify

import io
import random
from flask import Flask, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG

import matplotlib.pyplot as plt
import numpy as np

from numpy import ma
from matplotlib import ticker, cm



from matplotlib.figure import Figure

from sympy import *

app = Flask(__name__, static_folder='./public', static_url_path='')

@app.route('/', methods=['GET'])
def api():
    return app.send_static_file('index.html')

@app.route('/expr1', methods=['POST'])
def expr1():
    num = request.json['num']
    return jsonify({'expr': str(factorint(factorial(num)))})

@app.route('/expr2', methods=['POST'])
def expr2():
    expr = request.json['expr']
    return jsonify({'expr': str(factor(expr))})


@app.route("/plot")
def index():
    num_x_points = int(request.args.get("num_x_points", 50))
    # in a real app you probably want to use a flask template.
    return f"""
    <h1>Flask and matplotlib</h1>
    <h2>Random data with num_x_points={num_x_points}</h2>
    <form method=get action="/plot">
      <input name="num_x_points" type=number value="{num_x_points}" />
      <input type=submit value="update graph">
    </form>
    <h3>Plot as a png</h3>
    <img src="/matplot-as-image-{num_x_points}.png"
         alt="random points as png"
         height="200"
    >
    <h3>Plot as a SVG</h3>
    <img src="/matplot-as-image-{num_x_points}.svg"
         alt="random points as svg"
         height="200"
    >
    """

@app.route("/matplot-as-image-<int:num_x_points>.png")
def plot_png(num_x_points=50):
    """ renders the plot on the fly.
    """
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


@app.route("/matplot-as-image-<int:num_x_points>.svg")
def plot_svg(num_x_points=50):
    """ renders the plot on the fly.
    """
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


@app.route("/barchart.svg")
def plot_svg1(num_x_points=50):



    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Men')
    rects2 = ax.bar(x + width/2, women_means, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()





    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


@app.route("/contourf.svg")
def plot_svg2(num_x_points=50):

    N = 100
    x = np.linspace(-3.0, 3.0, N)
    y = np.linspace(-2.0, 2.0, N)

    X, Y = np.meshgrid(x, y)

    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
    z = Z1 + 50 * Z2

    z[:5, :5] = -1

    z = ma.masked_where(z <= 0, z)

    fig, ax = plt.subplots()
    cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)


    cbar = fig.colorbar(cs)


    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
