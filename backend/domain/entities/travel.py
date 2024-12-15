from infra.db.database import db


class Travel(db.Model):
    __tablename__ = 'travels'

    id = db.Column(db.Integer, primary_key=True)
    travel_info = db.Column(db.String(255), nullable=False)
    partner_url = db.Column(db.String(255), nullable=False)
    price_outbound = db.Column(db.Float, nullable=True)
    price_round_trip = db.Column(db.Float, nullable=True)

    emissions = db.relationship('Emission', backref='travel', lazy=True, cascade="all, delete")
    segments = db.relationship('Segment', backref='travel', lazy=True, cascade="all, delete")
    conditions = db.relationship('Condition', backref='travel', lazy=True, cascade="all, delete")
    services = db.relationship('Service', backref='travel', lazy=True, cascade="all, delete")