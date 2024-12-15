from domain.entities.travel import Travel
from infra.db.database import db


class TravelRepository:
    @staticmethod
    def create_travel(travel_info):
        travel = Travel(travel_info=travel_info)
        db.session.add(travel)
        db.session.flush()
        return travel

    @staticmethod
    def get_travel_by_id(travel_id):
        return db.session.query(Travel).filter_by(id=travel_id).first()

    @staticmethod
    def get_all_travels():
        return db.session.query(Travel).all()
