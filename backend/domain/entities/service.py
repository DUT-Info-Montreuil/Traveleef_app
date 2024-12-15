from infra.db.database import db


class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    travel_id = db.Column(db.Integer, db.ForeignKey('travels.id'), nullable=False)
    service_text = db.Column(db.String(255), nullable=False)
