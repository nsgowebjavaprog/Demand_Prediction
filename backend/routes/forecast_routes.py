from flask import Blueprint, jsonify

forecast_bp = Blueprint('forecast', __name__)

@forecast_bp.route('/forecast', methods=['GET'])
def forecast():
    return jsonify({'message': 'Forecast endpoint is working!'})
