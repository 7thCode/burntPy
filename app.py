from flask import Flask, request, jsonify

from sympy import *
from sympy.abc import *

from fibmodule import py_fib

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
