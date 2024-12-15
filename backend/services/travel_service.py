from sqlalchemy.exc import IntegrityError

from domain.repositories.condition_repository import ConditionRepository
from domain.repositories.emission_repository import EmissionRepository
from domain.repositories.segment_repository import SegmentRepository
from domain.repositories.service_repository import ServiceRepository
from domain.repositories.travel_repository import TravelRepository
from infra.db.database import db


class TravelService:

    @staticmethod
    def get_all_travels_details():
        travels = TravelRepository.get_all_travels()

        if not travels:
            return {"error": "No travels found"}

        all_travels_details = []
        for travel in travels:
            travel_id = travel.id
            emissions = EmissionRepository.get_emissions_by_travel_id(travel_id)
            segments = SegmentRepository.get_segments_by_travel_id(travel_id)
            conditions = ConditionRepository.get_conditions_by_travel_id(travel_id)
            services = ServiceRepository.get_services_by_travel_id(travel_id)

            if not emissions or not segments:
                continue

            price = travel.price_outbound
            if travel.price_round_trip:
                price = travel.price_round_trip

        travel_details = {
                "id": travel.id,
                "travelInfo": travel.travel_info,
                "partner_url": travel.partner_url,
                "price": price,
                "emissions": {
                    "aller": emissions.outbound_emission,
                    "retour": emissions.return_emission,
                    "pourcentage": emissions.percentage,
                },
                "aller": [{
                    "date": segment.flight_date.isoformat(),
                    "departureTime": segment.departure_time.strftime("%H:%M:%S"),
                    "departureLocation": segment.departure_location,
                    "arrivalTime": segment.arrival_time.strftime("%H:%M:%S"),
                    "arrivalLocation": segment.arrival_location,
                    "duration": segment.duration,
                    "logoUrl": segment.logo_url
                } for segment in segments if segment.segment_type == 'outbound'],
                "retour": [{
                    "date": segment.flight_date.isoformat(),
                    "departureTime": segment.departure_time.strftime("%H:%M:%S"),
                    "departureLocation": segment.departure_location,
                    "arrivalTime": segment.arrival_time.strftime("%H:%M:%S"),
                    "arrivalLocation": segment.arrival_location,
                    "duration": segment.duration,
                    "logoUrl": segment.logo_url
                } for segment in segments if segment.segment_type == 'return'],
                "conditions": [condition.condition_text for condition in conditions],
                "services": [service.service_text for service in services],
            }

        all_travels_details.append(travel_details)

        return all_travels_details

    @staticmethod
    def get_travel_details(travel_id):
        travel = TravelRepository.get_travel_by_id(travel_id)
        emissions = EmissionRepository.get_emissions_by_travel_id(travel_id)
        segments = SegmentRepository.get_segments_by_travel_id(travel_id)
        conditions = ConditionRepository.get_conditions_by_travel_id(travel_id)
        services = ServiceRepository.get_services_by_travel_id(travel_id)

        if not travel or not emissions or not segments:
            return {"error": "Travel or emissions or segments not found."}

        price = travel.price_outbound
        if travel.price_round_trip:
            price = travel.price_round_trip

        return {
            "id": travel.id,
            "travelInfo": travel.travel_info,
            "partner_url": travel.partner_url,
            "price": price,
            "emissions": {
                "aller": emissions.outbound_emission,
                "retour": emissions.return_emission,
                "pourcentage": emissions.percentage,
            },
            "aller": [{
                "date": segment.flight_date.isoformat(),
                "departureTime": segment.departure_time.strftime("%H:%M"),
                "departureLocation": segment.departure_location,
                "arrivalTime": segment.arrival_time.strftime("%H:%M"),
                "arrivalLocation": segment.arrival_location,
                "duration": segment.duration,
                "logoUrl": segment.logo_url
            } for segment in segments if segment.segment_type == 'outbound'],
            "retour": [{
                "date": segment.flight_date.isoformat(),
                "departureTime": segment.departure_time.strftime("%H:%M"),
                "departureLocation": segment.departure_location,
                "arrivalTime": segment.arrival_time.strftime("%H:%M"),
                "arrivalLocation": segment.arrival_location,
                "duration": segment.duration,
                "logoUrl": segment.logo_url
            } for segment in segments if segment.segment_type == 'return'],
            "conditions": [condition.condition_text for condition in conditions],
            "services": [service.service_text for service in services],
        }

    @staticmethod
    def create_travel(travel_data):
        required_keys = ['travelInfo', 'emissions', 'aller', 'conditions', 'services']
        for key in required_keys:
            if key not in travel_data:
                raise ValueError(f"Les données doivent contenir la clé '{key}'.")

        try:
            with db.session.begin():
                travel = TravelRepository.create_travel(
                    travel_data['travelInfo'],
                    travel_data.get('partner_url', ''),
                    travel_data.get('priceOutbound', None),
                    travel_data.get('priceRoundTrip', None)
                )

                EmissionRepository.create_emission(
                    travel.id,
                    travel_data['emissions']['aller'],
                    travel_data['emissions'].get('retour', None),
                    travel_data['emissions']['pourcentage']
                )

                if travel_data['aller']:
                    for segment_data in travel_data['aller']:
                        SegmentRepository.create_segment(
                            travel.id,
                            'outbound',
                            segment_data['date'],
                            segment_data['departureTime'],
                            segment_data['departureLocation'],
                            segment_data['arrivalTime'],
                            segment_data['arrivalLocation'],
                            segment_data['duration'],
                            segment_data.get('logoUrl', None)
                        )

                if travel_data.get('retour'):
                    for segment_data in travel_data['retour']:
                        SegmentRepository.create_segment(
                            travel.id,
                            'return',
                            segment_data['date'],
                            segment_data['departureTime'],
                            segment_data['departureLocation'],
                            segment_data['arrivalTime'],
                            segment_data['arrivalLocation'],
                            segment_data['duration'],
                            segment_data.get('logoUrl', None)
                        )

                for condition_text in travel_data['conditions']:
                    ConditionRepository.create_condition(travel.id, condition_text)

                for service_text in travel_data['services']:
                    ServiceRepository.create_service(travel.id, service_text)

            return travel

        except IntegrityError as ie:
            db.session.rollback()
            raise ValueError(f"Erreur d'intégrité dans les données fournies : {ie.orig}") from ie
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Une erreur est survenue lors de la création du voyage : {str(e)}") from e