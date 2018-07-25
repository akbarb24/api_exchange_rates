from apps import app
from apps.models.excurrency import ExchangeCurrency
from datetime import datetime
from flask import jsonify, Blueprint, make_response

EXCURRENCIES_ENDPOINT = '/currencies'
EXRATES_ENDPOINT = '/rates'


def is_exist_currency(from_currency, to_currency):
    if get_currency(from_currency, to_currency) is None:
        return False
    else:
        return True


def get_currency(from_currency, to_currency):
    currency = ExchangeCurrency.query.filter_by(from_currency=from_currency, to_currency=to_currency).first()
    return currency


def to_date(date):
    return datetime.strptime(date, '%Y-%m-%d')


def http_response(message, status_code):
    return make_response(jsonify(message=message), status_code)


from apps.views.excurrencyView import ExchangeCurrencyView
from apps.views.exrateView import ExchangeRateView

exchange = Blueprint('app', __name__)


@exchange.route('/')
def root():
    return 'Hello Hooman!'


excurrency_view = ExchangeCurrencyView.as_view('currency_view')
exrate_view = ExchangeRateView.as_view('rate_view')
app.add_url_rule(EXCURRENCIES_ENDPOINT, view_func=excurrency_view, methods=['GET', 'POST', 'DELETE'])
app.add_url_rule(EXRATES_ENDPOINT, view_func=exrate_view, methods=['GET', 'POST'])
