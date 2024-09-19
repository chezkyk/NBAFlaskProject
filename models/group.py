from app import db

class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    team_name = db.Column(db.String(20), nullable=False)
    c = db.Column(db.Integer, nullable=True)
    pf = db.Column(db.Integer, nullable=True)
    sf = db.Column(db.Integer, nullable=True)
    sg = db.Column(db.Integer, nullable=True)
    pg = db.Column(db.Integer, nullable=True)



    def __repr__(self):
        return f'<Group {self.team_name}>'

    def do_dict(self):
        return {"id": self.id, "team_name": self.team_name, "player_c": self.c,"player_pf": self.pf
            ,"player_sf": self.sf,"player_sg": self.sg,"player_pg": self.pg}