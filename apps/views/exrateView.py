from apps import db
from apps.models.excurrency import ExchangeCurrency
from apps.models.exrate import ExchangeRate
from apps.views import http_response, is_exist_currency, get_currency, to_date
from datetime import timedelta
from flask import request, jsonify
from flask.views import MethodView


class ExchangeRateView(MethodView):

    # # # # # REQUEST HTTP METHOD # # # # #

    def get(self):
        date = request.args.get('date')
        if date is None:
            return http_response('Parameter needed!', 400)
        else:
            return self.find_rates_by_date(date)

    def post(self):
        from_currency = request.json['from']
        to_currency = request.json['to']
        rate = request.json['rate']
        date = request.json['date']
        date = to_date(date)

        exrate = ExchangeRate(date, rate)

        if is_exist_currency(from_currency, to_currency):
            self.do_create_exist(from_currency, to_currency, exrate)
        else:
            self.do_create_new(from_currency, to_currency, exrate)
        return http_response('Data Created!', 200)

    # # # # # HELPER METHOD # # # # #

    @staticmethod
    def do_create_exist(from_currency, to_currency, exrate):
        excurrency = get_currency(from_currency, to_currency)
        exrate.currency_id = excurrency.id
        db.session.add(exrate)
        db.session.commit()

    @staticmethod
    def do_create_new(from_currency, to_currency, exrate):
        excurrency = ExchangeCurrency(from_currency, to_currency)
        excurrency.exrates.append(exrate)
        db.session.add(excurrency)
        db.session.commit()

    def find_rates_by_date(self, date):
        date = to_date(date)
        currencies = ExchangeCurrency.query.all()
        response = {}
        for currency in currencies:
            response["exchange_rates"] = {
                'from': currency.from_currency,
                'to': currency.to_currency,
                'rate': str(self.get_rate(date, currency.id)),
                'average': str(self.get_average(date, currency.id))
            }
        return jsonify(response)

    def get_average(self, date, currency_id):
        exrates = self.find_rate_between(date, currency_id)
        sum_rate = self.get_sum_rate(exrates)
        if len(exrates) == 7:
            return sum_rate / 7
        else:
            return "insufficient data"

    @staticmethod
    def get_sum_rate(exrates):
        sum_rate = 0.00
        for exrate in exrates:
            sum_rate = sum_rate + float(exrate.rate)
        return sum_rate

    @staticmethod
    def get_rate(date, currency):
        exrates = ExchangeRate.query.filter_by(date=date, currency_id=currency).first()
        if exrates is None:
            return "insufficient data"
        else:
            return exrates.rate

    @staticmethod
    def find_rate_between(param_date, currency_id):
        past_date = param_date - timedelta(days=7)
        exrates = ExchangeRate.query.filter(ExchangeRate.currency_id == currency_id,
                                            ExchangeRate.date.between(past_date, param_date)
                                            ).all()
        return exrates
