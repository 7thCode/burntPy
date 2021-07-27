from flask import Flask, request, jsonify

from sympy import *
from sympy.abc import *

from fibmodule import py_fib

app = Flask(__name__, static_folder='./public', static_url_path='')

@app.route('/', methods=['GET'])
def api():
    return app.send_static_file('index.html')

@app.route('/brython', methods=['GET'])
def brython():
    return app.send_static_file('brython.html')


@app.route('/data-a', methods=['GET'])
def data_a():
    result = [{"title": "商品1","price": 2100},
              {"title": "商品2","price": 2600},
              {"title": "商品3","price": 3400}]
    return jsonify(result)

@app.route('/data-b', methods=['GET'])
def data_b():
    result = [{"title": "商品1","price": 20000},
              {"title": "商品2","price": 1600},
              {"title": "商品3","price": 2000}]
    return jsonify(result)

@app.route('/data-c', methods=['GET'])
def data_c():
    result = [{"title": "商品1","price": 1000},
              {"title": "商品2","price": 2200},
              {"title": "商品3","price": 3100}]
    return jsonify(result)

@app.route('/papi/<name>')
def papi(name):
    return 'Hello!' + name

@app.route('/capi/<int:param>')
def capi(param):
    return str(py_fib(param))

@app.route('/expr1', methods=['POST'])
def expr1():
    num = request.json['num']
    return jsonify({'expr': str(factorint(factorial(num)))})

@app.route('/expr2', methods=['POST'])
def expr2():
    expr = request.json['expr']
    return jsonify({'expr': str(factor(expr))})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
