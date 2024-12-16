from flask import Blueprint, request, jsonify
import requests

from services.travel_service import TravelService

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


@travel_bp.route('/search', methods=['POST'])
def search_flights():
    dto = request.json

    required_keys = ['departure_id', 'arrival_id', 'outbound_date', 'trip_type', 'adults', 'children', 'infants']
    if not all(key in dto for key in required_keys):
        return {"error": "Missing required fields"}, 400

    base_url = "https://serpapi.com/search.json"
    params = {
        'engine': 'google_flights',
        'departure_id': dto['departure_id'],
        'arrival_id': dto['arrival_id'],
        'outbound_date': dto['outbound_date'],
        'currency': "EUR",
        'hl': 'fr',
        'adults': dto['adults'],
        'children': dto['children'],
        'infants': dto['infants'],
        'api_key': '7f25e8efc591b9c095d300192a582b0ba3d1b1862732c410118ea66bf8bca216'
    }

    if dto['trip_type'] == 'roundTrip' and 'return_date' in dto:
        params['return_date'] = dto['return_date']

    if dto['trip_type'] == 'oneWay' and 'return_date' in params:
        del params['return_date']

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API error: {response.json}"}, response.status_code