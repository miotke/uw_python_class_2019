import os
from flask import Flask

app = Flask(__name__)


@app.route('/hello/')
def hello_world():
    return 'Hello world'


@app.route('/hello/<name>/')
def hello_name(name):
    return f'Hello, {name}'


@app.route('/goodbye/<times>/<name>/')
def hello_name_multiple(times, name):
    return f'Hello, {name}'*int(times)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

