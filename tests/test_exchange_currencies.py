from apps import app
from apps.views import EXCURRENCIES_ENDPOINT
from flask import json
import unittest


class ExchangeCurrencyTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_create_currency(self):
        response = self.insert_data('IDR', 'USD')
        self.do_test(response, 'Data Created!', 200)

    def test_delete_currency(self):
        response = self.delete_data('IDR', 'USD')
        self.do_test(response, 'Data Deleted!', 200)

    def test_delete_no_param(self):
        response = self.app.delete(EXCURRENCIES_ENDPOINT)
        self.do_test(response, 'Parameter needed!', 400)

    def do_test(self, response, response_message, status_code):
        data = json.loads(response.get_data())
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(data['message'], response_message)
        self.assertEqual(response.status_code, status_code)

    def insert_data(self, from_currency, to_currency):
        data = {'from': from_currency, 'to': to_currency}
        return self.app.post(
            EXCURRENCIES_ENDPOINT,
            data=json.dumps(data),
            content_type='application/json',
            follow_redirects=True
        )

    def delete_data(self, from_currency, to_currency):
        return self.app.delete(EXCURRENCIES_ENDPOINT + '?from=%s&to=%s' % (from_currency, to_currency))
