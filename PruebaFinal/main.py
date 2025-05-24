from flask import Flask, jsonify, request

app = Flask("__hello__")

@app.route('/', methods='GET')
def hello():
    return 'Hola!'

app.run(host = '201.222.51.207', debug = True, port = 5003)

app.run(host = '0.0.0.0', debug = True, port = 5003)

app.run(debug=True)

