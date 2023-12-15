import os
from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from db.database import set_mysql
from dotenv import load_dotenv

# import blueprints for the api routes
from routes.games import games
from routes.events import events
from routes.players import players

# create the flask app
app = Flask(__name__)
# enable CORS
CORS(app)

# configure flask-mysql from environment variables (.env file)
load_dotenv()
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_PORT"] = int(os.getenv("MYSQL_PORT"))
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
# Extra configs, optional but mandatory for this project:
app.config["MYSQL_CURSORCLASS"] = os.getenv("MYSQL_CURSORCLASS")
app.config["MYSQL_AUTOCOMMIT"] = (
    True if os.getenv("MYSQL_AUTOCOMMIT") == "true" else False
)
mysql = MySQL(app)
set_mysql(mysql)

# register imported blueprints for api routes
app.register_blueprint(games, url_prefix="/games")
app.register_blueprint(events, url_prefix="/events")
app.register_blueprint(players, url_prefix="/players")

# run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT"))
