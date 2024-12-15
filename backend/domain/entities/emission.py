from infra.db.database import db


class Emission(db.Model):
    __tablename__ = 'emissions'

    id = db.Column(db.Integer, primary_key=True)
    travel_id = db.Column(db.Integer, db.ForeignKey('travels.id'), nullable=False)
    outbound_emission = db.Column(db.Float, nullable=False)
    return_emission = db.Column(db.Float, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
