import json
from flask import Flask, Response, jsonify, request
from .services import create_orders, retrieve_orders

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/health', methods=['GET'])
def health():
    result = json.dumps({'result': 'Hello, World!'})
    header = {'Content-Type': 'application/json'}
    status_code = 200
    return Response(result, status_code, header)


@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        return jsonify(create_orders(body=request.json))
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == '__main__':
    app.run()
