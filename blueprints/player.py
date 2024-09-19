from flask import Blueprint, jsonify, request
from services.player import insert_seasons_data_in_db , update_ppg_ratios ,get_players_by_position

player_bp = Blueprint('player', __name__, url_prefix='/player')


@player_bp.route('/', methods=['POST'])
def insert():
    seasons = [2022, 2023, 2024]
    path = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={}&&pageSize=1000"
    insert_seasons_data_in_db(seasons, path)
    return jsonify({"message": "data of players inserted successfully"}), 201

@player_bp.route('/updatePPG', methods=['POST'])
def update_ppg():
    seasons = [2022, 2023, 2024]
    for season in seasons:
        update_ppg_ratios(season)
    return jsonify({"message": "ppg_ratios from player was updating successfully"}), 200
@player_bp.route('/players', methods=['GET'])
def get_player_by_position():
    position = request.args.get('position')
    season = request.args.get('season')
    try:
        players = get_players_by_position(position, season)
        return jsonify(players), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


