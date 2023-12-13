from flask import Blueprint, jsonify, request
from db.players import create_player, get_player, get_players, update_player, delete_player

players = Blueprint("players", __name__)

@players.get("/")
def handle_get_all_players():
    data = get_players()
    return jsonify(data)

@players.get("/<int:id>")
def handle_get_player(id):
    data = get_player(id)
    return jsonify(data)

@players.post("/")
def handle_create_player():
    body = request.json
    name = body["name"]
    player_id = create_player(name)
    return jsonify({"player_id": player_id})

@players.put("/<int:id>")
def handle_update_player(id):
    body = request.json
    name = body["name"]
    total_wins = body["total_wins"]
    player_id = update_player(id, name, total_wins)
    return jsonify({"player_id": player_id})

@players.delete("/<int:id>")
def handle_delete_player(id):
    player_id = delete_player(id)
    return jsonify({"player_id": player_id})