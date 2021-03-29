import os
import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_time():
    epoch_time = time.time()

    return str(epoch_time)
    # return f'{epoch_time}'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6738))
    app.run(host='0.0.0.0', port=port)
