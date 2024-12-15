
from domain.entities.condition import Condition
from infra.db.database import db


class ConditionRepository:
    @staticmethod
    def create_condition(travel_id, condition_text):
        condition = Condition(
            travel_id=travel_id,
            condition_text=condition_text
        )
        db.session.add(condition)

    @staticmethod
    def get_conditions_by_travel_id(travel_id):
        return db.session.query(Condition).filter_by(travel_id=travel_id).all()