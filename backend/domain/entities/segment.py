from infra.db.database import db


class Segment(db.Model):
    __tablename__ = 'segments'

    id = db.Column(db.Integer, primary_key=True)
    travel_id = db.Column(db.Integer, db.ForeignKey('travels.id'), nullable=False)
    segment_type = db.Column(db.String(50), nullable=False)  # 'outbound' ou 'return'
    flight_date = db.Column(db.Date, nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    departure_location = db.Column(db.String(255), nullable=False)
    arrival_time = db.Column(db.Time, nullable=False)
    arrival_location = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    logo_url = db.Column(db.String(255), nullable=True)
