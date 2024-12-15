from domain.entities.travel import Travel
from infra.db.database import db


class TravelRepository:
    @staticmethod
    def create_travel(travel_info,  partner_url, price_outbound=None, price_round_trip=None, travel_type=None):
        travel = Travel(
            travel_info=travel_info,
            partner_url=partner_url,
            price_outbound=price_outbound,
            price_round_trip=price_round_trip,
            travel_type=travel_type
        )
        db.session.add(travel)
        db.session.flush()
        return travel

    @staticmethod
    def get_travel_by_id(travel_id):
        return db.session.query(Travel).filter_by(id=travel_id).first()

    @staticmethod
    def get_all_travels():
        return db.session.query(Travel).all()
