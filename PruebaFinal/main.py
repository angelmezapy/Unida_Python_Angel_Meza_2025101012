from flask import Flask, jsonify, request

app = Flask(__ci__)

@app.route('/', methods='GET')
def ci():
    return 'Hola!'

## app.run (host = '127.0.0.1', debug = true, port = 5003)

app.run(host='0.0.0.0', debug = true, port = 5003)

app.run(debug=true)

