import os
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from users import create_user, get_users, get_user, update_user, delete_user
from database import set_mysql
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
# Required
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_PORT"] = int(os.getenv("MYSQL_PORT"))
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
# Extra configs, optional but mandatory for this project:
app.config["MYSQL_CURSORCLASS"] = os.getenv("MYSQL_CURSORCLASS")
app.config["MYSQL_AUTOCOMMIT"] = True if os.getenv("MYSQL_AUTOCOMMIT") == "true" else False

mysql = MySQL(app)
set_mysql(mysql)

@app.route("/")
def home():
  return jsonify({"message": "Hello, CSIT327!"})

@app.route("/users", methods=["GET", "POST"])
def users():
  if request.method == "POST":
    data = request.get_json()
    user_id = create_user(
      data["name"], data["age"], data["occupation"],
      data["email"], data["password"]
    )
    return jsonify({"id": user_id})
  else:
    users = get_users()
    return jsonify(users)

@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def user(id):
  if request.method == "PUT":
    data = request.get_json()
    user_id = update_user(
      id,
      data["name"], data["age"], data["occupation"],
      data["email"], data["password"]
    )
    return jsonify({"id": user_id})
  elif request.method == "DELETE":
    user_id = delete_user(id)
    return jsonify({"id": user_id})
  else:
    user = get_user(id)
    return jsonify(user)