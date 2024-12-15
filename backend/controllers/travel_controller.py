from flask import Blueprint, request, jsonify

from services.travel_service import TravelService
from shared.dto.mappers.travel_mapper import mapper_travel_to_dict

travel_bp = Blueprint('travel_bp', __name__)


@travel_bp.route('/', methods=['POST'])
def create_travel():
    try:
        travel_data = request.get_json()
        travel = TravelService.create_travel(travel_data)
        return jsonify({"message": "Travel created successfully", "travel_id": travel.id}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@travel_bp.route('/<int:travel_id>', methods=['GET'])
def get_travel_details(travel_id):
    try:
        travel_details = TravelService.get_travel_details(travel_id)
        return jsonify(travel_details), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@travel_bp.route('/', methods=['GET'])
def get_all_travels():
    try:
        travels_list = TravelService.get_all_travels_details()
        return jsonify(travels_list), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@travel_bp.route('/search', methods=['GET'])
def search_travels():
    departure_location = request.args.get('departureLocation')
    arrival_location = request.args.get('arrivalLocation')
    travel_date = request.args.get('travelDate')
    return_travel_date = request.args.get('returnTravelDate')

    if not departure_location or not arrival_location or not travel_date:
        return jsonify({"message": "Les paramètres departureLocation, arrivalLocation et travelDate sont requis."}), 400

    try:
        results = TravelService.search_travels(departure_location, arrival_location, travel_date, return_travel_date)

        if isinstance(results, dict) and "message" in results:
            return jsonify(results), 404

        mapped_results = [mapper_travel_to_dict(travel) for travel in results]
        return jsonify({"travels": mapped_results}), 200

    except Exception as e:
        return jsonify({"message": f"Une erreur s'est produite lors de la recherche : {str(e)}"}), 500