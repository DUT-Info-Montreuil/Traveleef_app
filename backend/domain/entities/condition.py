from infra.db.database import db


class Condition(db.Model):
    __tablename__ = 'conditions'

    id = db.Column(db.Integer, primary_key=True)
    travel_id = db.Column(db.Integer, db.ForeignKey('travels.id'), nullable=False)
    condition_text = db.Column(db.String(255), nullable=False)
