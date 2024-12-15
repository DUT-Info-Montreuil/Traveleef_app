from flask import Blueprint, request, jsonify

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
