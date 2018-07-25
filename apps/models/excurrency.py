from apps import db


class ExchangeCurrency(db.Model):
    __tablename__ = 'exchange_currencies'

    id = db.Column(db.Integer, primary_key=True)
    from_currency = db.Column(db.String(3))
    to_currency = db.Column(db.String(3))
    exrates = db.relationship("ExchangeRate", backref="currencies", cascade='all')

    def __init__(self, from_currency, to_currency):
        self.from_currency = from_currency
        self.to_currency = to_currency

    def __repr__(self):
        return '%d %s %s' %(self.id, self.from_currency, self.to_currency)