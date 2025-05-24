from flask import Flask, jsonify, request

app = Flask("__ci__")

@app.route('/', methods='GET')
def cigit():
    return 'Nro de cédula'

app.run(host = '201.222.51.207', debug = True, port = 5000)

app.run(host = '0.0.0.0', debug = True, port = 5000)

app.run(debug=True)

