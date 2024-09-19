from flask import Flask
from db import db
from flask_migrate import Migrate
from blueprints.player import player_bp
from blueprints.group import group_bp
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)
app.register_blueprint(player_bp)
app.register_blueprint(group_bp)
if __name__ == '__main__':
    app.run()
