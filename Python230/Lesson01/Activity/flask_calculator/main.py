import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = b'\xb5u\x0e\xe4\xf2\xc3\xc2\n\x17\xd0#\xf1\x88\x94@\xc1:\x88"\x10\xba\x1f\x15\xb5\xda\xed\xca\xf9H>0\x00\x1bB'

@app.route('/add', methods=['GET', 'POST'])
def add():

    if 'total' not in session:
        session['total'] = 0

    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number
    return render_template('add.jinja2', session=session)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
