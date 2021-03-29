import os
from flask import Flask

app = Flask(__name__)


with open('zip-data.txt') as f:
    zipcodes = {}
    for line in f.readlines():
        data = line.split(',')
        zipcodes[data[0].strip()] = data[1:]


@app.route('/<zipcode>/')
def get_coordinate(zipcode):
    return str(zipcodes[zipcode])


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6738))
    app.run(host='0.0.0.0', port=port)
