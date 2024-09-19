from flask import Blueprint, jsonify, request
from services.group import create_group

group_bp = Blueprint('group', __name__, url_prefix='/group')

@group_bp.route('/createGroup', methods=['POST'])
def create_group_route():
    data = request.get_json()
    group_name = data.get('team_name')

    if not group_name:
        return jsonify({"error": "please enter a group name"}), 400

    new_team, error = create_group(data)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": f"group '{group_name}' created successfully!",
        "team": new_team.do_dict()
    }), 201

