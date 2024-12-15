def mapper_travel_to_dict(travel):
    return {
        "id": travel.id,
        "travelInfo": travel.travel_info,
        "partner_url": travel.partner_url,
        "price_outbound": travel.price_outbound,
        "price_round_trip": travel.price_round_trip,
        "segments": [
            {
                "id": segment.id,
                "segmentType": segment.segment_type,
                "flightDate": segment.flight_date.isoformat(),
                "departureTime": segment.departure_time.isoformat(),
                "departureLocation": segment.departure_location,
                "arrivalTime": segment.arrival_time.isoformat(),
                "arrivalLocation": segment.arrival_location,
                "duration": segment.duration,
                "logoUrl": segment.logo_url,
            }
            for segment in travel.segments
        ],
        "conditions": [
            {"id": condition.id, "conditionText": condition.condition_text}
            for condition in travel.conditions
        ],
        "services": [
            {"id": service.id, "serviceText": service.service_text}
            for service in travel.services
        ],
        "emissions": [
            {
                "id": emission.id,
                "outboundEmission": emission.outbound_emission,
                "returnEmission": emission.return_emission,
                "percentage": emission.percentage,
            }
            for emission in travel.emissions
        ],
    }
