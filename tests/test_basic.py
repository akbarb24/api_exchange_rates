from apps import app, db
import unittest


class BasicTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)