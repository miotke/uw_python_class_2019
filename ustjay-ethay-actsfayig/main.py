import os
import requests
from flask import Flask, send_file, Response, render_template, redirect
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def translate(fact):
    """ Translates text into pig latin """

    url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    data = {'input_text': fact}
    resp = requests.post(url, data, allow_redirects=False)
    link = resp.headers['Location']

    return link


@app.route('/', methods=['GET'])
def home():
    fact = get_fact()
    link = translate(fact)

    return render_template('base.html', fact=fact, link=link)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
