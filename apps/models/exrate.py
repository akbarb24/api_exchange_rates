from apps import db


class ExchangeRate(db.Model):
    __tablename__ = 'exchange_rates'

    id = db.Column(db.Integer, primary_key=True)
    currency_id = db.Column(db.Integer, db.ForeignKey('exchange_currencies.id'), nullable=False)
    date = db.Column(db.Date)
    rate = db.Column(db.Float(asdecimal=True))

    def __init__(self, date, rate):
        self.date = date
        self.rate = rate

    def __repr__(self):
        return '%d %d %s %f' %(self.id, self.currency_id, self.date, self.rate)