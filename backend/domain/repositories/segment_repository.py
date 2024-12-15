
from domain.entities.segment import Segment
from infra.db.database import db


class SegmentRepository:
    @staticmethod
    def create_segment(travel_id, segment_type, flight_date, departure_time, departure_location, arrival_time, arrival_location, duration, logo_url):
        segment = Segment(
            travel_id=travel_id,
            segment_type=segment_type,
            flight_date=flight_date,
            departure_time=departure_time,
            departure_location=departure_location,
            arrival_time=arrival_time,
            arrival_location=arrival_location,
            duration=duration,
            logo_url=logo_url
        )
        db.session.add(segment)

    @staticmethod
    def get_segments_by_travel_id(travel_id):
        return db.session.query(Segment).filter_by(travel_id=travel_id).all()