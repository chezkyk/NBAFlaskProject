import requests
from app import db
from models.player import Player

def insert_seasons_data_in_db(seasons, path):
    for season in seasons:
        response = requests.get(path.format(season))
        if response.status_code == 200:
            players_data = response.json()

            for player in players_data:
                new_player = Player(
                    id=player.get('id'),
                    playerId=player.get('playerId', 'Unknown'),
                    playerName=player.get('playerName', 'Unknown'),
                    team=player.get('team', 'Unknown'),
                    position=player.get('position', 'Unknown'),
                    season=player.get('season', 0),
                    points=player.get('points',0),
                    games=player.get('games',0),
                    twoPercent=str(player.get('twoPercent', 'Unknown')),
                    threePercent=str(player.get('threePercent', 'Unknown')),
                    atr=str(calc_atr(player.get('assists'), player.get('turnovers'))),
                    ppg_ratio=str(player.get('ppg_ratio', 'Unknown'))
                )
                db.session.add(new_player)

            try:
                db.session.commit()
                print(f"insert data for {season} season was successfully")
            except Exception as e:
                db.session.rollback()
                print(f"failed to insert data for {season} season: {str(e)}")
        else:
            print(f"failed to get data for players in the  {season} season")


def calc_atr(assists,turnovers):
    if assists is None or turnovers is None or turnovers == 0:
        return 0
    return float(assists) / float(turnovers)

def update_ppg_ratios(season):
    avg_ppg_by_position = db.session.query(
        Player.position, # position of player
        db.func.avg(Player.points / Player.games).label('avg_ppg') # calculation of the points of the game divided by number of games
    ).filter(Player.season == season).group_by(Player.position).all()# filter by year abd grouped theme by the position and bring all the results

    avg_ppg_dict = {position: avg_ppg for position, avg_ppg in avg_ppg_by_position} # creating a dict were the key is the position and the value is the avg of points for a game

    players = db.session.query(Player).filter(Player.season == season).all()# get all players from db filtered by year

    for player in players: #updates ppg_ratio value for all players
        avg_position_ppg = avg_ppg_dict.get(player.position, 0) # get avg points for game by position from the dictionary if its not exists he will return 0
        ppg = player.points / player.games if player.games else 0 # calculation  points for the player's game if there is no game he will be zero
        player.ppg_ratio = calc_ppg_ratio(ppg, avg_position_ppg) # calculation and updates the player's ppg_ratio by using the function the calc_ppg_ratio()

    try:
        db.session.commit()
        print(f"ppg_ratios updated successfully for season {season}")
    except Exception as e:
        db.session.rollback()
        print(f"Error updating ppg_ratios for season {season}: {str(e)}")


def calc_ppg_ratio(points_per_game, avg_position):
    if avg_position == 0:
        return 0
    return points_per_game / avg_position


def get_players_by_position(position, season):
    query = db.session.query(Player) #return all players from db
    if position:# check if their is a given position
        query = query.filter(Player.position == position)# filter by position
    if season:# check if their is a given season
        query = query.filter(Player.season == season)# filter by season

    players = query.all()# make query after filtering


    if not players:# check if nothing came back from db after filter
        return []

    return [player.do_dict() for player in players] # return all players




