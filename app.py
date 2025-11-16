from flask import Flask, render_template
import requests

app = Flask(__name__)

all_currency_pretty_name = requests.get(
    'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json').json()


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/all_currency_in_euro')
def all_currency_in_euro():
    request = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json")

    date = request.json()['date']
    currency = request.json()['eur']

    for currency_short_name, currency_pretty_name in all_currency_pretty_name.items():
        currency[currency_short_name] = [currency_pretty_name, currency[currency_short_name]]

    return render_template("all_currency_in_euro.html", date=date, currency=currency)


if __name__ == '__main__':
    app.run()
