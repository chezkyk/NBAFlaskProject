from flask import Blueprint, jsonify
from services.player import insert_seasons_data_in_db , update_ppg_ratios

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
