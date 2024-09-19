from models.player import Player
from models.group import Group
from app import db


def get_player_by_id_or_code(player_identifier):
    return Player.query.filter_by(playerId=player_identifier).first()

def create_group(team_data):
    team_name = team_data.get('team_name')
    positions = ['c', 'pf', 'sf', 'sg', 'pg']
    players = {}

    for position in positions:
        player_identifier = team_data.get(position)
        if player_identifier:
            player = get_player_by_id_or_code(player_identifier)
            if not player:
                return None, f"player not found with id {player_identifier} in position {position}"
            players[position] = player.id
        else:
            players[position] = None

    new_team = Group(
        team_name=team_name,
        c=players['c'],
        pf=players['pf'],
        sf=players['sf'],
        sg=players['sg'],
        pg=players['pg']
    )

    db.session.add(new_team)
    db.session.commit()

    return new_team, None