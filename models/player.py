from app import db

class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    playerId = db.Column(db.String(20), nullable=False)
    playerName = db.Column(db.String(100), nullable=False)  # Increased length for names
    team = db.Column(db.String(3), nullable=False)
    position = db.Column(db.String(2), nullable=False)
    season = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=True)
    games = db.Column(db.Integer, nullable=True)
    twoPercent = db.Column(db.String(20), nullable=True)
    threePercent = db.Column(db.String(20), nullable=True)
    atr = db.Column(db.String(20), nullable=True)
    ppg_ratio = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Player {self.playerName}>'