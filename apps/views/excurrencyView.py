from apps import app, db
from apps.models.excurrency import ExchangeCurrency
from apps.views import http_response, is_exist_currency, get_currency
from flask import request
from flask.views import MethodView


class ExchangeCurrencyView(MethodView):

    # # # # # REQUEST HTTP METHOD # # # # #

    def post(self):
        from_currency = request.json['from']
        to_currency = request.json['to']
        if not is_exist_currency(from_currency, to_currency):
            return self.do_create(from_currency, to_currency)
        else:
            return http_response('Data exist!', 200)

    def delete(self):
        from_currency = request.args.get('from')
        to_currency = request.args.get('to')
        if from_currency is None and to_currency is None:
            return http_response('Parameter needed!', 400)
        else:
            return self.do_delete(from_currency, to_currency)

    # # # # # HELPER METHOD # # # # #

    @staticmethod
    def do_create(from_currency, to_currency):
        excurrency = ExchangeCurrency(from_currency, to_currency)
        db.session.add(excurrency)
        db.session.commit()
        return http_response('Data Created!', 200)

    @staticmethod
    def do_delete(from_currency, to_currency):
        if is_exist_currency(from_currency, to_currency):
            excurrency = get_currency(from_currency, to_currency)
            db.session.delete(excurrency)
            db.session.commit()
            return http_response('Data Deleted!', 200)
        else:
            return http_response('Data Not Found!', 400)
