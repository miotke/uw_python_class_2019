import os
import base64
from flask import Flask, render_template, request, redirect, url_for, session
from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/create/', methods=['GET', 'POST'])
def add_donation():
    if request.method == 'POST':
        donation_value = int(request.form['value'])
        donor_name = request.form['name']

        try:
            donor = Donor.select().where(Donor.name == donor_name).get()
        except Donor.DoesNotExist as e:
            donor = Donor(name=donor_name)
            donation_made.save()
            print(e)

        donation_made = Donation(value=donation_value, donor=donor)
        donation_made.save()
        return redirect(url_for('all'))
    return render_template('create.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
