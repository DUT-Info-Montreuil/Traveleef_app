
from domain.entities.service import Service
from infra.db.database import db


class ServiceRepository:
    @staticmethod
    def create_service(travel_id, service_text):
        service = Service(
            travel_id=travel_id,
            service_text=service_text
        )
        db.session.add(service)

    @staticmethod
    def get_services_by_travel_id(travel_id):
        return db.session.query(Service).filter_by(travel_id=travel_id).all()
