from flask import Flask, request, jsonify

import io
import json
from json import JSONDecodeError
import urllib.parse

from flask import Flask, Response, request

import matplotlib.pyplot as plt
from matplotlib import ticker, cm, patheffects
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG

from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'public/fonts/NotoSansJP-Regular.otf', size=12)

from numpy import ma

from sympy import *

from copy import copy
import time

import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

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


def to_svg(fig):
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return output.getvalue()


def to_png(fig):
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return output.getvalue()


# First
@app.route("/ex0.svg")
def ex0():
    figure, axis = plt.subplots()
    axis.plot([0,1,2,3], [0,20,40,60])
#    plt.show()
    return Response(to_svg(figure), mimetype="image/svg+xml")


# with Param
@app.route("/ex1.svg")
def ex1():
    data_string = request.args.get('data')
    unquoted_data_string2 = urllib.parse.unquote(data_string)

    fig, ax = plt.subplots()
    if unquoted_data_string2:
        try:
            data = json.loads(unquoted_data_string2)
            ax.plot(data['x'], data['y'])
        except JSONDecodeError as e:
            return Response("<div>JSONDecodeError</div>", mimetype="text/html")
        except AttributeError as e:
            return Response("<div>AttributeError</div>", mimetype="text/html")

    return Response(to_svg(fig), mimetype="image/svg+xml")


# Full Element
@app.route("/ex2.svg")
def ex2():
    x = np.linspace(0, 2, 100)

    fig, ax = plt.subplots()
    ax.plot(x, x, label='??????')
    ax.plot(x, x ** 2, label='??????')
    ax.plot(x, x ** 3, label='??????')
    ax.set_xlabel('X???????????????')
    ax.set_ylabel('Y???????????????')
    ax.set_title("????????????")
    ax.legend()

    return Response(to_svg(fig), mimetype="image/svg+xml")


# Full Element ??????
@app.route("/ex2k.svg")
def ex2k():
    x = np.linspace(0, 2, 100)

    fig, ax = plt.subplots()
    ax.plot(x, x, label='??????')
    ax.plot(x, x ** 2, label='??????')
    ax.plot(x, x ** 3, label='??????')
    ax.set_xlabel('X???????????????', fontproperties=fp)
    ax.set_ylabel('Y???????????????', fontproperties=fp)
    ax.set_title("????????????", fontproperties=fp)
    ax.legend(['??????', '??????', '??????'], prop=fp)

    return Response(to_svg(fig), mimetype="image/svg+xml")


# Multi
@app.route("/ex3.svg")
def ex3():
    fig, ax1 = plt.subplots(1, 1)
    ax1.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax1.plot([1, 2, 3, 4], [4, 3, 4, 1], color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)

    return Response(to_svg(fig), mimetype="image/svg+xml")


# Line
@app.route("/linspace.png")
def llinspace_png():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot([0, 1], [0, 1], label="Line", path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])

    nx = 101
    x = np.linspace(0.0, 1.0, nx)
    y = 0.3 * np.sin(x * 8) + 0.4
    ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

    ax.legend()

    return Response(to_png(fig), mimetype="image/png")


#
@app.route("/barchart.svg")
def barchart_svg():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, men_means, width, label='Men')
    rects2 = ax.bar(x + width / 2, women_means, width, label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    return Response(to_svg(fig), mimetype="image/svg+xml")


@app.route("/contourf.svg")
def contourf_svg():
    N = 100
    x = np.linspace(-3.0, 3.0, N)
    y = np.linspace(-2.0, 2.0, N)

    X, Y = np.meshgrid(x, y)

    Z1 = np.exp(-X ** 2 - Y ** 2)
    Z2 = np.exp(-(X * 10) ** 2 - (Y * 10) ** 2)
    z = Z1 + 50 * Z2

    z[:5, :5] = -1

    z = ma.masked_where(z <= 0, z)

    fig, ax = plt.subplots()
    cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

    cbar = fig.colorbar(cs)

    return Response(to_svg(fig), mimetype="image/svg+xml")


@app.route("/histogram.svg")
def histogram_svg():
    fig, axes = plt.subplots(nrows=3, figsize=(6, 8), constrained_layout=True)

    num_series = 1000
    num_points = 100
    SNR = 0.10
    x = np.linspace(0, 4 * np.pi, num_points)

    Y = np.cumsum(np.random.randn(num_series, num_points), axis=-1)

    num_signal = int(round(SNR * num_series))
    phi = (np.pi / 8) * np.random.randn(num_signal, 1)
    Y[-num_signal:] = (np.sqrt(np.arange(num_points))[None, :] * (np.sin(x[None, :] - phi) + 0.05 * np.random.randn(num_signal, num_points)))

    tic = time.time()
    axes[0].plot(x, Y.T, color="C0", alpha=0.1)
    toc = time.time()
    axes[0].set_title("Line plot with alpha")

    tic = time.time()

    num_fine = 800
    x_fine = np.linspace(x.min(), x.max(), num_fine)
    y_fine = np.empty((num_series, num_fine), dtype=float)
    for i in range(num_series):
        y_fine[i, :] = np.interp(x_fine, x, Y[i, :])
    y_fine = y_fine.flatten()
    x_fine = np.matlib.repmat(x_fine, num_series, 1).flatten()

    cmap = copy(plt.cm.plasma)
    cmap.set_bad(cmap(0))
    h, xedges, yedges = np.histogram2d(x_fine, y_fine, bins=[400, 100])
    pcm = axes[1].pcolormesh(xedges, yedges, h.T, cmap=cmap, norm=LogNorm(vmax=1.5e2), rasterized=True)
    fig.colorbar(pcm, ax=axes[1], label="# points", pad=0)
    axes[1].set_title("2d histogram and log color scale")

    pcm = axes[2].pcolormesh(xedges, yedges, h.T, cmap=cmap, vmax=1.5e2, rasterized=True)
    fig.colorbar(pcm, ax=axes[2], label="# points", pad=0)
    axes[2].set_title("2d histogram and linear color scale")

    toc = time.time()

    return Response(to_svg(fig), mimetype="image/svg+xml")


@app.route("/ex1s.svg")
def ex1s():
    data_string = request.args.get('data')

    fig, ax = plt.subplots()
    ax.set_xlabel('X???????????????', fontproperties=fp)
    ax.set_ylabel('Y???????????????', fontproperties=fp)
    ax.set_title("????????????", fontproperties=fp)

    if data_string:
        unquoted_data_string = urllib.parse.unquote(data_string)
        try:
            data = json.loads(unquoted_data_string)
            x = [i for i in range(len(data))]
            ax.plot(x, data, label='?????????')
        except Exception as e:
            return Response("<div>" + e.msg + "</div>", mimetype="text/html")

    ax.legend(['?????????'], prop=fp)

    return Response(to_svg(fig), mimetype="image/svg+xml")


@app.route("/mplot3d.svg")
def mplot3d():

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import cm
    from mpl_toolkits.mplot3d import Axes3D

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    fig = plt.figure()
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

    return Response(to_svg(fig), mimetype="image/svg+xml")

@app.route("/oneshot.svg")
def oneshot():
    import numpy as np
    np.random.seed(19680801)
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    for color in ['tab:blue', 'tab:orange', 'tab:green']:
        n = 750
        x, y = np.random.rand(2, n)
        scale = 200.0 * np.random.rand(n)
        ax.scatter(x, y, c=color, s=scale, label=color,alpha=0.3, edgecolors='none')

    ax.legend()
    ax.grid(True)

    return Response(to_svg(fig), mimetype="image/svg+xml")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
