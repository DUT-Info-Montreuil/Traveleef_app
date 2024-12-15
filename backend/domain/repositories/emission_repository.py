
from domain.entities.emission import Emission
from infra.db.database import db


class EmissionRepository:
    @staticmethod
    def create_emission(travel_id, outbound_emission, return_emission, percentage):
        emission = Emission(
            travel_id=travel_id,
            outbound_emission=outbound_emission,
            return_emission=return_emission,
            percentage=percentage
        )
        db.session.add(emission)

    @staticmethod
    def get_emissions_by_travel_id(travel_id):
        return db.session.query(Emission).filter_by(travel_id=travel_id).first()
