from apps import app
from apps.views import EXRATES_ENDPOINT
from flask import json
import unittest


class ExchangeRateTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_create_rates(self):
        response = self.insert_data('IDR', 'USD', '2018-07-22', 2000)
        self.do_test(response, 'Data Created!', 200)

    def test_findby_date(self):
        response = self.find_by_date('2018-07-22')
        data = json.loads(response.get_data())
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(data['exchange_rates']['from'], 'IDR')
        self.assertEqual(data['exchange_rates']['to'], 'USD')
        self.assertEqual(float(data['exchange_rates']['rate']), 2000)
        self.assertEqual(data['exchange_rates']['average'], 'insufficient data')
        self.assertEqual(response.status_code, 200)

    def test_findby_date_no_param(self):
        response = self.app.get(EXRATES_ENDPOINT)
        self.do_test(response, 'Parameter needed!', 400)

    def do_test(self, response, response_message, status_code):
        data = json.loads(response.get_data())
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(data['message'], response_message)
        self.assertEqual(response.status_code, status_code)

    def insert_data(self, from_currency, to_currency, date, rate):
        data = {
            'from': from_currency,
            'to': to_currency,
            'date': date,
            'rate': rate
        }
        return self.app.post(
            EXRATES_ENDPOINT,
            data=json.dumps(data),
            content_type='application/json',
            follow_redirects=True
        )

    def find_by_date(self, date):
        return self.app.get(EXRATES_ENDPOINT + '?date=' + date)
